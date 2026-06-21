# Margin-aware reward rules

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MARGIN-RULES`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-06/REWARDS-ENGINE`

## Background

As a owner, I want to set margin-aware reward rules with caps and eligible items and see reward-cost vs retention, so that rewards drive retention without eroding margin.
Owners set value caps and eligible items; reporting shows reward-cost vs retention (REQ-MEMB-6). Reward comms respect advertising rules (C9/C23).

## How it works

Owners set margin-aware reward rules (value caps, eligible items) and see reward-cost vs retention in reporting. Reward communications go only to consented, logged-in clients (no public S4 price promotion) (C9/C23).
Keeps loyalty profitable and compliant; rule config is owner-gated.

## Requirements

- To set margin-aware reward rules with caps and eligible items and see reward-cost vs retention.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Reward rules enforce value caps and eligible-item lists.
- [ ] Reward-cost vs retention surfaces in reporting (PRD-08).
- [ ] Reward communications go only to consented, logged-in clients (no public S4 price promotion).
- [ ] Rule config is owner-gated.

## UI designs / screenshots

- Prototype: Memberships -> Pricing & what-if (memb-pricing.png, owner-only .fin) — caps + eligible items; reward-cost vs retention surfaces in Reports (PRD-08).

![memb-pricing — prototype screen](../screens/memb-pricing.png)

## Suggested data model

- **RewardRule.value_cap / eligible_items** — + reporting: reward_cost vs retention
  - _Owner-gated; reward comms consented-only._

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C9, C23); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
