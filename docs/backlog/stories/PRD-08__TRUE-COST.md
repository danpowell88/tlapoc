# True-cost / margin (COGS) reporting

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/TRUE-COST`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`, `PRD-04/VIAL-RECON`

## Background

As a owner, I want true-cost and margin reporting per treatment/service, so that I price and plan on real profitability.
The prototype adds true-cost reporting — cost of goods (units/vial cost, consumables) per treatment to show real margin, not just revenue.

## How it works

True-cost / margin (COGS) reporting so the owner prices and plans on real profitability, not just top-line revenue. It attributes cost of goods per treatment/service — product units/vial cost (from the per-product, per-unit stock model and vial reconciliation, PRD-04 VIAL-RECON) plus consumables — so margin = revenue − COGS surfaces per service and per practitioner. The Finance screen is the home: a light pricing + reporting hub, deliberately not a ledger.
This is attribution, not accounting (ADR-0027, revised): detailed accounting — payroll, super, commission/pay-splits, supplier POs/AP, refund/dispute management, GST/BAS lodgement — lives in Xero (PRD-10 XERO) and with the bookkeeper. The app keeps the clinical/commercial decisions: the margin numbers feed the pricing & what-if planner (PRD-06 PRICING-WHATIF / ADR-0022) so a price change can be modelled against real cost.
Every figure here is money and is gated behind the owner financial capability — the Finance area is owner-only; the 'Handled in Xero, not here' footnote makes the boundary explicit.

## Requirements

- True-cost and margin reporting per treatment/service.

## Acceptance Criteria

- [ ] Cost of goods (product units/vial cost + consumables) is attributed per treatment/service using the per-product/per-unit stock model.
- [ ] Margin = revenue − COGS surfaces per service and per practitioner.
- [ ] Margin feeds the pricing & what-if planner (PRD-06).
- [ ] Attribution only — detailed accounting (payroll/PO/AP/dispute/BAS) defers to Xero (ADR-0027); all figures owner-gated.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Finance (finance.png) — 'The books live in Xero … in the app you keep pricing and high-level reporting'.
- Xero-connected banner; tiles: Revenue today, This month, Avg / visit, Membership MRR (all owner-gated).
- Cards: 'Pricing & what-if' (Open pricing →) and 'Reporting' (Open reports →); true-cost/margin per treatment sits in the reporting view.
- Footnote: 'Handled in Xero / integrations, not here: payroll & super, commission / pay-splits, supplier POs & AP, refund reconciliation, GST/BAS lodgement.'
- Entire Finance area is owner-only (.fin).

![finance — prototype screen](../screens/finance.png)

## Suggested data model

- **(read) MarginByService** — service_id, practitioner_id?, period, revenue, cogs_product(vial/units), cogs_consumables, margin
  - _Uses VIAL-RECON (PRD-04) for vial/unit cost; attribution not a ledger (ADR-0027); owner-gated; feeds PRD-06 PRICING-WHATIF._

## Technical notes (high level)

- Architecture decisions: [ADR-0027](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection: true-cost / margin (COGS)**
  Project MarginByService = revenue − COGS per service (and per practitioner) over a window, where COGS = product/vial cost (from the per-product/per-unit stock model + VIAL-RECON, PRD-04) + consumables. Tag all fields owner-financial. Expose the margin figures to the PRD-06 PRICING-WHATIF planner. This is attribution over the read schema, not a ledger — no payroll/PO/AP/BAS computation (ADR-0027).
- [ ] **Web UI: Finance true-cost / margin (owner-only)**
  Build the Finance hub (finance.png): Xero-connected banner, the owner-gated tiles (Revenue today, This month, Avg/visit, Membership MRR), the Pricing & what-if and Reporting cards, the true-cost/margin-per-treatment view, and the explicit 'Handled in Xero, not here' footnote drawing the attribution/accounting boundary. Gate the entire area behind .fin.
