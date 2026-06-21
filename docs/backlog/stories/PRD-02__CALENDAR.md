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

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
