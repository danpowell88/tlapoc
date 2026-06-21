#!/usr/bin/env python3
"""
jira.py — create the whole backlog in Jira Cloud from docs/backlog/data/*.json:
  Epics (issuetype Epic) -> Stories (issuetype Story, parent=epic)
  -> Sub-tasks (issuetype Sub-task, parent=story) = the dev tasks from tasks_for()
  + "blocks / is blocked by" links from each story's depends_on (dependency map).

Items are created with their native Jira issue type (no "Story:"/"Epic:" prefix in summaries).
Descriptions use the consistent 6-section format (ADF).

Config (non-secret) in scripts/.jira-config (JSON) or env:
  { "site": "your.atlassian.net", "email": "you@example.com", "project": "TLA" }
Token (secret) in scripts/.jira-token or env JIRA_TOKEN.

Commands:
  python scripts/jira.py whoami     # verify auth + show project, issue types, link types
  python scripts/jira.py plan       # counts of what will be created (no API writes)
  python scripts/jira.py create     # create epics + stories + sub-tasks (idempotent via state)
  python scripts/jira.py links      # create dependency links (idempotent)
  python scripts/jira.py all        # create + links
  python scripts/jira.py wipe       # delete everything this tool created (uses state file)
"""
from __future__ import annotations
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backlog import load, MS_TITLE
from monday import (estimate, type_label, tasks_for, plan_sprints, MS_ORDER,
                    bg_text, req_bullets, ui_text, tech_blocks,
                    compliance_links, prd_link)

SPRINT_THEME = {"M0": "Setup", "M1": "Foundations", "M2": "Booking",
                "M3": "Clinical", "M4": "Commerce", "M5": "Reporting & apps",
                "M6": "Facility", "M7": "Backlog"}

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = os.path.join(HERE, ".jira-config")
TOKEN_FILE = os.path.join(HERE, ".jira-token")
STATE = os.path.join(HERE, ".jira-state.json")


# ---------------------------------------------------------------- config/auth
def cfg():
    c = {}
    if os.path.exists(CFG):
        with open(CFG, encoding="utf-8") as fh:
            c = json.load(fh)
    site = (c.get("site") or os.environ.get("JIRA_SITE", "")).strip().rstrip("/")
    email = (c.get("email") or os.environ.get("JIRA_EMAIL", "")).strip()
    project = (c.get("project") or os.environ.get("JIRA_PROJECT", "")).strip()
    site = site.replace("https://", "").replace("http://", "")
    if not (site and email and project):
        raise SystemExit("Need site, email, project in scripts/.jira-config or JIRA_* env.")
    return site, email, project


def token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, encoding="utf-8") as fh:
            t = fh.read().strip()
            if t:
                return t
    t = os.environ.get("JIRA_TOKEN", "").strip()
    if not t:
        raise SystemExit("No Jira token in scripts/.jira-token or JIRA_TOKEN.")
    return t


def api(method, path, payload=None, base="rest/api/3", _tries=0):
    site, email, _p = cfg()
    url = f"https://{site}/{base}/{path.lstrip('/')}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    auth = base64.b64encode(f"{email}:{token()}".encode()).decode()
    req.add_header("Authorization", f"Basic {auth}")
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        txt = e.read().decode("utf-8")
        if e.code == 429 and _tries < 6:
            time.sleep(int(e.headers.get("Retry-After", 2 ** _tries)) + 1)
            return api(method, path, payload, base, _tries + 1)
        if e.code in (500, 502, 503) and _tries < 5:
            time.sleep(2 ** _tries)
            return api(method, path, payload, base, _tries + 1)
        raise SystemExit(f"HTTP {e.code} {method} {path}: {txt[:600]}")


# ---------------------------------------------------------------- state
def load_state():
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def save_state(st):
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(st, fh, indent=2)


