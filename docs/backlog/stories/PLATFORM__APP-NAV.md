# App shell & collapsible workspace navigation

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/APP-NAV`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/WEB-SHELL`, `PRD-01/RBAC`

## Background

As a staff member, I want a navigation shell that groups screens into workspaces and only shows what my role can access, so that I find my tools fast and never see screens I can't use.
The prototype's sidebar groups screens into workspaces (Clinical, Front desk, Comms & growth, Memberships, Business, Team, Governance, Settings) plus top-level Today/Schedule/Clients/Follow-ups/Checkout, with collapsible sections and a mobile drawer. Nav entries are capability-gated (data-allow).

## How it works

The app shell is the frame every feature screen drops into. The prototype sidebar groups screens into collapsible workspaces — Clinical (Charting, Stock & medicines, Forms & consent, Treatment menu, Skin/Body/Complication/Imaging sub-screens), Front desk/Operations (Open-close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log), Comms & growth (Inbox, Automations, Campaigns, Leads, Reviews), Memberships, Business (Reports, Finance), Team (Roster, People & credentials, Compliance board), Governance (Overview, AE & DAEN, Recalls, Policies, Audit pack) and Settings — plus the top-level items Today, Schedule, Clients, Follow-ups and Checkout.
Every nav entry is capability-gated: the prototype tags each with data-allow and setPersona() shows/hides it from the active role's capabilities + concerns, then hides any workspace section whose children are all hidden. So a role only ever sees what it can use (an RN doesn't see Finance or Settings; Reception doesn't see Charting) — gating is sourced from RBAC, not hard-coded per item. This is presentation; the server-side capability check (RBAC) is the actual control.
Active screen + section open/closed state persist (user prefs); on mobile the sidebar becomes a drawer with an overlay (toggleNav). The Follow-ups item and the Governance item carry live count badges (the prototype shows the red Governance count and a Follow-ups job count) so outstanding work is visible from anywhere.
Edge cases: a role with no children in a section never sees the empty section header; switching active role (MULTI-ROLE/ROLE-CONTEXT) re-derives the visible nav immediately; deep-linking to a screen the role can't access falls back gracefully (the server still blocks the data).

## Requirements

- A navigation shell that groups screens into workspaces and only shows what my role can access.

## Acceptance Criteria

- [ ] Top-level items (Today, Schedule, Clients, Follow-ups, Checkout) + collapsible workspaces render per the IA.
- [ ] Each nav entry is capability-gated; entries outside the user's role are hidden.
- [ ] Active screen + section state persist; mobile uses a drawer + overlay.
- [ ] A Follow-ups badge and a Governance badge show outstanding counts.

## UI designs / screenshots

_Prototype screen: prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip)._

- Prototype: the left sidebar (dashboard.png) — clinic context at top, top-level items (Today, Schedule, Clients, Follow-ups with job badge, Checkout) and collapsible Workspaces sections; the active item is highlighted and section state persists; mobile uses a drawer + overlay.
- Each entry is capability-gated (data-allow); entries/sections outside the role are hidden entirely.
- Follow-ups and Governance show live count badges of outstanding items.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(derived) NavModel** — from Role.capabilities + concerns -> visible nav entries + section visibility + badge counts (Follow-ups, Governance)
  - _Capability-gated; derived from the RBAC session context, not separately persisted. Only user prefs (active screen, section open/closed) persist._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Capability-gated app shell, collapsible workspaces & badges**
  Build the shell on the Sprint-0 web shell: top-level items (Today/Schedule/Clients/Follow-ups/Checkout) + collapsible workspace sections per the IA, with the active item highlighted and section open/closed + active screen persisted as user prefs. Derive each entry's visibility from the caller's capabilities/concerns (from the RBAC session context — not hard-coded), and hide any section whose children are all hidden. Render live count badges on Follow-ups and Governance. Mobile: drawer + overlay. Re-derive nav on active-role switch (ROLE-CONTEXT).
