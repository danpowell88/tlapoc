# Packages/series, gift cards & client balances

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PACKAGES-GIFT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want to sell and redeem packages and gift cards and track client balances, so that clients can pre-pay and carry credit.
Sell/redeem packages (visits remaining) and gift cards, track client balances/credit and AR ageing (REQ-PAY-3/5).

## How it works

Sell/redeem packages/series ('visits remaining') and gift cards, and track client balances/credit + AR ageing. Redemptions appear in the closeout and post to Xero.
Lets clients pre-pay courses and carry credit.

## Requirements

- To sell and redeem packages and gift cards and track client balances.

## Acceptance Criteria

- [ ] Package/series sale + redemption with 'visits remaining'.
- [ ] Gift cards can be sold, balance-tracked and redeemed.
- [ ] Client balance/credit and AR ageing tracked.
- [ ] Redemptions appear in the closeout and post to Xero (PRD-10).

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Checkout (checkout.png) for sale/redeem; Memberships -> Gift cards (memb-gifts.png) for issuing/tracking gift-card balances; package 'visits remaining' on the Client 360.
- Balance/credit + AR ageing visible to owner/manager.

![memb-gifts — prototype screen](../screens/memb-gifts.png)

## Suggested data model

- **Package** — id, tenant_id, client_id, service_id, total_visits, remaining, purchased_at
  - _Redeemed over time._
- **GiftCard** — id, tenant_id, code, initial, balance, status
  - _Sell/redeem/track._
- **AccountBalance** — client_id, credit, ar_ageing
  - _Client credit + receivables ageing._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