# ---------------------------------------------------------------- ADF
def _block_lines(text):
    """Turn a section's text into ADF block nodes (paragraphs + bullet lists)."""
    nodes, bullets = [], []

    def flush():
        if bullets:
            nodes.append({"type": "bulletList", "content": [
                {"type": "listItem", "content": [
                    {"type": "paragraph", "content": [{"type": "text", "text": b}]}]}
                for b in bullets]})
            bullets.clear()

    for raw in (text or "").split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        s = line.lstrip()
        if s.startswith("- "):
            item = s[2:]
            if item.startswith("[ ] "):
                item = item[4:]
            bullets.append(item)
        else:
            flush()
            nodes.append({"type": "paragraph", "content": [{"type": "text", "text": line}]})
    flush()
    return nodes or [{"type": "paragraph", "content": [{"type": "text", "text": "—"}]}]


def adf(sections):
    content = []
    for title, text in sections:
        content.append({"type": "heading", "attrs": {"level": 3},
                        "content": [{"type": "text", "text": title}]})
        content.extend(_block_lines(text))
    return {"type": "doc", "version": 1, "content": content}


def adf_text(text):
    return {"type": "doc", "version": 1, "content": _block_lines(text)}


# ---- rich ADF nodes (headings, bullet lists, inline links) ------------------
def _t(text, marks=None):
    n = {"type": "text", "text": text}
    if marks:
        n["marks"] = marks
    return n


def _p(*nodes):
    return {"type": "paragraph", "content": list(nodes)}


def _h(title):
    return {"type": "heading", "attrs": {"level": 3}, "content": [_t(title)]}


def _ul(items):
    return {"type": "bulletList", "content": [
        {"type": "listItem", "content": [_p(_t(i))]} for i in items if i]}


def _linked(prefix, pairs):
    content = [_t(prefix)]
    for i, (label, url) in enumerate(pairs):
        if i:
            content.append(_t(", "))
        content.append(_t(label, [{"type": "link", "attrs": {"href": url}}]))
    return _p(*content)


def story_desc(ep, s):
    c = [_h("Background")]
    c += [_p(_t(p)) for p in bg_text(ep, s)]
    c.append(_h("Requirements"))
    c.append(_ul(req_bullets(ep, s)))
    cl = compliance_links(s)
    if cl:
        c.append(_linked("Compliance: ", cl))
    c.append(_h("Acceptance Criteria"))
    c.append(_ul(list(s["acceptance"])))
    uit = ui_text(ep, s)
    if uit:
        c += [_h("UI designs / screenshots"), _p(_t(uit))]
    tb = tech_blocks(ep, s)
    tech = []
    if tb["stack"]:
        tech.append(_p(_t("Stack: " + tb["stack"])))
    if tb["adrs"]:
        tech.append(_linked("Architecture decisions: ", tb["adrs"]))
    if tb["spike"]:
        tech.append(_p(_t("Time-boxed spike — produce findings + a go/no-go, not production code.")))
    if tech:
        c.append(_h("Technical notes (high level)"))
        c += tech
    return {"type": "doc", "version": 1, "content": c}


def epic_desc(ep):
    e = ep["epic"]
    return {"type": "doc", "version": 1, "content": [
        _p(_t(e["summary"])), _h("Stories"),
        _ul([s["title"] for s in ep["stories"]])]}


def labels_clean(s):
    out = ["tla-backlog"]
    if "compliance" in s.get("labels", []):
        out.append("compliance")
    if "phase:2plus" in s.get("labels", []):
        out.append("phase-2plus")
    return out


def story_type_id(meta, s):
    if "type:chore" in s.get("labels", []) or "type:spike" in s.get("labels", []):
        return meta["task"]
    return meta["story"]


# ---------------------------------------------------------------- labels
def sanitize(label):
    out = "".join(ch if ch.isalnum() or ch in "-_." else "-" for ch in label)
    return out.strip("-")[:255]


def add_weblink(key, pair, st):
    """Attach the source PRD as a Jira web link (proper data, not description text)."""
    if not pair:
        return
    lk = f"prdlink:{key}"
    if lk in st:
        return
    api("POST", f"issue/{key}/remotelink",
        {"object": {"url": pair[1], "title": "Source PRD: " + pair[0]}})
    st[lk] = True
    save_state(st)
    time.sleep(0.15)


