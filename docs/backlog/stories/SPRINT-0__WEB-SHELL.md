# Angular web shell: routing, auth guard, layout

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/WEB-SHELL`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/DESIGN`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a front-end developer, I want an Angular shell with the Entra auth guard, top-level routing, a role-aware navigation frame and the design-system theme applied, so that feature screens drop into a consistent, authenticated layout.

The admin/front-desk web app needs a shell — auth guard, role-aware nav, layout — before feature screens land.

## Requirements

- An Angular shell with the Entra auth guard, top-level routing, a role-aware navigation frame and the design-system theme applied.

## Acceptance Criteria

- [ ] Unauthenticated users are redirected to Entra sign-in; authenticated users land on a shell.
- [ ] Navigation is driven by capabilities/role (placeholder until PRD-01 RBAC lands).
- [ ] Design-system theme + tokens applied globally.
- [ ] A sample feature route renders inside the shell using the generated API client.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0005 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/AUTH-STAFF, SPRINT-0/DESIGN.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/WEB-SHELL.
Phase: 0 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Angular web shell: routing, auth guard, layout**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
