# Packages/series, gift cards & client balances

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PACKAGES-GIFT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want to sell and redeem packages and gift cards and track client balances, so that clients can pre-pay and carry credit.
What this is, plainly: selling and redeeming pre-paid value — a course of treatments bought up front, or a gift card — and keeping each client's running balance straight. Where it sits: it extends the POS checkout, so it follows the till and, like the rest of Payments, sits on the booked/charted visit after the clinical core. Sell/redeem packages (visits remaining) and gift cards, track client balances/credit and AR (accounts receivable) ageing (REQ-PAY-3/5).

## How it works

A Package is a pre-paid course: total_visits and remaining, decremented each time a session is redeemed at checkout; the Client 360 shows 'visits remaining'. A GiftCard has a code, an initial value and a running balance; it can be sold (issued), tracked and partially redeemed against any future sale — the gift-card screen shows each card's balance 'of' its initial, and whether it's assigned to a client, redeemed, or unassigned. AccountBalance holds client store-credit and AR (accounts receivable) ageing for owner/manager visibility.
Redemptions appear in the daily Closeout and post to Xero like any other tender (deferred revenue on sale, recognised on redemption — the accounting treatment lives in Xero/PRD-10). Gift cards remain non-S4-neutral: a gift card buys whatever the client likes, but the rewards engine still won't earn/redeem points against an S4 (Schedule 4 prescription-only medicine) line at checkout.

## Requirements

- To sell and redeem packages and gift cards and track client balances.

## Acceptance Criteria

- [ ] A package/series can be sold and redeemed, decrementing 'visits remaining'; the count shows on the Client 360.
- [ ] A gift card can be issued, balance-tracked and partially redeemed at checkout; balances sync to checkout.
- [ ] Client store-credit and AR (accounts receivable) ageing are tracked and visible to owner/manager.
- [ ] Package/gift redemptions appear in the Closeout and post to Xero (PRD-10).

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
  Behaviour: a Package is a pre-paid course of treatments (total_visits) with a running 'remaining' count, sold at checkout and redeemed one session at a time when the client attends; the Client 360 shows 'visits remaining' and the redemption history. Requirements: redeeming decrements remaining and guards against going below 0 (a depleted package can't redeem); redemption posts to the Closeout (the daily reconciliation of takings) and to Xero (PRD-10) — deferred revenue on sale, recognised on redemption, with the accounting treatment owned by Xero, not re-implemented here. A package is tied to a service_id so only matching sessions draw it down.
- [ ] **Gift cards: issue, balance-track, partial redeem (balances sync to checkout)**
  Behaviour: a gift card has a code, an initial value and a running balance; it can be issued ('Issue gift card'), assigned to a client or left unassigned, partially redeemed against any future sale, and shows status (active / redeemed / unassigned). The Gift-cards screen tiles each card as 'balance of initial' (e.g. 'GC-4471 H. Lawson $120 of $150', 'GC-3320 redeemed $0 of $100', 'GC-2207 gift — unassigned $200 of $200'). Requirements: balances sync live to checkout so a draw-down at the till is reflected immediately; partial redemption supported; a gift card is schedule-neutral (it buys anything) BUT the rewards engine still blocks S4 (Schedule 4 prescription-only medicine) earn/redeem at checkout (C9). Redemptions post to Closeout + Xero.
- [ ] **Client store-credit + AR (accounts receivable) ageing**
  Behaviour: an AccountBalance per client holds store-credit (usable as a checkout deduction) and AR (accounts receivable) ageing buckets (what the client owes, by age) for owner/manager visibility. Requirements: store credit applied at checkout decrements the balance; AR ageing is surfaced to owner/manager only; all money figures here are owner-gated (.fin) — Reception sees memberships/packages but not credit/AR dollar figures. Feeds the Client 360 billing tab.
- [ ] **Sell/redeem API (package decrement, gift draw-down, credit/AR queries)**
  Behaviour: server-side commands/queries — sell package / issue gift card / apply store credit; redeem a package visit (decrement remaining, guard 0) and draw down a gift-card balance at checkout (partial allowed); expose client-credit + AR-ageing read queries (owner/manager gated). Requirements: redemptions write to the Closeout and the Xero post; gift cards stay schedule-neutral while the rewards engine still blocks S4 (Schedule 4 prescription-only medicine) earn/redeem; every table tenant-scoped with RLS (row-level security). Deferred-revenue recognition is Xero's (PRD-10), not duplicated here.
- [ ] **Gift-cards web UI + Client-360 'visits remaining' chip**
  Behaviour: the Gift-cards screen renders a tile list (code, balance of initial, assignment status) with an 'Issue gift card' action and search; balances reflect checkout redemptions live. The Client 360 shows a package 'visits remaining' chip and redemption history. Requirements: loading/empty/error states; owner/manager gate (.fin) on credit/AR figures; tiles update without a full reload when a redemption happens at the till.
