#!/usr/bin/env python3
"""
backlog.py — single tool that turns the structured backlog under
docs/backlog/data/*.json into:

  render      docs/backlog/README.md   (human-readable, reviewable)
  csv         docs/backlog/backlog.csv (import into Jira/Linear/Trello/Notion)
  labels      create/update GitHub labels                (needs: repo scope)
  milestones  create GitHub milestones                   (needs: repo scope)
  issues      create epic + story issues (idempotent)     (needs: repo scope)
  project     create a GitHub Project (v2) + add items    (needs: project scope)
  all-repo    labels + milestones + issues
  verify      print a summary of what exists on GitHub

Data is the source of truth. Re-running is safe: issues are matched by a hidden
marker in the body (<!-- tla-backlog: EPIC/STORY -->) and updated, not duplicated.

Usage:
  python scripts/backlog.py render
  python scripts/backlog.py all-repo            # labels + milestones + issues
  python scripts/backlog.py issues --dry-run
  python scripts/backlog.py project
"""
from __future__ import annotations
import csv as csvmod
import glob
import json
import os
import subprocess
import sys
import tempfile
import time

REPO = "danpowell88/tlapoc"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_GLOB = os.path.join(ROOT, "docs", "backlog", "data", "*.json")
README = os.path.join(ROOT, "docs", "backlog", "README.md")
CSVOUT = os.path.join(ROOT, "docs", "backlog", "backlog.csv")
STATE = os.path.join(ROOT, "scripts", ".backlog-state.json")
PROJECT_TITLE = "TLA Platform — Delivery"

# ---------------------------------------------------------------- milestones
# id -> (title, description). Order = delivery sequence (honours PRD deps).
MILESTONES = [
    ("M0", "M0 · Sprint 0 — Foundations & setup",
     "Technical enablement before feature work: repos, CI/CD, environments (AU East), "
     "auth wiring, data + RLS baseline, API/web/app shells, design system, observability, "
     "security baseline, and the de-risk spikes. Phase 0."),
    ("M1", "M1 · Foundations & tenancy (PRD-01)",
     "Multi-tenant domain core: tenancy/RLS, RBAC + scope-of-practice, audit, retention & "
     "destruction, breach workflow, privacy rights. Unblocks everything."),
    ("M2", "M2 · Booking, CRM, intake & consent (PRD-02, PRD-03)",
     "Front-of-house + pre-visit: scope-aware calendar/booking, client 360, then digital "
     "intake, BDD screen, versioned e-consent, image-use consent, cooling-off and gating."),
    ("M3", "M3 · Consult, prescribing, S4 & charting (PRD-04, PRD-05)",
     "The compliance moat + the clinical record: synchronous consult, individual Rx, S4 "
     "medicines governance, injection mapping, photos, immutable notes, adverse events."),
    ("M4", "M4 · Commerce, comms & integrations (PRD-06, PRD-07, PRD-10)",
     "In-person POS, memberships/autopay, non-S4 rewards; reminders/aftercare/recall; "
     "Xero + calendar sync."),
    ("M5", "M5 · Reporting & apps (PRD-08, PRD-09)",
     "Business + compliance dashboards and exports; the Flutter client & provider apps."),
    ("M6", "M6 · Facility & complaints (PRD-11)",
     "Facility accreditation, infection-control logs, emergency kit, complaints register "
     "(lightweight in v1)."),
    ("M7", "M7 · Phase 2+ (later / placeholders)",
     "Deliberately deferred capability — tracked as placeholders so scope is visible and "
     "can be pulled forward."),
]
MS_TITLE = {mid: title for mid, title, _ in MILESTONES}

