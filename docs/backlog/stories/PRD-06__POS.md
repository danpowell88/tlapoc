# In-person POS checkout (card + cash)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

Payments (in-person POS + autopay), memberships & non-S4 rewards — Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law.

As a front desk, I want to take payment in person by Square card or recorded cash with receipts and split/partial support, so that I can check clients out at the desk.

Front desk takes payment in person via Square card-present or recorded cash, with receipts, partial/split, tips and surcharge config (REQ-PAY-2). Financial figures are owner-gated.

## Requirements

- To take payment in person by Square card or recorded cash with receipts and split/partial support.
- Traces to requirement(s): REQ-PAY-2.

## Acceptance Criteria

- [ ] A sale completes by Square card or recorded cash; both appear in the daily closeout.
- [ ] Receipts, partial/split payments, tips and surcharge config supported.
- [ ] Money figures respect the owner-only financial capability (reception sees no money totals beyond the sale).
- [ ] Online one-off checkout is not exposed (deferred).

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-06/PAYMENT-PROVIDER.

## Other

Epic: PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards.
Source PRD: docs/prds/PRD-06-payments-memberships-rewards.md.
Backlog key: PRD-06/POS.
Phase: 1 · Priority: P0 · Estimate: 5 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
