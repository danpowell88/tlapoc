# Row-level-security multi-tenancy baseline

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/RLS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/DB`, `SPRINT-0/SPIKE-RLS`

## Background

As a platform engineer, I want Postgres RLS policies keyed on tenant_id, with EF Core setting the session tenant context on every request, so that a query can never return another tenant's rows, even on a developer mistake.
Tenant isolation is enforced in the database via RLS, with the API setting tenant context per request (ADR-0003). This is the single most important safety property of the data layer.

## How it works

Postgres row-level-security policies keyed on tenant_id, with EF Core setting the session tenant on every request (ADR-0003), so a query can never return another tenant's rows — proven by an integration test (Tenant A cannot read Tenant B; cross-tenant id -> not-found). Background jobs use an explicit, audited elevated path. The single most important data-layer safety property.

## Requirements

- Postgres RLS policies keyed on tenant_id, with EF Core setting the session tenant context on every request.

## Acceptance Criteria

- [ ] RLS policies are applied to all tenant-scoped tables.
- [ ] API middleware sets the session tenant from the authenticated principal on every request.
- [ ] An integration test proves Tenant A cannot read Tenant B rows and a cross-tenant id returns not-found.
- [ ] Bypassing tenant context (e.g. background jobs) uses an explicit, audited elevated path.

## Suggested data model

- **RLS policy** — USING (tenant_id = current_setting('app.tenant'))
  - _Session tenant set per request; elevated path audited._

## Technical notes (high level)

- Stack: Postgres + EF Core (RLS)
- Architecture decisions: [ADR-0003](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Row-level-security multi-tenancy baseline**
- [ ] **Apply via migrations; verify RLS/tenancy**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
