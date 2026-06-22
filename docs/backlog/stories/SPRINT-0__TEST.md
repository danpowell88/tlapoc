# Test strategy & harness + quality gates

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/TEST`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/CICD`, `SPRINT-0/RLS`

## Background

As a developer, I want test harnesses for API (unit + integration), web and apps, plus an e2e smoke suite and coverage gates in CI, so that compliance invariants are protected by tests and regressions are caught automatically.
A clinical platform needs a serious automated-test culture: unit, integration (incl. RLS/auth/audit invariants) and end-to-end, with coverage gates.

## How it works

Test harnesses for API (unit + integration against a real Postgres with RLS), web and apps, plus an e2e smoke (sign-in + sample flow) and coverage gates in CI — with a documented convention for 'compliance invariant' tests (a gate MUST block). Protects the moat's invariants and catches regressions automatically.

## Requirements

- Test harnesses for API (unit + integration), web and apps, plus an e2e smoke suite and coverage gates in CI.

## Acceptance Criteria

- [ ] Unit + integration test projects exist for the API (integration tests run against a real Postgres with RLS).
- [ ] Web and app unit/widget test setups in place; an e2e smoke test covers sign-in + the sample flow.
- [ ] Coverage threshold enforced in CI.
- [ ] A documented convention for writing 'compliance invariant' tests (gate must block) exists.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Test strategy & harness + quality gates**
  Deliver per the acceptance criteria:
  - Unit + integration test projects exist for the API (integration tests run against a real Postgres with RLS).
  - Web and app unit/widget test setups in place; an e2e smoke test covers sign-in + the sample flow.
  - Coverage threshold enforced in CI.
  - A documented convention for writing 'compliance invariant' tests (gate must block) exists.
- [ ] **Document setup & usage**
  How to run/operate it; runbook notes for the team.
