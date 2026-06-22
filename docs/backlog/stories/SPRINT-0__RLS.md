# Row-level-security multi-tenancy baseline

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/RLS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/DB`, `SPRINT-0/SPIKE-RLS`

## Background

As a platform engineer, I want Postgres RLS policies keyed on tenant_id, with EF Core setting the session tenant context on every request, so that a query can never return another tenant's rows, even on a developer mistake.
Tenant isolation is enforced in the database via RLS, with the API setting tenant context per request (ADR-0003). This is the single most important safety property of the data layer.

## How it works

Every tenant-scoped table gets an RLS policy of the shape USING (tenant_id = current_setting('app.tenant_id')::uuid) for reads and a matching WITH CHECK for writes, with policies created in migrations alongside the tables. RLS is forced (not just enabled) so even the table owner is subject to it, closing the 'superuser bypass' hole.
The API sets the session tenant on every request: middleware resolves the authenticated principal's tenant claim, and an EF Core connection interceptor issues SET app.tenant_id (per the pattern SPIKE-RLS proved safe under connection pooling and async) before any query runs, then clears it on return so a pooled connection never leaks context. The application-layer tenant check stays as belt-and-braces.
Background jobs and migrations that legitimately need cross-tenant access use one explicit, audited elevated path — a dedicated bypass role/setting that is never reachable from request handling, and every use of it emits an AuditEvent (AUDIT-INFRA). The invariant is proven by an integration test: signed in as Tenant A, a query for Tenant B's rows returns nothing and a cross-tenant id resolves to not-found, never another tenant's record.

## Requirements

- Postgres RLS policies keyed on tenant_id, with EF Core setting the session tenant context on every request.

## Acceptance Criteria

- [ ] RLS policies are applied to all tenant-scoped tables.
- [ ] API middleware sets the session tenant from the authenticated principal on every request.
- [ ] An integration test proves Tenant A cannot read Tenant B rows and a cross-tenant id returns not-found.
- [ ] Bypassing tenant context (e.g. background jobs) uses an explicit, audited elevated path.

## Suggested data model

- **RLS policy** — USING (tenant_id = current_setting('app.tenant_id')::uuid); matching WITH CHECK; FORCE ROW LEVEL SECURITY
  - _Applied per tenant-scoped table in migrations; session tenant set per request; one audited elevated bypass for jobs._

## Technical notes (high level)

- Architecture decisions: [ADR-0003](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Author the RLS policies and the per-request session-tenant wiring**
  Implement the database isolation and the request-side context that drives it, using the SPIKE-RLS-proven pattern.
  - Per tenant-scoped table: enable + FORCE row level security and a USING/WITH CHECK policy keyed on current_setting('app.tenant_id'); created in migrations next to the table.
  - Middleware resolves the tenant from the authenticated principal; an EF Core connection interceptor SETs app.tenant_id before queries and clears it on connection return so pooled connections never leak context.
  - Keep the application-layer tenant check as defense-in-depth (ADR-0003).
- [ ] **Implement the audited elevated/bypass path for jobs & migrations**
  Provide exactly one sanctioned way to operate cross-tenant, and make every use of it visible.
  - A dedicated bypass role/setting usable only by background workers and migrations, never reachable from request handlers.
  - Each elevation emits an AuditEvent (who/why/scope) via AUDIT-INFRA, so an auditor can see every cross-tenant operation.
  - Document when elevation is allowed (JOBS-SCHEDULER consumes this) and the guard that prevents accidental use in request code.
- [ ] **Prove and document the isolation invariant**
  Codify the cross-tenant test as a compliance invariant and document the model.
  - An integration test against real Postgres: as Tenant A, reads of Tenant B data return empty and a cross-tenant id is not-found (never leaks a row); writes can't set a foreign tenant_id.
  - Flag this test under the TEST 'compliance invariant' convention so the gate must block on regression.
  - Document the policy shape, the session-context lifecycle and the bypass rule for future module authors.
