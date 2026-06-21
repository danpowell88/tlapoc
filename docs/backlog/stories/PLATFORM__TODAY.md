# Role-tailored Today dashboard

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/TODAY`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PLATFORM/APP-NAV`

## Background

As a staff member, I want a Today landing page showing the live state of the clinic and what needs my attention, tailored to my role, so that I start the day knowing exactly what to do.
The prototype opens on a Today board: waiting / in-room / checked-out columns, the day's appointments, the jobs/needs-attention digest and alerts — tailored to the signed-in role's 'concerns' (ADR-0017).

## How it works

The Today landing shows the live state of the clinic — waiting / in-room / checked-out and the day's schedule — tailored to the signed-in role's concerns (ADR-0017), plus the follow-up/needs-attention digest and key alerts (expiries, failed payments). Quick links jump to chart/profile/checkout for in-flight visits.
Each role starts the day knowing exactly what to do.

## Requirements

- A Today landing page showing the live state of the clinic and what needs my attention, tailored to my role.

## Acceptance Criteria

- [ ] Today shows waiting / in-room / checked-out and the day's schedule at a glance.
- [ ] The content is role-tailored by concern (e.g. reception sees front-desk tasks, NP sees clinical).
- [ ] Surfaces the follow-up/needs-attention digest and key alerts (expiries, failed payments).
- [ ] Quick links jump to chart/profile/checkout for in-flight visits.

## UI designs / screenshots

_Prototype screen: prototype.html — Today (waiting / in-room / checked-out)._

- Prototype: Today (dashboard.png) — waiting/in-room/checked-out columns, the day at a glance, role-tailored widgets, and the exceptions digest.
- Reception sees front-desk tasks; NP sees clinical; owner sees the business digest.

## Suggested data model

- **(read) TodayBoard** — from Appointment.status + Job + AttentionDigest, filtered by role concern
  - _Role-tailored; read aggregation._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Today (waiting / in-room / checked-out).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