# ---------------------------------------------------------------- labels
LABELS = {
    "type:epic":        ("6f42c1", "A PRD-sized body of work; parent of stories"),
    "type:story":       ("0e8a16", "A user-facing slice with acceptance criteria"),
    "type:spike":       ("fbca04", "Time-boxed investigation / de-risk"),
    "type:chore":       ("c2e0c6", "Setup / plumbing / non-user-facing"),
    "type:task":        ("bfdadc", "A discrete task under a story"),
    "phase:0":          ("d4c5f9", "Sprint 0 / foundations"),
    "phase:1":          ("c5def5", "v1 — anti-wrinkle end-to-end"),
    "phase:2plus":      ("e4e669", "Deferred — later"),
    "area:backend":     ("1d76db", ".NET API / domain"),
    "area:web":         ("0052cc", "Angular admin / front-desk / public booking"),
    "area:client-app":  ("5319e7", "Flutter client app"),
    "area:provider-app":("8b1fa9", "Flutter provider app"),
    "area:infra":       ("0b5394", "Azure, CI/CD, environments"),
    "area:data":        ("006b75", "Postgres, RLS, data model, read models"),
    "area:design":      ("d93f0b", "Design system / UX"),
    "area:integration": ("2188ff", "Xero, calendar, SMS, telehealth, devices"),
    "compliance":       ("b60205", "Carries a regulatory / AHPRA / TGA obligation"),
    "priority:P0":      ("b60205", "Must — blocks the build"),
    "priority:P1":      ("fbca04", "Should — core v1"),
    "priority:P2":      ("0e8a16", "Could — v1 nice-to-have / fast-follow"),
    "spike":            ("fbca04", "De-risk investigation"),
}
# PRD/epic key labels are added dynamically (one per epic key).
EPIC_KEY_COLOR = "ededed"


# ---------------------------------------------------------------- helpers
def run(args, check=True, capture=True):
    res = subprocess.run(args, capture_output=capture, text=True)
    if check and res.returncode != 0:
        sys.stderr.write(f"$ {' '.join(args)}\n{res.stdout}\n{res.stderr}\n")
        raise SystemExit(res.returncode)
    return res


def load():
    epics = []
    for path in sorted(glob.glob(DATA_GLOB)):
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
        doc["_file"] = os.path.basename(path)
        epics.append(doc)
    if not epics:
        raise SystemExit(f"No data files found at {DATA_GLOB}")
    return epics


def load_state():
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def save_state(state):
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2)


def marker(epic_key, story_key):
    return f"<!-- tla-backlog: {epic_key}/{story_key} -->"


def refs_line(refs):
    if not refs:
        return ""
    parts = []
    for label, key in (("REQ", "req"), ("Compliance", "compliance"),
                       ("ADR", "adr"), ("PRD AC", "prd_ac")):
        vals = refs.get(key)
        if vals:
            if key == "adr":
                vals = [f"ADR-{v}" for v in vals]
            parts.append(f"**{label}:** {', '.join(vals)}")
    return " · ".join(parts)


def story_body(epic, story):
    e = epic["epic"]
    lines = []
    lines.append(f"**Epic:** {e['key']} — {e['title']}  ·  "
                 f"**Milestone:** {MS_TITLE[e['milestone']]}  ·  "
                 f"**Priority:** {story.get('priority', 'P1')}")
    lines.append("")
    lines.append(f"**Context.** {story['context']}")
    lines.append("")
    lines.append(f"**Story.** As a **{story['as_a']}**, I want {story['i_want']}, "
                 f"so that {story['so_that']}.")
    lines.append("")
    lines.append("**Acceptance criteria**")
    for ac in story["acceptance"]:
        lines.append(f"- [ ] {ac}")
    rl = refs_line(story.get("refs"))
    if rl:
        lines.append("")
        lines.append(rl)
    if story.get("depends_on"):
        lines.append("")
        lines.append(f"**Depends on:** {', '.join(story['depends_on'])}")
    if story.get("notes"):
        lines.append("")
        lines.append(f"**Notes.** {story['notes']}")
    lines.append("")
    lines.append(f"_Source: [{os.path.basename(e['prd'])}]"
                 f"(../{os.path.relpath(os.path.join(ROOT, e['prd']), os.path.join(ROOT, 'docs', 'backlog'))})_"
                 if e.get("prd") else "")
    lines.append(marker(e["key"], story["key"]))
    return "\n".join(lines).strip() + "\n"


