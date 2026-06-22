# .NET API skeleton: architecture, tenant context, error model

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/API`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/RLS`, `SPRINT-0/AUTH-STAFF`

## Background

As a backend developer, I want an API skeleton with auth middleware, tenant-context resolution, a standard error/response model and health checks, so that feature modules are added consistently and cross-cutting concerns are solved once.
Sprint 0 (setup), the API foundation: this builds the shared skeleton of the back-end service — how every request is authenticated, scoped to the right clinic, error-handled, paged and logged — so each later feature just adds its own logic and inherits all of that for free. It sits on top of tenant isolation (RLS) and staff sign-in, and is the base that the generated API contract, observability, background jobs, media storage and feature flags all build on.  A consistent API skeleton (clean/layered architecture, request pipeline, problem-details errors, pagination) means every feature module plugs in the same way.

## How it works

The API host is a modular monolith: a thin host wires up the bounded-module libraries from REPO, each module owning its endpoints and domain. A single request pipeline handles auth, tenant-context resolution, correlation/logging and error mapping, so a feature module only writes its handler and gets the cross-cutting behaviour for free.
Auth middleware validates both staff (Entra ID) and client (External ID) tokens, resolves the tenant claim into the per-request tenant context RLS consumes, and exposes the actor identity for audit. Errors are returned as RFC 7807 problem-details with a consistent shape and codes; list endpoints share one pagination/filtering/sorting convention so clients (web, Flutter) handle them uniformly. Health and readiness endpoints support deploy/orchestration, and structured request logging carries the correlation id OBS stitches traces with.
A vertical-slice sample endpoint demonstrates the full pattern end to end — authenticated, tenant-scoped (RLS-enforced), problem-details errors, paginated, logged — and is the thing OPENAPI generates a client for and WEB-SHELL/FLUTTER call to prove the stack.

## Requirements

- An API skeleton with auth middleware, tenant-context resolution, a standard error/response model and health checks.

## Acceptance Criteria

- [ ] Auth middleware validates Entra tokens (staff + client) and resolves tenant context for RLS.
- [ ] Standard problem-details error responses and consistent pagination/filtering conventions.
- [ ] Health/readiness endpoints and structured request logging in place.
- [ ] A vertical-slice sample endpoint demonstrates the full pattern end-to-end.

## Technical notes (high level)

- Architecture decisions: [ADR-0005](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Build the request pipeline: auth, tenant context, problem-details, pagination, health & logging**
  Implement the modular-monolith host and the cross-cutting pipeline every module reuses.
  - Host wires the bounded-module libraries from REPO; each module contributes endpoints/domain.
  - Auth middleware validates staff (Entra ID) + client (External ID) tokens, resolves the tenant claim into per-request tenant context for RLS (row-level security), and surfaces the actor for audit.
  - RFC 7807 problem-details error model with consistent codes; one shared pagination/filtering/sorting convention for list endpoints.
  - Health + readiness endpoints; structured request logging emitting the correlation id OBS will use.
- [ ] **Ship the vertical-slice sample endpoint and document the module pattern**
  Prove the whole pattern end-to-end and document it so feature modules are added identically.
  - A sample endpoint exercising auth + tenant scoping (RLS-enforced) + problem-details + pagination + logging end to end.
  - This endpoint is what OPENAPI generates a typed client for and what WEB-SHELL/FLUTTER call to validate the stack.
  - Document how to add a module/endpoint: where it lives, how it gets tenant context, error/pagination conventions, and the health/logging it inherits.
