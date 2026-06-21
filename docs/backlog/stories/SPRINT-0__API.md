# .NET API skeleton: architecture, tenant context, error model

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/API`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/RLS`, `SPRINT-0/AUTH-STAFF`

## Background

As a backend developer, I want an API skeleton with auth middleware, tenant-context resolution, a standard error/response model and health checks, so that feature modules are added consistently and cross-cutting concerns are solved once.
A consistent API skeleton (clean/layered architecture, request pipeline, problem-details errors, pagination) means every feature module plugs in the same way.

## Requirements

- An API skeleton with auth middleware, tenant-context resolution, a standard error/response model and health checks.

## Acceptance Criteria

- [ ] Auth middleware validates Entra tokens (staff + client) and resolves tenant context for RLS.
- [ ] Standard problem-details error responses and consistent pagination/filtering conventions.
- [ ] Health/readiness endpoints and structured request logging in place.
- [ ] A vertical-slice sample endpoint demonstrates the full pattern end-to-end.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0005](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: .NET API skeleton: architecture, tenant context, error model**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
