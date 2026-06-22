# Synthetic seed data & local dev environment

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SEED`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P2  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/DB`

## Background

As a developer, I want a one-command local environment seeded with synthetic tenant, staff, clients, catalogue and stock, so that I can run and demo any module locally without touching real data.
Realistic synthetic data (clinic, staff with credentials, clients, services incl. S4/non-S4, stock) lets every module be developed and demoed without real PII. All data must stay synthetic (project rule).

## How it works

A one-command local environment seeded with a synthetic tenant: staff roles/credentials, clients (incl. an under-18), services flagged S4/non-S4, and stock lots — all clearly synthetic (project rule), reproducible, and reused by integration/e2e tests. Lets any module be developed/demoed without real PII.

## Requirements

- A one-command local environment seeded with synthetic tenant, staff, clients, catalogue and stock.

## Acceptance Criteria

- [ ] A script spins up Postgres + API + web locally and seeds a synthetic tenant.
- [ ] Seed covers staff roles/credentials, clients (incl. an under-18), services flagged S4/non-S4, and stock lots.
- [ ] All seed data is clearly synthetic; no real client/staff/business info.
- [ ] Seed is reproducible and used by integration/e2e tests.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Synthetic seed data & local dev environment**
  Deliver per the acceptance criteria:
  - A script spins up Postgres + API + web locally and seeds a synthetic tenant.
  - Seed covers staff roles/credentials, clients (incl. an under-18), services flagged S4/non-S4, and stock lots.
  - All seed data is clearly synthetic; no real client/staff/business info.
  - Seed is reproducible and used by integration/e2e tests.
- [ ] **Apply via migrations; verify RLS/tenancy**
  Migration runs per environment; prove tenant isolation holds.
- [ ] **Document setup & usage**
  How to run/operate it; runbook notes for the team.
