# Postgres + EF Core baseline & migrations

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/DB`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/IAC`

## Background

As a backend developer, I want a Postgres database with EF Core, a migration pipeline and base entity/columns conventions, so that every module adds schema consistently and migrations run automatically per environment.
A migrations-first data layer with a base entity convention (tenant_id, audit columns) underpins every module.

## How it works

EF Core connects to the Azure Postgres Flexible Server provisioned by IAC. Migrations are the single source of schema truth — generated in the codebase, reviewed in PRs, and applied automatically on deploy (the runner CICD invokes), never by hand-editing a database. Local dev runs a containerised Postgres seeded by SEED, so the same migrations produce the same schema everywhere.
A base-entity convention is inherited by every tenant-scoped table: a primary key, tenant_id (the column RLS will key on), and created/updated audit columns (created_at/by, updated_at/by) populated centrally via an EF Core SaveChanges interceptor so modules don't repeat the plumbing. This convention is configured once in the DbContext model-building so new entities pick it up by inheriting the base type.
A sample entity round-trips through a repository + migration in an integration test against a real Postgres, proving the convention, the migration pipeline and connectivity end-to-end before feature modules rely on it. The base-entity columns deliberately set up what RLS (tenant_id) and the audit interceptor (audit columns) need next.

## Requirements

- A Postgres database with EF Core, a migration pipeline and base entity/columns conventions.

## Acceptance Criteria

- [ ] EF Core connects to Postgres; migrations apply automatically on deploy.
- [ ] Base entity convention includes tenant_id and created/updated audit columns.
- [ ] A sample entity round-trips through repository + migration in tests.
- [ ] Local dev uses a containerised Postgres seeded by S0-SEED.

## Suggested data model

- **BaseEntity** — id, tenant_id, created_at, created_by, updated_at, updated_by
  - _Inherited by every tenant-scoped table; audit columns set by a SaveChanges interceptor; tenant_id is the RLS key._

## Technical notes (high level)

- Architecture decisions: [ADR-0002](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Stand up EF Core + the base-entity convention and migration pipeline**
  Establish the DbContext, the base-entity convention and the migrations-first workflow against the IAC-provisioned Postgres.
  - A BaseEntity (id, tenant_id, created/updated audit columns) applied via model-building conventions so every tenant-scoped entity inherits it.
  - A SaveChanges interceptor that stamps audit columns (and tenant_id from the request context once RLS lands) so modules never hand-set them.
  - Migration generation in the codebase as the only way schema changes; naming/folder convention for module migrations.
  - Connection comes from per-environment config/secret (SECRETS), never hard-coded.
- [ ] **Automate migrations on deploy and a containerised local Postgres**
  Make migrations apply automatically per environment and give every dev an identical local database.
  - A migration runner CICD invokes on deploy (idempotent, re-runnable, ordered) so each environment converges to the migrated schema.
  - A containerised Postgres for local dev that SEED populates; same migrations, same result as the cloud environments.
  - A sample entity that round-trips through a repository + migration in an integration test against a real Postgres, proving connectivity + convention before modules depend on it.
- [ ] **Document the data conventions and how modules add schema**
  Write the data-layer guide so every module adds tables consistently.
  - The base-entity convention, what the audit interceptor sets, and the rule that all tenant-scoped tables carry tenant_id (the RLS hook).
  - How to author + review a migration, and how it gets applied per environment.
  - How local containerised Postgres + SEED fit together for development and tests.
