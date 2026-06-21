# Append-only audit infrastructure baseline

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/AUDIT-INFRA`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/DB`

## Background

As a platform engineer, I want an append-only AuditEvent store and a simple API/interceptor for modules to record reads and writes, so that auditability is a built-in default rather than a per-feature afterthought.
C10/ADR-0010 require an immutable record of who read/changed clinical, medicines and PII data. Building the append-only AuditEvent plumbing now lets every later module just emit events.

## Requirements

- An append-only AuditEvent store and a simple API/interceptor for modules to record reads and writes.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] AuditEvent table is append-only (no update/delete path) and carries who/what/when/tenant.
- [ ] A reusable interceptor/helper records create/update/read for annotated entities or endpoints.
- [ ] Events are queryable and exportable (full register UI is PRD-01/PRD-08).
- [ ] Tampering attempts (update/delete) are rejected at the data layer.

## Technical notes (high level)

- Stack: Postgres + EF Core (RLS)
- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Implement: Append-only audit infrastructure baseline**
- [ ] **Apply via migrations; verify RLS/tenancy**
- [ ] **Document setup & usage**
- [ ] **Validate in dev + add a smoke test**
