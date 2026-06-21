# Repo governance: branch protection, PR & env protection

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/GOV`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P2  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/CICD`

## Background

As a maintainer, I want protected main with required status checks and reviews, PR/issue templates, and protected prod deployments, so that quality gates can't be bypassed and changes are traceable.
Branch protection, required checks, PR templates and environment protection rules keep the main branch deployable and reviewable.

## Requirements

- Protected main with required status checks and reviews, PR/issue templates, and protected prod deployments.

## Acceptance Criteria

- [ ] main requires passing checks + at least one review before merge.
- [ ] PR and issue templates committed (PR template references the backlog item).
- [ ] Production deploys require an approval gate.
- [ ] CODEOWNERS routes reviews for sensitive areas (auth, medicines, compliance).

## Technical notes (high level)

- Stack: Azure / CI-CD / IaC

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Repo governance: branch protection, PR & env protection**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
