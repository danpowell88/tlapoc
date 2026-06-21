# Domain-event / messaging backbone

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/DOMAIN-EVENTS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend, data
>
> **Depends on:** `SPRINT-0/AUDIT-INFRA`

## Background

As a backend developer, I want a domain-event mechanism (transactional outbox + dispatch) modules can publish to and subscribe from, so that read-models, jobs and notifications react to changes without tight coupling.
Reporting read-models, the follow-up job queue, notifications and cross-module reactions all consume domain events. A lightweight event backbone (outbox + dispatch) decouples modules.

## Requirements

- A domain-event mechanism (transactional outbox + dispatch) modules can publish to and subscribe from.

## Acceptance Criteria

- [ ] Modules publish domain events transactionally (outbox) with at-least-once dispatch.
- [ ] Subscribers (read-models, jobs, notifications) can consume events idempotently.
- [ ] Events carry tenant context and are observable.
- [ ] A sample event flows from a write to a read-model projection.

## Technical notes (high level)

- Stack: .NET API (domain/services); Postgres + EF Core (RLS)
- Architecture decisions: [ADR-0013](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Domain-event / messaging backbone**
- [ ] **Apply via migrations; verify RLS/tenancy**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
