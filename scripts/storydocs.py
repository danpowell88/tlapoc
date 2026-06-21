#!/usr/bin/env python3
"""
storydocs.py — generate the file deliverables from the backlog source of truth:

  docs/backlog/stories/<EPIC>__<STORY>.md   one file per story, in the format:
        Background · Requirements · Acceptance Criteria · UI designs / screenshots
        · Technical notes (high level) · Other · Tasks (dev pickup)
  docs/backlog/epics/<EPIC>.md              one file per epic, listing its stories
  docs/backlog/sprints.md                   ordered sequence split into sprints
  docs/backlog/INDEX.md                     index of the above

Source = docs/backlog/data/*.json (+ shared builders/tasks_for in monday.py).
Run: python scripts/storydocs.py
"""
from __future__ import annotations
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from backlog import load, MILESTONES, MS_TITLE, ROOT
from monday import (sec_ac, estimate, type_label, area_labels, stage_label,
                    plan_sprints, tasks_for, bg_text, req_bullets, ui_text,
                    tech_blocks, compliance_links, prd_link, screen_rel_path, screen_name)


def md_links(pairs):
    return ", ".join(f"[{lbl}]({url})" for lbl, url in pairs)

OUT = os.path.join(ROOT, "docs", "backlog")
STORIES = os.path.join(OUT, "stories")
EPICS = os.path.join(OUT, "epics")


def write(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text if text.endswith("\n") else text + "\n")


def story_file(ep, s):
    return f"{ep['epic']['key']}__{s['key']}.md"


def write_story(ep, s):
    e = ep["epic"]
    tks = tasks_for(ep, s)
    L = [f"# {s['title']}", ""]
    L.append(f"> **Epic:** [{e['key']} — {e['title']}](../epics/{e['key']}.md)  ·  "
             f"**Key:** `{e['key']}/{s['key']}`  ·  **Type:** {type_label(s)}  ·  "
             f"**Stage:** {stage_label(ep)}  ·  **Priority:** {s.get('priority','P1')}  ·  "
             f"**Estimate:** {estimate(s)} pts  ·  **Area:** {', '.join(area_labels(s)) or '—'}")
    if s.get("depends_on"):
        L.append(">")
        L.append("> **Depends on:** " + ", ".join(f"`{d}`" for d in s["depends_on"]))

    # Background
    L += ["", "## Background", ""] + bg_text(ep, s)

    # How it works (deep detail)
    if s.get("detail"):
        L += ["", "## How it works", ""] + list(s["detail"])

    # Requirements (+ linked compliance)
    L += ["", "## Requirements", ""]
    L += [f"- {b}" for b in req_bullets(ep, s)]
    cl = compliance_links(s)
    if cl:
        L.append(f"- Compliance: {md_links(cl)}")

    # Acceptance Criteria
    L += ["", "## Acceptance Criteria", "", sec_ac(s)]

    # UI — spec (prototype-derived) + screen pointer + inline screenshot
    uit = ui_text(ep, s)
    ui_added = False
    if s.get("ui_spec"):
        L += ["", "## UI designs / screenshots", ""]
        ui_added = True
        if uit:
            L += [f"_Prototype screen: {uit}_", ""]
        L += [f"- {b}" for b in s["ui_spec"]]
    elif uit:
        L += ["", "## UI designs / screenshots", "", uit]
        ui_added = True
    rel = screen_rel_path(ep, s)
    if rel and ui_added:
        L += ["", f"![{screen_name(ep, s)} — prototype screen]({rel})"]

    # Suggested data model
    if s.get("data_model"):
        L += ["", "## Suggested data model", ""]
        for d in s["data_model"]:
            L.append(f"- **{d['entity']}** — {d['fields']}")
            if d.get("notes"):
                L.append(f"  - _{d['notes']}_")

    # Technical notes — only if there's something to say
    tb = tech_blocks(ep, s)
    tech = []
    if tb["stack"]:
        tech.append(f"- Stack: {tb['stack']}")
    if tb["adrs"]:
        tech.append(f"- Architecture decisions: {md_links(tb['adrs'])}")
    if tb["spike"]:
        tech.append("- Time-boxed spike — produce findings + a go/no-go, not production code.")
    if tech:
        L += ["", "## Technical notes (high level)", ""] + tech

    # Other — relevant documents (PRD link) only
    pl = prd_link(ep)
    if pl:
        L += ["", "## Other", "", f"- Source PRD: [{pl[0]}]({pl[1]})"]

    L += ["", "## Tasks (dev pickup)", ""]
    for t in tks:
        note = f" — {t['note']}" if t.get("note") else ""
        L.append(f"- [ ] **{t['title']}**{note}")
    write(os.path.join(STORIES, story_file(ep, s)), "\n".join(L))
    return len(tks)


