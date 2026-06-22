# Rewards engine — non-S4 only

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/REWARDS-ENGINE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a client, I want to earn and redeem rewards on non-S4 items only, so that I'm rewarded without breaching S4 advertising rules.
Visit-based + membership rewards that the engine blocks from ever applying to S4 items; configuring an S4 reward is blocked (REQ-MEMB-4/5/7, C9/ADR-0014).

## How it works

Visit-based rewards (milestones/every-Nth-visit) + membership perks that the engine blocks from ever applying to S4 items; configuring an S4 reward is blocked (C9/ADR-0014). Rewards apply to non-S4 items, add-ons, or account/gift credit — never the toxin itself.
Drives repeat visits without eroding margin or breaching advertising law. The catalog schedule flag (PRD-04) drives eligibility.

## Requirements

- To earn and redeem rewards on non-S4 items only.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Visit-based rewards (milestones/every-Nth-visit) + membership perks on non-S4 items, add-ons or account/gift credit.
- [ ] The engine refuses to earn, redeem or discount against any S4-flagged item.
- [ ] Attempting to configure an S4 reward is blocked.
- [ ] Catalog schedule flag (from PRD-04) drives eligibility.

## UI designs / screenshots

- Prototype: Memberships -> Loyalty (memb-loyalty.png) — reward rules + ledger; S4 items in the catalog show disabled reward/discount controls with a tooltip (the S4 guardrail).
- Earn/redeem visible on the Client 360 + client app rewards.

![memb-loyalty — prototype screen](../screens/memb-loyalty.png)

## Suggested data model

- **RewardRule** — id, tenant_id, basis(milestone|nth_visit|membership), eligible_items(non-S4), value_cap
  - _S4 eligibility blocked (C9)._
- **RewardLedger** — id, client_id, earned, redeemed, balance, ref
  - _Non-S4 redemptions only._

## Technical notes (high level)

- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - RewardRule — id, tenant_id, basis(milestone|nth_visit|membership), eligible_items(non-S4), value_cap (S4 eligibility blocked (C9).)
  - RewardLedger — id, client_id, earned, redeemed, balance, ref (Non-S4 redemptions only.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Visit-based rewards (milestones/every-Nth-visit) + membership perks on non-S4 items, add-ons or account/gift credit.
  - Rule: The engine refuses to earn, redeem or discount against any S4-flagged item.
  - Rule: Attempting to configure an S4 reward is blocked.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/PRODUCT-CATALOGUE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C9 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Attempting to configure an S4 reward is blocked.
