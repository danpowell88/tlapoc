# Synthetic seed data & local dev environment

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SEED`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P2  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/DB`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a developer, I want a one-command local environment seeded with synthetic tenant, staff, clients, catalogue and stock, so that I can run and demo any module locally without touching real data.

Realistic synthetic data (clinic, staff with credentials, clients, services incl. S4/non-S4, stock) lets every module be developed and demoed without real PII. All data must stay synthetic (project rule).

## Requirements

- A one-command local environment seeded with synthetic tenant, staff, clients, catalogue and stock.

## Acceptance Criteria

- [ ] A script spins up Postgres + API + web locally and seeds a synthetic tenant.
- [ ] Seed covers staff roles/credentials, clients (incl. an under-18), services flagged S4/non-S4, and stock lots.
- [ ] All seed data is clearly synthetic; no real client/staff/business info.
- [ ] Seed is reproducible and used by integration/e2e tests.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Postgres + EF Core (RLS).
Depends on: SPRINT-0/DB.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/SEED.
Phase: 0 · Priority: P2 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Synthetic seed data & local dev environment**
- [ ] **Apply via migrations; verify RLS/tenancy**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
