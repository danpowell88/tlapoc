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

- Architecture decisions: [ADR-0031](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - DaenReport — id, adverse_event_id, target(medicine|device), seriousness, mandatory(bool), prefilled(json), submitted_at (From AdverseEvent (PRD-05); export/file.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: An adverse event produces a prefilled DAEN report with seriousness set, targeting the correct database (medicine vs device).
  - Rule: Mandatory-reporting cases are flagged.
  - Rule: Recall execution + acknowledgement tracking lives in the hub.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-05/ADVERSE-EVENT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C12 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Web UI**
  Build on the Angular web app: the gov-ae per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Governance -> Adverse events & DAEN (gov-ae.png) — AE list, open a case, prefilled DAEN form routed medicine/device, mandatory-trigger flag, submit/export (openDaen/submitDaen).
