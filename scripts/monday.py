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
    ("Type", "status"),
    ("Epic (tag)", "dropdown"),
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

# Clinic-first delivery order (overrides milestone order for sequencing/sprints):
# reception → injectables → compliance → some reporting FIRST;
# payments, comms, integrations, apps & client-facing come much later.
EPIC_TRACK = {
    "SPRINT-0": 1,   # engineering foundations & setup
    "PRD-01": 2,     # tenancy, RBAC, credentials, audit (compliance core)
    "PLATFORM": 3,   # staff app shell, Today, nav, financial gating
    "PRD-02": 4,     # reception: booking, calendar, clients, check-in
    "PRD-03": 5,     # intake, consent & gating (compliance)
    "PRD-04": 6,     # injectables: consult, prescribing, S4 governance
    "PRD-05": 7,     # injectables: clinical charting
    "PRD-08": 8,     # reporting & compliance dashboards
    "PRD-11": 9,     # facility, infection-control & complaints (compliance)
    "PRD-06": 10,    # payments, memberships & rewards
    "PRD-07": 11,    # comms, reminders, recall & growth
    "PRD-10": 12,    # integrations: Xero & calendar (later)
    "PRD-09": 13,    # apps (Flutter client & provider) (much later)
    "PHASE-2": 99,   # deferred placeholders
}
EPIC_THEME = {
    "SPRINT-0": "Setup", "PRD-01": "Foundations", "PLATFORM": "App shell",
    "PRD-02": "Reception", "PRD-03": "Consent", "PRD-04": "Injectables",
    "PRD-05": "Charting", "PRD-08": "Reporting", "PRD-11": "Compliance ops",
    "PRD-06": "Payments", "PRD-07": "Comms & growth", "PRD-10": "Integrations",
    "PRD-09": "Apps", "PHASE-2": "Backlog",
}

