# Exportable audit trail for clinical / medicines / PII

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/AUDIT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** data
>
> **Depends on:** `PRD-01/TENANT`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a compliance officer, I want to export an audit trail of who viewed or changed clinical, medicines and PII data, so that we can evidence access and changes in an inspection.

Every read/write of clinical, medicines and PII data must produce an immutable AuditEvent that a compliance officer can export (C10/ADR-0010). Built on the Sprint 0 audit infra.

## Requirements

- To export an audit trail of who viewed or changed clinical, medicines and PII data.
- Traces to requirement(s): REQ-SEC-3.
- Must satisfy compliance obligation(s): C10.

## Acceptance Criteria

- [ ] Every read/write of clinical/medicines/PII produces an immutable AuditEvent (who/what/when/tenant).
- [ ] The log cannot be edited or deleted.
- [ ] A compliance officer can filter and export the trail.
- [ ] Sensitive-data reads (not just writes) are captured.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: Postgres + EF Core (RLS).
Architecture decisions: ADR-0010 (see docs/adr/decision-log.md).
Depends on: PRD-01/TENANT.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/AUDIT.
Phase: 0 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C10.

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns; tenant_id + RLS.
- [ ] **Enforce compliance gate + audit events** — Server-side (C10); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
