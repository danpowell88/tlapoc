# Packages/series, gift cards & client balances

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PACKAGES-GIFT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

Payments (in-person POS + autopay), memberships & non-S4 rewards — Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law.

As a front desk, I want to sell and redeem packages and gift cards and track client balances, so that clients can pre-pay and carry credit.

Sell/redeem packages (visits remaining) and gift cards, track client balances/credit and AR ageing (REQ-PAY-3/5).

## Requirements

- To sell and redeem packages and gift cards and track client balances.
- Traces to requirement(s): REQ-PAY-3, REQ-PAY-5.

## Acceptance Criteria

- [ ] Package/series sale + redemption with 'visits remaining'.
- [ ] Gift cards can be sold, balance-tracked and redeemed.
- [ ] Client balance/credit and AR ageing tracked.
- [ ] Redemptions appear in the closeout and post to Xero (PRD-10).

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-06/POS.

## Other

Epic: PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards.
Source PRD: docs/prds/PRD-06-payments-memberships-rewards.md.
Backlog key: PRD-06/PACKAGES-GIFT.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
