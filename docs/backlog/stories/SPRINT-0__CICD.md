# CI/CD pipelines (build, test, deploy)

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/CICD`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/REPO`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a developer, I want pipelines that build and test the API, web and apps on every PR and deploy to dev/staging on merge, so that broken code is caught early and releases are repeatable.

Continuous build/test on every PR and automated deploys to environments prevent integration drift and make the compliance posture (tests, scans) enforceable.

## Requirements

- Pipelines that build and test the API, web and apps on every PR and deploy to dev/staging on merge.

## Acceptance Criteria

- [ ] PR pipeline runs build + unit/integration tests for API, web and apps and blocks merge on failure.
- [ ] Merge to main deploys API + web to the dev environment automatically.
- [ ] Mobile app builds produce installable artifacts for internal distribution.
- [ ] Pipeline status is required for merge (branch protection ties in via S0-GOV).

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Azure / CI-CD / IaC.
Depends on: SPRINT-0/REPO.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/CICD.
Phase: 0 · Priority: P0 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: CI/CD pipelines (build, test, deploy)**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
