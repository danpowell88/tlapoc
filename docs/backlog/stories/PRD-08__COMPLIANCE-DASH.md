# Compliance dashboards & register exports

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COMPLIANCE-DASH`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`, `PRD-04/RECALL-LOOKUP`

## Background

As a compliance officer, I want compliance dashboards and exports covering consent, consult-before-script, the S4 register, recalls, expiry and the breach/complaints registers, so that I can evidence compliance and act on gaps.
Consent coverage, consult-before-script adherence (C1), S4 register export (C8), lot→clients recall, cooling-off adherence (C6), registration-expiry watch (C19), records-retention-due (C18), S4 stock discrepancies (C17), breach (C22) & complaints (C24) registers (REQ-RPT-3).

## How it works

The compliance side of the Governance hub overview: the moat's data turned into audit-ready evidence. Metrics are queries over the reporting read-models + the AuditEvent stream (ADR-0013/0010): consent coverage, consult-before-script adherence (C1), cooling-off adherence (C6), registration-expiry watch (C19), records-retention/destruction due (C18) and S4 stock discrepancies (C17). Consult-before-script reads 100% by construction because the PRD-04 domain invariant makes a script without a linked synchronous consult impossible to record; the dashboard surfaces that and flags any cross-check exception rather than computing a soft percentage.
Alongside the metrics sit immutable register exports: the S4 medicines register (C8) exports a complete record of administrations (lot + expiry per administration), and a lot→clients recall lookup (C8, reusing PRD-04 RECALL-LOOKUP) returns every client treated from a given lot. The breach register (C22, notifiable data breaches) and complaints register (C24, including the right to complain to AHPRA) are viewable and exportable. Exports are generated as point-in-time evidence artefacts recorded against the audit trail.
The registration-expiry watch and records-due-for-destruction lists each render with their basis — the AHPRA expiry date / the retention rule (adults ≥7yr from last contact; minors to 25; indefinite where a complaint/adverse outcome exists) — so an inspector sees not just a number but why each item is on the list. Surfaced on the Governance Overview tile band (Inspection-ready / Open AE / Unsigned policies / Active recalls) and the Needs-attention list. No money figures appear here.

## Requirements

- Compliance dashboards and exports covering consent, consult-before-script, the S4 register, recalls, expiry and the breach/complaints registers.
- Compliance: [C1](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C19](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C22](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C24](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Consult-before-script adherence reads 100% by construction (PRD-04 invariant); any cross-check exception is flagged, not silently averaged.
- [ ] Consent coverage, cooling-off adherence and S4 stock-discrepancy metrics render from the read-models + audit stream.
- [ ] The S4 register exports a complete, immutable record of administrations (lot + expiry); a lot lookup returns all affected clients.
- [ ] Registration-expiry watch and records-due-for-destruction lists render with their basis (expiry date / retention rule).
- [ ] Breach (C22) and complaints (C24) registers are viewable and exportable; each export is recorded against the audit trail.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Governance → Overview (gov-overview.png). Intro: 'your compliance command centre … most rules enforced quietly inside everyday work'.
- Status tiles: Inspection-ready (Review/Ready), Open AE cases, Unsigned policies, Active recalls — live counts.
- 'Needs attention' column (open items linking to source) and 'Quietly handled for you' column (Registrations & indemnity current, Cold-chain logged twice daily in range, Last stocktake reconciled, Client privacy self-served).
- Register exports: S4 register, lot-recall lookup, breach register, complaints register (download/export actions).
- Registration-expiry watch + records-due lists each show their basis (AHPRA expiry / retention rule); 'Key terms' expander explains the acronyms.

![gov-overview — prototype screen](../screens/gov-overview.png)

## Suggested data model

- **ComplianceMetric** — key(consent_coverage|consult_adherence|cooling_off|reg_expiry|retention_due|stock_discrepancy), value, basis, exceptions[], computed_at
  - _Query over read-models + AuditEvent; consult_adherence is 100% by construction with exceptions flagged._
- **RegisterExport** — id, tenant_id, type(s4_register|lot_recall|breach|complaints), params(lot?, date_range?), generated_at, actor_id, artifact_ref
  - _Immutable point-in-time evidence; recorded against the audit trail (C8/C22/C24)._
- **(read) ExpiryWatch / RetentionDue** — subject_ref, basis(ahpra_expiry|retention_rule), due_date, status
  - _Renders with its basis (C18/C19)._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection: compliance metrics + expiry/retention watch**
  Project ComplianceMetric values (consent coverage, cooling-off adherence, stock-discrepancy from PRD-04 reconciliation, reg-expiry from credentials) over the read-models + AuditEvent. Compute consult-before-script as 100%-by-construction: read it from the absence of unlinked-script audit events and flag any cross-check exception explicitly rather than averaging. Build ExpiryWatch/RetentionDue lists that carry their basis (AHPRA expiry date / the C18 retention rule). Eventual consistency acceptable.
- [ ] **Register exports (S4 register, breach, complaints) as immutable evidence**
  Build the export queries that produce a complete S4 administration register (lot+expiry per administration, ordered, tamper-evident), the breach register (C22) and complaints register (C24). Each export is a point-in-time artefact recorded as a RegisterExport row + an AuditEvent (who/when/params). No mutation of source data; exports are reproducible from the read-models.
- [ ] **Lot → clients recall lookup**
  Reuse PRD-04 RECALL-LOOKUP: given a lot number, return every client treated from that lot (via the administration register projection), with treatment date and contactability, as the input both to the recall campaign (gov-recalls) and the register export. Must be instant at clinic volumes (indexed projection, not an OLTP scan).
- [ ] **Web UI: Governance Overview + register-export actions**
  Build the Governance Overview (gov-overview.png): status tile band (Inspection-ready/Open AE/Unsigned policies/Active recalls), 'Needs attention' list with deep links to source, 'Quietly handled for you' assurances, and the Key-terms expander. Wire the export/download actions for S4 register, lot-recall, breach and complaints. Render expiry-watch and retention-due lists with their basis. Capability-gate to the compliance concern; no money figures.
