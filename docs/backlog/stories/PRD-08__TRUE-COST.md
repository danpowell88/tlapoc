# True-cost / margin (COGS) reporting

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/TRUE-COST`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`, `PRD-04/VIAL-RECON`

## Background

As a owner, I want true-cost and margin reporting per treatment/service, so that I price and plan on real profitability.
The prototype adds true-cost reporting — cost of goods (units/vial cost, consumables) per treatment to show real margin, not just revenue.

## How it works

True-cost / margin (COGS) reporting: cost of goods (product units/vial cost, consumables) attributed per treatment/service, so margin = revenue - COGS is visible per service and practitioner. Feeds pricing & what-if (PRD-06); figures owner-gated. Detailed accounting still defers to Xero.
Shows real profitability, not just revenue.

## Requirements

- True-cost and margin reporting per treatment/service.

## Acceptance Criteria

- [ ] Cost of goods (product units/vial cost, consumables) is attributed per treatment/service.
- [ ] Margin = revenue − COGS surfaces per service and per practitioner.
- [ ] Feeds pricing & what-if (PRD-06/PRICING-WHATIF); figures are owner-gated.
- [ ] Detailed accounting still defers to Xero (attribution, not a ledger).

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Finance (finance.png) — true-cost/margin per treatment using vial/consumable cost; owner-only.

## Suggested data model

- **(read) MarginByService** — service_id, revenue, cogs(vial+consumables), margin by date
  - _Uses VIAL-RECON (PRD-04); attribution not a ledger (ADR-0027)._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0027](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
