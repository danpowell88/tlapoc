#!/usr/bin/env python3
"""
monday.py — set up the monday.com board from the same backlog source of truth
(docs/backlog/data/*.json) used for the GitHub seeder.

It builds a consistent, sprint-planned board:
  - Columns: Status, Type, Epic, Stage, Priority, Area, Estimate, Key, Depends on,
    + six consistent long-text story sections:
      Background · Requirements · Acceptance Criteria · UI / Designs · Technical notes · Other
  - Groups = Sprints (dependency-ordered, capacity-packed) + a "Backlog — Phase 2+" group.
  - One item per story (epics are a column, not items), each fully populated.

Auth: put a monday personal API token in scripts/.monday-token (gitignored) OR set
env MONDAY_TOKEN. Get one at monday.com → avatar → Developers → My access tokens.

Commands:
  python scripts/monday.py inspect      # read-only: show current board contents
  python scripts/monday.py plan         # print the sprint plan (no API calls)
  python scripts/monday.py rebuild      # create columns+groups, clear old groups/cols
  python scripts/monday.py seed         # create all story items
  python scripts/monday.py all          # rebuild + seed
"""
from __future__ import annotations
import json
import math
import os
import sys
import time
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backlog import load, MILESTONES, MS_TITLE, ROOT  # reuse the backlog loader

BOARD_ID = os.environ.get("MONDAY_BOARD_ID", "5029378984")
API = "https://api.monday.com/v2"
TARGET_SPRINTS = 23          # aim for ~this many sprints; capacity adapts
TOKEN_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".monday-token")

# ---- column plan: title -> monday column_type -------------------------------
COLUMNS = [
    ("Status", "status"),
    ("Type", "dropdown"),
    ("Epic", "dropdown"),
    ("Stage", "dropdown"),
    ("Priority", "status"),
    ("Area", "dropdown"),
    ("Estimate (pts)", "numbers"),
    ("Key", "text"),
    ("Depends on", "text"),
    ("Background", "long_text"),
    ("Requirements", "long_text"),
    ("Acceptance Criteria", "long_text"),
    ("UI / Designs", "long_text"),
    ("Technical notes", "long_text"),
    ("Other", "long_text"),
]

MS_ORDER = {mid: i for i, (mid, _t, _d) in enumerate(MILESTONES)}

# epic -> where it lives in the prototype (for the UI / Designs section)
EPIC_UI = {
    "SPRINT-0": "Non-UI / platform scaffolding — no prototype screen.",
    "PRD-01": "prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.",
    "PRD-02": "prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.",
    "PRD-03": "prototype.html — Forms & consent; client-app.html intake/consent; checkin.html.",
    "PRD-04": "prototype.html — Stock & medicines, Charting (lot select), Governance → Recalls.",
    "PRD-05": "prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.",
    "PRD-06": "prototype.html — Checkout, Memberships; client-app.html Rewards/Account.",
    "PRD-07": "prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.",
    "PRD-08": "prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).",
    "PRD-09": "client-app.html, treatment-room.html, checkin.html, backroom.html.",
    "PRD-10": "prototype.html — Settings → Integrations.",
    "PRD-11": "prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.",
    "PLATFORM": "prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).",
    "PHASE-2": "Future — not built in the prototype (some shown as concept cards in Settings → Integrations).",
}
STORY_UI = {
    "PRD-05/SKIN-ANALYSIS": "prototype.html — Clinical → Skin analysis (scan + push-to-client); client-app.html.",
    "PRD-05/BODY-CONTOURING": "prototype.html — Clinical → Body contouring (body map).",
    "PRD-05/COMPLICATION-LIBRARY": "prototype.html — Clinical → Complication protocols.",
    "PRD-05/OUTCOMES": "prototype.html — Clinical → Photography & outcomes.",
    "PRD-09/CHECKIN-KIOSK": "checkin.html.",
    "PRD-09/BACKOFFICE-TABLET": "backroom.html.",
    "PRD-09/CLIENT-CONCERN": "client-app.html — Report a concern; prototype Follow-ups.",
    "PLATFORM/TODAY": "prototype.html — Today (waiting / in-room / checked-out).",
    "PLATFORM/SEARCH": "prototype.html — header search box.",
    "PLATFORM/CLINIC-SWITCH": "prototype.html — sidebar clinic switcher.",
    "PRD-11/OPENCLOSE": "prototype.html — Operations → Open/close & fridge log; backroom.html.",
    "PRD-11/TEMP-MONITORS": "prototype.html — Operations → Temperature monitors.",
}
AREA_TECH = {
    "area:backend": ".NET API (domain/services)",
    "area:web": "Angular web (admin/front-desk/public)",
    "area:client-app": "Flutter client app",
    "area:provider-app": "Flutter provider app",
    "area:infra": "Azure / CI-CD / IaC",
    "area:data": "Postgres + EF Core (RLS)",
    "area:design": "Shared design system",
    "area:integration": "Ports-and-adapters integration",
}


