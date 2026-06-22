# Data-quality checks

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/DATA-QUALITY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`

## Background

As a owner, I want data-quality checks that flag anomalies in my records, so that the data stays clean and trustworthy.
This story keeps the records trustworthy: scheduled checks that flag anomalies — clients marked active but never seen, appointments completed without a check-in, likely duplicates, missing contact details, impossible dates — and offer a jump-to-fix. It sits in the Reporting layer (step 6 of the clinic-first build): it runs over the reporting read-models (READ-MODELS), so it depends on those, and its unresolved findings feed the owner needs-attention digest (ATTENTION-DIGEST). This is data hygiene, not compliance evidence and not financial — no money figures. Carry over anomaly checks: active-but-unseen, completed-not-checked-in, duplicates, missing contacts, implausible dates (REQ-RPT-4).

## How it works

Scheduled anomaly checks that keep the records trustworthy, carried over from the prototype's logic: clients marked active but not seen in N months (active-but-unseen), appointments completed without a check-in/lifecycle transition (completed-not-checked-in), likely duplicate client records, records missing required contact details, and implausible dates (e.g. DOB in the future, treatment before registration). Checks run on a schedule over the reporting read-models (READ-MODELS), so they never load the transactional path, and produce DataQualityFinding rows.
Findings are listed and actionable — each carries an entity reference and a jump-to-fix into the relevant module (client record, appointment, etc.) — and unresolved findings feed the owner needs-attention digest (ATTENTION-DIGEST). A finding is closed when its underlying condition no longer holds (resolved_at stamped) on the next run, so the list self-cleans rather than requiring manual dismissal.
This is operational data hygiene, not compliance evidence and not financial — no money figures, no role-gating beyond the owner/manager view.

## Requirements

- Data-quality checks that flag anomalies in my records.

## Acceptance Criteria

- [ ] Checks flag active-but-unseen, completed-not-checked-in, likely duplicates, missing contacts and implausible dates.
- [ ] Findings are listed with an entity reference and a jump-to-fix into the source module.
- [ ] Checks run on a schedule over the read-models (not OLTP).
- [ ] Unresolved findings feed the needs-attention digest; a finding auto-resolves when its condition no longer holds.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Reports → data-quality findings (reports.png context) — a list of anomalies grouped by check type.
- Each finding: check type, the affected client/appointment, a short detail, and a jump-to-fix link to the source record.
- Findings feed the owner needs-attention digest (dashboard.png); resolved findings drop off on the next run.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **DataQualityFinding** — id, tenant_id, check(active_unseen|not_checked_in|duplicate|missing_contact|implausible_date), entity_ref, detail, detected_at, resolved_at?
  - _Scheduled checks over the read-models; feeds ATTENTION-DIGEST; auto-resolves._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection support for data-quality checks**
  Ensure the read-models expose the fields each check needs (last-seen date per client, appointment lifecycle state, normalised contact fields, key dates) so checks query the read schema, not OLTP. Add any supporting projection (e.g. last-contact per client) the checks depend on.
- [ ] **Scheduled data-quality checks + findings store**
  Implement the five checks (active-but-unseen, completed-not-checked-in, duplicate detection, missing-contact, implausible-date) as scheduled jobs (Sprint-0 JOBS-SCHEDULER) that upsert DataQualityFinding rows and auto-resolve findings whose condition no longer holds (stamp resolved_at). Duplicate detection is advisory (name/DOB/contact match) and never auto-merges. Findings carry an entity_ref for the jump-to-fix and feed ATTENTION-DIGEST.
- [ ] **Web UI: data-quality findings list**
  Build the findings list under Reports: grouped by check type, each row showing the affected record, a short detail and a jump-to-fix deep link into the source module. Resolved findings fall off on the next run. Owner/manager view; no money figures.
