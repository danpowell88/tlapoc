# Pricing & what-if planning (owner)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PRICING-WHATIF`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want to model pricing and run what-if scenarios, so that I can set prices and plan membership economics.
An owner pricing + what-if planner over the reporting read-models (REQ-MEMB-9, ADR-0022). The Finance screen is a light pricing + reporting hub; the ledger defers to Xero.

## How it works

An owner pricing + what-if planner over the reporting read-models — model prices and scenarios (e.g. membership economics). The Finance area is a light pricing + reporting hub; the ledger/payroll/AP/BAS tooling defers to Xero. Invoices/payments still sync from checkout.
Scenario outputs are owner-gated.

## Requirements

- To model pricing and run what-if scenarios.

## Acceptance Criteria

- [ ] Pricing/what-if planner uses the same read-models as reporting (PRD-08).
- [ ] Scenario outputs are owner-gated.
- [ ] The Finance area is a pricing + reporting hub; in-app ledger/payroll/AP/BAS tooling is out of scope (Xero).
- [ ] Invoices/payments still sync to Xero from checkout.

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Memberships -> Pricing & what-if (memb-pricing.png) and Finance (finance.png) — pricing model + scenario sliders; owner-only.
- Reads the same read-models as Reports (PRD-08).

![memb-pricing — prototype screen](../screens/memb-pricing.png)

## Suggested data model

- **PricingScenario** — id, tenant_id, inputs(json), outputs(json)
  - _Over PRD-08 read-models; owner-gated. No in-app ledger (ADR-0027)._

## Technical notes (high level)

- Architecture decisions: [ADR-0022](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0027](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - PricingScenario — id, tenant_id, inputs(json), outputs(json) (Over PRD-08 read-models; owner-gated. No in-app ledger (ADR-0027).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Pricing/what-if planner uses the same read-models as reporting (PRD-08).
  - Rule: Scenario outputs are owner-gated.
  - Rule: The Finance area is a pricing + reporting hub; in-app ledger/payroll/AP/BAS tooling is out of scope (Xero).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-06/POS.
- [ ] **Web UI**
  Build on the Angular web app: the memb-pricing per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Memberships -> Pricing & what-if (memb-pricing.png) and Finance (finance.png) — pricing model + scenario sliders; owner-only.
  - Reads the same read-models as Reports (PRD-08).
