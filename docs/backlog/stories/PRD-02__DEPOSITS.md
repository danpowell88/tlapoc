# Booking deposits / card-on-file hold (placeholder)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/DEPOSITS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** backend

## Background

Booking & scheduling (+ client/CRM basics) — The calendar that runs the front desk and the 360° client record everything hangs off.

As a owner, I want to optionally require a booking deposit or card-on-file hold, so that no-shows cost less.

An opt-in, ACL-fair booking deposit / card-on-file hold, suppressed during cooling-off (F14 invariant). Deferred to Phase 2 — placeholder.

## Requirements

- To optionally require a booking deposit or card-on-file hold.
- Traces to requirement(s): REQ-BOOK-3.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Placeholder — not in v1 (no deposits/holds in v1).
- [ ] Design must keep the cooling-off suppression invariant (F14): no hold during a cooling-off period.

## UI designs / screenshots

prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0036 (see docs/adr/decision-log.md).

## Other

Epic: PRD-02 — Booking & scheduling (+ client/CRM basics).
Source PRD: docs/prds/PRD-02-booking-scheduling.md.
Backlog key: PRD-02/DEPOSITS.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
