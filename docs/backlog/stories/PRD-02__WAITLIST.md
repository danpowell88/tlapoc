# Waitlist & cancellation backfill

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WAITLIST`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/REMINDERS`

## Background

As a front desk, I want a waitlist that auto-offers a freed slot when an appointment cancels or no-shows, so that we keep the diary full.
Clients can join a waitlist; cancellations/no-shows auto-offer the freed slot to fill quiet windows.

## Requirements

- A waitlist that auto-offers a freed slot when an appointment cancels or no-shows.

## Acceptance Criteria

- [ ] Clients can be added to a waitlist for a service/window.
- [ ] Cancelling/no-showing a slot offers it to the waitlist.
- [ ] Quiet-window fill suggestions surface from utilisation data.
- [ ] Offered/accepted/expired waitlist states are tracked.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
