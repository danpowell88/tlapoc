# Feature flags & per-tenant configuration

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/FEATURE-FLAGS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P2  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/API`

## Background

As a platform engineer, I want feature flags and a typed per-tenant configuration store, so that we can ship features progressively and tailor behaviour per clinic.
The build is staged and many capabilities are configurable per tenant (cooling-off policy, S4 naming, telehealth path risk, modality availability, deferred features). A flag + config mechanism lets features ship dark and toggle per tenant.

## Requirements

- Feature flags and a typed per-tenant configuration store.

## Acceptance Criteria

- [ ] Feature flags can be toggled globally and per tenant.
- [ ] Per-tenant configuration (e.g. cooling-off N days, S4 naming, modality availability) is typed and validated.
- [ ] Flag/config reads are cached and observable.
- [ ] Changing a flag/config is audited.

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Feature flags & per-tenant configuration**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
