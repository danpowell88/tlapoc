# Observability: logging, tracing, metrics, alerting

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/OBS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/API`

## Background

As a platform engineer, I want structured logging, distributed tracing, key metrics dashboards and alerting wired across API and apps, so that we can diagnose issues and detect incidents (feeding the breach workflow) quickly.
You cannot run a compliance-critical platform blind. Centralised logs, distributed traces, metrics and alerting are needed from the first deploy.

## How it works

Structured logging, distributed tracing (correlation ids across web/app/API), key metrics dashboards and alerting from the first deploy, with audit/security-relevant signals distinguishable so they can seed the breach workflow (PRD-01). You can't run a compliance-critical platform blind.

## Requirements

- Structured logging, distributed tracing, key metrics dashboards and alerting wired across API and apps.

## Acceptance Criteria

- [ ] Structured logs and traces flow to a central store with correlation ids across web/app/API.
- [ ] Dashboards cover request rate, latency, errors and key resource health.
- [ ] Alerts fire for error-rate and availability thresholds.
- [ ] Audit/security-relevant signals are distinguishable to feed the breach workflow (PRD-01).

## Technical notes (high level)

- Stack: Azure / CI-CD / IaC

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Observability: logging, tracing, metrics, alerting**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
