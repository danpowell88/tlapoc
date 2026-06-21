# Visit lifecycle & status state-machine

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/LIFECYCLE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

Booking & scheduling (+ client/CRM basics) — The calendar that runs the front desk and the 360° client record everything hangs off.

As a front desk, I want a clear visit status flow with check-in, an in-room-now indicator and late/no-show flags, so that the team always knows where each client is in the visit.

Bookings move through booked → reminded → checked-in → in-room → checked-out, with late/no-show flags and role hand-offs (REQ-BOOK-7).

## Requirements

- A clear visit status flow with check-in, an in-room-now indicator and late/no-show flags.
- Traces to requirement(s): REQ-BOOK-4, REQ-BOOK-7.

## Acceptance Criteria

- [ ] Status state-machine with role hand-offs; check-in on arrival.
- [ ] An 'in-room now' indicator with quick links to chart/profile.
- [ ] Late and no-show flags; a no-show raises a follow-up call (feeds PRD-07 jobs).
- [ ] New-vs-returning, reason and roster captured on the booking.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0024 (see docs/adr/decision-log.md).
Depends on: PRD-02/CALENDAR.

## Other

Epic: PRD-02 — Booking & scheduling (+ client/CRM basics).
Source PRD: docs/prds/PRD-02-booking-scheduling.md.
Backlog key: PRD-02/LIFECYCLE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