def write_epic(ep):
    e = ep["epic"]
    L = [f"# {e['key']} — {e['title']}", ""]
    L.append(f"> **Stage / Milestone:** {MS_TITLE[e['milestone']]}  ·  "
             f"**Phase:** {e.get('phase','1')}  ·  **Stories:** {len(ep['stories'])}")
    L += ["", e["summary"], ""]
    if e.get("prd"):
        L += [f"**Source PRD:** `{e['prd']}`", ""]
    L += ["## Stories", "", "| Key | Story | Type | Priority | Est | Tasks |",
          "|---|---|---|---|---|---|"]
    ntasks = 0
    for s in ep["stories"]:
        n = len(tasks_for(ep, s))
        ntasks += n
        L.append(f"| `{s['key']}` | [{s['title']}](../stories/{story_file(ep, s)}) | "
                 f"{type_label(s)} | {s.get('priority','P1')} | {estimate(s)} | {n} |")
    L += ["", f"_Totals: {len(ep['stories'])} stories · {ntasks} tasks._"]
    write(os.path.join(EPICS, f"{e['key']}.md"), "\n".join(L))


def write_sprints(epics):
    named, cap, total = plan_sprints(epics)
    sprints = [(t, items) for t, items in named if t.lower().startswith("sprint")]
    backlog = [items for t, items in named if not t.lower().startswith("sprint")]
    backlog = backlog[0] if backlog else []

    L = ["# Sprint plan & sequencing", ""]
    L.append("> Generated from `docs/backlog/data/*.json`. Regenerate with "
             "`python scripts/storydocs.py`.")
    L += ["",
          "**Assumptions.** One developer, AI-assisted, ~1–2 days/week (a side project — "
          "elapsed time is not the constraint). Sprints are *work-sized*, not calendar-boxed: "
          f"~{cap} story points each (≈5–6 items). Sequencing is dependency-ordered "
          "(a story never precedes something it depends on) and grouped by delivery stage.",
          "",
          f"**Totals.** {sum(len(i) for _t, i in sprints)} scheduled stories across "
          f"{len(sprints)} sprints (~{total} pts), plus {len(backlog)} deferred items in the backlog.",
          "",
          "## Sequence rationale", "",
          "1. **Sprints 1–5 — Sprint 0 foundations:** repo/CI/CD/IaC, Postgres+RLS, auth wiring, "
          "API/web/app shells, design system, observability, security + the de-risk spikes. Nothing "
          "clinical ships until the platform is safe to build on.",
          "2. **Foundations & tenancy:** RBAC + scope-of-practice, the canInject gate, audit, "
          "retention, breach, sign-in/MFA and owner-only financial gating — unblocks everything.",
          "3. **Booking → intake/consent:** front-of-house + the pre-visit gates.",
          "4. **Consult → prescribing → S4 → charting:** the compliance moat and the clinical record.",
          "5. **Commerce, comms & integrations**, then **reporting & the apps**, then "
          "**facility & complaints**.",
          "6. **Backlog (Phase 2+):** deferred placeholders, pulled forward only if the case appears.",
          "",
          "## Sprints", "",
          "| Sprint | Theme | Items | Points |", "|---|---|---|---|"]
    for i, (title, items) in enumerate(sprints, 1):
        theme = title.split("—", 1)[-1].strip()
        pts = sum(estimate(s) for _e, s in items)
        L.append(f"| {i:02d} | {theme} | {len(items)} | {pts} |")
    L.append("")

    for i, (title, items) in enumerate(sprints, 1):
        pts = sum(estimate(s) for _e, s in items)
        L += ["", f"### {title}  ·  {len(items)} items · {pts} pts", ""]
        L.append("| Story | Epic | Type | Pri | Est | Depends on |")
        L.append("|---|---|---|---|---|---|")
        for ep, s in items:
            deps = ", ".join(s.get("depends_on", [])) or "—"
            L.append(f"| [{s['title']}](stories/{story_file(ep, s)}) | {ep['epic']['key']} | "
                     f"{type_label(s)} | {s.get('priority','P1')} | {estimate(s)} | {deps} |")

    if backlog:
        bpts = sum(estimate(s) for _e, s in backlog)
        L += ["", f"### Backlog — Phase 2+ (later)  ·  {len(backlog)} items · {bpts} pts", "",
              "| Story | Epic | Pri | Est |", "|---|---|---|---|"]
        for ep, s in backlog:
            L.append(f"| [{s['title']}](stories/{story_file(ep, s)}) | {ep['epic']['key']} | "
                     f"{s.get('priority','P1')} | {estimate(s)} |")
    write(os.path.join(OUT, "sprints.md"), "\n".join(L))


def write_index(epics):
    L = ["# Backlog index", "",
         "- [Sprint plan & sequencing](sprints.md)",
         "- [Full backlog (generated)](README.md)", "",
         "## Epics", "", "| Epic | Stage | Stories |", "|---|---|---|"]
    for ep in epics:
        e = ep["epic"]
        L.append(f"| [{e['key']} — {e['title']}](epics/{e['key']}.md) | "
                 f"{stage_label(ep)} | {len(ep['stories'])} |")
    write(os.path.join(OUT, "INDEX.md"), "\n".join(L))


def main():
    epics = load()
    for d in (STORIES, EPICS):
        if os.path.isdir(d):
            shutil.rmtree(d)
        os.makedirs(d)
    ns = nt = 0
    for ep in epics:
        write_epic(ep)
        for s in ep["stories"]:
            nt += write_story(ep, s)
            ns += 1
    write_sprints(epics)
    write_index(epics)
    print(f"Wrote {len(epics)} epic files, {ns} story files ({nt} tasks), sprints.md, INDEX.md")


if __name__ == "__main__":
    main()
