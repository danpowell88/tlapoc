# Exportable audit trail for clinical / medicines / PII

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/AUDIT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** data
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a compliance officer, I want to export an audit trail of who viewed or changed clinical, medicines and PII data, so that we can evidence access and changes in an inspection.
Every read/write of clinical, medicines and PII data must produce an immutable AuditEvent that a compliance officer can export (C10/ADR-0010). Built on the Sprint 0 audit infra.

## Requirements

- To export an audit trail of who viewed or changed clinical, medicines and PII data.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Every read/write of clinical/medicines/PII produces an immutable AuditEvent (who/what/when/tenant).
- [ ] The log cannot be edited or deleted.
- [ ] A compliance officer can filter and export the trail.
- [ ] Sensitive-data reads (not just writes) are captured.

## Technical notes (high level)

- Stack: Postgres + EF Core (RLS)
- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns; tenant_id + RLS.
- [ ] **Enforce compliance gate + audit events** — Server-side (C10); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
