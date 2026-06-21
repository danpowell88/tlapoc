# Background jobs & scheduler infrastructure

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/JOBS-SCHEDULER`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend, infra
>
> **Depends on:** `SPRINT-0/API`, `SPRINT-0/RLS`

## Background

As a platform engineer, I want a background-job framework with scheduling, retries, idempotency and dead-lettering, so that time-driven and async work runs reliably and observably.
Many features are time-driven, not user-driven: reminders/recall sends, membership autopay + dunning retries, retention timers, temperature polling, expiry alerts, read-model projections. A reliable background worker + scheduler is needed before those features land.

## How it works

A background-job framework (scheduler + queue) with retry, back-off, idempotency and dead-lettering — the engine behind every time-driven feature: reminder/recall sends, membership autopay + dunning, retention timers, temperature polling, expiry alerts and read-model projections. Jobs are tenant-aware and run under an audited elevated context (the RLS bypass path), and runs are observable.

## Requirements

- A background-job framework with scheduling, retries, idempotency and dead-lettering.

## Acceptance Criteria

- [ ] A worker host runs scheduled + queued jobs with retry, back-off and dead-letter handling.
- [ ] Jobs are tenant-aware and run under an audited elevated context (per RLS bypass path).
- [ ] Job runs are observable (metrics/logs/alerts) via the Sprint 0 observability stack.
- [ ] A sample recurring job (e.g. expiry scan) and a sample queued job are demonstrated.

## Suggested data model

- **JobRun** — id, type, payload, scheduled_for, attempts, status(queued|running|done|dead), tenant_id
  - _Retry/back-off; dead-letter; audited elevated context._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Background jobs & scheduler infrastructure**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