# ---------------------------------------------------------------- auth + gql
def token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, encoding="utf-8") as fh:
            t = fh.read().strip()
            if t:
                return t
    t = os.environ.get("MONDAY_TOKEN", "").strip()
    if not t:
        raise SystemExit("No monday token. Put it in scripts/.monday-token or set MONDAY_TOKEN.")
    return t


def gql(query, variables=None, _tries=0):
    body = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    req = urllib.request.Request(API, data=body, method="POST")
    req.add_header("Authorization", token())
    req.add_header("Content-Type", "application/json")
    req.add_header("API-Version", "2024-10")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code in (429, 500, 502, 503) and _tries < 6:
            time.sleep(2 ** _tries)
            return gql(query, variables, _tries + 1)
        raise SystemExit(f"HTTP {e.code}: {e.read().decode('utf-8')[:500]}")
    if "errors" in data:
        msg = json.dumps(data["errors"])[:400]
        if ("Complexity" in msg or "rate" in msg.lower()) and _tries < 6:
            time.sleep(2 ** _tries + 1)
            return gql(query, variables, _tries + 1)
        raise SystemExit(f"GraphQL error: {msg}")
    return data["data"]


# ---------------------------------------------------------------- planning
def estimate(story):
    labs = story.get("labels", [])
    if "type:spike" in labs:
        return 2
    if "phase:2plus" in labs:
        return 1
    if "type:chore" in labs:
        return 3
    return {"P0": 5, "P1": 3, "P2": 2}.get(story.get("priority", "P1"), 3)


def all_stories(epics):
    """Flatten to (epic, story) with a stable sequence index."""
    out = []
    for ei, ep in enumerate(epics):
        for si, s in enumerate(ep["stories"]):
            out.append((ei, si, ep, s))
    return out


