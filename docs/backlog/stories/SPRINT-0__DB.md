# Postgres + EF Core baseline & migrations

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/DB`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/IAC`

## Background

As a backend developer, I want a Postgres database with EF Core, a migration pipeline and base entity/columns conventions, so that every module adds schema consistently and migrations run automatically per environment.
A migrations-first data layer with a base entity convention (tenant_id, audit columns) underpins every module.

## Requirements

- A Postgres database with EF Core, a migration pipeline and base entity/columns conventions.

## Acceptance Criteria

- [ ] EF Core connects to Postgres; migrations apply automatically on deploy.
- [ ] Base entity convention includes tenant_id and created/updated audit columns.
- [ ] A sample entity round-trips through repository + migration in tests.
- [ ] Local dev uses a containerised Postgres seeded by S0-SEED.

## Technical notes (high level)

- Stack: Postgres + EF Core (RLS)
- Architecture decisions: [ADR-0002](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Postgres + EF Core baseline & migrations**
- [ ] **Apply via migrations; verify RLS/tenancy**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