def epic_body(epic, child_lines=None):
    e = epic["epic"]
    lines = [f"**Milestone:** {MS_TITLE[e['milestone']]}  ·  **Phase:** {e.get('phase','1')}",
             "", e["summary"], ""]
    if e.get("prd"):
        lines.append(f"**Source PRD:** `{e['prd']}`")
        lines.append("")
    if child_lines:
        lines.append("## Stories")
        lines.extend(child_lines)
        lines.append("")
    lines.append(marker(e["key"], "EPIC"))
    return "\n".join(lines).strip() + "\n"


def all_labels(epics):
    labs = dict(LABELS)
    for ep in epics:
        labs[ep["epic"]["key"]] = (EPIC_KEY_COLOR, f"{ep['epic']['title']}")
    return labs


# ---------------------------------------------------------------- commands
def cmd_render(epics):
    out = []
    out.append("# Backlog — The Lounge Aesthetics Platform\n")
    out.append("> **Generated file.** Source of truth is `docs/backlog/data/*.json`. "
               "Regenerate with `python scripts/backlog.py render`. "
               "Seed GitHub with `python scripts/backlog.py all-repo`.\n")
    out.append("This backlog slices the 11 PRDs (+ a Sprint 0) into **epics** and **stories**. "
               "Every story carries context, a user story, acceptance criteria (its definition "
               "of done) and traceability back to `REQ-*` / `C*` / `ADR-*`.\n")

    # milestone overview
    out.append("## Delivery stages (milestones)\n")
    out.append("| # | Milestone | What lands |")
    out.append("|---|-----------|------------|")
    for mid, title, desc in MILESTONES:
        out.append(f"| {mid} | {title.split(' · ',1)[-1]} | {desc} |")
    out.append("")

    # counts
    n_epics = len(epics)
    n_stories = sum(len(e["stories"]) for e in epics)
    out.append(f"**{n_epics} epics · {n_stories} stories.**\n")

    # label legend
    out.append("## Labels\n")
    out.append("Type: `type:epic` `type:story` `type:spike` `type:chore` · "
               "Phase: `phase:0` `phase:1` `phase:2plus` · "
               "Area: `area:backend` `area:web` `area:client-app` `area:provider-app` "
               "`area:infra` `area:data` `area:design` `area:integration` · "
               "Priority: `priority:P0/P1/P2` · plus `compliance` and a per-epic key label.\n")

    # per epic
    for ep in epics:
        e = ep["epic"]
        out.append("---\n")
        out.append(f"## {e['key']} — {e['title']}")
        out.append(f"*{MS_TITLE[e['milestone']]} · Phase {e.get('phase','1')} · "
                   f"{len(ep['stories'])} stories*\n")
        out.append(e["summary"] + "\n")
        for s in ep["stories"]:
            out.append(f"### {s['key']} — {s['title']}")
            out.append(f"`{s.get('priority','P1')}` · {', '.join(s.get('labels', []))}\n")
            out.append(f"{s['context']}\n")
            out.append(f"> **As a {s['as_a']}**, I want {s['i_want']}, so that {s['so_that']}.\n")
            out.append("**Acceptance criteria**\n")
            for ac in s["acceptance"]:
                out.append(f"- [ ] {ac}")
            rl = refs_line(s.get("refs"))
            if rl:
                out.append(f"\n{rl}")
            if s.get("depends_on"):
                out.append(f"\n**Depends on:** {', '.join(s['depends_on'])}")
            out.append("")
    with open(README, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out).rstrip() + "\n")
    print(f"Wrote {README}  ({n_epics} epics, {n_stories} stories)")


