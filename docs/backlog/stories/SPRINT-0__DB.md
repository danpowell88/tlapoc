# Postgres + EF Core baseline & migrations

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/DB`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/IAC`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a backend developer, I want a Postgres database with EF Core, a migration pipeline and base entity/columns conventions, so that every module adds schema consistently and migrations run automatically per environment.

A migrations-first data layer with a base entity convention (tenant_id, audit columns) underpins every module.

## Requirements

- A Postgres database with EF Core, a migration pipeline and base entity/columns conventions.

## Acceptance Criteria

- [ ] EF Core connects to Postgres; migrations apply automatically on deploy.
- [ ] Base entity convention includes tenant_id and created/updated audit columns.
- [ ] A sample entity round-trips through repository + migration in tests.
- [ ] Local dev uses a containerised Postgres seeded by S0-SEED.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Postgres + EF Core (RLS).
Architecture decisions: ADR-0002 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/IAC.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/DB.
Phase: 0 · Priority: P0 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Postgres + EF Core baseline & migrations**
- [ ] **Apply via migrations; verify RLS/tenancy**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
