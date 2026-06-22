# Multi-resource calendar (practitioner + room)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/ROSTER`

## Background

As a front desk, I want a day/week/room calendar showing practitioners and rooms with correct service durations and buffers, so that I can run the diary at a glance and book without clashes.
Front desk needs a fast day/week/room calendar with service durations, buffers and rosters — the core of the diary.

## How it works

The calendar is the operational heart of reception: a multi-resource diary (practitioner + room/chair/device) that the whole front desk runs from. Service durations include buffer/processing/turnaround so back-to-back bookings are realistic.
Availability is derived from roster intersected with canInject (PRD-01), so only rostered, cleared practitioners are offered — injectables never offer an uncredentialed staffer. Drag-to-move rebooks; room/device conflicts are flagged.

## Requirements

- A day/week/room calendar showing practitioners and rooms with correct service durations and buffers.

## Acceptance Criteria

- [ ] Resources = practitioner + room; service durations include buffer/processing/turnaround.
- [ ] Day, week and room views render; rosters and time-off block availability.
- [ ] Drag to move an appointment; conflicts on room/chair/device are flagged.
- [ ] Per-day and per-treatment-type counts + utilisation surfaced.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Schedule (schedule.png) — day/week/room views with practitioner columns; appointment blocks colour-coded by type/status.
- Per-day and per-treatment-type counts + utilisation; quiet-window fill suggestions.
- Drag an appointment to move it; conflicting room/chair/device usage is flagged inline.
- Time-off and unrostered periods render as unavailable.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Appointment** — id, tenant_id, location_id, client_id, service_id, practitioner_id, room_id, start, end, status, reason, source(online|desk|walkin)
  - _Status drives the visit lifecycle (LIFECYCLE)._
- **Resource** — id, tenant_id, type(room|chair|device), name, status
  - _Booked alongside the practitioner; conflict-checked._
- **(derived) Availability** — = RosterShift - TimeOff - existing appts, intersected with canInject + resource free
  - _Feeds the slot picker._

## Technical notes (high level)

- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Appointment — id, tenant_id, location_id, client_id, service_id, practitioner_id, room_id, start, end, status, reason, source(online|desk|walkin) (Status drives the visit lifecycle (LIFECYCLE).)
  - Resource — id, tenant_id, type(room|chair|device), name, status (Booked alongside the practitioner; conflict-checked.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Resources = practitioner + room; service durations include buffer/processing/turnaround.
  - Rule: Day, week and room views render; rosters and time-off block availability.
  - Rule: Drag to move an appointment; conflicts on room/chair/device are flagged.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/ROSTER.
- [ ] **Web UI**
  Build on the Angular web app: the schedule per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Schedule (schedule.png) — day/week/room views with practitioner columns; appointment blocks colour-coded by type/status.
  - Per-day and per-treatment-type counts + utilisation; quiet-window fill suggestions.
  - Drag an appointment to move it; conflicting room/chair/device usage is flagged inline.
  - Time-off and unrostered periods render as unavailable.
