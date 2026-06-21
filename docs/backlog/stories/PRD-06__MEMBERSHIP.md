# Memberships with automatic autopay & dunning

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

Payments (in-person POS + autopay), memberships & non-S4 rewards — Commerce for the clinic: in-person POS (Square card-present + recorded cash + gift cards), automatic recurring membership autopay via stored card-on-file, packages/series, and a rewards engine that only ever applies to non-S4 items — driving repeat visits without eroding margin or breaching advertising law.

As a client, I want to join a membership and have my card auto-charged on schedule, so that I get member perks without manual payments.

Membership plans/tiers with automatic recurring billing from a tokenised card-on-file (added online/in-app or at desk) and failed-payment dunning (REQ-MEMB-1/2/3).

## Requirements

- To join a membership and have my card auto-charged on schedule.
- Traces to requirement(s): REQ-MEMB-1, REQ-MEMB-2, REQ-MEMB-3.

## Acceptance Criteria

- [ ] A membership auto-charges on schedule from a stored token (card added online/in-app or in person).
- [ ] A failed charge triggers dunning/recovery.
- [ ] Lifecycle (join/pause/cancel/win-back) tracked → MRR/churn reporting (PRD-08).
- [ ] Benefits/credits auto-apply at checkout.

## UI designs / screenshots

prototype.html — Checkout, Memberships; client-app.html Rewards/Account.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-06/PAYMENT-PROVIDER.

## Other

Epic: PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards.
Source PRD: docs/prds/PRD-06-payments-memberships-rewards.md.
Backlog key: PRD-06/MEMBERSHIP.
Phase: 1 · Priority: P0 · Estimate: 5 pts.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
