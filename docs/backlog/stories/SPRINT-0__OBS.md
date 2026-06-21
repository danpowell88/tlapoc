# Observability: logging, tracing, metrics, alerting

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/OBS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/API`

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a platform engineer, I want structured logging, distributed tracing, key metrics dashboards and alerting wired across API and apps, so that we can diagnose issues and detect incidents (feeding the breach workflow) quickly.

You cannot run a compliance-critical platform blind. Centralised logs, distributed traces, metrics and alerting are needed from the first deploy.

## Requirements

- Structured logging, distributed tracing, key metrics dashboards and alerting wired across API and apps.

## Acceptance Criteria

- [ ] Structured logs and traces flow to a central store with correlation ids across web/app/API.
- [ ] Dashboards cover request rate, latency, errors and key resource health.
- [ ] Alerts fire for error-rate and availability thresholds.
- [ ] Audit/security-relevant signals are distinguishable to feed the breach workflow (PRD-01).

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Azure / CI-CD / IaC.
Depends on: SPRINT-0/API.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/OBS.
Phase: 0 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Implement: Observability: logging, tracing, metrics, alerting**
- [ ] **Wire into CI/CD + per-environment config**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
