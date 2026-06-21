# Reporting read-models / materialized views

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/READ-MODELS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `PRD-01/AUDIT`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a developer, I want read-models/materialized views fed by domain events and the audit stream, so that dashboards are fast and don't hammer the transactional DB.

Dashboards read from dedicated read-models/materialized views fed by domain events + the audit stream; eventual consistency acceptable (ADR-0013). Build incrementally as modules land.

## Requirements

- Read-models/materialized views fed by domain events and the audit stream.
- Traces to requirement(s): REQ-RPT-1.

## Acceptance Criteria

- [ ] Read-models are populated from domain events + the audit stream.
- [ ] Dashboards read from materialized views, not OLTP, and load within target on clinic data volumes.
- [ ] Read-models are built incrementally per module.
- [ ] Backfill/rebuild of a read-model is supported.

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Postgres + EF Core (RLS).
Architecture decisions: ADR-0013, ADR-0010 (see docs/adr/decision-log.md).
Depends on: PRD-01/AUDIT.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/READ-MODELS.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns; tenant_id + RLS.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
