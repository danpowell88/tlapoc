# Gift cards: issue, balance-track & partial redeem

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PACKAGES-GIFTCARD`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/PACKAGES-GIFT`

## Background

As a front desk, I want to issue gift cards, track their balance and partially redeem them at the till, so that clients can buy and spend pre-paid gift value.
Plainly: sell a gift card with a starting value, track its running balance, and let it be spent (in part) against any future sale. Where it fits: a follow-up to the basic pre-paid value story (PRD-06/PACKAGES-GIFT) that adds gift cards alongside packages. A gift card is schedule-neutral — it buys anything — but the rewards engine still blocks S4 (Schedule 4 prescription-only medicine) earn/redeem at checkout (C9), so spending a gift card on an S4 treatment is fine while earning/redeeming points on that line is not. Balances sync live to checkout so a draw-down at the till reflects immediately. Redemptions post to the Closeout (PRD-06/CLOSEOUT). Money figures stay owner-aware; owner-only credit/AR figures are separate.

## How it works

A GiftCard has a code, an initial value and a running balance; it can be issued ('Issue gift card'), assigned to a client or left unassigned, partially redeemed against any future sale, and shows status (active / redeemed / unassigned). Balances sync live to checkout so a draw-down at the till is reflected immediately; partial redemption is supported.
A gift card is schedule-neutral — it buys whatever the client likes — BUT the rewards engine still won't earn/redeem points against an S4 (Schedule 4 prescription-only medicine) line at checkout (C9). Redemptions post to the daily Closeout (PRD-06/CLOSEOUT); deferred-revenue recognition is Xero's (PRD-10), not duplicated here. This extends the basic pre-paid-value story (PRD-06/PACKAGES-GIFT).

## Requirements

- To issue gift cards, track their balance and partially redeem them at the till.

## Acceptance Criteria

- [ ] A gift card can be issued with a code and initial value, assigned to a client or left unassigned, and shows status (active / redeemed / unassigned).
- [ ] A gift card can be partially redeemed against any future sale; the balance updates and syncs live to checkout.
- [ ] A gift card is schedule-neutral (buys anything) but the rewards engine still blocks S4 (Schedule 4 prescription-only medicine) earn/redeem at checkout (C9).
- [ ] Gift-card redemptions appear in the daily Closeout (PRD-06/CLOSEOUT).

## UI designs / screenshots

- Prototype: Memberships → Gift cards — 'Sell, track & redeem gift cards. Balances sync to checkout.'; 'Issue gift card' button; card tiles showing code, balance 'of' initial, and assignment (e.g. 'GC-4471 H. Lawson $120 of $150', 'GC-3320 redeemed $0 of $100', 'GC-2207 gift — unassigned $200 of $200').

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **GiftCard** — id, tenant_id, code, initial, balance, status(active|redeemed|void), assigned_client_id?
  - _New entity; sell/track/redeem; balances sync to checkout; schedule-neutral but S4 earn/redeem still blocked (C9)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **GiftCard model: issue, balance-track, partial redeem**
  Behaviour: a GiftCard (code, initial, balance, status, optional assigned_client_id) is issued, partially redeemed against any sale, and tracks status. Requirements: balances sync live to checkout; partial redemption supported; redemptions post to Closeout (PRD-06/CLOSEOUT); schedule-neutral but the rewards engine still blocks S4 (Schedule 4 prescription-only medicine) earn/redeem (C9); tenant-scoped with RLS (row-level security).
- [ ] **Gift-cards web UI (tiles + issue + search)**
  Behaviour: the Gift-cards screen renders a tile list (code, balance of initial, assignment status) with an 'Issue gift card' action and search; tiles update without a full reload when a redemption happens at the till. Requirements: loading/empty/error states; balances reflect checkout redemptions live.
