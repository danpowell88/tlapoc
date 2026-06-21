# Visit lifecycle & status state-machine

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/LIFECYCLE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

As a front desk, I want a clear visit status flow with check-in, an in-room-now indicator and late/no-show flags, so that the team always knows where each client is in the visit.
Bookings move through booked → reminded → checked-in → in-room → checked-out, with late/no-show flags and role hand-offs (REQ-BOOK-7).

## How it works

The visit lifecycle is a status state-machine: booked -> reminded -> checked-in -> in-room -> checked-out, with role hand-offs. Late and no-show flags are raised; a no-show automatically creates a follow-up call (PRD-07).
Captures new-vs-returning, reason and roster so reporting and recall work.

## Requirements

- A clear visit status flow with check-in, an in-room-now indicator and late/no-show flags.

## Acceptance Criteria

- [ ] Status state-machine with role hand-offs; check-in on arrival.
- [ ] An 'in-room now' indicator with quick links to chart/profile.
- [ ] Late and no-show flags; a no-show raises a follow-up call (feeds PRD-07 jobs).
- [ ] New-vs-returning, reason and roster captured on the booking.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Today (dashboard.png) — waiting / in-room / checked-out columns; an 'in-room now' indicator with quick links to chart/profile.
- Check-in on arrival; late/no-show flags; status chips on each appointment.

## Suggested data model

- **Appointment.status** — booked|reminded|checked_in|in_room|checked_out|late|no_show|cancelled
  - _Transitions audited; no_show raises a Job (PRD-07)._
- **VisitEvent** — id, appointment_id, status, at, actor_id
  - _Audit trail of the visit's transitions._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
