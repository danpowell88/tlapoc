# Walk-ins, same-day add-ons & resources

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WALKINS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CALENDAR`

## Background

Booking & scheduling (+ client/CRM basics) — The calendar that runs the front desk and the 360° client record everything hangs off.

As a front desk, I want to add walk-ins and same-day add-ons against available rooms/chairs/devices, so that we capture opportunistic demand without breaking the rules or double-booking resources.

Walk-ins and same-day add-ons are supported but gate-respecting (an injectable walk-in still needs a consult first); room/chair/device resources are scheduled with conflict-flagging.

## Requirements

- To add walk-ins and same-day add-ons against available rooms/chairs/devices.
- Traces to requirement(s): REQ-BOOK-3, REQ-BOOK-6.

## Acceptance Criteria

- [ ] Walk-in and same-day add-on flows exist; an injectable walk-in still requires a consult first.
- [ ] Room/chair/device resources are bookable with conflict-flagging and utilisation.
- [ ] VIP / first-time appointment tags supported.
- [ ] Resource conflicts are surfaced before confirmation.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0026 (see docs/adr/decision-log.md).
Depends on: PRD-02/CALENDAR.

## Other

Epic: PRD-02 — Booking & scheduling (+ client/CRM basics).
Source PRD: docs/prds/PRD-02-booking-scheduling.md.
Backlog key: PRD-02/WALKINS.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
