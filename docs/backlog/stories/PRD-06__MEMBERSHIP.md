# Memberships with automatic autopay & dunning

> **Epic:** [PRD-06 — Payments (in-person POS + autopay), memberships & non-S4 rewards](../epics/PRD-06.md)  ·  **Key:** `PRD-06/MEMBERSHIP`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-06/PAYMENT-PROVIDER`

## Background

As a client, I want to join a membership and have my card auto-charged on schedule, so that I get member perks without manual payments.
Membership plans/tiers with automatic recurring billing from a tokenised card-on-file (added online/in-app or at desk) and failed-payment dunning (REQ-MEMB-1/2/3).

## Requirements

- To join a membership and have my card auto-charged on schedule.

## Acceptance Criteria

- [ ] A membership auto-charges on schedule from a stored token (card added online/in-app or in person).
- [ ] A failed charge triggers dunning/recovery.
- [ ] Lifecycle (join/pause/cancel/win-back) tracked → MRR/churn reporting (PRD-08).
- [ ] Benefits/credits auto-apply at checkout.

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-06-payments-memberships-rewards.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-06-payments-memberships-rewards.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