def plan_sprints(epics):
    """Dependency-ordered, capacity-packed sprints. phase:2plus -> Backlog."""
    flat = all_stories(epics)
    key_of = {f"{ep['epic']['key']}/{s['key']}": (ep, s) for _, _, ep, s in flat}
    sprintable = [(ep, s) for _, _, ep, s in flat if "phase:2plus" not in s.get("labels", [])]
    later = [(ep, s) for _, _, ep, s in flat if "phase:2plus" in s.get("labels", [])]

    # rank for tie-breaking: milestone order, priority, then declaration order
    seq = {f"{ep['epic']['key']}/{s['key']}": i for i, (_, _, ep, s) in enumerate(flat)}
    prio = {"P0": 0, "P1": 1, "P2": 2}

    def rank(ep, s):
        k = f"{ep['epic']['key']}/{s['key']}"
        return (MS_ORDER.get(ep["epic"]["milestone"], 99),
                prio.get(s.get("priority", "P1"), 1), seq[k])

    # Kahn topo sort honouring depends_on within the sprintable set
    keys = {f"{ep['epic']['key']}/{s['key']}" for ep, s in sprintable}
    indeg = {}
    deps = {}
    for ep, s in sprintable:
        k = f"{ep['epic']['key']}/{s['key']}"
        d = [x for x in s.get("depends_on", []) if x in keys]
        deps[k] = d
        indeg[k] = len(d)
    dependents = {k: [] for k in keys}
    for k, d in deps.items():
        for x in d:
            dependents[x].append(k)
    ready = sorted([k for k in keys if indeg[k] == 0], key=lambda k: rank(*key_of[k]))
    ordered = []
    while ready:
        ready.sort(key=lambda k: rank(*key_of[k]))
        k = ready.pop(0)
        ordered.append(k)
        for m in dependents[k]:
            indeg[m] -= 1
            if indeg[m] == 0:
                ready.append(m)
    # any cycle leftovers (shouldn't happen) appended by rank
    for k in keys:
        if k not in ordered:
            ordered.append(k)

    total = sum(estimate(key_of[k][1]) for k in ordered)
    cap = max(14, math.ceil(total / TARGET_SPRINTS))

    sprints, cur, load = [], [], 0
    for k in ordered:
        e = estimate(key_of[k][1])
        if cur and load + e > cap:
            sprints.append(cur)
            cur, load = [], 0
        cur.append(k)
        load += e
    if cur:
        sprints.append(cur)

    # name each sprint by its dominant milestone
    named = []
    for i, grp in enumerate(sprints, 1):
        ms = [key_of[k][0]["epic"]["milestone"] for k in grp]
        dom = max(set(ms), key=ms.count)
        label = MS_TITLE[dom].split("·", 1)[-1].split("(")[0].strip()
        named.append((f"Sprint {i:02d} — {label}", [key_of[k] for k in grp]))
    named.append(("Backlog — Phase 2+ (later)", later))
    return named, cap, total


# ---------------------------------------------------------------- content
def first_sentence(text):
    for sep in (". ", " — "):
        if sep in text:
            return text.split(sep)[0].strip() + ("." if sep == ". " else "")
    return text


def refs(s, kind):
    r = s.get("refs", {}) or {}
    v = r.get(kind, [])
    if kind == "adr":
        v = [f"ADR-{x}" for x in v]
    return v


def sec_background(ep, s):
    e = ep["epic"]
    return (f"{e['title']} — {first_sentence(e['summary'])}\n\n"
            f"As a {s['as_a']}, I want {s['i_want']}, so that {s['so_that']}.\n\n"
            f"{s['context']}")


def sec_requirements(ep, s):
    lines = [f"- {s['i_want'][0].upper() + s['i_want'][1:]}."]
    rq = refs(s, "req")
    if rq:
        lines.append(f"- Traces to requirement(s): {', '.join(rq)}.")
    if "compliance" in s.get("labels", []):
        cs = refs(s, "compliance")
        lines.append(f"- Must satisfy compliance obligation(s): {', '.join(cs) or 'see Other'}.")
    if s.get("notes"):
        lines.append(f"- Note: {s['notes']}")
    if "phase:2plus" in s.get("labels", []):
        lines.append("- Deferred (Phase 2+): placeholder — design-only for now.")
    return "\n".join(lines)


def sec_ac(s):
    return "\n".join(f"- [ ] {a}" for a in s["acceptance"])


def sec_ui(ep, s):
    k = f"{ep['epic']['key']}/{s['key']}"
    return STORY_UI.get(k, EPIC_UI.get(ep["epic"]["key"], "See prototype.html."))


def sec_tech(ep, s):
    areas = [AREA_TECH[a] for a in s.get("labels", []) if a in AREA_TECH]
    parts = []
    if areas:
        parts.append("Stack: " + "; ".join(areas) + ".")
    adrs = refs(s, "adr")
    if adrs:
        parts.append("Architecture decisions: " + ", ".join(adrs) + " (see docs/adr/decision-log.md).")
    if s.get("depends_on"):
        parts.append("Depends on: " + ", ".join(s["depends_on"]) + ".")
    if "type:spike" in s.get("labels", []):
        parts.append("Time-boxed spike — produce findings + a go/no-go, not production code.")
    return "\n".join(parts) or "High-level: standard module pattern over the shared API."


