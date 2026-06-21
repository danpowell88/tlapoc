# Reporting read-models / materialized views

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/READ-MODELS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `PRD-01/AUDIT`

## Background

As a developer, I want read-models/materialized views fed by domain events and the audit stream, so that dashboards are fast and don't hammer the transactional DB.
Dashboards read from dedicated read-models/materialized views fed by domain events + the audit stream; eventual consistency acceptable (ADR-0013). Build incrementally as modules land.

## How it works

Dashboards read from dedicated read-models / materialized views fed by domain events + the audit stream (ADR-0013), not the transactional DB. Eventual consistency is acceptable; views are built incrementally per module and support backfill/rebuild.
Keeps dashboards fast and avoids hammering OLTP — the foundation every report sits on.

## Requirements

- Read-models/materialized views fed by domain events and the audit stream.

## Acceptance Criteria

- [ ] Read-models are populated from domain events + the audit stream.
- [ ] Dashboards read from materialized views, not OLTP, and load within target on clinic data volumes.
- [ ] Read-models are built incrementally per module.
- [ ] Backfill/rebuild of a read-model is supported.

## UI designs / screenshots

- No screen — backend projections feeding all of Reports + Governance.
- A sample event flows from a write to a read-model projection (Sprint-0 DOMAIN-EVENTS).

## Suggested data model

- **ReportingView** — materialized views per metric (revenue, retention, utilisation, MRR, compliance)
  - _Fed by domain events + AuditEvent; rebuildable._

## Technical notes (high level)

- Stack: Postgres + EF Core (RLS)
- Architecture decisions: [ADR-0013](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns; tenant_id + RLS.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
