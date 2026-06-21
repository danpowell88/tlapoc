# In-person POS checkout (card + cash)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

As a front desk, I want to take payment in person by Square card or recorded cash with receipts and split/partial support, so that I can check clients out at the desk.
Front desk takes payment in person via Square card-present or recorded cash, with receipts, partial/split, tips and surcharge config (REQ-PAY-2). Financial figures are owner-gated.

## Requirements

- To take payment in person by Square card or recorded cash with receipts and split/partial support.

## Acceptance Criteria

- [ ] A sale completes by Square card or recorded cash; both appear in the daily closeout.
- [ ] Receipts, partial/split payments, tips and surcharge config supported.
- [ ] Money figures respect the owner-only financial capability (reception sees no money totals beyond the sale).
- [ ] Online one-off checkout is not exposed (deferred).

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
