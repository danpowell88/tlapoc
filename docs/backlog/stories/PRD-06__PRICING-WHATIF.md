# Pricing & what-if planning (owner)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PRICING-WHATIF`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want to model pricing and run what-if scenarios, so that I can set prices and plan membership economics.
What this is, plainly: an owner's pricing sandbox — change prices, drag a churn assumption, and watch projected revenue move, without touching live prices until you choose to. Where it sits: it reads the same reporting read-models (PRD-08) and sits in the Payments layer after the clinical core; the real ledger lives in Xero (PRD-10). An owner pricing + what-if planner over the reporting read-models (REQ-MEMB-9, ADR-0022). The Finance screen is a light pricing + reporting hub; the ledger defers to Xero.

## How it works

The planner reads the same read-models as Reports (PRD-08): current plan member counts and MRR (monthly recurring revenue), service volumes and revenue. The owner edits plan/service prices inline and moves a churn-sensitivity slider (e.g. '6% leave / +$10'); a Projected impact panel computes Membership MRR, Service rev/mo, Net/month and projected annual impact under that elasticity assumption (ADR-0022). It proposes and projects — it does not mutate live pricing; applying a change goes through the normal catalogue/membership admin (capability-gated, audited).
Scope is deliberately narrow: the Finance screen is pricing + reporting only. In-app ledger, commission pay-run, supplier POs/AP, refund/dispute management and BAS (business activity statement)/GST (goods and services tax) tooling are out (ADR-0027 revised) — those defer to Xero; invoices/payments still sync from checkout. A PricingScenario can be saved (inputs/outputs JSON) for comparison.

## Requirements

- To model pricing and run what-if scenarios.

## Acceptance Criteria

- [ ] The pricing/what-if planner reads the same read-models as reporting (PRD-08) and projects MRR (monthly recurring revenue)/revenue/net under a churn-sensitivity assumption.
- [ ] It proposes/projects only — it does not mutate live pricing; applying a change goes through normal admin (audited).
- [ ] Scenario outputs are owner-gated.
- [ ] In-app ledger/payroll/AP (accounts payable)/BAS (business activity statement) tooling is out of scope (Xero); invoices/payments still sync from checkout.

## UI designs / screenshots

_Prototype screen: prototype.html — Checkout, Memberships; client-app.html Rewards/Account._

- Prototype: Memberships -> Pricing & what-if (owner-only) — editable membership plan prices with member counts + per-tier MRR, a Churn-sensitivity slider ('6% leave / +$10'), a Projected impact panel (Membership MRR, Service rev/mo, Net/month, Projected annual impact), and editable Service pricing rows; Finance screen as the pricing + reporting hub.

![memb-pricing — prototype screen](../screens/memb-pricing.png)

## Suggested data model

- **PricingScenario** — id, tenant_id, inputs(json: plan/service prices, churn assumption), outputs(json: MRR/rev/net), created_by
  - _Over PRD-08 read-models; owner-gated; no in-app ledger (ADR-0027). Apply goes via normal admin._

## Technical notes (high level)

- Architecture decisions: [ADR-0022](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0027](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **PricingScenario model over PRD-08 read-models (migrations)**
  Model PricingScenario (tenant_id + RLS (row-level security)): inputs JSON (plan/service prices + churn assumption) and computed outputs JSON (MRR (monthly recurring revenue) — monthly recurring revenue/rev/net).
  - No live-pricing mutation here; read current state from PRD-08 read-models.
  - Owner-gated.
- [ ] **What-if compute API (read-only) + apply-via-admin handoff**
  Server-side.
  - Compute projected Membership MRR (monthly recurring revenue), Service rev/mo, Net/month and annual impact from edited prices + the churn-sensitivity assumption (elasticity) over PRD-08 read-models.
  - Save/load scenarios; owner-only.
  - 'Apply' does NOT write here — it hands the proposed prices to the normal catalogue/membership admin (capability-gated, audited).
- [ ] **Pricing & what-if web UI (owner-only)**
  Angular per the screenshot.
  - Editable plan prices with member counts + per-tier MRR (monthly recurring revenue); churn-sensitivity slider; live Projected-impact panel; editable service pricing rows.
  - Read-only planner styling (proposes, doesn't apply); owner-only .fin capability gate; loading/empty/error states.
