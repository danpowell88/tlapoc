# CI/CD pipelines (build, test, deploy)

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/CICD`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/REPO`

## Background

As a developer, I want pipelines that build and test the API, web and apps on every PR and deploy to dev/staging on merge, so that broken code is caught early and releases are repeatable.
Continuous build/test on every PR and automated deploys to environments prevent integration drift and make the compliance posture (tests, scans) enforceable.

## How it works

Pipelines build + test the API/web/apps on every PR (blocking merge on failure) and auto-deploy to dev on merge; mobile builds produce installable artifacts. This makes the compliance posture (tests, scans) enforceable rather than aspirational and is the backbone for repeatable releases.

## Requirements

- Pipelines that build and test the API, web and apps on every PR and deploy to dev/staging on merge.

## Acceptance Criteria

- [ ] PR pipeline runs build + unit/integration tests for API, web and apps and blocks merge on failure.
- [ ] Merge to main deploys API + web to the dev environment automatically.
- [ ] Mobile app builds produce installable artifacts for internal distribution.
- [ ] Pipeline status is required for merge (branch protection ties in via S0-GOV).

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: CI/CD pipelines (build, test, deploy)**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
