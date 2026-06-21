# Multi-resource calendar (practitioner + room)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CALENDAR`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/ROSTER`

## Background

As a front desk, I want a day/week/room calendar showing practitioners and rooms with correct service durations and buffers, so that I can run the diary at a glance and book without clashes.
Front desk needs a fast day/week/room calendar with service durations, buffers and rosters — the core of the diary.

## Requirements

- A day/week/room calendar showing practitioners and rooms with correct service durations and buffers.

## Acceptance Criteria

- [ ] Resources = practitioner + room; service durations include buffer/processing/turnaround.
- [ ] Day, week and room views render; rosters and time-off block availability.
- [ ] Drag to move an appointment; conflicts on room/chair/device are flagged.
- [ ] Per-day and per-treatment-type counts + utilisation surfaced.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0026](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
