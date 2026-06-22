# Visit lifecycle: per-row role-appropriate next actions

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/LIFECYCLE-ROW-ACTIONS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

As a front desk, I want each Today row to offer the next action for whoever owns the visit now, so that the team always sees the one right thing to do next.
Plainly: the per-row action buttons on the Today schedule (Confirmed / Start / Resume / Late / No-show / Profile) that surface the next legal step for the visit's current owner. Where it fits: a follow-up to the visit lifecycle basic state-machine (PRD-02/LIFECYCLE) that adds the role-aware action set on top of the status chips. Each action calls the validated transition API and reflects the consult/consent gate. It sits in Reception (PRD-02).

## How it works

The basic list shows a status chip per row; this follow-up adds the role-appropriate next action. Each 'Today's schedule' row surfaces the one next step for whoever owns it now — Confirmed, Start, Resume, Late, No-show, Profile — handing off automatically as the visit moves between roles.
Each action calls the validated transition API and is shown only when the transition is legal for the row's state and the user's role, so a user never sees an action they can't take.
The row reflects the consult/consent gate ('Awaiting consent — treatment gated until done') and deep-links to the chart/profile; everything live-updates from the transition events the basic emits.

## Requirements

- Each Today row to offer the next action for whoever owns the visit now.

## Acceptance Criteria

- [ ] Each row shows the next action for whoever owns it now (Confirmed / Start / Resume / Late / No-show / Profile).
- [ ] Each action calls the transition API and is shown only when legal for the row's state and the user's role.
- [ ] The row reflects the consult/consent gate ('Awaiting consent — treatment gated') and deep-links to chart/profile.
- [ ] Rows live-update from transition events.

## UI designs / screenshots

- Prototype: Today (dashboard.png) — each row's status chips + actions (Confirmed, Start, Late, No-show, Resume, Profile).
- Actions appear only when legal for the row's state and the user's role; rows deep-link to chart/profile.
- A gated row shows 'Awaiting consent — treatment gated'.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends LIFECYCLE)** — no new entities; derives the legal next-actions set from Appointment.status + user role + gate state
  - _Each action calls the basic's transition API; gate state from the consult/consent gates._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Per-row status chips + role-appropriate next action**
  Behaviour: each 'Today's schedule' row shows its current status chip and the next action for whoever owns it now (Confirmed / Start / Resume / Late / No-show / Profile). Requirements: each action calls the transition API and is shown only when legal for the row's state and the user's role; the row reflects the consult/consent gate ('Awaiting consent — treatment gated') and deep-links to chart/profile; live-updates from transition events.
