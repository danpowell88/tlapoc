# Background jobs & scheduler infrastructure

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/JOBS-SCHEDULER`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend, infra
>
> **Depends on:** `SPRINT-0/API`, `SPRINT-0/RLS`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a platform engineer, I want a background-job framework with scheduling, retries, idempotency and dead-lettering, so that time-driven and async work runs reliably and observably.

Many features are time-driven, not user-driven: reminders/recall sends, membership autopay + dunning retries, retention timers, temperature polling, expiry alerts, read-model projections. A reliable background worker + scheduler is needed before those features land.

## Requirements

- A background-job framework with scheduling, retries, idempotency and dead-lettering.

## Acceptance Criteria

- [ ] A worker host runs scheduled + queued jobs with retry, back-off and dead-letter handling.
- [ ] Jobs are tenant-aware and run under an audited elevated context (per RLS bypass path).
- [ ] Job runs are observable (metrics/logs/alerts) via the Sprint 0 observability stack.
- [ ] A sample recurring job (e.g. expiry scan) and a sample queued job are demonstrated.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: .NET API (domain/services); Azure / CI-CD / IaC.
Depends on: SPRINT-0/API, SPRINT-0/RLS.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/JOBS-SCHEDULER.
Phase: 0 · Priority: P0 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Background jobs & scheduler infrastructure**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
