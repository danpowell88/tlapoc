# Observability: logging, tracing, metrics, alerting

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/OBS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/API`

## Background

As a platform engineer, I want structured logging, distributed tracing, key metrics dashboards and alerting wired across API and apps, so that we can diagnose issues and detect incidents (feeding the breach workflow) quickly.
You cannot run a compliance-critical platform blind. Centralised logs, distributed traces, metrics and alerting are needed from the first deploy.

## How it works

Structured logs and distributed traces flow to a central store (Azure Monitor / Application Insights) with a correlation id propagated across web/app/API, so one user action can be followed end to end. The API's request logging (API) and the front-ends emit the same correlation id, and traces span service boundaries.
Dashboards cover the golden signals — request rate, latency, error rate — plus key resource health (database, queue/jobs, storage). Alerts fire on error-rate and availability thresholds so on-call is paged before users notice, with sensible thresholds and routing.
Audit/security-relevant signals are kept distinguishable from ordinary operational logs — tagged so they can seed the data-breach detection/assessment workflow in PRD-01 (REQ-SEC-7, C22) rather than being lost in noise. This is the hook BREACH builds on; OBS just makes the signal separable and observable.

## Requirements

- Structured logging, distributed tracing, key metrics dashboards and alerting wired across API and apps.

## Acceptance Criteria

- [ ] Structured logs and traces flow to a central store with correlation ids across web/app/API.
- [ ] Dashboards cover request rate, latency, errors and key resource health.
- [ ] Alerts fire for error-rate and availability thresholds.
- [ ] Audit/security-relevant signals are distinguishable to feed the breach workflow (PRD-01).

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Wire structured logging, distributed tracing and correlation ids across API and apps**
  Make every request followable end to end through a central store.
  - Logs + traces to a central store (the IAC observability workspace) with a correlation id propagated web/app/API.
  - API request logging emits the correlation id; front-ends propagate it; traces span service boundaries.
  - Security/audit-relevant signals tagged distinctly so they can seed the PRD-01 breach workflow (don't drown them in operational noise).
- [ ] **Build dashboards and alerting for golden signals and resource health**
  Give the team eyes and a pager from the first deploy.
  - Dashboards: request rate, latency, error rate, plus resource health (database, jobs/queue, storage).
  - Alerts on error-rate and availability thresholds with routing to on-call; thresholds documented and tunable.
  - Wire alert definitions per environment (ties to IAC/CICD).
- [ ] **Document the observability stack and the breach-signal contract**
  Write the ops guide and the hand-off to the breach workflow.
  - What's logged/traced, how correlation ids flow, and how to read the dashboards.
  - The alerting catalogue and escalation.
  - How security/audit signals are tagged and consumed by BREACH (PRD-01) so that story can build on a defined stream.
