# Pricing & what-if: Finance hub framing (defers to Xero)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PRICING-FINANCE-HUB`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/PRICING-WHATIF`

## Background

As a owner, I want the Finance screen to frame Pricing + Reports as a light hub that defers the ledger to Xero, so that it's clear what the platform does and what lives in the accounting system.
Plainly: wrap the pricing planner in a Finance screen that links Pricing and Reports and clearly states the books (payroll, AP, GST/BAS, reconciliation) live in Xero. Where it fits: a follow-up to the pricing core (PRD-06/PRICING-WHATIF) that adds the surrounding framing; it does not add new financial tooling. Owner-only (.fin); the ledger defers to Xero (PRD-10, ADR-0027).

## How it works

The surrounding Finance screen frames the pricing planner as a light pricing + reporting hub ('the books live in Xero'). It links to Pricing and Reports and states what's handled in Xero (the clinic's cloud accounting system) — payroll, AP (accounts payable), GST/BAS (business activity statement), reconciliation.
No in-app ledger/payroll/AP/BAS tooling is introduced (ADR-0027 revised); invoices/payments still sync from checkout (PRD-06/POS-XERO-POST). This extends the pricing core (PRD-06/PRICING-WHATIF). Owner-only (.fin); loading/empty/error states handled.

## Requirements

- The Finance screen to frame Pricing + Reports as a light hub that defers the ledger to Xero.

## Acceptance Criteria

- [ ] The Finance screen frames Pricing + Reports as a light pricing + reporting hub ('the books live in Xero').
- [ ] It links to Pricing and Reports and states what's handled in Xero (the clinic's cloud accounting system): payroll, AP (accounts payable), GST/BAS (business activity statement), reconciliation.
- [ ] No in-app ledger/payroll/AP/BAS tooling is introduced (ADR-0027); invoices/payments still sync from checkout (PRD-06/POS-XERO-POST).
- [ ] Owner-only (.fin); loading/empty/error states handled.

## UI designs / screenshots

- Prototype: Finance screen as the pricing + reporting hub — links to Pricing & what-if and Reports, with a note that payroll/AP/GST-BAS/reconciliation live in Xero.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(framing over PRD-06/PRICING-WHATIF + PRD-08)** — Finance hub linking Pricing + Reports; no ledger entity
  - _No new entity; defers the ledger to Xero (ADR-0027)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Finance hub framing (links Pricing + Reports; defers to Xero)**
  Behaviour: the Finance screen frames Pricing + Reports as a light hub and states what lives in Xero (payroll, AP, GST/BAS, reconciliation). Requirements: no in-app ledger/payroll/AP/BAS tooling (ADR-0027); invoices/payments still sync from checkout (PRD-06/POS-XERO-POST); owner-only (.fin); loading/empty/error states.
