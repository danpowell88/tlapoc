# Booking deposits / card-on-file hold (placeholder)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/DEPOSITS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** backend

## Background

As a owner, I want to optionally require a booking deposit or card-on-file hold, so that no-shows cost less.
Booking deposits / card-on-file holds are a deferred Phase-2 placeholder, parked in Reception (PRD-02) so the no-show-cost lever is captured but explicitly NOT built in v1 — there are no deposits or holds in version 1.  Its one job today is to preserve a design constraint for whenever it is built: a hold must never be placed during an under-18 cooling-off period, coordinating with the cooling-off rule in Intake/Consent (PRD-03/COOLING-OFF).  As an owner, I want to optionally require a booking deposit or card-on-file hold, so that no-shows cost less.  Deferred to Phase 2 — placeholder. There are no deposits or holds in v1.

## How it works

Placeholder (Phase 2). An opt-in, ACL-fair booking deposit / card-on-file hold to reduce no-shows — front-desk-controlled, disclosed at booking, refundable on notice, never a pressure mechanism (ADR-0026). NOT in v1: there are no deposits or holds in v1 (REQ-BOOK-3, scoping decision).
Design constraint that must survive into Phase 2: the cooling-off suppression invariant (F14) — no deposit/hold may be placed or held during an under-18 cooling-off period (coordinates with PRD-03 COOLING-OFF). When built it sits behind the existing IPaymentProvider (ADR-0036); S4 is never priced/sold online.

## Requirements

- To optionally require a booking deposit or card-on-file hold.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — not in v1 (no deposits/holds in v1).
- [ ] Design must keep the cooling-off suppression invariant (F14): no hold during a cooling-off period.

## Suggested data model

- **BookingHold** — id, tenant_id, appointment_id, amount, token_ref, status(placed|captured|released|refunded)
  - _Placeholder; behind IPaymentProvider; SUPPRESSED during cooling-off (F14)._

## Technical notes (high level)

- Architecture decisions: [ADR-0036](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Design note: ACL-fair deposits + cooling-off suppression (F14) — Phase 2**
  Placeholder design task (no v1 build). Document the opt-in deposit / card-on-file hold model behind IPaymentProvider (ADR-0036): disclosed at booking, refundable on notice, ACL-fair, never coercive. Capture the hard invariant F14 — a BookingHold must NOT be placed or held during an under-18 cooling-off period (coordinates with PRD-03 COOLING-OFF). S4 (Schedule 4 prescription-only medicine) is never priced or sold online. Produce the design only; defer implementation to Phase 2.
