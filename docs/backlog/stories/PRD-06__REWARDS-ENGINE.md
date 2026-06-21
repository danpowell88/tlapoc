# Rewards engine — non-S4 only

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/REWARDS-ENGINE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a client, I want to earn and redeem rewards on non-S4 items only, so that I'm rewarded without breaching S4 advertising rules.
Visit-based + membership rewards that the engine blocks from ever applying to S4 items; configuring an S4 reward is blocked (REQ-MEMB-4/5/7, C9/ADR-0014).

## Requirements

- To earn and redeem rewards on non-S4 items only.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Visit-based rewards (milestones/every-Nth-visit) + membership perks on non-S4 items, add-ons or account/gift credit.
- [ ] The engine refuses to earn, redeem or discount against any S4-flagged item.
- [ ] Attempting to configure an S4 reward is blocked.
- [ ] Catalog schedule flag (from PRD-04) drives eligibility.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C9); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
