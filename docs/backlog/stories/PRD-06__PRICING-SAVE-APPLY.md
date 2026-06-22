# Pricing & what-if: save scenario + apply-via-admin handoff

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PRICING-SAVE-APPLY`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/PRICING-WHATIF`

## Background

As a owner, I want to save a pricing scenario and hand proposed prices to the normal admin, so that I can compare scenarios and apply a chosen one through the audited path.
Plainly: keep a what-if scenario for comparison, and let 'Apply' pass the proposed prices to the real admin — it never writes live prices itself. Where it fits: a follow-up to the pricing core (PRD-06/PRICING-WHATIF), which projects but doesn't persist or apply; this adds saving and the handoff. The planner proposes and projects only — the ledger lives in Xero (PRD-10) and live pricing changes go through PRD-06/MEMBERSHIP-PLANS-ADMIN (capability-gated, audited). Owner-only (.fin).

## How it works

A PricingScenario (inputs/outputs JSON) can be saved for comparison; an 'Apply' action does NOT write live prices — it hands the proposed prices to the normal catalogue/membership admin (PRD-06/MEMBERSHIP-PLANS-ADMIN, capability-gated, audited).
The planner proposes and projects only (read-only over the ledger, which lives in Xero, PRD-10); in-app ledger/payroll/AP (accounts payable)/BAS (business activity statement) tooling is explicitly out of scope. This extends the pricing core (PRD-06/PRICING-WHATIF). Owner-only (.fin).

## Requirements

- To save a pricing scenario and hand proposed prices to the normal admin.

## Acceptance Criteria

- [ ] A PricingScenario (inputs/outputs JSON) can be saved for comparison.
- [ ] An 'Apply' action does NOT write live prices — it hands the proposed prices to the normal catalogue/membership admin (PRD-06/MEMBERSHIP-PLANS-ADMIN, capability-gated, audited).
- [ ] The planner proposes and projects only; in-app ledger/payroll/AP (accounts payable)/BAS (business activity statement) tooling is explicitly out of scope (Xero).
- [ ] Owner-only (.fin).

## UI designs / screenshots

- Prototype: Pricing & what-if — save/compare scenarios; an 'Apply' that routes proposed prices to the admin path (does not write live prices).

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **PricingScenario** — id, tenant_id, inputs(json: plan/service prices, churn assumption), outputs(json: MRR/rev/net), created_by
  - _New entity; over PRD-08 read-models; owner-gated; no in-app ledger (ADR-0027). Apply goes via PRD-06/MEMBERSHIP-PLANS-ADMIN._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Save PricingScenario + apply-via-admin handoff**
  Behaviour: a PricingScenario (inputs/outputs JSON) is saved for comparison; 'Apply' hands proposed prices to PRD-06/MEMBERSHIP-PLANS-ADMIN (capability-gated, audited) rather than writing live prices. Requirements: planner proposes/projects only; ledger lives in Xero (PRD-10); in-app ledger/payroll/AP/BAS out of scope (ADR-0027); owner-only (.fin).
