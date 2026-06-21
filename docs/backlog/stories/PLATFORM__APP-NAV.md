# App shell & collapsible workspace navigation

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/APP-NAV`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/WEB-SHELL`, `PRD-01/RBAC`

## Background

Platform shell, navigation & cross-cutting UX — The cross-cutting product surfaces the prototype exercises that don't belong to a single feature PRD: the app shell + collapsible workspace navigation, the role-tailored Today dashboard, global search, the in-app notification centre, the clinic switcher, the persona/active-role + scope-of-practice display, and the owner-only financial (.fin) gating that hides money figures from non-owner roles.

As a staff member, I want a navigation shell that groups screens into workspaces and only shows what my role can access, so that I find my tools fast and never see screens I can't use.

The prototype's sidebar groups screens into workspaces (Clinical, Front desk, Comms & growth, Memberships, Business, Team, Governance, Settings) plus top-level Today/Schedule/Clients/Follow-ups/Checkout, with collapsible sections and a mobile drawer. Nav entries are capability-gated (data-allow).

## Requirements

- A navigation shell that groups screens into workspaces and only shows what my role can access.
- Traces to requirement(s): REQ-TEN-3.

## Acceptance Criteria

- [ ] Top-level items (Today, Schedule, Clients, Follow-ups, Checkout) + collapsible workspaces render per the IA.
- [ ] Each nav entry is capability-gated; entries outside the user's role are hidden.
- [ ] Active screen + section state persist; mobile uses a drawer + overlay.
- [ ] A Follow-ups badge and a Governance badge show outstanding counts.

## UI designs / screenshots

prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0017 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/WEB-SHELL, PRD-01/RBAC.

## Other

Epic: PLATFORM — Platform shell, navigation & cross-cutting UX.
Source PRD: docs/ux/README.md.
Backlog key: PLATFORM/APP-NAV.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — sidebar/app shell, Today dashboard, header (global search, clinic switcher, switch-user, scope tooltip).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