def sec_other(ep, s):
    e = ep["epic"]
    parts = [f"Epic: {e['key']} — {e['title']}.",
             f"Source PRD: {e.get('prd','')}.",
             f"Backlog key: {e['key']}/{s['key']}.",
             f"Phase: {'2+' if 'phase:2plus' in s.get('labels',[]) else e.get('phase','1')} · "
             f"Priority: {s.get('priority','P1')} · Estimate: {estimate(s)} pts."]
    cs = refs(s, "compliance")
    if cs:
        parts.append(f"Compliance criteria: {', '.join(cs)}.")
    return "\n".join(parts)


def stage_label(ep):
    return MS_TITLE[ep["epic"]["milestone"]].split("·", 1)[0].strip()


def type_label(s):
    labs = s.get("labels", [])
    if "type:spike" in labs:
        return "Spike"
    if "type:chore" in labs:
        return "Chore"
    return "Story"


def area_labels(s):
    return [a.split(":", 1)[1] for a in s.get("labels", []) if a.startswith("area:")]


# ---------------------------------------------------------------- board ops
def board_state():
    q = """query($id:[ID!]){ boards(ids:$id){ name
        groups{ id title }
        columns{ id title type } } }"""
    b = gql(q, {"id": [BOARD_ID]})["boards"][0]
    return b


def cmd_inspect():
    b = board_state()
    print(f"Board: {b['name']} (id {BOARD_ID})")
    print(f"Groups ({len(b['groups'])}):")
    for g in b["groups"]:
        print(f"  - {g['title']}  [{g['id']}]")
    print(f"Columns ({len(b['columns'])}):")
    for c in b["columns"]:
        print(f"  - {c['title']}  ({c['type']})  [{c['id']}]")


def ensure_columns(existing):
    """Create missing columns; return {title: id}."""
    by_title = {c["title"]: c["id"] for c in existing}
    for title, ctype in COLUMNS:
        if title in by_title:
            print(f"col ✓ exists  {title}")
            continue
        q = """mutation($b:ID!,$t:String!,$ct:ColumnType!){
            create_column(board_id:$b, title:$t, column_type:$ct){ id title } }"""
        d = gql(q, {"b": BOARD_ID, "t": title, "ct": ctype})
        by_title[title] = d["create_column"]["id"]
        print(f"col + created {title}")
        time.sleep(0.3)
    return by_title


def create_groups(named):
    """Create sprint groups in order; return {title: id}."""
    ids = {}
    prev = None
    for title, _items in named:
        if prev is None:
            q = """mutation($b:ID!,$t:String!){ create_group(board_id:$b, group_name:$t){ id } }"""
            d = gql(q, {"b": BOARD_ID, "t": title})
        else:
            q = """mutation($b:ID!,$t:String!,$r:String!){
                create_group(board_id:$b, group_name:$t, relative_to:$r,
                             position_relative_method:after_at){ id } }"""
            d = gql(q, {"b": BOARD_ID, "t": title, "r": prev})
        gid = d["create_group"]["id"]
        ids[title] = gid
        prev = gid
        print(f"group + {title}")
        time.sleep(0.3)
    return ids


def delete_old(old_groups, old_columns, keep_group_ids, keep_col_titles):
    for g in old_groups:
        if g["id"] in keep_group_ids:
            continue
        gql("mutation($b:ID!,$g:String!){ delete_group(board_id:$b, group_id:$g){ id } }",
            {"b": BOARD_ID, "g": g["id"]})
        print(f"group - {g['title']}")
        time.sleep(0.2)
    for c in old_columns:
        if c["title"] in keep_col_titles or c["type"] in ("name", "subtasks", "subitems"):
            continue
        try:
            gql("mutation($b:ID!,$c:String!){ delete_column(board_id:$b, column_id:$c){ id } }",
                {"b": BOARD_ID, "c": c["id"]})
            print(f"col - {c['title']}")
        except SystemExit as e:
            print(f"col - skip {c['title']} ({e})")
        time.sleep(0.2)


