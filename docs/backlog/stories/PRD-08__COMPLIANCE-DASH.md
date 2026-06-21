# Compliance dashboards & register exports

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/COMPLIANCE-DASH`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`, `PRD-04/RECALL-LOOKUP`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a compliance officer, I want compliance dashboards and exports covering consent, consult-before-script, the S4 register, recalls, expiry and the breach/complaints registers, so that I can evidence compliance and act on gaps.

Consent coverage, consult-before-script adherence (C1), S4 register export (C8), lot→clients recall, cooling-off adherence (C6), registration-expiry watch (C19), records-retention-due (C18), S4 stock discrepancies (C17), breach (C22) & complaints (C24) registers (REQ-RPT-3).

## Requirements

- Compliance dashboards and exports covering consent, consult-before-script, the S4 register, recalls, expiry and the breach/complaints registers.
- Traces to requirement(s): REQ-RPT-3.
- Must satisfy compliance obligation(s): C1, C8, C18, C19, C22, C24.

## Acceptance Criteria

- [ ] Consult-before-script adherence shows 100% by construction; any exception is flagged.
- [ ] The S4 register exports a complete immutable record; a lot lookup returns all affected clients.
- [ ] Registration-expiry watch and records-due-for-destruction lists render with their basis.
- [ ] Breach and complaints registers are viewable/exportable.

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-08/READ-MODELS, PRD-04/RECALL-LOOKUP.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/COMPLIANCE-DASH.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C1, C8, C18, C19, C22, C24.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C1, C8, C18, C19, C22, C24); blocked path explains why.
- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
