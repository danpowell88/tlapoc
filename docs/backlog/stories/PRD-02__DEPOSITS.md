# Booking deposits / card-on-file hold (placeholder)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/DEPOSITS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** backend

## Background

As a owner, I want to optionally require a booking deposit or card-on-file hold, so that no-shows cost less.
An opt-in, ACL-fair booking deposit / card-on-file hold, suppressed during cooling-off (F14 invariant). Deferred to Phase 2 — placeholder.

## How it works

Placeholder (Phase 2): an opt-in booking deposit / card-on-file hold to reduce no-shows. Must keep the cooling-off suppression invariant (F14) — no hold during a cooling-off period. Not in v1.

## Requirements

- To optionally require a booking deposit or card-on-file hold.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — not in v1 (no deposits/holds in v1).
- [ ] Design must keep the cooling-off suppression invariant (F14): no hold during a cooling-off period.

## Suggested data model

- **BookingHold** — id, appointment_id, amount, token_ref, status
  - _Placeholder; suppressed during cooling-off._

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0036](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
