# Append-only audit infrastructure baseline

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/AUDIT-INFRA`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 3 pts  ·  **Area:** data
>
> **Depends on:** `SPRINT-0/DB`

## Background

As a platform engineer, I want an append-only AuditEvent store and a simple API/interceptor for modules to record reads and writes, so that auditability is a built-in default rather than a per-feature afterthought.
Sprint 0 (setup), compliance plumbing: this builds the tamper-proof, add-only record of who read or changed sensitive data (clinical notes, medicines, personal details). Because the trail is built once here, every later feature just records events into it rather than inventing its own. It builds on the database baseline and is relied on everywhere afterwards: the tenant-isolation bypass logging, the audit register and export screens, the breach workflow, and the domain-event outbox all sit on this append-only discipline.  C10/ADR-0010 require an immutable record of who read/changed clinical, medicines and PII data. Building the append-only AuditEvent plumbing now lets every later module just emit events.

## How it works

An AuditEvent table records who/what/when/tenant — actor id, action (read/create/update), entity type + id, timestamp, tenant_id, and a JSON context for extra detail. It is append-only by construction: no update or delete path exists in the data layer, and the database rejects update/delete attempts (revoked privileges plus a trigger), so the trail is tamper-evident, not merely tamper-discouraged.
A reusable interceptor/helper lets modules record events with one call or by annotation: an EF Core SaveChanges interceptor captures create/update for audited entity types, and a small helper records reads (which aren't captured by SaveChanges) at the point clinical/PII data is served. Events carry the actor and tenant from the API's request context (API/RLS), so modules don't re-plumb identity.
Events are queryable and exportable here at the data level; the full register UI with filtering and export-for-regulator is PRD-01/AUDIT and PRD-08 reporting, which read this stream. Read-auditing scope (clinical, medicines, PII) is deliberate so the volume stays meaningful for an auditor.

## Requirements

- An append-only AuditEvent store and a simple API/interceptor for modules to record reads and writes.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] AuditEvent table is append-only (no update/delete path) and carries who/what/when/tenant.
- [ ] A reusable interceptor/helper records create/update/read for annotated entities or endpoints.
- [ ] Events are queryable and exportable (full register UI is PRD-01/PRD-08).
- [ ] Tampering attempts (update/delete) are rejected at the data layer.

## Suggested data model

- **AuditEvent** — id, tenant_id, actor_id, action(read|create|update), entity_type, entity_id, at, context(jsonb)
  - _Append-only — no update/delete path; DB rejects mutation (revoked privileges + trigger); reads of clinical/medicines/PII are audited too._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Create the append-only AuditEvent store with tamper rejection**
  Build the immutable event table and make mutation impossible at the data layer.
  - AuditEvent table (who/what/when/tenant + jsonb context) created via migration; tenant-scoped under RLS (row-level security).
  - No application update/delete path; the database itself rejects update/delete (revoked privileges + a trigger that raises), so attempts fail — the C10 'tamper-evident' guarantee.
  - An integration test asserting that an update/delete on AuditEvent is rejected (flag it as a compliance invariant for TEST).
- [ ] **Provide the reusable record-event interceptor/helper for writes and reads**
  Give modules one easy, consistent way to emit audit events so it's the default, not an afterthought.
  - A SaveChanges interceptor that records create/update for annotated/audited entity types automatically.
  - A helper to record reads (not caught by SaveChanges) at the point clinical/medicines/PII data is served.
  - Actor + tenant taken from the API request context (API/RLS (row-level security)); the RLS elevated path also emits events through this helper.
- [ ] **Expose queryable/exportable events and document the audit contract**
  Make the stream usable downstream and document how modules opt in.
  - Query access (tenant-scoped) so PRD-01/AUDIT and PRD-08 can build the register UI and exports on top — full UI is out of scope here.
  - Document which entities/endpoints must be audited (clinical, medicines, PII reads + writes), how to annotate them, and the append-only rule for future authors.
