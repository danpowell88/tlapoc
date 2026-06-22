# Checkout: split / partial tenders, tips & card surcharge

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS-SPLIT-TENDER`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want to take a sale across more than one payment, with tips and a card surcharge, so that clients can pay how they like and the sale still balances.
Plainly: let a single sale be paid by more than one payment — say $200 on card and the rest on cash or a gift card — and support a tip and a configurable card surcharge. Where it fits: a follow-up to the basic in-person POS checkout (PRD-06/POS), which takes the whole sale on one tender; this adds multi-tender settlement. Each tender still becomes its own Payment row and lands in the day's Closeout. Money figures stay sale-level for Reception; owner-only takings/margin read-models stay behind .fin. Gift-card draw-down as a tender depends on PRD-06/PACKAGES-GIFT.

## How it works

The basic checkout (PRD-06/POS) settles a sale on one tender; this adds split/partial settlement: a sale can be paid across several Payments (e.g. $200 on card + remainder on a gift card), with a running 'remaining' until fully settled. Tips and a configurable card surcharge are supported and attach to the relevant Payment.
Card tenders go through IPaymentProvider authorize+capture (PRD-06/PAYMENT-PROVIDER); cash is recorded as an internal tender; gift-card tender draws down a balance (PRD-06/PACKAGES-GIFT). Every tender becomes a Payment row and lands in the day's Closeout (PRD-06/CLOSEOUT). Money figures stay sale-level for Reception; owner-only takings/margin read-models stay behind .fin.

## Requirements

- To take a sale across more than one payment, with tips and a card surcharge.

## Acceptance Criteria

- [ ] A sale can be settled by one tender or split/partial across several (e.g. $200 on card + remainder on cash/gift card).
- [ ] A tip and a configurable card surcharge are supported and recorded on the relevant Payment.
- [ ] Each tender writes its own Payment row and lands in the day's Closeout (PRD-06/CLOSEOUT).
- [ ] The remaining balance updates live until the sale is fully settled.

## UI designs / screenshots

- Prototype: Checkout 'Take payment (in person)' panel — multiple tender rows (Square card / Record cash / Gift card), a 'remaining' figure, tip entry and a card-surcharge line; sale completes only when remaining is zero.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **Payment (extends PRD-06/POS)** — + tip, surcharge; split/partial = multiple Payment rows per Invoice
  - _Extends the basic Payment; no new entity. Gift-card tender draws on PRD-06/PACKAGES-GIFT._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Multi-tender settlement (split / partial) with running remaining**
  Behaviour: a sale accepts several Payments until the remaining balance is zero; each tender (card / cash / gift card) writes its own Payment row. Requirements: card via IPaymentProvider; cash recorded; gift-card draw-down (PRD-06/PACKAGES-GIFT); the sale only completes when fully settled; idempotent so a retried tender doesn't double-charge.
- [ ] **Tips + configurable card surcharge**
  Behaviour: a tip and a configurable card surcharge attach to the relevant Payment and show on the receipt and in the Closeout. Requirements: surcharge configurable per tenant; both recorded on the Payment; owner-only .fin gate on any takings figures.