def editmeta_caps(sample_key):
    em = api("GET", f"issue/{sample_key}/editmeta").get("fields", {})
    sp = next((fid for fid, m in em.items() if "story point" in m.get("name", "").lower()), None)
    names = [p["name"] for p in api("GET", "priority")]
    def pk(*prefs):
        return next((n for n in prefs if n in names), (names[0] if names else "Medium"))
    return {"priority": "priority" in em, "sp_field": sp,
            "type_editable": "issuetype" in em,
            "prio_map": {"P0": pk("Highest", "High"), "P1": pk("High", "Medium"),
                         "P2": pk("Low", "Lowest", "Medium")}}


# ---------------------------------------------------------------- meta
def resolve_meta():
    site, email, project = cfg()
    proj = api("GET", f"project/{project}")
    style = proj.get("style", "classic")
    its = {it["name"].lower(): it for it in proj.get("issueTypes", [])}
    def pick(*names, subtask=None):
        for it in proj.get("issueTypes", []):
            if subtask is not None and bool(it.get("subtask")) != subtask:
                continue
            if it["name"].lower() in names:
                return it
        if subtask:
            for it in proj.get("issueTypes", []):
                if it.get("subtask"):
                    return it
        return None
    epic = pick("epic")
    story = pick("story") or pick("task", subtask=False)
    task = pick("task", subtask=False) or story
    sub = pick("sub-task", "subtask", subtask=True)
    if not (epic and story and sub):
        raise SystemExit(f"Could not resolve issue types. Available: {list(its)}")
    # epic-link field (company-managed may need it instead of parent)
    epic_link_field = None
    if style != "next-gen":
        for f in api("GET", "field"):
            if f.get("name") == "Epic Link":
                epic_link_field = f["id"]
                break
    # blocks link type
    blocks = None
    for lt in api("GET", "issueLinkType")["issueLinkTypes"]:
        if lt["name"].lower() == "blocks":
            blocks = lt
            break
    return {"project": project, "style": style, "epic": epic["id"], "story": story["id"],
            "task": task["id"], "sub": sub["id"], "epic_link_field": epic_link_field,
            "blocks": blocks}


# ---------------------------------------------------------------- create
def create_issue(fields):
    return api("POST", "issue", {"fields": fields})["key"]


def cmd_create():
    meta = resolve_meta()
    st = load_state()
    epics = load()
    pj = meta["project"]
    n = 0

    # 1. epics
    for ep in epics:
        e = ep["epic"]
        k = f"epic:{e['key']}"
        if k in st:
            continue
        fields = {"project": {"key": pj}, "issuetype": {"id": meta["epic"]},
                  "summary": e["title"], "description": epic_desc(ep),
                  "labels": ["tla-backlog"]}
        st[k] = create_issue(fields)
        save_state(st)
        print(f"epic  {st[k]}  {e['title']}")
        time.sleep(0.3)

    # 2. stories
    for ep in epics:
        e = ep["epic"]
        epic_key = st[f"epic:{e['key']}"]
        for s in ep["stories"]:
            k = f"story:{e['key']}/{s['key']}"
            if k in st:
                continue
            fields = {"project": {"key": pj}, "issuetype": {"id": story_type_id(meta, s)},
                      "summary": s["title"], "description": story_desc(ep, s),
                      "labels": labels_clean(s)}
            if meta["style"] == "next-gen" or not meta["epic_link_field"]:
                fields["parent"] = {"key": epic_key}
            else:
                fields[meta["epic_link_field"]] = epic_key
            try:
                st[k] = create_issue(fields)
            except SystemExit:
                # fallback: swap parent/epic-link strategy
                fields.pop("parent", None)
                if meta["epic_link_field"]:
                    fields[meta["epic_link_field"]] = epic_key
                else:
                    fields["parent"] = {"key": epic_key}
                st[k] = create_issue(fields)
            save_state(st)
            n += 1
            if n % 10 == 0:
                print(f"  …{n} stories")
            time.sleep(0.3)
    print(f"stories created (total mapped: {sum(1 for x in st if x.startswith('story:'))})")

    # 3. sub-tasks (dev tasks)
    nt = 0
    for ep in epics:
        e = ep["epic"]
        for s in ep["stories"]:
            parent = st[f"story:{e['key']}/{s['key']}"]
            for i, t in enumerate(tasks_for(ep, s)):
                k = f"task:{e['key']}/{s['key']}#{i}"
                if k in st:
                    continue
                body = t["title"] + (f"\n\n{t['note']}" if t.get("note") else "") + \
                    f"\n\nPart of story: {s['title']}."
                fields = {"project": {"key": pj}, "issuetype": {"id": meta["sub"]},
                          "summary": t["title"][:250], "description": adf_text(body),
                          "parent": {"key": parent},
                          "labels": ["tla-backlog", "dev-task"]}
                st[k] = create_issue(fields)
                save_state(st)
                nt += 1
                if nt % 25 == 0:
                    print(f"  …{nt} sub-tasks")
                time.sleep(0.3)
    print(f"sub-tasks created (total: {nt} this run)")
    save_state(st)


