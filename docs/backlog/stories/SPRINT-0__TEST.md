# Test strategy & harness + quality gates

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/TEST`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/CICD`, `SPRINT-0/RLS`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a developer, I want test harnesses for API (unit + integration), web and apps, plus an e2e smoke suite and coverage gates in CI, so that compliance invariants are protected by tests and regressions are caught automatically.

A clinical platform needs a serious automated-test culture: unit, integration (incl. RLS/auth/audit invariants) and end-to-end, with coverage gates.

## Requirements

- Test harnesses for API (unit + integration), web and apps, plus an e2e smoke suite and coverage gates in CI.

## Acceptance Criteria

- [ ] Unit + integration test projects exist for the API (integration tests run against a real Postgres with RLS).
- [ ] Web and app unit/widget test setups in place; an e2e smoke test covers sign-in + the sample flow.
- [ ] Coverage threshold enforced in CI.
- [ ] A documented convention for writing 'compliance invariant' tests (gate must block) exists.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: SPRINT-0/CICD, SPRINT-0/RLS.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/TEST.
Phase: 0 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Test strategy & harness + quality gates**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
