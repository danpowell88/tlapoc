# Reporting read-models / materialized views

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/READ-MODELS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `PRD-01/AUDIT`

## Background

As a developer, I want read-models/materialized views fed by domain events and the audit stream, so that dashboards are fast and don't hammer the transactional DB.
This is the data plumbing under all of Reporting (PRD-08): a separate, query-optimised copy of the data that every dashboard and register reads from, kept up to date by listening to events from the rest of the app. It sits at step 6 of the clinic-first build — after the clinical and operations core (Reception, Consent, Injectables, Charting) has started emitting events, and before the dashboards (BUSINESS-DASH, COMPLIANCE-DASH) that depend on it. Its only upstream dependency is the audit stream (PRD-01 AUDIT); almost everything else in Reporting depends on it. Dashboards read from dedicated read-models/materialized views fed by domain events + the audit stream; eventual consistency acceptable (ADR-0013). Build incrementally as modules land.

## How it works

Every dashboard and register in the platform reads from a dedicated read schema — a set of materialised views and projection tables — never from the transactional (OLTP) tables directly (ADR-0013). Projections are fed two ways: from domain events emitted on the write side (Sprint-0 DOMAIN-EVENTS) as modules finalise appointments, administrations, payments, memberships and credentials; and from the append-only AuditEvent stream (ADR-0010), which carries the read/write trail the compliance metrics are computed over.
Eventual consistency is the explicit trade: a projection may lag the write by seconds, which is acceptable for reporting and removes read load and lock contention from the booking/charting/checkout paths. Each view is owned by the module that produces its source events and is built incrementally as that module lands — there is no big-bang reporting layer.
Every projection is rebuildable: a backfill replays the source events/audit rows from a checkpoint to reconstruct a view from cold, so a new metric, a bug fix, or a schema change never requires touching live OLTP data. Projections record their last-processed event offset so an incremental catch-up and a full rebuild use the same code path. Money-bearing views (revenue, MRR (Monthly Recurring Revenue), margin) carry the owner-financial capability tag so the gating layer can suppress them for non-owner roles.

## Requirements

- Read-models/materialized views fed by domain events and the audit stream.

## Acceptance Criteria

- [ ] Projections are populated from domain events + the AuditEvent stream; each records its last-processed offset.
- [ ] Dashboards and registers query the read schema (materialised views / projection tables), never OLTP, and load within target at clinic data volumes.
- [ ] Views are built incrementally per module as its events land; eventual-consistency lag is bounded and observable.
- [ ] A projection can be rebuilt/backfilled from cold via event replay using the same code path as incremental catch-up.
- [ ] Money-bearing projections carry the owner-financial capability tag for downstream gating.

## UI designs / screenshots

- No screen of its own — this is the projection layer behind every Reports tab and the Governance hub.
- Validated end-to-end by a sample event: a write (e.g. an Administration finalised) flows through the domain-event bus (Sprint-0 DOMAIN-EVENTS) into its projection and surfaces on a dashboard within the eventual-consistency window.
- Operability: a small internal view of projection lag + last-processed offset per read-model (for ops, not clinic users).

## Suggested data model

- **ReportingView** — name, source_events[], last_offset, refreshed_at, rebuildable(bool), owner_financial(bool)
  - _One per metric family (revenue, retention, utilisation, MRR, compliance); materialised view or projection table._
- **ProjectionCheckpoint** — view_name, last_event_id, last_audit_id, updated_at
  - _Drives incremental catch-up and full rebuild from the same replay path._

## Technical notes (high level)

- Architecture decisions: [ADR-0013](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection layer & event subscriptions**
  Stand up the read schema (separate from OLTP) and the projection runtime that subscribes to the domain-event bus (Sprint-0 DOMAIN-EVENTS) and the AuditEvent stream (ADR-0010). Define a projection contract: handle(event) -> upsert into a materialised view/projection table, advance the ProjectionCheckpoint offset. One projection per metric family so modules can add views as they land. Tag money-bearing views with the owner-financial capability for downstream gating. Keep eventual-consistency lag bounded and expose lag + last-offset per view for ops.
- [ ] **Backfill / rebuild via event replay + scheduled refresh**
  Implement the rebuild path: replay source events/audit rows from a checkpoint (or from zero) to reconstruct any view from cold, reusing the incremental handler so there is one code path. Schedule periodic refresh for views derived from time-windowed aggregates. Make a single view independently rebuildable without touching OLTP or other views. Cover idempotency (replaying an event must not double-count) and out-of-order/duplicate event handling.
