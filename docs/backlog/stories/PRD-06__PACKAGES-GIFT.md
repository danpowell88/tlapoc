# Packages/series: sell & redeem (visits remaining) — basic pre-paid value (core)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PACKAGES-GIFT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want to sell and redeem a treatment package and see visits remaining, so that clients can pre-pay a course of treatments.
What this is, plainly: selling a course of treatments up front and drawing it down one visit at a time, keeping the 'visits remaining' count straight. This is the minimal pre-paid-value core; gift cards, store-credit/AR ageing and the gift-cards admin screen are each added as their own follow-ups. Where it sits: it extends the POS checkout, so it follows the till and, like the rest of Payments, sits on the booked/charted visit after the clinical core. Sell/redeem packages (visits remaining) (REQ-PAY-3/5).

## How it works

A Package is a pre-paid course: total_visits and remaining, decremented each time a session is redeemed at checkout; the Client 360 shows 'visits remaining'. A GiftCard has a code, an initial value and a running balance; it can be sold (issued), tracked and partially redeemed against any future sale — the gift-card screen shows each card's balance 'of' its initial, and whether it's assigned to a client, redeemed, or unassigned. AccountBalance holds client store-credit and AR (accounts receivable) ageing for owner/manager visibility.
Redemptions appear in the daily Closeout and post to Xero like any other tender (deferred revenue on sale, recognised on redemption — the accounting treatment lives in Xero/PRD-10). Gift cards remain non-S4-neutral: a gift card buys whatever the client likes, but the rewards engine still won't earn/redeem points against an S4 (Schedule 4 prescription-only medicine) line at checkout.

## Requirements

- To sell and redeem a treatment package and see visits remaining.

## Acceptance Criteria

- [ ] A package/series can be sold and redeemed, decrementing 'visits remaining'; the count shows on the Client 360.
- [ ] Redeeming guards against going below zero (a depleted package can't redeem) and is tied to a service so only matching sessions draw it down.
- [ ] Package redemptions appear in the daily Closeout (PRD-06/CLOSEOUT).
- [ ] Money figures stay owner-aware; Reception sees the package but not owner-only credit/AR figures.

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Memberships -> Gift cards — 'Sell, track & redeem gift cards. Balances sync to checkout.'; 'Issue gift card' button; card tiles showing code, balance 'of' initial, and assignment (e.g. 'GC-4471 H. Lawson $120 of $150', 'GC-3320 redeemed $0 of $100', 'GC-2207 gift — unassigned $200 of $200').
- Package 'visits remaining' shows on the Client 360; sale/redeem happen in Checkout.

![memb-gifts — prototype screen](../screens/memb-gifts.png)

## Suggested data model

- **Package** — id, tenant_id, client_id, service_id, total_visits, remaining, purchased_at
  - _Decremented on redemption; 'visits remaining' on Client 360._
- **GiftCard** — id, tenant_id, code, initial, balance, status(active|redeemed|void), assigned_client_id?
  - _Sell/track/redeem; balances sync to checkout._
- **AccountBalance** — client_id, credit, ar_ageing
  - _Client store credit + AR (accounts receivable) ageing (owner/manager visibility)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Packages / series: sell + redeem (decrement visits-remaining)**
  Behaviour: a Package is a pre-paid course of treatments (total_visits) with a running 'remaining' count, sold at checkout and redeemed one session at a time when the client attends; the Client 360 shows 'visits remaining' and the redemption history. Requirements: redeeming decrements remaining and guards against going below 0 (a depleted package can't redeem); redemption posts to the Closeout (the daily reconciliation of takings) — deferred revenue on sale, recognised on redemption, with the accounting treatment owned by Xero (PRD-10), not re-implemented here. A package is tied to a service_id so only matching sessions draw it down. Tenant-scoped with RLS (row-level security).
- [ ] **Package sell/redeem API + Client-360 'visits remaining' chip**
  Behaviour: server-side commands — sell package and redeem a package visit (decrement remaining, guard 0); the Client 360 shows a package 'visits remaining' chip and redemption history. Requirements: redemptions write to the Closeout (PRD-06/CLOSEOUT); tied to a service_id so only matching sessions draw down; tenant-scoped with RLS; money figures owner-aware (Reception sees the package, owner-only credit/AR figures are added by the follow-up).