def cmd_csv(epics):
    with open(CSVOUT, "w", newline="", encoding="utf-8") as fh:
        w = csvmod.writer(fh)
        w.writerow(["Type", "Key", "Title", "Epic", "Milestone", "Priority",
                    "Labels", "AsA", "IWant", "SoThat", "Acceptance", "Refs", "DependsOn"])
        for ep in epics:
            e = ep["epic"]
            w.writerow(["Epic", e["key"], e["title"], "", MS_TITLE[e["milestone"]],
                        "", " ".join(e.get("labels", [])), "", "", "", "", "", ""])
            for s in ep["stories"]:
                w.writerow(["Story", s["key"], s["title"], e["key"], MS_TITLE[e["milestone"]],
                            s.get("priority", "P1"), " ".join(s.get("labels", [])),
                            s.get("as_a", ""), s.get("i_want", ""), s.get("so_that", ""),
                            " | ".join(s["acceptance"]), refs_line(s.get("refs")).replace("**", ""),
                            " ".join(s.get("depends_on", []))])
    print(f"Wrote {CSVOUT}")


def cmd_labels(epics):
    for name, (color, desc) in all_labels(epics).items():
        run(["gh", "label", "create", name, "--repo", REPO, "--color", color,
             "--description", desc[:100], "--force"])
        print(f"label  ✓ {name}")


def existing_milestones():
    res = run(["gh", "api", f"repos/{REPO}/milestones?state=all&per_page=100"])
    return {m["title"]: m["number"] for m in json.loads(res.stdout)}


def cmd_milestones(_epics):
    have = existing_milestones()
    for _mid, title, desc in MILESTONES:
        if title in have:
            print(f"milestone ✓ (exists) {title}")
            continue
        run(["gh", "api", f"repos/{REPO}/milestones", "-f", f"title={title}",
             "-f", f"description={desc}"])
        print(f"milestone ✓ (created) {title}")


def find_issue_by_marker(mark):
    """Return issue number whose body contains the marker, else None."""
    res = run(["gh", "issue", "list", "--repo", REPO, "--state", "all",
               "--search", mark, "--json", "number,body", "--limit", "50"], check=False)
    if res.returncode != 0:
        return None
    try:
        for it in json.loads(res.stdout):
            if mark in (it.get("body") or ""):
                return it["number"]
    except json.JSONDecodeError:
        return None
    return None


def create_or_update(title, body, labels, milestone, state, key, dry):
    mark = body.strip().splitlines()[-1]
    num = state.get(key) or find_issue_by_marker(mark)
    bf = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
    bf.write(body)
    bf.close()
    try:
        if num:
            if dry:
                print(f"  would UPDATE #{num}  {title}")
            else:
                args = ["gh", "issue", "edit", str(num), "--repo", REPO,
                        "--body-file", bf.name, "--milestone", milestone]
                for l in labels:
                    args += ["--add-label", l]
                run(args)
                print(f"  updated #{num}  {title}")
        else:
            if dry:
                print(f"  would CREATE        {title}")
                num = f"DRY-{key}"
            else:
                args = ["gh", "issue", "create", "--repo", REPO, "--title", title,
                        "--body-file", bf.name, "--milestone", milestone]
                for l in labels:
                    args += ["--label", l]
                res = run(args)
                url = res.stdout.strip().splitlines()[-1]
                num = int(url.rsplit("/", 1)[-1])
                print(f"  created #{num}  {title}")
                time.sleep(1.5)  # be gentle with secondary rate limits
    finally:
        os.unlink(bf.name)
    state[key] = num
    return num