def cmd_links():
    meta = resolve_meta()
    if not meta["blocks"]:
        raise SystemExit("No 'Blocks' link type available.")
    st = load_state()
    epics = load()
    made = 0
    for ep in epics:
        e = ep["epic"]
        for s in ep["stories"]:
            dependent = st.get(f"story:{e['key']}/{s['key']}")
            if not dependent:
                continue
            for dep in s.get("depends_on", []):
                blocker = st.get(f"story:{dep}")
                if not blocker:
                    continue
                lk = f"link:{dep}->{e['key']}/{s['key']}"
                if lk in st:
                    continue
                # blocker BLOCKS dependent ; dependent IS BLOCKED BY blocker
                api("POST", "issueLink", {
                    "type": {"name": meta["blocks"]["name"]},
                    "outwardIssue": {"key": blocker},
                    "inwardIssue": {"key": dependent}})
                st[lk] = True
                save_state(st)
                made += 1
                time.sleep(0.25)
    print(f"created {made} dependency links this run.")


def cmd_refresh():
    """Update existing epics + stories: clean description, real fields, trimmed labels,
    proper issue type (chore/spike -> Task), and PRD web link."""
    meta = resolve_meta()
    st = load_state()
    epics = load()
    sample = next((v for k, v in st.items() if k.startswith("story:")), None)
    if not sample:
        raise SystemExit("No stories in state; run create first.")
    cap = editmeta_caps(sample)
    print(f"caps: priority={cap['priority']} sp_field={cap['sp_field']} "
          f"type_editable={cap['type_editable']} prio_map={cap['prio_map']}")
    for ep in epics:
        ek = st.get(f"epic:{ep['epic']['key']}")
        if not ek:
            continue
        api("PUT", f"issue/{ek}", {"fields": {"summary": ep["epic"]["title"],
            "description": epic_desc(ep), "labels": ["tla-backlog"]}})
        add_weblink(ek, prd_link(ep), st)
        time.sleep(0.2)
    print("epics refreshed")
    n = 0
    for ep in epics:
        for s in ep["stories"]:
            k = st.get(f"story:{ep['epic']['key']}/{s['key']}")
            if not k:
                continue
            f = {"summary": s["title"], "description": story_desc(ep, s),
                 "labels": labels_clean(s)}
            if cap["priority"]:
                f["priority"] = {"name": cap["prio_map"][s.get("priority", "P1")]}
            if cap["sp_field"]:
                f[cap["sp_field"]] = estimate(s)
            if cap["type_editable"]:
                f["issuetype"] = {"id": story_type_id(meta, s)}
            try:
                api("PUT", f"issue/{k}", {"fields": f})
            except SystemExit:
                f.pop("issuetype", None)
                api("PUT", f"issue/{k}", {"fields": f})
            add_weblink(k, prd_link(ep), st)
            n += 1
            if n % 20 == 0:
                print(f"  …{n} stories")
            time.sleep(0.25)
    print(f"refreshed {n} stories")


