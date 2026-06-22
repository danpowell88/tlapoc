# Exportable audit trail for clinical / medicines / PII

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/AUDIT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** data
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a compliance officer, I want to export an audit trail of who viewed or changed clinical, medicines and PII data, so that we can evidence access and changes in an inspection.
Every read/write of clinical, medicines and PII data must produce an immutable AuditEvent that a compliance officer can export (C10/ADR-0010). Built on the Sprint 0 audit infra.

## How it works

Every read and write of clinical, medicines and PII data writes an immutable, append-only AuditEvent (who, what, when, tenant) on the Sprint-0 audit infrastructure. The log cannot be edited or deleted; a compliance officer can filter and export it.
This is the evidentiary spine for AHPRA/QLD Health inspections and underpins the breach workflow.

## Requirements

- To export an audit trail of who viewed or changed clinical, medicines and PII data.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Every read/write of clinical/medicines/PII produces an immutable AuditEvent (who/what/when/tenant).
- [ ] The log cannot be edited or deleted.
- [ ] A compliance officer can filter and export the trail.
- [ ] Sensitive-data reads (not just writes) are captured.

## UI designs / screenshots

- Surfaces in Governance -> Audit pack (gov-audit.png) and an admin audit-log viewer with filters (who/entity/date) and export.

## Suggested data model

- **AuditEvent** — id, tenant_id, actor_id, action(read|create|update|delete), entity_type, entity_id, at, context(json)
  - _Append-only; no update/delete path at the data layer (ADR-0010)._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - AuditEvent — id, tenant_id, actor_id, action(read|create|update|delete), entity_type, entity_id, at, context(json) (Append-only; no update/delete path at the data layer (ADR-0010).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Every read/write of clinical/medicines/PII produces an immutable AuditEvent (who/what/when/tenant).
  - Rule: The log cannot be edited or deleted.
  - Rule: A compliance officer can filter and export the trail.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/TENANT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C10 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Every read/write of clinical/medicines/PII produces an immutable AuditEvent (who/what/when/tenant).
  - The log cannot be edited or deleted.
