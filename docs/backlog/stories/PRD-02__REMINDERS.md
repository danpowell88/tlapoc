# Reminders & self-service reschedule/cancel

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/REMINDERS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/LIFECYCLE`

## Background

Booking & scheduling (+ client/CRM basics) — The calendar that runs the front desk and the 360° client record everything hangs off.

As a client, I want appointment reminders I can confirm/decline and the ability to reschedule or cancel within policy myself, so that I don't need to call and the clinic's diary stays accurate.

Clients get reminders they can confirm/decline and can self-reschedule or cancel within policy without calling.

## Requirements

- Appointment reminders I can confirm/decline and the ability to reschedule or cancel within policy myself.
- Traces to requirement(s): REQ-BOOK-3, REQ-BOOK-4.

## Acceptance Criteria

- [ ] Reminders fire per template (SMS/app/email); confirm/decline updates status.
- [ ] Self-reschedule/cancel within policy; outside policy the configured rule applies (no auto-charge in v1).
- [ ] Cancellation/no-show policy is configurable.
- [ ] Reminder channel is provided by PRD-07.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-02/LIFECYCLE.

## Other

Epic: PRD-02 — Booking & scheduling (+ client/CRM basics).
Source PRD: docs/prds/PRD-02-booking-scheduling.md.
Backlog key: PRD-02/REMINDERS.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