def cmd_issues(epics, dry=False):
    state = load_state()
    for ep in epics:
        e = ep["epic"]
        print(f"\n== {e['key']} — {e['title']} ==")
        # epic first (so stories can reference it)
        epic_num = create_or_update(
            f"[EPIC] {e['key']} — {e['title']}",
            epic_body(ep),
            e.get("labels", []), MS_TITLE[e["milestone"]],
            state, f"{e['key']}/EPIC", dry)
        child = []
        for s in ep["stories"]:
            num = create_or_update(
                f"[{e['key']}] {s['title']}",
                story_body(ep, s),
                s.get("labels", []), MS_TITLE[e["milestone"]],
                state, f"{e['key']}/{s['key']}", dry)
            child.append(f"- [ ] {'#'+str(num) if isinstance(num,int) else num} {s['title']}")
        if not dry:
            save_state(state)
            # refresh epic body with the child checklist
            if isinstance(epic_num, int):
                bf = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8")
                bf.write(epic_body(ep, child))
                bf.close()
                run(["gh", "issue", "edit", str(epic_num), "--repo", REPO, "--body-file", bf.name])
                os.unlink(bf.name)
    if not dry:
        save_state(state)
    print("\nDone." + ("  (dry-run)" if dry else ""))


def cmd_project(epics, dry=False):
    # needs `project` scope: gh auth refresh -s project
    check = run(["gh", "project", "list", "--owner", "danpowell88", "--format", "json"],
                check=False)
    if check.returncode != 0:
        print("Cannot access Projects v2 — missing scope.\n"
              "Run:  gh auth refresh -s project\n"
              "then: python scripts/backlog.py project")
        return
    state = load_state()
    nums = sorted({v for v in state.values() if isinstance(v, int)})
    if not nums:
        print("No issues created yet — run `issues` first.")
        return
    # find or create project
    projs = json.loads(check.stdout).get("projects", [])
    proj = next((p for p in projs if p["title"] == PROJECT_TITLE), None)
    if not proj:
        if dry:
            print(f"would CREATE project '{PROJECT_TITLE}'")
            return
        res = run(["gh", "project", "create", "--owner", "danpowell88",
                   "--title", PROJECT_TITLE, "--format", "json"])
        proj = json.loads(res.stdout)
        print(f"created project: {proj.get('url')}")
    else:
        print(f"project exists: {proj.get('url')}")
    pnum = str(proj["number"])
    failed = []
    for n in nums:
        url = f"https://github.com/{REPO}/issues/{n}"
        if dry:
            print(f"  would add #{n}")
            continue
        res = run(["gh", "project", "item-add", pnum, "--owner", "danpowell88", "--url", url],
                  check=False)
        if res.returncode != 0:
            failed.append(n)
        time.sleep(0.4)  # pace GraphQL mutations
    print(f"Added {len(nums) - len(failed)} / {len(nums)} issues to project {PROJECT_TITLE}.")
    if failed:
        print(f"Failed (re-run `project` to retry, item-add is idempotent): {failed}")


def cmd_verify(_epics):
    print("Milestones:")
    for t in existing_milestones():
        print("  ", t)
    res = run(["gh", "issue", "list", "--repo", REPO, "--state", "all",
               "--search", "tla-backlog", "--json", "number", "--limit", "500"], check=False)
    try:
        print(f"Backlog issues on GitHub: {len(json.loads(res.stdout))}")
    except Exception:
        print("Backlog issues on GitHub: (could not count)")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "render"
    dry = "--dry-run" in sys.argv
    epics = load()
    if cmd == "render":
        cmd_render(epics); cmd_csv(epics)
    elif cmd == "csv":
        cmd_csv(epics)
    elif cmd == "labels":
        cmd_labels(epics)
    elif cmd == "milestones":
        cmd_milestones(epics)
    elif cmd == "issues":
        cmd_issues(epics, dry)
    elif cmd == "project":
        cmd_project(epics, dry)
    elif cmd == "all-repo":
        cmd_labels(epics); cmd_milestones(epics); cmd_issues(epics, dry)
    elif cmd == "verify":
        cmd_verify(epics)
    else:
        print(__doc__)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
