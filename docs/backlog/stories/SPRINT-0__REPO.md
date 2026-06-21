# Monorepo & solution scaffolding

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/REPO`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra

## Background

As a developer, I want a scaffolded repo with the API, web, app and shared-package folders, a clean .NET solution, an Angular workspace and a Flutter workspace wired together, so that everyone builds against one consistent structure and shared code has an obvious home.
A single, well-structured repo (or workspace) for the .NET API, Angular web, two Flutter apps and shared packages keeps versioning, CI and code-sharing sane from day one.

## How it works

A single, well-structured workspace for the .NET API, Angular web, two Flutter apps and shared packages (design system + API client), with consistent formatter/linter/editorconfig from day one. Keeps versioning, CI and code-sharing sane and gives shared code an obvious home (ADR-0005/0006).

## Requirements

- A scaffolded repo with the API, web, app and shared-package folders, a clean .NET solution, an Angular workspace and a Flutter workspace wired together.

## Acceptance Criteria

- [ ] Repo layout documented in a top-level README (api/, web/, apps/, packages/, infra/, scripts/).
- [ ] .NET solution builds; Angular workspace serves; both Flutter app shells run on a simulator.
- [ ] Shared design-system and API-client packages exist as empty-but-buildable libraries.
- [ ] Editorconfig, formatter and linter configs committed and enforced locally.

## Technical notes (high level)

- Stack: Azure / CI-CD / IaC
- Architecture decisions: [ADR-0005](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0006](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Monorepo & solution scaffolding**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
