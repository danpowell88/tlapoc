# CI/CD pipelines (build, test, deploy)

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/CICD`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/REPO`

## Background

As a developer, I want pipelines that build and test the API, web and apps on every PR and deploy to dev/staging on merge, so that broken code is caught early and releases are repeatable.
Continuous build/test on every PR and automated deploys to environments prevent integration drift and make the compliance posture (tests, scans) enforceable.

## How it works

GitHub Actions (the repo already deploys the POC via Actions) runs two pipeline shapes. The PR pipeline builds and tests all surfaces in parallel jobs — .NET (restore/build/unit + integration), Angular (build + unit), and both Flutter flavours (build + widget tests) — and is a required status check that blocks merge on any failure. The merge-to-main pipeline builds release artifacts and deploys API + web to the dev environment automatically.
Stages flow lint -> build -> unit -> integration -> package -> deploy(dev) -> (manual gate) -> deploy(staging/prod). Integration tests run against an ephemeral Postgres service container so RLS/auth invariants are exercised in CI, not just locally. SEC-BASE inserts dependency, secret and SAST scan stages; TEST inserts the coverage threshold; both gate the pipeline.
Mobile builds produce installable artifacts for internal distribution (the wiring of distribution channels is APP-DISTRIBUTION later; here we just produce signed-able artifacts). Deploys read configuration and secrets per environment from Key Vault (SECRETS) and target Australia-East infrastructure provisioned by IAC. Environments dev/staging/prod map to GitHub Environments so GOV can attach approval gates.

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

- [ ] **Build the PR pipeline: parallel build + test for all surfaces, blocking merge**
  Author the PR workflow that fans out per surface and is the required gate before merge.
  - Parallel jobs: .NET (restore, build, unit + integration tests against a Postgres service container), Angular (build + unit), Flutter client and provider (build + widget tests).
  - Lint/format-check runs first and fails fast (reusing REPO's commands).
  - Caching for package restores to keep PR feedback fast; matrix where it helps.
  - Pipeline result published as a status check GOV will mark required; any job failure blocks merge.
  - Leaves clearly-marked insertion points where SEC-BASE adds scan stages and TEST adds the coverage gate.
- [ ] **Build the deploy pipeline to dev/staging/prod with per-environment config**
  Author the merge/deploy workflow targeting the AU-East environments from IAC, reading config/secrets per environment from Key Vault (SECRETS).
  - Merge to main: build release artifacts, then auto-deploy API + web to dev.
  - staging/prod are separate jobs/targets gated by a manual approval (GitHub Environments) so GOV can require an approver for prod.
  - Mobile flavours build installable artifacts for internal distribution (signing/store wiring deferred to APP-DISTRIBUTION).
  - Migrations apply on deploy (DB owns the migration runner); deploy is idempotent and re-runnable.
  - Each environment selects its own connection strings/identities so a deploy can never cross environments.
- [ ] **Document the pipeline: stages, gates, environments & how to add a check**
  Write the pipeline reference so the team understands what runs, when it blocks, and how to extend it.
  - The stage diagram (lint -> build -> unit -> integration -> package -> deploy(dev) -> gate -> staging/prod) and which stages are blocking.
  - How required checks tie to branch protection (cross-reference GOV) and where approval gates live.
  - The convention for adding a new blocking check (so SEC-BASE/TEST additions are consistent) and how to read a failed run.
