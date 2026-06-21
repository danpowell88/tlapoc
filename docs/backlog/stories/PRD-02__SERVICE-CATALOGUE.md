# Services & treatment-menu admin (durations, eligible roles, S4 flag)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/SERVICE-CATALOGUE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

Booking & scheduling (+ client/CRM basics) — The calendar that runs the front desk and the 360° client record everything hangs off.

As a owner / manager, I want to manage the menu of services with durations, eligible roles and the S4 flag, so that booking, rewards and the public page all behave correctly per service.

The prototype's clinical Treatment menu + admin services list defines bookable services with durations, eligible roles, and the S4/non-S4 flag that drives scope-aware booking, rewards eligibility and public-page naming.

## Requirements

- To manage the menu of services with durations, eligible roles and the S4 flag.
- Traces to requirement(s): REQ-BOOK-2.
- Must satisfy compliance obligation(s): C4, C9.

## Acceptance Criteria

- [ ] Services carry duration/buffer, eligible roles, price and the S4/non-S4 flag.
- [ ] The S4 flag drives scope-aware booking (C4), rewards eligibility (C9) and public naming (PRD-07).
- [ ] Capability-gated admin; changes are audited.
- [ ] Linked to the medicines/products catalogue (PRD-04) where a service consumes a product.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0014 (see docs/adr/decision-log.md).
Depends on: PRD-04/PRODUCT-CATALOGUE.

## Other

Epic: PRD-02 — Booking & scheduling (+ client/CRM basics).
Source PRD: docs/prds/PRD-02-booking-scheduling.md.
Backlog key: PRD-02/SERVICE-CATALOGUE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C4, C9.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C9); blocked path explains why.
- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
