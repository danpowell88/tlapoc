# Compliance: registration-expiry watch & records-due lists

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COMPLIANCE-DASH-EXPIRY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/COMPLIANCE-DASH`

## Background

As a compliance officer, I want a registration-expiry watch and a records-due-for-destruction list, each showing its basis, so that an inspector sees not just a number but why each item is on the list.
Plainly: two watchlists on the compliance dashboard — practitioner registrations approaching expiry, and client records that have reached their legal destruction-due date — each row showing not just a date but WHY it is on the list. Where it fits: a follow-up to the compliance dashboards core (PRD-08/COMPLIANCE-DASH) that adds the expiry/retention projections beyond the core consent/consult metrics. The expiry watch reads credential expiry (PRD-01/CREDENTIALS) and the records-due list the retention rules (PRD-01/RETENTION); both project over the read-models. No money figures.

## How it works

This follow-up adds the two watchlists the compliance dashboard needs beyond the core consent/consult metrics: the registration-expiry watch (C19) — practitioner registrations approaching or past expiry — and the records-due-for-destruction list (C18) — client records that have reached their legal retention horizon. The point is that each row shows not just a date but its basis, so an inspector sees why each item is on the list.
The expiry watch carries the AHPRA (Australian Health Practitioner Regulation Agency) expiry date sourced from credentials (PRD-01/CREDENTIALS); the records-due list carries the C18 retention rule that made the record eligible (adults ≥7yr from last contact; minors to 25; indefinite where a complaint / adverse outcome exists), sourced from the retention engine (PRD-01/RETENTION). Both are projected over the read-models with eventual consistency acceptable. It also includes the S4 stock-discrepancy metric (C17, from the PRD-04 reconciliation) as a read. No money figures appear.

## Requirements

- A registration-expiry watch and a records-due-for-destruction list, each showing its basis.

## Acceptance Criteria

- [ ] The registration-expiry watch (C19) and records-due-for-destruction (C18) lists render with their basis.
- [ ] The expiry watch carries the AHPRA expiry date (from CREDENTIALS).
- [ ] The records-due list carries the C18 retention rule that made the record eligible (adults ≥7yr from last contact; minors to 25; indefinite where a complaint/adverse outcome exists).
- [ ] Both project over the read-models; eventual consistency acceptable; no money figures.

## UI designs / screenshots

- Prototype: Governance → Overview — the registration-expiry watch and records-due lists, each row showing its basis (AHPRA expiry date / the retention rule); the 'Key terms' expander explains the acronyms.
- Both project over the read-models; the stock-discrepancy (C17) metric reads the PRD-04 reconciliation; no money figures.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) ExpiryWatch / RetentionDue** — subject_ref, basis(ahpra_expiry|retention_rule), due_date, status
  - _Renders with its basis (C18/C19); expiry from CREDENTIALS, retention rule from RETENTION; projected over the read-models._
- **ComplianceMetric (stock_discrepancy slice, extends PRD-08/COMPLIANCE-DASH)** — key(stock_discrepancy), value, basis, computed_at
  - _S4 stock-discrepancy (C17) read from the PRD-04 reconciliation; extends the core ComplianceMetric._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Registration-expiry watch & records-due-for-destruction lists (with basis)**
  Behaviour: render the registration-expiry watch (C19) and records-due-for-destruction (C18) lists, each row showing not just a date but WHY it is on the list. Requirements: the expiry watch carries the AHPRA (Australian Health Practitioner Regulation Agency) expiry date (from CREDENTIALS); the retention list carries the C18 retention rule that made the record eligible (adults ≥7yr from last contact; minors to 25; indefinite where a complaint/adverse outcome exists); both project over the read-models; eventual consistency acceptable.
- [ ] **Stock-discrepancy metric read (C17)**
  Behaviour: surface the S4 (Schedule 4 prescription-only medicine) stock-discrepancy metric (C17) as a ComplianceMetric read from the PRD-04 vial reconciliation. Requirements: extends the core ComplianceMetric projection; computed over the read-models + AuditEvent; eventual consistency acceptable; no money figures.
