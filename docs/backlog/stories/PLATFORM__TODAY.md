# Role-tailored Today dashboard

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/TODAY`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`

## Background

Platform shell, navigation & cross-cutting UX — The cross-cutting product surfaces the prototype exercises that don't belong to a single feature PRD: the app shell + collapsible workspace navigation, the role-tailored Today dashboard, global search, the in-app notification centre, the clinic switcher, the persona/active-role + scope-of-practice display, and the owner-only financial (.fin) gating that hides money figures from non-owner roles.

As a staff member, I want a Today landing page showing the live state of the clinic and what needs my attention, tailored to my role, so that I start the day knowing exactly what to do.

The prototype opens on a Today board: waiting / in-room / checked-out columns, the day's appointments, the jobs/needs-attention digest and alerts — tailored to the signed-in role's 'concerns' (ADR-0017).

## Requirements

- A Today landing page showing the live state of the clinic and what needs my attention, tailored to my role.
- Traces to requirement(s): REQ-RPT-5.

## Acceptance Criteria

- [ ] Today shows waiting / in-room / checked-out and the day's schedule at a glance.
- [ ] The content is role-tailored by concern (e.g. reception sees front-desk tasks, NP sees clinical).
- [ ] Surfaces the follow-up/needs-attention digest and key alerts (expiries, failed payments).
- [ ] Quick links jump to chart/profile/checkout for in-flight visits.

## UI designs / screenshots

prototype.html — Today (waiting / in-room / checked-out).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0017 (see docs/adr/decision-log.md).
Depends on: PLATFORM/APP-NAV.

## Other

Epic: PLATFORM — Platform shell, navigation & cross-cutting UX.
Source PRD: docs/ux/README.md.
Backlog key: PLATFORM/TODAY.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Today (waiting / in-room / checked-out).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
