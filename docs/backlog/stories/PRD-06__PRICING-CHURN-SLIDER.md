# Pricing & what-if: churn-sensitivity slider

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/PRICING-CHURN-SLIDER`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-06/PRICING-WHATIF`

## Background

As a owner, I want a churn-sensitivity slider that adjusts the projection under an elasticity assumption, so that I can see how a price rise might shed members before I commit.
Plainly: a slider that says 'if I raise the price, this share of members leave' and re-runs the projection on that assumption. Where it fits: a follow-up to the pricing core (PRD-06/PRICING-WHATIF), which projects MRR/revenue/net from plan-price edits; this adds the churn elasticity dimension. The projection stays a clearly-labelled model, not a guarantee (ADR-0022). Owner-only (.fin).

## How it works

A churn-sensitivity slider (e.g. '6% leave / +$10') drives the live Projected-impact panel computing Membership MRR (monthly recurring revenue) and net under that elasticity assumption (ADR-0022). It extends the pricing core (PRD-06/PRICING-WHATIF) projection with a churn dimension.
The projection is a model, clearly labelled as an assumption, not a guarantee; it recomputes live as prices/slider change; a Reset returns to current actuals. Owner-only (.fin).

## Requirements

- A churn-sensitivity slider that adjusts the projection under an elasticity assumption.

## Acceptance Criteria

- [ ] A churn-sensitivity slider (e.g. '6% leave / +$10') drives the live Projected-impact panel under that elasticity assumption (ADR-0022).
- [ ] The projection recomputes live as the slider moves and is clearly labelled as a model/assumption, not a guarantee.
- [ ] A Reset returns to current actuals.
- [ ] Owner-only (.fin).

## UI designs / screenshots

- Prototype: Pricing & what-if — a Churn-sensitivity slider ('6% leave / +$10') feeding the Projected-impact panel.

![checkout — prototype screen](../screens/checkout.png)

## Suggested data model

- **(extends PRD-06/PRICING-WHATIF projection)** — + churn assumption input → adjusted MRR/net projection
  - _No new entity; elasticity assumption per ADR-0022; owner-only (.fin)._

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Churn-sensitivity slider feeding the Projected-impact panel**
  Behaviour: a churn-sensitivity slider (e.g. '6% leave / +$10') drives the Projected-impact panel under that elasticity assumption (ADR-0022). Requirements: clearly labelled as a model/assumption; recomputes live; Reset returns to actuals; owner-only (.fin).
