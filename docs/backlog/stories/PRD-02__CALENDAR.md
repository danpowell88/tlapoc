# Multi-resource calendar (practitioner + room)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/ROSTER`

## Background

As a front desk, I want a day/week/room calendar showing practitioners and rooms with correct service durations and buffers, so that I can run the diary at a glance and book without clashes.
The multi-resource calendar is the first feature built in Reception (PRD-02), the front-of-house entry point to a visit, and sits directly on top of Foundations (PRD-01) — it consumes the practitioner roster and the canInject (the derived gate deciding whether a staff member may administer injectables right now) scope-of-practice gate. It is the diary that every other booking surface draws on. In the build timeline it comes after the platform and Foundations are in place and before everything else in Reception: the booking wizard, online self-booking, walk-ins and the visit lifecycle all reuse the availability engine this story creates, and it precedes the Intake/Consent gating (PRD-03) that runs between booking and treatment. As front desk, I want a day/week/room calendar showing practitioners and rooms with correct service durations and buffers, so that I can run the diary at a glance and book without clashes.  Front desk needs a fast day/week/room calendar with service durations, buffers and rosters — the core of the diary.

## How it works

The calendar is the operational heart of reception: a multi-resource diary that books a practitioner AND a room/chair/device together, with every service carrying its real duration plus buffer/processing/turnaround so back-to-back bookings reflect the room actually being cleaned and the toxin settling, not just chair time.
Availability is never raw roster. It is the intersection of (a) the practitioner's RosterShift for the day (PRD-01/ROSTER), minus TimeOff and existing appointments, with (b) the practitioner's canInject capability for the service's schedule class, AND (c) a free room/chair/device for the whole block including buffers. An uncredentialled or unrostered staffer is simply not offered for an injectable. Drag-to-move recomputes the same intersection at the drop target and flags a clash on room/chair/device before it commits.
The week grid surfaces operational signal the front desk runs on: per-day appointment counts, per-treatment-type counts (anti-wrinkle / filler / skin / consult), chairs-booked utilisation %, idle chair-hours, and amber quiet-window cells that can be back-filled (feeds WAITLIST/REMINDERS recall).

## Requirements

- A day/week/room calendar showing practitioners and rooms with correct service durations and buffers.

## Acceptance Criteria

- [ ] Resources = practitioner + room; service durations include buffer/processing/turnaround.
- [ ] Day, week and room views render; rosters and time-off block availability.
- [ ] Drag to move an appointment; conflicts on room/chair/device are flagged.
- [ ] Per-day and per-treatment-type counts + utilisation surfaced.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Schedule (schedule.png) — Day/Week toggle, week-range stepper, '+ New' opens the booking wizard. Practitioner/day columns with hourly rows; appointment blocks are colour-coded by treatment type with a legend (anti-wrinkle / filler / skin / consult) and carry the client name, type and status icons.
- Summary strip above the grid: total appointments (14), chairs booked (68%), idle chair time (~12h), and per-type counts as chips.
- Open cells render as bookable; quiet/amber cells are flagged 'quiet — fill'; tap an appointment to open the move/cancel modal; in move mode, valid drop targets show a dashed add-location affordance and conflicting room/chair/device usage is flagged inline.
- Unrostered periods and TimeOff render as unavailable (not bookable); a 'Quiet windows to fill' panel lists open chairs per day with an 'Offer recall' / 'Fill' action.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Appointment** — id, tenant_id, location_id, client_id, service_id, practitioner_id, room_id, start, end, status, reason, source(online|desk|walkin), tags[]
  - _Status drives the visit lifecycle (LIFECYCLE); colour in the grid is derived from service.treatment_type._
- **Resource** — id, tenant_id, location_id, type(room|chair|device), name, status(active|maintenance)
  - _Booked alongside the practitioner and conflict-checked for the whole block incl. buffers; maps to the prototype's 'Rm 1/2/3'._
- **Service (ref)** — duration, buffer, processing_time, turnaround, schedule(S4|non-S4), eligible_roles[]
  - _Owned by SERVICE-CATALOGUE; supplies block length + scope class._
- **(derived) Availability** — = RosterShift − TimeOff − existing Appointments, ∩ canInject(service.schedule), ∩ free Resource for the block
  - _The single function that feeds the slot picker, the wizard and online booking; recomputed on drag-drop._

## Technical notes (high level)

- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Calendar header & date navigation**
  Behaviour: a sticky header with Today / prev / next, a date picker and a range label that reflects the active view; remembers the last-used date+view per user. Requirements: jumping to any date re-queries that range; Today resets to the current day; keyboard shortcuts (t=today, arrows=step). The header drives every other element on the screen (the grid, filters and quiet-windows all react to the selected range).
- [ ] **Day / week view toggle & time-axis layout**
  Behaviour: switch between a single-day and a Mon-Fri week layout; the time axis spans configured opening hours with off-hours visually muted; selectable slot interval (e.g. 15 min). Requirements: the choice persists per user; week view collapses resource columns into day columns; closed days/public holidays render non-bookable.
- [ ] **Resource & practitioner filters**
  Behaviour: filter the visible columns by practitioner, room and treatment type (multi-select), plus a 'my schedule' quick filter. Requirements: filters compose (AND); only practitioners rostered for the range are offered (reads the roster); the active filter set persists in the URL/state so a refresh or share keeps it.
- [ ] **Multi-resource grid & occupancy rendering**
  Behaviour: columns are practitioner x room resources; each appointment renders in its slot and consumes BOTH a practitioner and a room; the grid shows occupancy density and flags conflicts/double-books. Requirements: a booking is valid only if both resources are free; scope-of-practice (the canInject gate) is reflected so non-injectors are never shown as available for S4 work; conflicts are visually unmistakable.
- [ ] **Slot interaction: drag-to-book, move & resize**
  Behaviour: click an empty slot to start a booking; drag an appointment to move it; resize to change duration; everything snaps to the slot interval. Requirements: availability (practitioner scope + room free + roster) is re-checked server-side on drop and the move is rejected with a reason if invalid; optimistic UI updates immediately then confirms or rolls back.
- [ ] **Appointment cards & status colours**
  Behaviour: each card shows client, treatment and status (booked / confirmed / arrived / in-progress / complete / cancelled / no-show) with a colour legend and quick actions. Requirements: status drives the colour; clicking opens the appointment detail; a no-show raises a follow-up job (PRD-07); arrived/in-progress feed the check-in and treatment-room surfaces.
