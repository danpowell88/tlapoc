# Closeout: reconcile to the Xero posting

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/CLOSEOUT-XERO-RECONCILE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/CLOSEOUT`

## Background

As a owner, I want the closeout to reconcile against the day's Xero posting, so that the till totals foot to the accounts and mismatches surface.
Plainly: check that the day's invoices and payments that posted to Xero (the clinic's cloud accounting system) add up to the closeout totals, and flag it if they don't. Where it fits: a follow-up to the basic daily closeout (PRD-06/CLOSEOUT); the basic slice balances and locks the till in-platform but does not cross-check Xero. Depends on the checkout-side Xero post (PRD-06/POS-XERO-POST) and the PRD-10 sync engine that owns the ledger. Figures are owner-gated (.fin).

## How it works

The basic closeout (PRD-06/CLOSEOUT) balances and locks the till in-platform; this follow-up reconciles it against the Xero (the clinic's cloud accounting system) post (PRD-10) — the day's posted invoices/payments should foot to the closeout totals, and a mismatch is flagged for investigation.
It does not re-implement the ledger; the accounting treatment lives in Xero. Depends on the checkout-side Xero post (PRD-06/POS-XERO-POST). All figures are owner-gated (.fin).

## Requirements

- The closeout to reconcile against the day's Xero posting.

## Acceptance Criteria

- [ ] The day's posted invoices/payments (PRD-06/POS-XERO-POST, PRD-10) foot to the closeout totals.
- [ ] A mismatch between the posted Xero (the clinic's cloud accounting system) figures and the closeout is flagged.
- [ ] Reconciliation does not re-implement the ledger — the ledger lives in Xero (PRD-10).
- [ ] Figures are owner-gated (.fin).

## UI designs / screenshots

- Prototype: Closeout — a 'reconciles to Xero' line comparing posted invoices/payments to the closeout totals, with a mismatch flag.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(reconciles against PRD-10)** — compares Closeout totals to the day's Xero-posted invoices/payments
  - _No new entity; reads the PRD-06/POS-XERO-POST output owned by PRD-10._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Reconcile closeout totals to the Xero posting + mismatch flag**
  Behaviour: the day's posted invoices/payments (PRD-06/POS-XERO-POST, PRD-10) foot to the closeout totals; a mismatch is flagged. Requirements: read the posted figures from PRD-10, do not re-implement the ledger; owner-only (.fin); audit any mismatch resolution.