# ---- story -> prototype screen PNG (captured by capture.py; committed under docs/backlog/screens)
SCREENS_RAW_BASE = "https://raw.githubusercontent.com/danpowell88/tlapoc/main/docs/backlog/screens"
EPIC_SCREEN = {
    "SPRINT-0": None, "PRD-01": None, "PRD-02": "schedule", "PRD-03": "forms-consent",
    "PRD-04": "stock", "PRD-05": "charting", "PRD-06": "checkout", "PRD-07": "marketing-inbox",
    "PRD-08": "reports", "PRD-09": "client-app", "PRD-10": "settings-integrations",
    "PRD-11": "ops-openclose", "PLATFORM": "dashboard", "PHASE-2": None,
}
SCREEN_OVERRIDE = {
    "PRD-01/CREDENTIALS": "team-people", "PRD-01/REG-WATCH": "team-compliance",
    "PRD-01/ROSTER": "team-roster", "PRD-01/CLIENT-CORE": "client-360",
    "PRD-01/PRIVACY-RIGHTS": "client-app",
    "PRD-02/BOOKING-WIZARD": "booking-wizard", "PRD-02/ONLINE-BOOK": "public-booking",
    "PRD-02/CLIENT-360": "client-360", "PRD-02/CLIENT-DIR": "clients",
    "PRD-02/SERVICE-CATALOGUE": "clinical-menu", "PRD-02/CONSULT-GATE": "charting",
    "PRD-02/LIFECYCLE": "dashboard", "PRD-02/DEPOSITS": None,
    "PRD-03/GATING": "charting",
    "PRD-04/COLD-CHAIN": "ops-monitors", "PRD-04/RECALL-LOOKUP": "gov-recalls",
    "PRD-04/ADMIN-GATE": "charting", "PRD-04/CONSULT": "charting",
    "PRD-04/PRESCRIPTION": "charting", "PRD-04/MODE-B": None,
    "PRD-05/PHOTOS": "clinical-imaging", "PRD-05/OFFLINE": "treatment-room",
    "PRD-05/ADVERSE-EVENT": "clinical-safety", "PRD-05/SKIN-ANALYSIS": "clinical-skin",
    "PRD-05/BODY-CONTOURING": "clinical-body", "PRD-05/COMPLICATION-LIBRARY": "clinical-safety",
    "PRD-05/OUTCOMES": "clinical-imaging", "PRD-05/MODALITY": "clinical-body",
    "PRD-05/MAPPING": "charting",
    "PRD-06/PACKAGES-GIFT": "memb-gifts", "PRD-06/MEMBERSHIP": "memb-members",
    "PRD-06/REWARDS-ENGINE": "memb-loyalty", "PRD-06/MARGIN-RULES": "memb-pricing",
    "PRD-06/PRICING-WHATIF": "memb-pricing", "PRD-06/REFERRALS": "memb-referrals",
    "PRD-07/FOLLOWUPS": "followups", "PRD-07/RECALL": "followups",
    "PRD-07/AUTOMATIONS": "marketing-auto", "PRD-07/REMINDERS-CARE": "marketing-auto",
    "PRD-07/CAMPAIGNS": "marketing-camp", "PRD-07/REVIEWS": "growth-reviews",
    "PRD-07/LEADS-CRM": "growth-leads", "PRD-07/BOOKING-PAGE": "settings-booking",
    "PRD-07/MARKETING-CONSENT": "settings-booking", "PRD-07/CHANNELS": None,
    "PRD-08/COMPLIANCE-DASH": "gov-overview", "PRD-08/DAEN": "gov-ae",
    "PRD-08/INSPECTION-PACK": "gov-audit", "PRD-08/POLICIES": "gov-policies",
    "PRD-08/TRUE-COST": "finance", "PRD-08/ATTENTION-DIGEST": "dashboard",
    "PRD-08/READ-MODELS": None,
    "PRD-09/PROVIDER-DAY": "treatment-room", "PRD-09/PROVIDER-ROOMSIDE": "treatment-room",
    "PRD-09/PROVIDER-OFFLINE": "treatment-room", "PRD-09/CHECKIN-KIOSK": "checkin",
    "PRD-09/BACKOFFICE-TABLET": "backroom", "PRD-09/APP-DISTRIBUTION": None,
    "PRD-11/TEMP-MONITORS": "ops-monitors", "PRD-11/ROOMS-DEVICES": "ops-resources",
    "PRD-11/EQUIPMENT": "ops-equipment", "PRD-11/CALL-LOG": "ops-phone",
    "PRD-11/SHIFT-HANDOVER": "backroom", "PRD-11/COMPLAINTS": "gov-overview",
    "PRD-11/EMERGENCY-KIT": "clinical-safety", "PRD-11/FACILITY": "ops-equipment",
    "PRD-11/FAC-WORKFLOWS": "ops-equipment",
    "PLATFORM/FIN-GATING": "finance",
}


def screen_for(epic_key, story_key):
    k = f"{epic_key}/{story_key}"
    return SCREEN_OVERRIDE[k] if k in SCREEN_OVERRIDE else EPIC_SCREEN.get(epic_key)


def screen_name(ep, s):
    return screen_for(ep["epic"]["key"], s["key"])


def screen_raw_url(ep, s):
    sc = screen_name(ep, s)
    return f"{SCREENS_RAW_BASE}/{sc}.png" if sc else None