def cmd_sprints():
    _s, _e, project = cfg()
    st = load_state()
    boards = api("GET", f"board?projectKeyOrId={project}", base="rest/agile/1.0")["values"]
    scrum = next((b for b in boards if b.get("type") == "scrum"), boards[0] if boards else None)
    if not scrum:
        raise SystemExit("No board found for project.")
    bid = scrum["id"]
    print(f"board {bid} ({scrum['name']}, type={scrum.get('type')})")
    named, _cap, _total = plan_sprints(load())
    i = 0
    for title, items in named:
        if not title.lower().startswith("sprint"):
            continue
        i += 1
        ms = [ep["epic"]["milestone"] for ep, _s in items]
        dom = min(ms, key=lambda m: (-ms.count(m), MS_ORDER[m]))
        name = f"Sprint {i:02d} · {SPRINT_THEME.get(dom, '')}".strip()[:29]
        sk = f"sprint:{name}"
        if sk in st:
            sid = st[sk]
        else:
            sid = api("POST", "sprint",
                      {"name": name, "originBoardId": bid, "goal": MS_TITLE[dom]},
                      base="rest/agile/1.0")["id"]
            st[sk] = sid
            save_state(st)
        keys = [st.get(f"story:{ep['epic']['key']}/{s['key']}") for ep, s in items]
        keys = [k for k in keys if k]
        for off in range(0, len(keys), 50):
            api("POST", f"sprint/{sid}/issue", {"issues": keys[off:off + 50]}, base="rest/agile/1.0")
        print(f"{name}: {len(keys)} stories -> sprint {sid}")
        time.sleep(0.2)
    print("sprint mapping done (Backlog group left unscheduled).")


def cmd_whoami():
    me = api("GET", "myself")
    print(f"Auth OK: {me.get('displayName')} <{me.get('emailAddress')}>")
    meta = resolve_meta()
    print(f"Project: {meta['project']} (style={meta['style']})")
    print(f"  Epic id={meta['epic']}  Story id={meta['story']}  Sub-task id={meta['sub']}")
    print(f"  Epic-link field: {meta['epic_link_field'] or '(uses parent)'}")
    print(f"  Blocks link: {meta['blocks']['name'] if meta['blocks'] else 'MISSING'}")


def cmd_plan():
    epics = load()
    ne = len(epics)
    ns = sum(len(ep["stories"]) for ep in epics)
    nt = sum(len(tasks_for(ep, s)) for ep in epics for s in ep["stories"])
    nl = sum(len(s.get("depends_on", [])) for ep in epics for s in ep["stories"])
    print(f"Would create: {ne} epics, {ns} stories, {nt} sub-tasks, ~{nl} dependency links "
          f"({ne+ns+nt} issues).")


def cmd_wipe():
    st = load_state()
    keys = [v for k, v in st.items() if isinstance(v, str)]
    # delete sub-tasks first, then stories, then epics (children before parents)
    order = ([v for k, v in st.items() if k.startswith("task:")] +
             [v for k, v in st.items() if k.startswith("story:")] +
             [v for k, v in st.items() if k.startswith("epic:")])
    for key in order:
        try:
            api("DELETE", f"issue/{key}?deleteSubtasks=true")
            print(f"deleted {key}")
        except SystemExit as e:
            print(f"skip {key} ({str(e)[:60]})")
        time.sleep(0.2)
    save_state({})
    print("wiped; state cleared.")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "whoami"
    {"whoami": cmd_whoami, "plan": cmd_plan, "create": cmd_create,
     "links": cmd_links, "all": lambda: (cmd_create(), cmd_links()),
     "refresh": cmd_refresh, "sprints": cmd_sprints,
     "wipe": cmd_wipe}.get(cmd, lambda: (_ for _ in ()).throw(SystemExit(__doc__)))()


if __name__ == "__main__":
    main()
