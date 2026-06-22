# Repo governance: branch protection, PR & env protection

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/GOV`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P2  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/CICD`

## Background

As a maintainer, I want protected main with required status checks and reviews, PR/issue templates, and protected prod deployments, so that quality gates can't be bypassed and changes are traceable.
Branch protection, required checks, PR templates and environment protection rules keep the main branch deployable and reviewable.

## How it works

main is protected: merging requires the CICD pipeline status to pass and at least one approving review, so broken or unreviewed code can't reach the deployable branch. The PR and issue templates are committed, and the PR template references the backlog item (the SCRUM key), keeping changes traceable back to the story they implement.
Production deploys sit behind an approval gate (GitHub Environments) so a human approves before prod, while dev stays automatic for fast feedback. CODEOWNERS routes reviews for sensitive areas — auth, medicines, compliance code — to the right reviewers, so changes touching the moat get the right eyes by construction.
Together these make the gates from SEC-BASE (scans) and TEST (coverage + compliance invariants) actually required rather than advisory: the branch protection lists them as mandatory checks. The rules are documented so contributors know what's enforced and why.

## Requirements

- Protected main with required status checks and reviews, PR/issue templates, and protected prod deployments.

## Acceptance Criteria

- [ ] main requires passing checks + at least one review before merge.
- [ ] PR and issue templates committed (PR template references the backlog item).
- [ ] Production deploys require an approval gate.
- [ ] CODEOWNERS routes reviews for sensitive areas (auth, medicines, compliance).

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Protect main with required checks + review and commit PR/issue templates**
  Make merging to main impossible without passing gates and a review.
  - Branch protection on main: require the CICD pipeline status + the SEC-BASE/TEST gates + at least one approving review.
  - PR and issue templates committed; the PR template references the backlog item (SCRUM key) for traceability.
  - No direct pushes / force-pushes to main.
- [ ] **Add production approval gates and CODEOWNERS for sensitive areas**
  Gate prod and route sensitive reviews automatically.
  - Production deploys require an approval gate (GitHub Environments), dev stays automatic (ties to CICD).
  - CODEOWNERS routes reviews for auth, medicines and compliance code to the right reviewers so moat changes get the right eyes.
  - Verify the required checks listed in protection match the gates SEC-BASE/TEST produce.
- [ ] **Document the governance rules**
  Write the contributor-facing governance guide.
  - What's required to merge, which checks are mandatory and why, and how the PR template ties to backlog items.
  - The prod approval flow and the CODEOWNERS map for sensitive areas.
