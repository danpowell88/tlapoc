# Monorepo & solution scaffolding

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/REPO`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a developer, I want a scaffolded repo with the API, web, app and shared-package folders, a clean .NET solution, an Angular workspace and a Flutter workspace wired together, so that everyone builds against one consistent structure and shared code has an obvious home.

A single, well-structured repo (or workspace) for the .NET API, Angular web, two Flutter apps and shared packages keeps versioning, CI and code-sharing sane from day one.

## Requirements

- A scaffolded repo with the API, web, app and shared-package folders, a clean .NET solution, an Angular workspace and a Flutter workspace wired together.

## Acceptance Criteria

- [ ] Repo layout documented in a top-level README (api/, web/, apps/, packages/, infra/, scripts/).
- [ ] .NET solution builds; Angular workspace serves; both Flutter app shells run on a simulator.
- [ ] Shared design-system and API-client packages exist as empty-but-buildable libraries.
- [ ] Editorconfig, formatter and linter configs committed and enforced locally.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Azure / CI-CD / IaC.
Architecture decisions: ADR-0005, ADR-0006 (see docs/adr/decision-log.md).

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/REPO.
Phase: 0 · Priority: P0 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Monorepo & solution scaffolding**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
