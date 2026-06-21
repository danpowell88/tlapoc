# Pricing & what-if planning (owner)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PRICING-WHATIF`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

Payments (in-person POS + autopay), memberships & non-S4 rewards — Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law.

As a owner, I want to model pricing and run what-if scenarios, so that I can set prices and plan membership economics.

An owner pricing + what-if planner over the reporting read-models (REQ-MEMB-9, ADR-0022). The Finance screen is a light pricing + reporting hub; the ledger defers to Xero.

## Requirements

- To model pricing and run what-if scenarios.
- Traces to requirement(s): REQ-MEMB-9.

## Acceptance Criteria

- [ ] Pricing/what-if planner uses the same read-models as reporting (PRD-08).
- [ ] Scenario outputs are owner-gated.
- [ ] The Finance area is a pricing + reporting hub; in-app ledger/payroll/AP/BAS tooling is out of scope (Xero).
- [ ] Invoices/payments still sync to Xero from checkout.

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0022, ADR-0027 (see docs/adr/decision-log.md).
Depends on: PRD-06/POS.

## Other

Epic: PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards.
Source PRD: docs/prds/PRD-06-payments-memberships-rewards.md.
Backlog key: PRD-06/PRICING-WHATIF.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Checkout, Memberships; client-app.html Rewards/Account.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
