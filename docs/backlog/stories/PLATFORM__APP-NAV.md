# App shell & collapsible workspace navigation

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/APP-NAV`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/WEB-SHELL`, `PRD-01/RBAC`

## Background

As a staff member, I want a navigation shell that groups screens into workspaces and only shows what my role can access, so that I find my tools fast and never see screens I can't use.
The prototype's sidebar groups screens into workspaces (Clinical, Front desk, Comms & growth, Memberships, Business, Team, Governance, Settings) plus top-level Today/Schedule/Clients/Follow-ups/Checkout, with collapsible sections and a mobile drawer. Nav entries are capability-gated (data-allow).

## How it works

The app shell groups screens into workspaces (Clinical, Front desk, Comms & growth, Memberships, Business, Team, Governance, Settings) plus top-level Today/Schedule/Clients/Follow-ups/Checkout, with collapsible sections and a mobile drawer. Every nav entry is capability-gated (data-allow) so a role only sees what it can use.
The frame every feature screen drops into; badges show outstanding Follow-ups + Governance counts.

## Requirements

- A navigation shell that groups screens into workspaces and only shows what my role can access.

## Acceptance Criteria

- [ ] Top-level items (Today, Schedule, Clients, Follow-ups, Checkout) + collapsible workspaces render per the IA.
- [ ] Each nav entry is capability-gated; entries outside the user's role are hidden.
- [ ] Active screen + section state persist; mobile uses a drawer + overlay.
- [ ] A Follow-ups badge and a Governance badge show outstanding counts.

## UI designs / screenshots

_Prototype screen: prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip)._

- Prototype: the left sidebar (dashboard.png) — top-level items + collapsible 'Workspaces'; active screen/section persist; mobile uses a drawer + overlay.
- Follow-ups and Governance show count badges; entries outside the role are hidden.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(derived) NavModel** — from Role.capabilities -> visible nav entries + badge counts
  - _Capability-gated; no separate persistence beyond user prefs._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Web UI**
  Build on the Angular web app: the dashboard per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: the left sidebar (dashboard.png) — top-level items + collapsible 'Workspaces'; active screen/section persist; mobile uses a drawer + overlay.
  - Follow-ups and Governance show count badges; entries outside the role are hidden.
