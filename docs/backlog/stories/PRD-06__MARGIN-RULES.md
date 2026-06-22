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

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - RewardRule.value_cap / eligible_items — + reporting: reward_cost vs retention (Owner-gated; reward comms consented-only.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Reward rules enforce value caps and eligible-item lists.
  - Rule: Reward-cost vs retention surfaces in reporting (PRD-08).
  - Rule: Reward communications go only to consented, logged-in clients (no public S4 price promotion).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-06/REWARDS-ENGINE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C9, C23 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Reward communications go only to consented, logged-in clients (no public S4 price promotion).
  - Rule config is owner-gated.
