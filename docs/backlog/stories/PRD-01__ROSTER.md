# Rosters & engagement type

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/ROSTER`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/CREDENTIALS`

## Background

As a manager, I want to record staff rosters/time-off and each person's engagement type, so that booking availability reflects who is actually working and cleared.
Plainly: this records who is working when, and combines that with who is cleared to treat, to decide who can actually be booked. It sits in Foundations just after credentials. The diary (the Reception epic that comes next) reads directly from it, so it can only ever offer a slot backed by a rostered, cleared practitioner — this story unblocks booking availability. A roster (plus employee/contractor engagement type) drives booking availability and feeds commission/pay attribution downstream.

## How it works

The roster records who is working when, per staff member and location, plus time-off/leave. It is the source of truth for booking availability (ADR-0029): a practitioner is bookable for a service if and only if they are rostered at that location that day AND they are scope/credential-compliant for the service (canInject (the derived cleared-to-inject gate) from CREDENTIALS for S4 (Schedule 4 prescription-only medicine)). The prototype encodes this as a weekly grid (rosterMap) plus a leave list, with the banner 'only practitioners rostered & compliant appear as bookable'.
Availability is therefore roster shifts, minus approved time-off, intersected with canInject — the diary (PRD-02) only ever offers slots backed by a rostered, cleared practitioner, so it can't double-book or schedule a non-compliant or off injector.
Engagement type (employee/contractor) is recorded per staff member (it already lives on StaffProfile from CREDENTIALS) for downstream commission/pay attribution and the contractor compliance banner (ADR-0027) — the platform attributes revenue by engagement type but is explicitly not a payroll/super engine.
Management is capability-gated: Owner/Lead manage the roster and approve leave; Reception is read-only (it needs to see who's in, not edit shifts). All roster and leave changes are audited.

## Requirements

- To record staff rosters/time-off and each person's engagement type.

## Acceptance Criteria

- [ ] Rosters and time-off are recorded per staff member and location.
- [ ] Booking availability is derived from roster ∩ canInject (consumed by PRD-02).
- [ ] Engagement type (employee/contractor) is recorded per staff member.
- [ ] Roster changes are audited.

## UI designs / screenshots

- Prototype: Team -> Roster & leave (team-roster.png) — a weekly grid (Mon-Fri columns x practitioner rows) with shaded rostered cells, and a Leave list below (e.g. 'Dr Lena Park · Annual leave · Thu 26 – Fri 27 Jun · Pending', 'Chloe Adams · Personal · Mon 23 Jun · Approved') with status chips.
- Banner states the rule: the roster is the source of truth for booking availability; only rostered & compliant practitioners appear as bookable (ADR-0029).
- Owner/Lead can edit shifts and approve/decline leave; Reception sees it read-only.

![team-roster — prototype screen](../screens/team-roster.png)

## Suggested data model

- **RosterShift** — id, tenant_id, staff_id, location_id, start, end, role
  - _Availability = shifts - approved time-off, intersected with canInject for the service scope._
- **TimeOff** — id, tenant_id, staff_id, kind(annual|personal|other), start, end, status(pending|approved|declined), approved_by
  - _Approved leave blocks availability; pending does not yet block but is visible._

## Technical notes (high level)

- Architecture decisions: [ADR-0028](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0029](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Roster & leave model + availability derivation**
  Model RosterShift (per staff + location) and TimeOff with an approval status, all tenant_id + RLS (row-level security). Compute bookable availability as shifts minus approved leave, intersected with the canInject (the derived cleared-to-inject gate)/scope check for the requested service — and expose it as the query PRD-02 booking consumes so it cannot offer a slot for an off or non-compliant practitioner. Record engagement type usage for downstream attribution (it lives on StaffProfile). Audit every roster/leave change and leave approval.
- [ ] **Roster & leave UI (Team workspace)**
  Build Team -> Roster & leave (team-roster.png): the weekly grid (day columns x practitioner rows) with editable rostered cells and the Leave list with pending/approved status chips and approve/decline actions. Show the ADR-0029 availability banner. Owner/Lead edit; Reception read-only (capability-gate to team:manage for edits, read for frontdesk). No payroll/commission UI here — attribution is downstream (ADR-0027).
