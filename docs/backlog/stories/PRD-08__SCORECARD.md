# Practitioner scorecard

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/SCORECARD`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

As a owner, I want a per-practitioner scorecard, so that I can coach the team and see who drives retention.
This story is the per-practitioner view: revenue, retention, rebooking, utilisation and outcome signals for each clinician, so the owner can coach the team and see who actually drives retention — not just who bills the most. It sits in the Reporting layer (step 6 of the clinic-first build): it is the business dashboards (BUSINESS-DASH) sliced by practitioner, so it depends on that story. Revenue figures stay owner-only; the non-money signals stay visible to managers. The prototype's Reports → Scorecard view shows per-practitioner performance (revenue, retention, rebooking, utilisation, outcomes).

## How it works

A per-practitioner scorecard so the owner can coach the team and see who actually drives retention, not just who bills the most. Reads from the reporting read-models (BUSINESS-DASH metrics sliced by practitioner): revenue, retention and rebooking rate, chair/room utilisation, and outcome/revision signals (e.g. complication or revision rate from the clinical record). Date-filterable on the same presets as the business dashboards.
Each metric drills into the underlying clients/appointments so a number is never a dead end — the owner can go from 'this injector's rebooking is low' to the actual list of clients who didn't rebook. The Insights strip on the Reports landing already calls out scorecard-level patterns ('Filler earns the most per chair-hour …'); the scorecard is the per-practitioner detail behind those callouts.
Financial figures (revenue, revenue-per-chair-hour) are gated behind the owner financial capability; the non-financial signals (retention, rebooking, utilisation, outcomes) remain visible to managers without the money.

## Requirements

- A per-practitioner scorecard.

## Acceptance Criteria

- [ ] Scorecard shows per-practitioner revenue, retention/rebooking, utilisation and outcome/revision signals.
- [ ] Date-filterable on the same presets as the business dashboards.
- [ ] Each metric drills into the underlying clients/appointments.
- [ ] Reads from the reporting read-models; financial figures are owner-gated (non-money signals visible to managers).

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Reports → Scorecard (reports.png, goRep('scorecard')) — the default Reports tab.
- Insights strip with per-practitioner callouts; per-practitioner rows/cards: revenue (owner-gated), retention, rebooking, utilisation, outcome/revision.
- Drill-down from any metric into the underlying client/appointment list; date presets shared with the business view.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) PractitionerScorecard** — practitioner_id, period, revenue, revenue_per_chair_hour, retention, rebooking, utilisation, revision_rate
  - _Projection over BUSINESS-DASH metrics + clinical outcomes, sliced by practitioner; money fields owner-gated._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection: per-practitioner scorecard**
  Slice the business metrics by practitioner and join the clinical outcome/revision signal (from PRD-05) into PractitionerScorecard keyed by practitioner+period: revenue, revenue-per-chair-hour, retention, rebooking, utilisation, revision rate. Tag money fields owner-financial. Support drill-down by exposing the underlying client/appointment ids per metric.
- [ ] **Web UI: practitioner scorecard + drill-down**
  Build the Scorecard tab (default Reports tab): the Insights strip plus per-practitioner rows/cards, with .fin gating on money metrics (non-money signals stay visible to managers). Each metric drills into the underlying client/appointment list. Share the date presets with the business view.
