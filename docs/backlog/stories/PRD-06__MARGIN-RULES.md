# Margin-aware reward rules

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MARGIN-RULES`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-06/REWARDS-ENGINE`

## Background

Payments (in-person POS + autopay), memberships & non-S4 rewards — Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law.

As a owner, I want to set margin-aware reward rules with caps and eligible items and see reward-cost vs retention, so that rewards drive retention without eroding margin.

Owners set value caps and eligible items; reporting shows reward-cost vs retention (REQ-MEMB-6). Reward comms respect advertising rules (C9/C23).

## Requirements

- To set margin-aware reward rules with caps and eligible items and see reward-cost vs retention.
- Traces to requirement(s): REQ-MEMB-6.
- Must satisfy compliance obligation(s): C9, C23.

## Acceptance Criteria

- [ ] Reward rules enforce value caps and eligible-item lists.
- [ ] Reward-cost vs retention surfaces in reporting (PRD-08).
- [ ] Reward communications go only to consented, logged-in clients (no public S4 price promotion).
- [ ] Rule config is owner-gated.

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-06/REWARDS-ENGINE.

## Other

Epic: PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards.
Source PRD: docs/prds/PRD-06-payments-memberships-rewards.md.
Backlog key: PRD-06/MARGIN-RULES.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C9, C23.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C9, C23); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
