# Compliance: S4 register export

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COMPLIANCE-DASH-S4REGISTER`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/COMPLIANCE-DASH`

## Background

As a compliance officer, I want to export a complete, immutable S4 medicines register, so that I can evidence every controlled-medicine administration in an inspection.
Plainly: a one-click export of the complete Schedule 4 (S4, prescription-only medicine) medicines register — every administration with its lot and expiry — as a tamper-evident, dated evidence file an inspector can be handed. Where it fits: a follow-up to the compliance dashboards core (PRD-08/COMPLIANCE-DASH) that adds the first of the register exports. It reads the administration-register projection (PRD-08/READ-MODELS), not OLTP, and each export is recorded as immutable evidence against the audit trail. No money figures.

## How it works

The S4 (Schedule 4 prescription-only medicine) register export produces a complete, ordered, tamper-evident record of every administration with its lot + expiry (C8) — the controlled-medicine evidence an AHPRA / TGA / state-Health inspector asks for. It reads the administration-register projection (PRD-08/READ-MODELS), never an OLTP scan, so it is reproducible and never touches the clinical write path.
Each export is a point-in-time evidence artefact: it writes a RegisterExport row plus an AuditEvent capturing who exported it, when and with what parameters, and it never mutates the source data. The export is one of the categories the inspection-readiness pack (PRD-08/INSPECTION-PACK) later assembles. No money figures appear.

## Requirements

- To export a complete, immutable S4 medicines register.

## Acceptance Criteria

- [ ] The S4 register exports a complete record of administrations, each with lot + expiry, ordered and tamper-evident (C8).
- [ ] Each export is a point-in-time evidence artefact recorded as a RegisterExport row + an AuditEvent (who / when / params).
- [ ] No mutation of source data; the export is reproducible from the administration-register projection, not an OLTP scan.
- [ ] No money figures.

## UI designs / screenshots

- Prototype: Governance → Overview register exports — the S4 register download/export action.
- Each export records a RegisterExport row + an AuditEvent; reproducible from the administration-register projection; no money figures.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **RegisterExport (extends PRD-08/COMPLIANCE-DASH)** — id, tenant_id, type(s4_register), params(date_range?), generated_at, actor_id, artifact_ref
  - _Immutable point-in-time evidence; recorded against the audit trail (C8); reproducible from the administration-register projection._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **S4 register export (immutable administration record)**
  Behaviour: export a complete S4 (Schedule 4 prescription-only medicine) medicines register — every administration with its lot + expiry, ordered and tamper-evident (C8). Requirements: each export is a point-in-time evidence artefact recorded as a RegisterExport row + an AuditEvent (who/when/params); no mutation of source data; reproducible from the administration-register projection, not an OLTP scan.
