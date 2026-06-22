# Checkout: post completed sale to Xero (per-line tax mapping)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/POS-XERO-POST`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want completed sales to post to Xero with per-line account and tax mapping, so that the books reconcile without re-keying invoices.
Plainly: when a sale completes, send the invoice and payment to Xero (the clinic's cloud accounting system) with each line mapped to the right account and tax code. Where it fits: a follow-up to the basic in-person POS checkout (PRD-06/POS); the basic slice records the sale and Closeout in-platform but does not post to Xero. The detailed integration and auth live in PRD-10; this story is the checkout-side enqueue + per-line mapping that PRD-10 consumes. Per-line tax comes from PRD-06/POS-GST. All money figures are owner-only (.fin); the ledger itself lives in Xero.

## How it works

On completion a sale enqueues a Xero (the clinic's cloud accounting system) post (PRD-10) carrying per-line account/tax mapping (per-line GST from PRD-06/POS-GST). This extends the basic checkout (PRD-06/POS), which records the sale and writes the Closeout but does not post externally. The enqueue is idempotent so a retried completion never double-posts the same invoice.
The Xero integration, auth and sync engine are owned by PRD-10; this story is the checkout-side hand-off and the per-line mapping. The day's posted invoices/payments should foot to the Closeout totals (PRD-06/CLOSEOUT). All money figures are owner-only (.fin); the actual ledger lives in Xero.

## Requirements

- Completed sales to post to Xero with per-line account and tax mapping.

## Acceptance Criteria

- [ ] On sale completion the invoice + payment(s) enqueue a Xero (the clinic's cloud accounting system) post with per-line account/tax mapping (PRD-10).
- [ ] The post is idempotent — a retried completion never double-posts the same invoice.
- [ ] Closeout reconciles to the posted Xero figures (PRD-06/CLOSEOUT).
- [ ] All money figures are owner-only (.fin); the ledger lives in Xero, not re-implemented here.

## UI designs / screenshots

- Prototype: checkout note 'Invoice posts to Xero on completion'; no dedicated screen — surfaces via the Closeout reconciliation and PRD-10 sync status.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(enqueue to PRD-10)** — Invoice + Payment(s) → Xero post job with per-line account/tax mapping
  - _Per-line tax from PRD-06/POS-GST; idempotent; ledger owned by Xero (PRD-10)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Enqueue Xero post on completion with per-line mapping**
  Behaviour: completing a sale enqueues a Xero post job carrying each line's account + tax code. Requirements: idempotent per invoice (no double-post on retry); per-line tax from PRD-06/POS-GST; the PRD-10 sync engine consumes the job; owner-only (.fin).
- [ ] **Closeout-to-Xero reconciliation hook**
  Behaviour: the day's posted invoices/payments foot to the Closeout totals (PRD-06/CLOSEOUT); a mismatch is flagged. Requirements: reconcile against the Xero post, not re-implement the ledger; owner-only.
