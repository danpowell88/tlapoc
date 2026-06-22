# Checkout: Square-terminal modal (Processing → Approved) + decline path

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS-TERMINAL-MODAL`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/POS`

## Background

As a front desk, I want a clear terminal progress modal when taking a card payment, with a decline path, so that I can see the card transaction's real state and recover from a decline.
Plainly: when the desk takes a card payment, show a modal that tracks the real Square terminal state — 'Processing…' then 'Payment approved' — and offers a clear path if the card declines. Where it fits: a follow-up to the basic in-person POS checkout (PRD-06/POS), which completes a card sale without a progress modal. The modal reflects the real ProviderTxn state from the Square adapter (PRD-06/PAYMENT-PROVIDER), not a fixed timer; a decline surfaces retry / alternate-tender. On completion the post-checkout rebook view (PRD-06/CHECKOUT-ASSIST) is offered. Money figures stay sale-level for Reception; owner-only takings/margin behind .fin.

## How it works

Taking a card payment opens a terminal modal that shows 'Processing on Square terminal…' then 'Payment approved', after which the sale completes. The modal reflects the real ProviderTxn state from the Square adapter (PRD-06/PAYMENT-PROVIDER) — not a fixed timer in production — and a decline surfaces a clear retry/alternate-tender path so the desk can recover. On completion the post-checkout rebook view (PRD-06/CHECKOUT-ASSIST) is offered.
This is a UX layer over the basic card tender in PRD-06/POS; it does not change how the charge is taken, only how its progress and outcome are shown. Money figures stay sale-level for Reception; owner-only takings/margin stay behind .fin.

## Requirements

- A clear terminal progress modal when taking a card payment, with a decline path.

## Acceptance Criteria

- [ ] Taking a card payment opens a terminal modal showing 'Processing on Square terminal…' then 'Payment approved', reflecting the real ProviderTxn state (not a fixed timer).
- [ ] A decline surfaces a clear retry / alternate-tender path rather than failing silently.
- [ ] On approval the sale completes and the post-checkout rebook view (PRD-06/CHECKOUT-ASSIST) is offered.
- [ ] Receipts remain available for card sales.

## UI designs / screenshots

- Prototype: Square-terminal modal (Processing → Approved) over the checkout; on decline, a retry / choose-another-tender prompt; on approval, the post-checkout rebook view (CHECKOUT-ASSIST).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(reads PRD-06/PAYMENT-PROVIDER)** — ProviderTxn state drives the modal; no new entity
  - _Modal mirrors ProviderTxn (auth/capture/decline); extends PRD-06/POS card tender._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Terminal progress modal bound to ProviderTxn state**
  Behaviour: a modal tracks the real ProviderTxn lifecycle (Processing → Approved) from the Square adapter (PRD-06/PAYMENT-PROVIDER). Requirements: reflects real state, not a fixed timer; on approval the sale completes and offers the rebook view (PRD-06/CHECKOUT-ASSIST).
- [ ] **Decline / retry / alternate-tender path**
  Behaviour: a declined card shows a clear retry or choose-another-tender prompt rather than failing silently. Requirements: maps the adapter's decline result to a recoverable UI state; never double-charges on retry (idempotent).
