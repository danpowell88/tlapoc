# Test strategy & harness + quality gates

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/TEST`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `SPRINT-0/CICD`, `SPRINT-0/RLS`

## Background

As a developer, I want test harnesses for API (unit + integration), web and apps, plus an e2e smoke suite and coverage gates in CI, so that compliance invariants are protected by tests and regressions are caught automatically.
Sprint 0 (setup), quality foundation: this sets up the automated test harnesses for every surface and the coverage gate in the build, so the compliance rules the product depends on are protected by tests that run on every change — not by hope. It builds on the pipeline (where the gates run) and tenant isolation (the headline rule it protects), and defines the must-block convention that later compliance stories tag their critical tests with. A clinical platform needs a serious automated-test culture: unit, integration (incl. RLS (row-level security)/auth/audit invariants) and end-to-end, with coverage gates.

## How it works

Test harnesses exist per surface: API unit tests plus integration tests that run against a real Postgres with RLS (row-level security) (so tenant isolation, auth and audit behaviour are exercised as they'll run in production, using the ephemeral Postgres from CICD); web and Flutter unit/widget test setups; and an end-to-end smoke suite covering sign-in plus the sample flow across the stack.
A coverage threshold is enforced in CI (continuous integration) so coverage can't silently rot. More importantly, a documented convention exists for writing 'compliance invariant' tests — the ones that encode a regulatory rule (RLS isolation, audit append-only, consent gates) and whose failure MUST block merge — so these aren't treated as ordinary tests that can be skipped under deadline.
The harness deliberately runs integration tests against real Postgres rather than an in-memory fake, because the invariants that matter (RLS, constraints, triggers) only exist in the real engine. This is what makes the tests trustworthy as the moat's guardrails.

## Requirements

- Test harnesses for API (unit + integration), web and apps, plus an e2e smoke suite and coverage gates in CI.

## Acceptance Criteria

- [ ] Unit + integration test projects exist for the API (integration tests run against a real Postgres with RLS).
- [ ] Web and app unit/widget test setups in place; an e2e (end-to-end) smoke test covers sign-in + the sample flow.
- [ ] Coverage threshold enforced in CI.
- [ ] A documented convention for writing 'compliance invariant' tests (gate must block) exists.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Stand up the test harnesses (API unit + real-Postgres integration, web/Flutter, e2e smoke) and the coverage gate**
  Build the multi-surface test foundation and wire the gates into CI (continuous integration).
  - API unit test project + integration tests against a real Postgres with RLS (row-level security) (reuse the CICD Postgres service container), exercising tenancy/auth/audit as in production.
  - Web and Flutter unit/widget test setups; an e2e (end-to-end) smoke covering sign-in + the sample flow end to end.
  - Coverage threshold enforced in CI so coverage can't rot.
- [ ] **Define and document the 'compliance invariant' test convention**
  Make regulatory tests a distinct, must-block category.
  - A documented convention (naming/tagging) for tests that encode a compliance rule — RLS (row-level security) isolation, audit append-only, consent/cooling-off gates — whose failure MUST block merge and can't be skipped under deadline.
  - Wire it so RLS, AUDIT-INFRA and later compliance stories tag their invariant tests consistently, and CI (continuous integration) treats the tag as non-negotiable.
