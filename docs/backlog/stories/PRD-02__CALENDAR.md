# Multi-resource calendar (practitioner + room)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/ROSTER`

## Background

Booking & scheduling (+ client/CRM basics) — The calendar that runs the front desk and the 360° client record everything hangs off.

As a front desk, I want a day/week/room calendar showing practitioners and rooms with correct service durations and buffers, so that I can run the diary at a glance and book without clashes.

Front desk needs a fast day/week/room calendar with service durations, buffers and rosters — the core of the diary.

## Requirements

- A day/week/room calendar showing practitioners and rooms with correct service durations and buffers.
- Traces to requirement(s): REQ-BOOK-1.

## Acceptance Criteria

- [ ] Resources = practitioner + room; service durations include buffer/processing/turnaround.
- [ ] Day, week and room views render; rosters and time-off block availability.
- [ ] Drag to move an appointment; conflicts on room/chair/device are flagged.
- [ ] Per-day and per-treatment-type counts + utilisation surfaced.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0024, ADR-0026 (see docs/adr/decision-log.md).
Depends on: PRD-01/ROSTER.

## Other

Epic: PRD-02 — Booking & scheduling (+ client/CRM basics).
Source PRD: docs/prds/PRD-02-booking-scheduling.md.
Backlog key: PRD-02/CALENDAR.
Phase: 1 · Priority: P0 · Estimate: 5 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
