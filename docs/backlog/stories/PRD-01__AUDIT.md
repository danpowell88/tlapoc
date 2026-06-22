# Exportable audit trail for clinical / medicines / PII

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/AUDIT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** data
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a compliance officer, I want to export an audit trail of who viewed or changed clinical, medicines and PII data, so that we can evidence access and changes in an inspection.
Every read/write of clinical, medicines and PII data must produce an immutable AuditEvent that a compliance officer can export (C10/ADR-0010). Built on the Sprint 0 audit infra.

## How it works

Every read AND write of clinical, medicines and PII data writes an immutable, append-only AuditEvent (who, what, when, tenant, entity, action) on the Sprint-0 audit infrastructure (ADR-0010, C10, REQ-SEC-3). Capturing reads — not just writes — is the point: an inspector asks 'who viewed this patient's record', and the answer must exist.
The log has no update or delete path at the data layer — corrections to clinical records are appended and linked, never edited (the same immutability ADR-0010 applies to finalised ChartEntry and medicine-register rows). This makes the trail tamper-evident and defensible in an AHPRA / QLD Health / Privacy audit.
Writing the event is part of the same logical operation as the access it records (so an access can't succeed unaudited), but the audit store is append-only and isolated so audit volume never blocks the transactional path. The capability/scope pipeline (RBAC) emits its own authorisation events (AUTH-AUDIT) as peers of these data-access events; together they are the evidentiary spine the breach workflow (BREACH) and retention/destruction register (RETENTION) build on.
A compliance officer can filter the trail (by actor, entity type/id, date range, action) and export it. Edge cases: a denied read still records the attempt (via the scope_block path); bulk/report reads over the read-models record an aggregate access event rather than one per row, to stay meaningful.

## Requirements

- To export an audit trail of who viewed or changed clinical, medicines and PII data.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Every read/write of clinical/medicines/PII produces an immutable AuditEvent (who/what/when/tenant).
- [ ] The log cannot be edited or deleted.
- [ ] A compliance officer can filter and export the trail.
- [ ] Sensitive-data reads (not just writes) are captured.

## UI designs / screenshots

- Surfaces in Governance -> Audit pack (gov-audit.png) and an admin audit-log viewer: filters for who / entity / date / action, a results table, and an export action. (Non-UI core; the viewer is the human window onto it.)
- No edit/delete affordances anywhere — the log is read + filter + export only.

## Suggested data model

- **AuditEvent** — id, tenant_id, actor_id, action(read|create|update|delete|export), entity_type, entity_id, at, context(json)
  - _Append-only; no update/delete path at the data layer (ADR-0010). tenant_id + RLS; indexed on (entity_type, entity_id), actor_id and at for the viewer filters._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Append-only AuditEvent store (immutable, RLS, no update/delete path)**
  Build the AuditEvent store on the Sprint-0 audit infra: append-only, with no update/delete code path or grant at the data layer (ADR-0010), tenant_id + RLS, and indexes on entity (type+id), actor and timestamp for the viewer. Define the context(json) shape so each event is self-describing. Ensure audit writes are part of the recorded operation (no unaudited access) but isolated so they never block or fail the transactional path.
- [ ] **Capture clinical/medicines/PII reads + writes across modules**
  Provide the cross-cutting hook that every clinical/medicines/PII read and write goes through, capturing actor/action/entity/tenant/context — reads included (AC4 explicitly requires sensitive-data reads). Use an aggregate access event for bulk/report reads over the read-models so the log stays meaningful. This is the single mechanism other PRDs (clients, charting, Rx, stock) attach to rather than each rolling its own.
- [ ] **Audit viewer with filters + export**
  Build the admin/Governance audit viewer (gov-audit.png): filter by actor, entity type/id, date range and action; paginated results table; and an export (CSV/file) for a compliance officer. Read + filter + export only — no edit/delete affordances. Capability-gate to compliance/owner. Exports themselves write an export audit event.
