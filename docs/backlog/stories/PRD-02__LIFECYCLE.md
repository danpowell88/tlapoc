# Visit lifecycle & status state-machine

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/LIFECYCLE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want a clear visit status flow with check-in, an in-room-now indicator and late/no-show flags, so that the team always knows where each client is in the visit.
Bookings move through booked → reminded → checked-in → in-room → checked-out, with late/no-show flags and role hand-offs (REQ-BOOK-7).

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
  Model Appointment.status as a state machine (booked→reminded→checked_in→in_room→for_checkout→checked_out, plus late/no_show/cancelled). Transition endpoints validate legal transitions server-side and reject illegal ones; each write appends a VisitEvent (from/to/actor/at) to the audit stream. Emit domain events per transition for the Today board, reminders and read models. Capture new_or_returning/reason/practitioner at booking.
- [ ] **No-show → auto follow-up call job**
  When status transitions to no_show, automatically create a Follow-up CALL job in the PRD-07 jobs queue (assignee=reception, source=system, due=today) so the no-show is recovered. Late is a flag only (no job). Idempotent — re-flagging doesn't duplicate the job.
- [ ] **Today board: in-room-now strip + per-row status actions**
  Angular Today screen: KPI tiles; 'Today's schedule' list with a 'WITH YOU NOW' in-room strip (current client + Open chart / Profile). Each row shows the current status chip and the role-appropriate next action (Confirmed/Start/Resume/Late/No-show/Profile) wired to the transition API. Reflect the consult/consent gate state ('Awaiting consent — treatment gated'). Live-update from transition events.
