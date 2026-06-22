# Compliance dashboards (core: overview band + consent & consult adherence)

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COMPLIANCE-DASH`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`, `PRD-04/RECALL-LOOKUP`

## Background

As a compliance officer, I want compliance dashboards and exports covering consent, consult-before-script, the S4 register, recalls, expiry and the breach/complaints registers, so that I can evidence compliance and act on gaps.
This is the compliance half of the Governance hub: it turns the clinic's everyday records into audit-ready evidence — consent coverage, the prescription-medicine register, recalls, registration and retention watch, and the breach/complaints registers. It sits in the Reporting layer (step 6 of the clinic-first build): it reads from the reporting read-models (READ-MODELS) plus the audit stream and reuses the lot-recall lookup from Injectables (PRD-04), so it depends on both. The owner exceptions digest (ATTENTION-DIGEST) and the inspection-readiness pack (INSPECTION-PACK) are built on top of it. No money figures appear here. Consent coverage, consult-before-script adherence (C1), S4 (Schedule 4 prescription-only medicine) register export (C8), lot→clients recall, cooling-off adherence (C6), registration-expiry watch (C19), records-retention-due (C18), S4 stock discrepancies (C17), breach (C22) & complaints (C24) registers (REQ-RPT-3).

## How it works

The compliance side of the Governance hub overview: the moat's data turned into audit-ready evidence. Metrics are queries over the reporting read-models + the AuditEvent stream (ADR-0013/0010): consent coverage, consult-before-script adherence (C1), cooling-off adherence (C6), registration-expiry watch (C19), records-retention/destruction due (C18) and S4 stock discrepancies (C17). Consult-before-script reads 100% by construction because the PRD-04 domain invariant makes a script without a linked synchronous consult impossible to record; the dashboard surfaces that and flags any cross-check exception rather than computing a soft percentage.
Alongside the metrics sit immutable register exports: the S4 medicines register (C8) exports a complete record of administrations (lot + expiry per administration), and a lot→clients recall lookup (C8, reusing PRD-04 RECALL-LOOKUP) returns every client treated from a given lot. The breach register (C22, notifiable data breaches) and complaints register (C24, including the right to complain to AHPRA) are viewable and exportable. Exports are generated as point-in-time evidence artefacts recorded against the audit trail.
The registration-expiry watch and records-due-for-destruction lists each render with their basis — the AHPRA (Australian Health Practitioner Regulation Agency) expiry date / the retention rule (adults ≥7yr from last contact; minors to 25; indefinite where a complaint/adverse outcome exists) — so an inspector sees not just a number but why each item is on the list. Surfaced on the Governance Overview tile band (Inspection-ready / Open AE / Unsigned policies / Active recalls) and the Needs-attention list. No money figures appear here.

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

- [ ] **Read-model / projection: core compliance metrics**
  Behaviour: project the core ComplianceMetric values — consent coverage, cooling-off adherence (C6), and consult-before-script adherence (C1) — over the read-models + AuditEvent stream (ADR-0013/0010). Requirements: compute consult-before-script as 100%-by-construction from the ABSENCE of unlinked-script audit events; a gap surfaces as a flagged exception, never a silently-averaged number; eventual consistency acceptable; no money figures. (Stock-discrepancy and the expiry/retention watch projections are the follow-up COMPLIANCE-DASH-EXPIRY; register exports are separate follow-ups.)
- [ ] **Consent-coverage & cooling-off adherence metrics**
  Behaviour: render consent-coverage (share of treatments with a current, version-correct consent on file) and cooling-off adherence (C6, under-18 7-day wait honoured) as compliance metrics with their basis. Requirements: computed over the read-models + AuditEvent stream (ADR-0013/0010); a gap surfaces as a flagged exception with a deep link to the affected client/visit, never a silently-averaged number; eventual consistency acceptable; no money figures.
- [ ] **Consult-before-script adherence (100% by construction, exceptions flagged)**
  Behaviour: surface consult-before-script adherence (C1) as 100% by construction — the PRD-04 domain invariant makes a script without a linked synchronous consult impossible to record. Requirements: read it from the ABSENCE of unlinked-script audit events rather than averaging a soft percentage; if any cross-check finds an exception, flag it explicitly with its source rather than diluting the headline; expand the acronyms (S4, consult) in the surface copy.
- [ ] **Governance Overview tile band + 'Needs attention' + 'Quietly handled' columns**
  Behaviour: build the Governance Overview (gov-overview.png) — the live status tile band (Inspection-ready Review/Ready, Open AE cases, Unsigned policies, Active recalls), the 'Needs attention' column with per-item deep links into source, the 'Quietly handled for you' assurance column (registrations & indemnity current, cold-chain logged twice daily in range, last stocktake reconciled, client-privacy self-served), and the Key-terms expander explaining the acronyms. Requirements: tiles and the needs-attention list derive from the compliance metrics + the open AE/policy/recall counts and live-update on action; the 'quietly handled' assurances read cross-module signals (PRD-04 cold chain/stock, PRD-01 privacy) — read-only here; capability-gate to the compliance concern; no money figures.
