# Adverse-event / DAEN prefilled submission

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/DAEN`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-05/ADVERSE-EVENT`

## Background

Reporting & compliance dashboards (Governance hub) — Turns the platform's data into the business intelligence the clinic relies on and the audit-ready compliance evidence that makes the moat real — consent coverage, the S4 register, lot recall, registration/retention watch, breach & complaints registers, the DAEN adverse-event prefill, plus a one-click inspection-readiness pack.

As a prescriber, I want to generate a prefilled DAEN adverse-event report targeting the correct database, so that reporting an adverse event is fast and correct.

Classify seriousness, route medicine vs device, produce a prefilled DAEN export/submission and flag mandatory cases (C12, ADR-0031).

## Requirements

- To generate a prefilled DAEN adverse-event report targeting the correct database.
- Must satisfy compliance obligation(s): C12.

## Acceptance Criteria

- [ ] An adverse event produces a prefilled DAEN report with seriousness set, targeting the correct database (medicine vs device).
- [ ] Mandatory-reporting cases are flagged.
- [ ] Recall execution + acknowledgement tracking lives in the hub.
- [ ] Submission is export/file (electronic channel is an open option).

## UI designs / screenshots

prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0031 (see docs/adr/decision-log.md).
Depends on: PRD-05/ADVERSE-EVENT.

## Other

Epic: PRD-08 — Reporting & compliance dashboards (Governance hub).
Source PRD: docs/prds/PRD-08-reporting-compliance.md.
Backlog key: PRD-08/DAEN.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C12.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C12); blocked path explains why.
- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
