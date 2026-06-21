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

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C9); blocked path explains why.
