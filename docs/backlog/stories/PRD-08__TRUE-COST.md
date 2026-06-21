# True-cost / margin (COGS) reporting

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/TRUE-COST`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`, `PRD-04/VIAL-RECON`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a owner, I want true-cost and margin reporting per treatment/service, so that I price and plan on real profitability.

The prototype adds true-cost reporting — cost of goods (units/vial cost, consumables) per treatment to show real margin, not just revenue.

## Requirements

- True-cost and margin reporting per treatment/service.
- Traces to requirement(s): REQ-RPT-6.

## Acceptance Criteria

- [ ] Cost of goods (product units/vial cost, consumables) is attributed per treatment/service.
- [ ] Margin = revenue − COGS surfaces per service and per practitioner.
- [ ] Feeds pricing & what-if (PRD-06/PRICING-WHATIF); figures are owner-gated.
- [ ] Detailed accounting still defers to Xero (attribution, not a ledger).

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0027 (see docs/adr/decision-log.md).
Depends on: PRD-08/READ-MODELS, PRD-04/VIAL-RECON.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/TRUE-COST.
Phase: 1 · Priority: P2 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
