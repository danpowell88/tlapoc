# Background jobs & scheduler infrastructure

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/JOBS-SCHEDULER`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** backend, infra
>
> **Depends on:** `SPRINT-0/API`, `SPRINT-0/RLS`

## Background

As a platform engineer, I want a background-job framework with scheduling, retries, idempotency and dead-lettering, so that time-driven and async work runs reliably and observably.
Many features are time-driven, not user-driven: reminders/recall sends, membership autopay + dunning retries, retention timers, temperature polling, expiry alerts, read-model projections. A reliable background worker + scheduler is needed before those features land.

## How it works

A worker host runs both scheduled jobs (cron-like recurring work) and queued jobs (work enqueued by request handlers or domain events). Each job execution has retry with back-off, idempotency (a job that runs twice produces one effect) and dead-lettering (a job that keeps failing is parked for inspection rather than retried forever), so time-driven work runs reliably without manual babysitting.
Jobs are tenant-aware: a job carries its tenant_id and runs under the audited elevated context from RLS (the only sanctioned cross-tenant path), so a recall scan or projection touches the right tenant's data and every elevation is recorded in the audit stream. Job runs are observable through the OBS stack — metrics, logs and alerts on failures and dead-letters.
A sample recurring job (e.g. an expiry scan) and a sample queued job are demonstrated end to end to prove scheduling, retry, idempotency, tenancy and observability before features rely on the framework. The JobRun record tracks type, payload, schedule, attempts and status.

## Requirements

- A background-job framework with scheduling, retries, idempotency and dead-lettering.

## Acceptance Criteria

- [ ] A worker host runs scheduled + queued jobs with retry, back-off and dead-letter handling.
- [ ] Jobs are tenant-aware and run under an audited elevated context (per RLS bypass path).
- [ ] Job runs are observable (metrics/logs/alerts) via the Sprint 0 observability stack.
- [ ] A sample recurring job (e.g. expiry scan) and a sample queued job are demonstrated.

## Suggested data model

- **JobRun** — id, tenant_id, type, payload(jsonb), scheduled_for, attempts, status(queued|running|done|dead), last_error
  - _Retry with back-off; idempotent; dead-letter on repeated failure; runs under the RLS audited elevated context._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Build the worker host with scheduling, retry/back-off, idempotency and dead-lettering**
  Stand up the reliable engine for time-driven and async work.
  - A worker host running scheduled (recurring) and queued jobs.
  - Per-execution retry with back-off, idempotency (run-twice = one effect), and dead-lettering for repeatedly-failing jobs.
  - JobRun record (type, payload, schedule, attempts, status) tracking lifecycle.
- [ ] **Make jobs tenant-aware under the audited elevated context**
  Ensure jobs touch the right tenant and every cross-tenant run is recorded.
  - Jobs carry tenant_id and run under the RLS audited elevated/bypass path (the only sanctioned cross-tenant route) so isolation holds and elevations are audited (AUDIT-INFRA).
  - A sample recurring job (e.g. expiry scan) and a sample queued job demonstrated end to end (schedule, retry, idempotency, tenancy).
- [ ] **Wire job observability and document the framework**
  Make runs visible and document how features add jobs.
  - Metrics/logs/alerts for job runs, failures and dead-letters via OBS.
  - Document how to define a scheduled vs queued job, the idempotency contract, and the tenant/elevation rules — so REMINDERS, MEMBERSHIP autopay, RETENTION, TEMP-MONITORS, recall/expiry scans and DOMAIN-EVENTS projections build on it consistently.