def screen_rel_path(ep, s):
    sc = screen_name(ep, s)
    return f"../screens/{sc}.png" if sc else None

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
        return (EPIC_TRACK.get(ep["epic"]["key"], 50),
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
        eks = [key_of[k][0]["epic"]["key"] for k in grp]
        dom = min(eks, key=lambda e: (-eks.count(e), EPIC_TRACK.get(e, 50)))
        label = EPIC_THEME.get(dom, dom)
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


def _accept(s, n=3):
    return list(s.get("acceptance", []))[:n]


def _dm_note(s):
    real = [e for e in (s.get("data_model") or []) if not e["entity"].startswith("(")]
    if not real:
        return "Define/extend persistence for this story; EF Core migrations; every table tenant_id + RLS."
    out = ["Model + migrate (EF Core; every table carries tenant_id with an RLS policy):"]
    for e in real:
        out.append(f"- {e['entity']} — {e['fields']}" + (f" ({e['notes']})" if e.get("notes") else ""))
    out.append("- Add the FKs/relationships above; index the columns this story filters or looks up on; "
               "make records append-only/immutable where the story requires it.")
    return "\n".join(out)


def _readmodel_note(s):
    reads = [e for e in (s.get("data_model") or [])
             if e["entity"].lower().startswith("(read") or "reportingview" in e["entity"].lower()]
    shape = reads[0]["fields"] if reads else "the metrics this screen shows"
    return ("Build a materialised read-model/projection (don't query OLTP directly):\n"
            f"- Shape: {shape}.\n"
            "- Populate from domain events + the audit stream; eventual consistency is fine; support rebuild/backfill.\n"
            "- Expose a query API with this story's date/role filters; respect owner-only .fin gating.")


def _backend_note(ep, s):
    out = ["Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):",
           "- Endpoints: the commands + queries for the entities above and each action in the acceptance criteria."]
    for a in _accept(s, 3):
        out.append(f"- Rule: {a}")
    out.append("- Emit domain events for read-models / notifications / follow-up jobs where relevant.")
    out.append("- Publish the OpenAPI contract so the generated clients update.")
    if s.get("depends_on"):
        out.append("- Depends on: " + ", ".join(s["depends_on"]) + ".")
    return "\n".join(out)


def _compliance_note(s):
    cs = ", ".join(refs(s, "compliance")) or "the relevant criteria"
    out = [f"Enforce {cs} as a server-side invariant that cannot be bypassed via the API:",
           "- Block the action when prerequisites are missing; return a clear reason for the blocked-action "
           "banner (what's blocked / which rule / how to resolve / who can resolve).",
           "- Write an immutable AuditEvent for the attempt and its outcome."]
    for a in [a for a in s.get("acceptance", []) if any(
            w in a.lower() for w in ("block", "cannot", "reject", "valid", "consent", "immutab", "gate", "only"))][:3]:
        out.append(f"- {a}")
    return "\n".join(out)


def _integration_note(ep, s):
    return ("Implement the provider behind its swappable port:\n"
            "- Connection/config (OAuth tokens stored encrypted) + the field mapping this story needs.\n"
            "- Trigger on the relevant event; idempotent sync with retries, back-off and a visible reconciliation/status.\n"
            "- Handle partial failures + replays; surface errors to the user.\n"
            "- Residency: AU-resident or APP-8-assessed + consented before any PII leaves (C21).")


def _ui_note(ep, s, platform):
    out = [f"Build on {platform}: the {screen_name(ep, s) or 'screen'} per the UI spec. Wire to the API with "
           "loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / "
           "gate chips where gated; respect owner-only .fin gating for money figures."]
    spec = s.get("ui_spec") or []
    if spec:
        out.append("Key elements (from the prototype):")
        out += [f"- {b}" for b in spec[:5]]
    return "\n".join(out)


def _design_note(s):
    return ("Build/extend the shared design-system component(s) this story needs (use tokens, not bespoke CSS); "
            "cover all states + accessibility (contrast, focus order, hit-target size); document in the gallery.")


def _offline_note(s):
    return ("Offline-tolerant capture (provider app):\n"
            "- Encrypted on-device queue for drafts + pending media; last-write-wins for drafts.\n"
            "- Sync on reconnect with no data loss; finalisation happens server-side.\n"
            "- Persistent sync indicator (queued count + last-sync); finalise disabled until synced.")


def _chore_note(s):
    out = ["Deliver per the acceptance criteria:"]
    out += [f"- {a}" for a in _accept(s, 4)]
    return "\n".join(out)


def tasks_for(ep, s):
    """Dev-task breakdown for a story. A hand-authored s['tasks'] override wins."""
    if s.get("tasks"):
        return s["tasks"]
    labs = s.get("labels", [])
    areas = area_labels(s)
    text = (s.get("context", "") + " " + " ".join(s.get("acceptance", []))).lower()
    out = []

    def add(title, note=""):
        out.append({"title": title, "note": note})

    if "type:spike" in labs:
        add("Define spike scope, questions & success criteria",
            "List the unknowns to resolve and the pass/fail bar before building; time-box it.")
        add("Build a throwaway prototype",
            "Smallest end-to-end slice that answers the questions (not production code); measure the risky bits.")
        add("Write up findings + go/no-go recommendation (ADR if warranted)",
            "What worked, the gotchas, the chosen approach + its impact on the dependent stories.")
        return out

    if "phase:2plus" in labs:
        add("Scope & design when pulled into a sprint",
            "Deferred placeholder — no build in v1; confirm it still fits scope/regulatory stance, then break down.")
        return out

    if "type:chore" in labs:
        add(f"Implement: {s['title']}", _chore_note(s))
        if "area:infra" in labs:
            add("Wire into CI/CD + per-environment config",
                "Build/test/deploy steps + env-specific config & secrets; required for merge.")
        if "area:data" in labs:
            add("Apply via migrations; verify RLS/tenancy",
                "Migration runs per environment; prove tenant isolation holds.")
        add("Document setup & usage", "How to run/operate it; runbook notes for the team.")
        return _dedup(out, 4)

    # regular feature story — full slice (UI -> API -> DB -> integrations), coarse, tests implicit
    dm = s.get("data_model") or []
    real = [e for e in dm if not e["entity"].startswith("(")]
    read_model = any(e["entity"].lower().startswith("(read") or "reportingview" in e["entity"].lower()
                     for e in dm)
    integ = "area:integration" in labs
    if real:
        add("Data model & migrations", _dm_note(s))
    elif read_model:
        add("Read-model / projection", _readmodel_note(s))
    if "area:backend" in labs or (real and not integ):
        add("Backend: domain logic, rules & API endpoint(s)", _backend_note(ep, s))
    if "compliance" in labs:
        add("Enforce compliance gate + audit events", _compliance_note(s))
    if integ:
        add("Integration adapter, sync & config", _integration_note(ep, s))
    if "area:web" in labs:
        add("Web UI", _ui_note(ep, s, "the Angular web app"))
    if "area:client-app" in labs:
        add("Client app UI (Flutter)", _ui_note(ep, s, "the Flutter client app"))
    if "area:provider-app" in labs:
        add("Provider app UI (Flutter)", _ui_note(ep, s, "the Flutter provider app"))
    if "area:design" in labs:
        add("Design-system component(s)", _design_note(s))
    if "offline" in text or ("queue" in text and "sync" in text):
        add("Offline queue + sync handling", _offline_note(s))
    out = _dedup(out, 6)
    if not out:
        add(f"Implement: {s['title']}", _chore_note(s))
    return out


def _dedup(tasks, cap):
    seen, out = set(), []
    for t in tasks:
        if t["title"] in seen:
            continue
        seen.add(t["title"])
        out.append(t)
    return out[:cap]


# ---- clean, link-aware content helpers (used by storydocs.py + jira.py) ------
REPO_BLOB = "https://github.com/danpowell88/tlapoc/blob/main"


def is_ui(s):
    return any(a in s.get("labels", []) for a in
              ("area:web", "area:client-app", "area:provider-app", "area:design"))


def adr_links(s):
    raw = (s.get("refs", {}) or {}).get("adr", [])
    return [(f"ADR-{x}", f"{REPO_BLOB}/docs/adr/decision-log.md") for x in raw]


def compliance_links(s):
    return [(c, f"{REPO_BLOB}/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria")
            for c in refs(s, "compliance")]


def prd_link(ep):
    p = ep["epic"].get("prd")
    return (os.path.basename(p), f"{REPO_BLOB}/{p}") if p else None


def bg_text(ep, s):
    return [f"As a {s['as_a']}, I want {s['i_want']}, so that {s['so_that']}.",
            s["context"]]


def req_bullets(ep, s):
    bs = [s["i_want"][0].upper() + s["i_want"][1:] + "."]
    if s.get("notes"):
        bs.append(s["notes"])
    if "phase:2plus" in s.get("labels", []):
        bs.append("Deferred (Phase 2+): placeholder, design-only for now.")
    return bs


def ui_text(ep, s):
    return sec_ui(ep, s) if (is_ui(s) or f"{ep['epic']['key']}/{s['key']}" in STORY_UI) else None


def tech_blocks(ep, s):
    # Stack (.NET/Angular/Flutter/Postgres/Azure) is a platform-wide given — not repeated per story.
    # Only story-specific technical info: the relevant ADRs and the spike caveat.
    return {"adrs": adr_links(s), "spike": "type:spike" in s.get("labels", [])}


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


def create_groups(named, existing_titles=()):
    """Create sprint groups in order (idempotent); return {title: id} for created."""
    ids = {}
    prev = None
    for title, _items in named:
        if title in existing_titles:
            print(f"group ✓ exists {title}")
            prev = None
            continue
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


PROTECTED_COL_TYPES = ("name", "item_id", "subtasks", "subitems")


def delete_columns(old_columns, keep=()):
    """Wipe non-protected columns for a clean slate (but keep my own)."""
    for c in old_columns:
        if c["type"] in PROTECTED_COL_TYPES or c["title"] in keep:
            continue
        try:
            gql("mutation($b:ID!,$c:String!){ delete_column(board_id:$b, column_id:$c){ id } }",
                {"b": BOARD_ID, "c": c["id"]})
            print(f"col - {c['title']}")
        except SystemExit as e:
            print(f"col - skip {c['title']} ({str(e)[:60]})")
        time.sleep(0.2)


def delete_groups(old_groups):
    for g in old_groups:
        try:
            gql("mutation($b:ID!,$g:String!){ delete_group(board_id:$b, group_id:$g){ id } }",
                {"b": BOARD_ID, "g": g["id"]})
            print(f"group - {g['title']}")
        except SystemExit as e:
            print(f"group - skip {g['title']} ({str(e)[:60]})")
        time.sleep(0.2)


def cmd_rebuild():
    named, cap, total = plan_sprints(load())
    my_cols = {t for t, _ in COLUMNS}
    b = board_state()
    # 1. columns: wipe template (keep mine), then create mine clean
    delete_columns(b["columns"], keep=my_cols)
    ensure_columns(board_state()["columns"])
    # 2. groups: clean reset in correct order via a temp group (board never hits zero)
    tmp = gql("mutation($b:ID!){ create_group(board_id:$b, group_name:\"_tmp\"){ id } }",
              {"b": BOARD_ID})["create_group"]["id"]
    delete_groups([g for g in board_state()["groups"] if g["id"] != tmp])
    create_groups(named)                                       # all fresh, ordered
    delete_groups([g for g in board_state()["groups"] if g["id"] == tmp])
    print(f"\nRebuild done. {len(named)} groups, capacity {cap} pts/sprint, {total} pts total.")


def clear_items():
    """Delete all items on the board so seed is safe to re-run."""
    d = gql("query($id:[ID!]){ boards(ids:$id){ items_page(limit:200){ cursor items{ id } } } }",
            {"id": [BOARD_ID]})
    page = d["boards"][0]["items_page"]
    items, cursor = page["items"], page["cursor"]
    while cursor:
        nd = gql("query($c:String!){ next_items_page(limit:200, cursor:$c){ cursor items{ id } } }",
                 {"c": cursor})
        items += nd["next_items_page"]["items"]
        cursor = nd["next_items_page"]["cursor"]
    for it in items:
        gql("mutation($i:ID!){ delete_item(item_id:$i){ id } }", {"i": it["id"]})
        time.sleep(0.1)
    if items:
        print(f"cleared {len(items)} existing items")


def cmd_seed():
    b = board_state()
    cols = {c["title"]: c["id"] for c in b["columns"]}
    gids = {g["title"]: g["id"] for g in b["groups"]}
    missing = [t for t, _ in COLUMNS if t not in cols]
    if missing:
        raise SystemExit(f"Missing columns {missing}; run rebuild first.")
    clear_items()
    named, cap, total = plan_sprints(load())
    n = 0
    for gtitle, items in named:
        gid = gids.get(gtitle)
        if not gid:
            raise SystemExit(f"Missing group '{gtitle}'; run rebuild first.")
        for ep, s in items:
            cv = {
                cols["Status"]: {"label": "Backlog"},
                cols["Type"]: {"label": type_label(s)},
                cols["Epic (tag)"]: {"labels": [ep["epic"]["key"]]},
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
