# Walk-ins, same-day add-ons & resources

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WALKINS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want to add walk-ins and same-day add-ons against available rooms/chairs/devices, so that we capture opportunistic demand without breaking the rules or double-booking resources.
Walk-ins and same-day add-ons let Reception (PRD-02) capture opportunistic demand at the desk. The story sits on top of the calendar (PRD-02/CALENDAR) — reusing its availability engine and room/chair/device resources — and the visit lifecycle, and is deliberately gate-respecting: nothing about a walk-in bypasses scope-of-practice or the compliance gates.  In the flow it complements scheduled and online bookings: an injectable walk-in still feeds the consult gate (PRD-02/CONSULT-GATE) and the Intake/Consent step (PRD-03) before any treatment, exactly as a planned injectable booking would.  As front desk, I want to add walk-ins and same-day add-ons against available rooms/chairs/devices, so that we capture opportunistic demand without breaking the rules or double-booking resources.  Walk-ins and same-day add-ons are supported but gate-respecting (an injectable walk-in still needs a consult first); room/chair/device resources are scheduled with conflict-flagging.

## How it works

Walk-ins and same-day add-ons let the clinic capture opportunistic demand, but they are gate-respecting: an injectable walk-in still needs a synchronous consult before charting (the CONSULT-GATE applies regardless of source=walkin), and still requires consent (PRD-03). The walk-in flow attaches/creates the client, picks an available practitioner+resource and books source=walkin.
Rooms/chairs/devices are scheduled as Resources with conflict-flagging and utilisation — a same-day add-on must land on a free resource for its whole block (incl. buffers); conflicts are surfaced BEFORE confirmation. VIP and first-time appointment tags are supported and shown on the appointment.
This reuses the calendar's availability engine and the visit lifecycle; nothing about walk-ins bypasses scope or the compliance gates.

## Requirements

- To add walk-ins and same-day add-ons against available rooms/chairs/devices.

## Acceptance Criteria

- [ ] Walk-in and same-day add-on flows exist; an injectable walk-in still requires a consult first.
- [ ] Room/chair/device resources are bookable with conflict-flagging and utilisation.
- [ ] VIP / first-time appointment tags supported.
- [ ] Resource conflicts are surfaced before confirmation.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Schedule (schedule.png) — add walk-in / same-day add-on against an available resource (the grid shows a 'Walk-in NEW · Skin' block); resource conflicts flagged before confirm; VIP / first-time appointment tags on the appointment.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Appointment** — (as CALENDAR) source=walkin; tags[](vip|first_time)
  - _Injectable walk-in still requires consult_id before charting (CONSULT-GATE) and consent (PRD-03)._
- **Resource (ref)** — free/busy for the block incl. buffers
  - _Conflict-checked before a walk-in/add-on confirms; surfaces utilisation._

## Technical notes (high level)

- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Walk-in / same-day add-on booking flow (gate-respecting)**
  Quick-add flow from the Schedule that attaches an existing or new client, picks a free practitioner+resource via the availability engine, and books source=walkin. For S4 (Schedule 4 prescription-only medicine) services, the resulting appointment still carries the consult gate (consult_id null ⇒ charting blocked) and requires consent — walk-ins never bypass C1/C5. Same-day add-on appends a service to an in-progress visit on a free resource.
- [ ] **Resource conflict-flagging before confirm + tags**
  Before a walk-in/add-on confirms, check the chosen room/chair/device is free for the whole block incl. buffers and surface any conflict inline (block confirm until resolved). Support appointment tags[] (vip, first_time) set at booking and rendered on the calendar block. Feed resource utilisation.
- [ ] **Walk-in UI on the Schedule grid**
  Render walk-in blocks distinctly (e.g. 'Walk-in NEW') and add the quick-add affordance from an open/quiet cell. Show VIP/first-time tags. Surface the conflict warning before confirmation. Reuse the move/cancel modal.
