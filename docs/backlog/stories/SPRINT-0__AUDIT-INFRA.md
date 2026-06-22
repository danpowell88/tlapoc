# Append-only audit infrastructure baseline

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/AUDIT-INFRA`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/DB`

## Background

As a platform engineer, I want an append-only AuditEvent store and a simple API/interceptor for modules to record reads and writes, so that auditability is a built-in default rather than a per-feature afterthought.
C10/ADR-0010 require an immutable record of who read/changed clinical, medicines and PII data. Building the append-only AuditEvent plumbing now lets every later module just emit events.

## How it works

The append-only AuditEvent store + a reusable interceptor/helper so any module records create/update/read with who/what/when/tenant, and tampering (update/delete) is rejected at the data layer (C10/ADR-0010). Makes auditability a built-in default, not a per-feature afterthought; PRD-01/AUDIT builds the export UI on top.

## Requirements

- An append-only AuditEvent store and a simple API/interceptor for modules to record reads and writes.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] AuditEvent table is append-only (no update/delete path) and carries who/what/when/tenant.
- [ ] A reusable interceptor/helper records create/update/read for annotated entities or endpoints.
- [ ] Events are queryable and exportable (full register UI is PRD-01/PRD-08).
- [ ] Tampering attempts (update/delete) are rejected at the data layer.

## Suggested data model

- **AuditEvent** — id, tenant_id, actor_id, action, entity_type, entity_id, at, context(json)
  - _Append-only; no update/delete path._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Append-only audit infrastructure baseline**
  Deliver per the acceptance criteria:
  - AuditEvent table is append-only (no update/delete path) and carries who/what/when/tenant.
  - A reusable interceptor/helper records create/update/read for annotated entities or endpoints.
  - Events are queryable and exportable (full register UI is PRD-01/PRD-08).
  - Tampering attempts (update/delete) are rejected at the data layer.
- [ ] **Apply via migrations; verify RLS/tenancy**
  Migration runs per environment; prove tenant isolation holds.
- [ ] **Document setup & usage**
  How to run/operate it; runbook notes for the team.
