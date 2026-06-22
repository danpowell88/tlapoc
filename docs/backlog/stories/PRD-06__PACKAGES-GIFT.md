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

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Package — id, tenant_id, client_id, service_id, total_visits, remaining, purchased_at (Redeemed over time.)
  - GiftCard — id, tenant_id, code, initial, balance, status (Sell/redeem/track.)
  - AccountBalance — client_id, credit, ar_ageing (Client credit + receivables ageing.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Package/series sale + redemption with 'visits remaining'.
  - Rule: Gift cards can be sold, balance-tracked and redeemed.
  - Rule: Client balance/credit and AR ageing tracked.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-06/POS.
- [ ] **Web UI**
  Build on the Angular web app: the memb-gifts per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Checkout (checkout.png) for sale/redeem; Memberships -> Gift cards (memb-gifts.png) for issuing/tracking gift-card balances; package 'visits remaining' on the Client 360.
  - Balance/credit + AR ageing visible to owner/manager.
