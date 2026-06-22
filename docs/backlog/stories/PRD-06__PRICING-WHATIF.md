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

- [ ] **Editable membership plan prices + per-tier MRR (read-models)**
  Behaviour: the planner lists each plan with its member count and per-tier MRR (monthly recurring revenue), and lets the owner edit the monthly price inline; the figures read the same PRD-08 read-models as Reports. Requirements: editing here is a what-if input only — it does NOT mutate live plan pricing (that's PRD-06/MEMBERSHIP-PLANS); owner-only (.fin); reads current member counts/MRR from the read-models, not from a separate copy.
- [ ] **Churn-sensitivity slider + Projected-impact panel**
  Behaviour: a churn-sensitivity slider (e.g. '6% leave / +$10') drives a live Projected-impact panel computing Membership MRR, Service rev/mo, Net/month and projected annual impact under that elasticity assumption (ADR-0022). Requirements: the projection is a model, clearly labelled as an assumption, not a guarantee; recomputes live as prices/slider change; a Reset returns to current actuals; owner-only.
- [ ] **Editable service pricing rows + projection**
  Behaviour: editable service-pricing rows (Anti-wrinkle, Dermal filler, Skin treatment, Consultation) with per-service volume and projected monthly revenue, feeding the same Projected-impact panel. Requirements: 'per-treatment price · assumes volume holds' is stated; editing is a what-if input only; volumes read from PRD-08 read-models; owner-only.
- [ ] **Save scenario + apply-via-admin handoff**
  Behaviour: a PricingScenario (inputs/outputs JSON) can be saved for comparison; an 'Apply' action does NOT write live prices — it hands the proposed prices to the normal catalogue/membership admin (capability-gated, audited). Requirements: the planner proposes and projects only (read-only over the ledger, which lives in Xero); in-app ledger/payroll/AP (accounts payable)/BAS (business activity statement) tooling is explicitly out of scope; owner-only (.fin).
- [ ] **Pricing & what-if web UI + Finance hub framing (owner-only)**
  Behaviour: the Angular Pricing & what-if screen wires the plan-price editor, churn slider, Projected-impact panel and service-pricing rows together; the surrounding Finance screen frames it as a light pricing + reporting hub ('the books live in Xero'). Requirements: read-only planner styling (proposes, doesn't apply); owner-only .fin capability gate; the Finance hub links to Pricing and Reports and states what's handled in Xero (payroll, AP, GST/BAS, reconciliation); loading/empty/error states.
