# Cost catalogue: single-source feed to margin report + pricing planner

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COST-CATALOGUE-FEED`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/COST-CATALOGUE`

## Background

As a owner, I want the cost catalogue to be the single source my margin report and pricing planner read, so that I change a cost once and every report and model stays consistent.
Plainly: wiring the per-procedure cost catalogue so the true-cost/margin report and the pricing what-if planner both read it — change a cost once and both update, with no re-keying. Where it fits: a follow-up to the per-procedure cost catalogue core (PRD-08/COST-CATALOGUE), which owns the editable cost components; this story makes those components the single source of truth the downstream surfaces consume. Margins and costs stay owner-only (.fin) across the hand-off.

## How it works

This follow-up makes the per-procedure cost catalogue (PRD-08/COST-CATALOGUE) the single source of truth the downstream money surfaces read: the true-cost/margin report (PRD-08/TRUE-COST) and the pricing & what-if planner (PRD-06/PRICING-WHATIF, ADR-0022). Change a consumable or device-per-use cost once in the catalogue and both surfaces reflect it — there is no re-keying of figures, so a margin and a price model can never silently disagree on what a treatment costs.
Costs and margins stay gated behind the owner-only financial (.fin) capability across the hand-off. The downstream projections may be eventually consistent (a cost change re-flows a moment later), consistent with the rest of Reporting.

## Requirements

- The cost catalogue to be the single source my margin report and pricing planner read.

## Acceptance Criteria

- [ ] The catalogue is the single source the true-cost/margin report (TRUE-COST) and the pricing & what-if planner (PRD-06) read.
- [ ] Changing a cost once re-flows into both surfaces (no re-keying).
- [ ] Margins/costs stay owner-only (.fin) across the hand-off.
- [ ] Eventual consistency acceptable for the downstream projections.

## UI designs / screenshots

- No new screen — this is the wiring that makes the catalogue's figures flow into the True-cost & margin table (TRUE-COST) and the Pricing & what-if planner (PRD-06).
- A cost change in the catalogue re-flows into both; margins/costs stay .fin owner-only across the hand-off.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **ProcedureCost (extends PRD-08/COST-CATALOGUE)** — consumed by MarginByService (TRUE-COST) + the PRD-06 pricing planner
  - _No new entity — exposes the existing ProcedureCost as the single source both downstream surfaces read; owner-gated._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Single-source feed to margin report + pricing planner**
  Behaviour: expose the catalogue as the single source the true-cost/margin report (TRUE-COST) and the pricing & what-if planner (PRD-06 PRICING-WHATIF) read. Requirements: changing a cost once re-flows into both surfaces (no re-keying); margins/costs stay owner-only across the hand-off; eventual consistency acceptable for the downstream projections.
