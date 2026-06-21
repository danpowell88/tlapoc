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

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