def cmd_rebuild():
    b = board_state()
    old_groups, old_cols = b["groups"], b["columns"]
    cols = ensure_columns(old_cols)               # create my columns first
    named, cap, total = plan_sprints(load())
    gids = create_groups(named)                   # create my groups first
    keep_titles = {t for t, _ in COLUMNS} | {"Name"}
    delete_old(old_groups, old_cols, set(gids.values()), keep_titles)
    print(f"\nRebuild done. {len(named)} groups, capacity {cap} pts/sprint, {total} pts total.")


def cmd_seed():
    b = board_state()
    cols = {c["title"]: c["id"] for c in b["columns"]}
    gids = {g["title"]: g["id"] for g in b["groups"]}
    missing = [t for t, _ in COLUMNS if t not in cols]
    if missing:
        raise SystemExit(f"Missing columns {missing}; run rebuild first.")
    named, cap, total = plan_sprints(load())
    n = 0
    for gtitle, items in named:
        gid = gids.get(gtitle)
        if not gid:
            raise SystemExit(f"Missing group '{gtitle}'; run rebuild first.")
        for ep, s in items:
            cv = {
                cols["Status"]: {"label": "Backlog"},
                cols["Type"]: {"labels": [type_label(s)]},
                cols["Epic"]: {"labels": [ep["epic"]["key"]]},
                cols["Stage"]: {"labels": [stage_label(ep)]},
                cols["Priority"]: {"label": s.get("priority", "P1")},
                cols["Estimate (pts)"]: estimate(s),
                cols["Key"]: f"{ep['epic']['key']}/{s['key']}",
                cols["Depends on"]: ", ".join(s.get("depends_on", [])),
                cols["Background"]: {"text": sec_background(ep, s)},
                cols["Requirements"]: {"text": sec_requirements(ep, s)},
                cols["Acceptance Criteria"]: {"text": sec_ac(s)},
                cols["UI / Designs"]: {"text": sec_ui(ep, s)},
                cols["Technical notes"]: {"text": sec_tech(ep, s)},
                cols["Other"]: {"text": sec_other(ep, s)},
            }
            al = area_labels(s)
            if al:
                cv[cols["Area"]] = {"labels": al}
            name = f"[{ep['epic']['key']}] {s['title']}"
            q = """mutation($b:ID!,$g:String!,$n:String!,$cv:JSON!){
                create_item(board_id:$b, group_id:$g, item_name:$n,
                            column_values:$cv, create_labels_if_missing:true){ id } }"""
            gql(q, {"b": BOARD_ID, "g": gid, "n": name, "cv": json.dumps(cv)})
            n += 1
            if n % 10 == 0:
                print(f"  …{n} items")
            time.sleep(0.35)
    print(f"Seeded {n} items across {len(named)} groups.")


def cmd_plan():
    named, cap, total = plan_sprints(load())
    print(f"Capacity {cap} pts/sprint · {total} pts total · {len(named)} groups\n")
    for title, items in named:
        pts = sum(estimate(s) for _ep, s in items)
        print(f"{title}  ({len(items)} items, {pts} pts)")
        for ep, s in items:
            print(f"    [{ep['epic']['key']}] {s['title']}  ({s.get('priority','P1')}, {estimate(s)})")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "inspect"
    {"inspect": cmd_inspect, "plan": cmd_plan, "rebuild": cmd_rebuild,
     "seed": cmd_seed, "all": lambda: (cmd_rebuild(), cmd_seed())}.get(
        cmd, lambda: (_ for _ in ()).throw(SystemExit(__doc__)))()


if __name__ == "__main__":
    main()
