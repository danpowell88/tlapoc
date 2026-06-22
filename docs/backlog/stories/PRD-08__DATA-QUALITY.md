# Data-quality checks

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/DATA-QUALITY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`

## Background

As a owner, I want data-quality checks that flag anomalies in my records, so that the data stays clean and trustworthy.
Carry over anomaly checks: active-but-unseen, completed-not-checked-in, duplicates, missing contacts, implausible dates (REQ-RPT-4).

## How it works

Anomaly checks carried over from the prototype: active-but-unseen, completed-not-checked-in, duplicates, missing contacts, implausible dates. Findings are listed, actionable, run on a schedule, and feed the needs-attention digest.
Keeps the data clean and trustworthy.

## Requirements

- Data-quality checks that flag anomalies in my records.

## Acceptance Criteria

- [ ] Checks flag active-but-unseen, completed-not-checked-in, duplicates, missing contacts and implausible dates.
- [ ] Findings are listed and actionable.
- [ ] Checks run on a schedule.
- [ ] Findings feed the needs-attention digest.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Reports -> data-quality findings (reports.png) — a list of anomalies with a jump-to-fix; feeds the owner digest.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **DataQualityFinding** — id, tenant_id, check, entity_ref, detail, detected_at, resolved_at
  - _Scheduled checks; feeds ATTENTION-DIGEST._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - DataQualityFinding — id, tenant_id, check, entity_ref, detail, detected_at, resolved_at (Scheduled checks; feeds ATTENTION-DIGEST.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Checks flag active-but-unseen, completed-not-checked-in, duplicates, missing contacts and implausible dates.
  - Rule: Findings are listed and actionable.
  - Rule: Checks run on a schedule.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-08/READ-MODELS.
- [ ] **Web UI**
  Build on the Angular web app: the reports per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Reports -> data-quality findings (reports.png) — a list of anomalies with a jump-to-fix; feeds the owner digest.
