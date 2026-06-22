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

- Architecture decisions: [ADR-0013](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ReportingView — materialized views per metric (revenue, retention, utilisation, MRR, compliance) (Fed by domain events + AuditEvent; rebuildable.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Read-models are populated from domain events + the audit stream.
  - Rule: Dashboards read from materialized views, not OLTP, and load within target on clinic data volumes.
  - Rule: Read-models are built incrementally per module.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/AUDIT.
