# Visit lifecycle — basic status state-machine

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/LIFECYCLE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want a clear visit status flow with check-in, an in-room-now indicator and late/no-show flags, so that the team always knows where each client is in the visit.
The visit lifecycle is the status spine that carries a client through a visit in Reception (PRD-02): it turns a booking made on the calendar (PRD-02/CALENDAR) into a tracked journey from arrival to checkout, and is what the Today board, reminders and the consent/consult gates all read. It sits after the calendar and before reminders (PRD-02/REMINDERS) and waitlist backfill in the clinic-first flow; downstream it also feeds the check-in kiosk (PRD-09) and the no-show follow-up jobs in Comms (PRD-07). As front desk, I want a clear visit status flow with check-in, an in-room-now indicator and late/no-show flags, so that the team always knows where each client is in the visit.  Bookings move through booked → reminded → checked-in → in-room → checked-out, with late/no-show flags and role hand-offs (REQ-BOOK-7).

## How it works

The visit is the spine that carries the client between roles (ADR-0024). The Appointment is a state machine — booked → reminded/confirmed → checked-in → in-room (in treatment) → for-checkout → checked-out/done (→ recall) — and each state surfaces the next action for whoever is responsible now, handing off automatically (reception flags late/no-show; a clinician starts treatment; finalise sets for-checkout, lighting up reception's queue).
Reception flags late attendance and no-show; a no-show auto-creates a follow-up CALL job (PRD-07 jobs queue) so it is never lost. An 'in-room now' indicator shows who is being treated with quick links to their chart/profile. (Small clinics may skip a formal check-in — late/no-show are the flags that matter.)
Booking captures new-vs-returning (full intake vs quick re-screen), reason/notes and respects the practitioner roster — these drive recall, reporting and the intake send. Every transition is audited via VisitEvent.

## Requirements

- A clear visit status flow with check-in, an in-room-now indicator and late/no-show flags.

## Acceptance Criteria

- [ ] Status state-machine with role hand-offs; check-in on arrival.
- [ ] An 'in-room now' indicator with quick links to chart/profile.
- [ ] Late and no-show flags; a no-show raises a follow-up call (feeds PRD-07 jobs).
- [ ] New-vs-returning, reason and roster captured on the booking.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Today (dashboard.png) — KPI tiles (appointments, checked in, awaiting consent, stock, follow-ups); 'Today's schedule' with a 'WITH YOU NOW' in-room strip (client + Open chart/Profile), and each row showing status chips + actions: Confirmed, Start, Late, No-show, Resume, Profile.
- Status chips per appointment; check-in on arrival; late/no-show flags; a no-show row links into Follow-ups.
- 'Awaiting consent — treatment gated until done' tile ties the lifecycle to the gates.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **Appointment.status** — booked|reminded|checked_in|in_room|for_checkout|checked_out|late|no_show|cancelled
  - _State machine with role hand-offs (ADR-0024); transitions validated server-side; no_show raises a Job (PRD-07)._
- **VisitEvent** — id, tenant_id, appointment_id, from_status, to_status, at, actor_id
  - _Append-only audit trail of the visit's transitions._
- **Appointment (booking fields)** — new_or_returning, reason, practitioner_id
  - _Captured at booking; drives intake type (full vs re-screen), recall and reporting._

## Technical notes (high level)

- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Visit state-machine + transition API (server-validated)**
  Behaviour: model Appointment.status as a state machine (booked→reminded→checked_in→in_room→for_checkout→checked_out, plus late/no_show/cancelled) with role hand-offs. Requirements: transition endpoints validate legal transitions server-side and reject illegal ones; each write appends a VisitEvent (from/to/actor/at) to the audit stream; every transition emits a domain event (a fact emitted when something happens in the system) for the Today board, reminders and read models (a query-optimised view built from domain events).
- [ ] **Minimal Today list with check-in (per-row status chips)**
  Behaviour: a 'Today's schedule' list where each row shows its current status chip and a check-in-on-arrival action driving the transition API. Requirements: rows reflect the live status from transition events; the action calls the validated transition endpoint; the booking-capture fields, the no-show→job rule, the KPI tiles + in-room strip, and the full role-aware action set are follow-ups.
