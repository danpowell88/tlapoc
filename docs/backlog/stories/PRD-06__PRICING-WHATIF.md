# Pricing & what-if — editable plan prices + projected impact (core)

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PRICING-WHATIF`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-06/POS`

## Background

As a owner, I want to edit membership plan prices and see projected impact, so that I can model a price change before committing to it.
What this is, plainly: an owner's pricing sandbox core — change membership plan prices and watch projected MRR/revenue/net move, without touching live prices. This is the minimal end-to-end core; the churn-sensitivity slider, editable service-pricing rows, saving a scenario + apply-via-admin handoff, and the Finance-hub framing are each added as their own follow-ups. Where it sits: it reads the same reporting read-models (PRD-08) and sits in the Payments layer after the clinical core; the real ledger lives in Xero (PRD-10). An owner pricing + what-if planner over the reporting read-models (REQ-MEMB-9, ADR-0022).

## How it works

The planner reads the same read-models as Reports (PRD-08): current plan member counts and MRR (monthly recurring revenue), service volumes and revenue. The owner edits plan/service prices inline and moves a churn-sensitivity slider (e.g. '6% leave / +$10'); a Projected impact panel computes Membership MRR, Service rev/mo, Net/month and projected annual impact under that elasticity assumption (ADR-0022). It proposes and projects — it does not mutate live pricing; applying a change goes through the normal catalogue/membership admin (capability-gated, audited).
Scope is deliberately narrow: the Finance screen is pricing + reporting only. In-app ledger, commission pay-run, supplier POs/AP, refund/dispute management and BAS (business activity statement)/GST (goods and services tax) tooling are out (ADR-0027 revised) — those defer to Xero; invoices/payments still sync from checkout. A PricingScenario can be saved (inputs/outputs JSON) for comparison.

## Requirements

- To edit membership plan prices and see projected impact.

## Acceptance Criteria

- [ ] The planner lists each plan with its member count and per-tier MRR (monthly recurring revenue), reading the same read-models as Reports (PRD-08).
- [ ] Editing a plan price is a what-if input only — it does NOT mutate live pricing (that's PRD-06/MEMBERSHIP-PLANS-ADMIN).
- [ ] A Projected-impact panel computes Membership MRR / revenue / net from the edits.
- [ ] Scenario outputs are owner-gated (.fin).

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

- [ ] **Editable membership plan prices + per-tier MRR (read-models)**
  Behaviour: the planner lists each plan with its member count and per-tier MRR (monthly recurring revenue), and lets the owner edit the monthly price inline; the figures read the same PRD-08 read-models as Reports. Requirements: editing here is a what-if input only — it does NOT mutate live plan pricing (that's PRD-06/MEMBERSHIP-PLANS-ADMIN); owner-only (.fin); reads current member counts/MRR from the read-models, not from a separate copy.
- [ ] **Projected-impact panel (MRR / revenue / net) + basic web UI**
  Behaviour: a Projected-impact panel computes Membership MRR (monthly recurring revenue), revenue and net from the edited plan prices, recomputing live as prices change; a basic owner-only screen wires the plan-price editor to the panel. Requirements: the projection is clearly labelled as a model/assumption, not a guarantee; a Reset returns to current actuals; read-only planner styling (proposes, doesn't apply); owner-only (.fin); loading/empty/error states. (Churn slider, service rows, save/apply and the Finance-hub framing are follow-ups.)
