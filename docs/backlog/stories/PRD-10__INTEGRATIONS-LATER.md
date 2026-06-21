# Online checkout, e-prescribing, webhooks/API (placeholder)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/INTEGRATIONS-LATER`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** integration

## Background

Integrations: Xero & calendar — Outbound integrations that remove double-entry: push sales/payments to Xero, and keep appointments in sync with staff calendars (M365 / Google)

As a owner, I want future integrations: online checkout/deposits, e-prescribing and a public API, so that the platform extends as we scale.

Online checkout & deposits (S4 never priced/sold online), e-prescribing (eRx/ETP, 🔬), public API/webhooks (Phase 3) and Medicare/HICAPS (non-applicable to cosmetic). Placeholder (REQ-INT-2a/4/5/6/7, ADR-0035/0036).

## Requirements

- Future integrations: online checkout/deposits, e-prescribing and a public API.
- Traces to requirement(s): REQ-INT-4, REQ-INT-5, REQ-INT-6, REQ-INT-7.
- Deferred (Phase 2+): placeholder — design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2/3; each behind its existing port (IPaymentProvider, IPrescribingProvider).
- [ ] S4 is never priced or sold online (invariant carried forward).
- [ ] Medicare/HICAPS recorded as non-applicable to cosmetic.
- [ ] e-prescribing flagged for feasibility validation.

## UI designs / screenshots

prototype.html — Settings → Integrations.

## Technical notes (high level)

Stack: Ports-and-adapters integration.
Architecture decisions: ADR-0035, ADR-0036 (see docs/adr/decision-log.md).

## Other

Epic: PRD-10 — Integrations: Xero & calendar.
Source PRD: docs/prds/PRD-10-integrations.md.
Backlog key: PRD-10/INTEGRATIONS-LATER.
Phase: 2+ · Priority: P2 · Estimate: 1 pts.

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
