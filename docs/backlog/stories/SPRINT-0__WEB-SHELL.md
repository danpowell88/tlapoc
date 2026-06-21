# Angular web shell: routing, auth guard, layout

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/WEB-SHELL`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/DESIGN`

## Background

As a front-end developer, I want an Angular shell with the Entra auth guard, top-level routing, a role-aware navigation frame and the design-system theme applied, so that feature screens drop into a consistent, authenticated layout.
The admin/front-desk web app needs a shell — auth guard, role-aware nav, layout — before feature screens land.

## How it works

Angular shell with the Entra auth guard, top-level routing, a role-aware navigation frame and the design-system theme applied, so feature screens drop into a consistent authenticated layout. Foundation for PLATFORM/APP-NAV (ADR-0005).

## Requirements

- An Angular shell with the Entra auth guard, top-level routing, a role-aware navigation frame and the design-system theme applied.

## Acceptance Criteria

- [ ] Unauthenticated users are redirected to Entra sign-in; authenticated users land on a shell.
- [ ] Navigation is driven by capabilities/role (placeholder until PRD-01 RBAC lands).
- [ ] Design-system theme + tokens applied globally.
- [ ] A sample feature route renders inside the shell using the generated API client.

## UI designs / screenshots

_Prototype screen: Non-UI / platform scaffolding — no prototype screen._

- The authenticated app frame (later filled by PLATFORM/APP-NAV; see dashboard.png) — sign-in redirect, shell layout, themed.

## Technical notes (high level)

- Architecture decisions: [ADR-0005](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Angular web shell: routing, auth guard, layout**
- [ ] **Document setup & usage**
