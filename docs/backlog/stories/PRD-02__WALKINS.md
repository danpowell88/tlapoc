# Walk-ins, same-day add-ons & resources

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WALKINS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want to add walk-ins and same-day add-ons against available rooms/chairs/devices, so that we capture opportunistic demand without breaking the rules or double-booking resources.
Walk-ins and same-day add-ons are supported but gate-respecting (an injectable walk-in still needs a consult first); room/chair/device resources are scheduled with conflict-flagging.

## How it works

Walk-ins and same-day add-ons are supported but gate-respecting: an injectable walk-in still needs a consult first. Rooms/chairs/devices are scheduled as resources with conflict-flagging and utilisation; VIP/first-time tags supported.
Lets the clinic capture opportunistic demand without breaking the rules or double-booking.

## Requirements

- To add walk-ins and same-day add-ons against available rooms/chairs/devices.

## Acceptance Criteria

- [ ] Walk-in and same-day add-on flows exist; an injectable walk-in still requires a consult first.
- [ ] Room/chair/device resources are bookable with conflict-flagging and utilisation.
- [ ] VIP / first-time appointment tags supported.
- [ ] Resource conflicts are surfaced before confirmation.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Schedule (schedule.png) — add walk-in / same-day add-on against an available resource; resource conflicts flagged before confirm; VIP / first-time appointment tags.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Appointment** — (as CALENDAR) source=walkin; tags[](vip|first_time)
  - _Injectable walk-in still requires consult_id before charting._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Appointment — (as CALENDAR) source=walkin; tags[](vip|first_time) (Injectable walk-in still requires consult_id before charting.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Walk-in and same-day add-on flows exist; an injectable walk-in still requires a consult first.
  - Rule: Room/chair/device resources are bookable with conflict-flagging and utilisation.
  - Rule: VIP / first-time appointment tags supported.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-02/CALENDAR.
- [ ] **Web UI**
  Build on the Angular web app: the schedule per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Schedule (schedule.png) — add walk-in / same-day add-on against an available resource; resource conflicts flagged before confirm; VIP / first-time appointment tags.
