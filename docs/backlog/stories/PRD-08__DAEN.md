# Adverse-event / DAEN prefilled submission

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/DAEN`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-05/ADVERSE-EVENT`

## Background

As a prescriber, I want to generate a prefilled DAEN adverse-event report targeting the correct database, so that reporting an adverse event is fast and correct.
Classify seriousness, route medicine vs device, produce a prefilled DAEN export/submission and flag mandatory cases (C12, ADR-0031).

## How it works

Generate a prefilled DAEN adverse-event report with seriousness set, targeting the correct database (medicine vs device), and flag mandatory-reporting cases (C12, ADR-0031). Recall execution + acknowledgement tracking lives in the hub.
Makes reporting an adverse event fast and correct; submission is export/file (electronic channel an open option).

## Requirements

- To generate a prefilled DAEN adverse-event report targeting the correct database.
- Compliance: [C12](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] An adverse event produces a prefilled DAEN report with seriousness set, targeting the correct database (medicine vs device).
- [ ] Mandatory-reporting cases are flagged.
- [ ] Recall execution + acknowledgement tracking lives in the hub.
- [ ] Submission is export/file (electronic channel is an open option).

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Governance -> Adverse events & DAEN (gov-ae.png) — AE list, open a case, prefilled DAEN form routed medicine/device, mandatory-trigger flag, submit/export (openDaen/submitDaen).

![gov-ae — prototype screen](../screens/gov-ae.png)

## Suggested data model

- **DaenReport** — id, adverse_event_id, target(medicine|device), seriousness, mandatory(bool), prefilled(json), submitted_at
  - _From AdverseEvent (PRD-05); export/file._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)
- Architecture decisions: [ADR-0031](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C12); blocked path explains why.
- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
