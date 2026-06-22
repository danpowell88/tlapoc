# Domain-event / messaging backbone

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/DOMAIN-EVENTS`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend, data
>
> **Depends on:** `SPRINT-0/AUDIT-INFRA`

## Background

As a backend developer, I want a domain-event mechanism (transactional outbox + dispatch) modules can publish to and subscribe from, so that read-models, jobs and notifications react to changes without tight coupling.
Reporting read-models, the follow-up job queue, notifications and cross-module reactions all consume domain events. A lightweight event backbone (outbox + dispatch) decouples modules.

## How it works

Modules publish domain events transactionally using a transactional outbox: the event row is written in the same database transaction as the state change, so an event is never lost if the transaction commits and never emitted if it rolls back. A dispatcher then delivers events at-least-once to subscribers, which is the realistic guarantee for distributed delivery.
Because delivery is at-least-once, subscribers (read-model projections, the Jobs queue, notifications) consume idempotently — processing the same event twice produces one effect (an idempotency key / dedupe on the consumer side). Events carry tenant context (so a projection updates the right tenant's read model under the RLS-aware path) and are observable through OBS (dispatch lag, failures).
A sample event flows end to end from a write to a read-model projection to prove the outbox -> dispatch -> idempotent-consume path before modules depend on it. The OutboxEvent record holds type, payload, occurred_at and dispatched_at.

## Requirements

- A domain-event mechanism (transactional outbox + dispatch) modules can publish to and subscribe from.

## Acceptance Criteria

- [ ] Modules publish domain events transactionally (outbox) with at-least-once dispatch.
- [ ] Subscribers (read-models, jobs, notifications) can consume events idempotently.
- [ ] Events carry tenant context and are observable.
- [ ] A sample event flows from a write to a read-model projection.

## Suggested data model

- **OutboxEvent** — id, tenant_id, type, payload(jsonb), occurred_at, dispatched_at, attempts
  - _Written in the same transaction as the state change; at-least-once dispatch; consumers idempotent; tenant-scoped._

## Technical notes (high level)

- Architecture decisions: [ADR-0013](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement the transactional outbox and at-least-once dispatch**
  Let modules publish events that can't be lost or phantom-emitted.
  - OutboxEvent written in the SAME transaction as the state change (committed -> guaranteed; rolled back -> never emitted).
  - A dispatcher delivering events at-least-once to subscribers, running on JOBS-SCHEDULER (retry/back-off applies).
  - Events carry tenant context so projections update the right tenant under the RLS-aware path.
- [ ] **Provide idempotent subscription and a sample write-to-read-model flow**
  Make consumers safe under at-least-once delivery and prove the path.
  - A subscription mechanism where consumers (read-models, Jobs queue, notifications) process idempotently (idempotency key/dedupe) — run-twice = one effect.
  - A sample event flowing from a write to a read-model projection end to end (outbox -> dispatch -> idempotent consume).
- [ ] **Wire event observability and document the backbone**
  Make events visible and document how modules publish/subscribe.
  - Observability via OBS: dispatch lag, failures, dead-letters (reusing JOBS-SCHEDULER's handling).
  - Document how to publish a domain event transactionally and how to write an idempotent subscriber, so READ-MODELS, FOLLOWUPS and notifications build on it consistently (ADR-0013/0010).
