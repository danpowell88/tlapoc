# Retention cohort analysis & at-risk worklist

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/RETENTION-COHORTS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

As a owner, I want a cohort retention grid and an at-risk / lapsed client list I can act on, so that I can see whether new clients actually stick and win back the ones slipping away.
Plainly: the Retention tab's deeper analysis — a cohort grid showing, for each month's intake of new clients, how many are still active over time, plus a list of clients who are at-risk or lapsed with a one-click hand-off into the recall worklist. Where it fits: a sibling of the business dashboards (PRD-08/BUSINESS-DASH) in the Reporting layer (step 6 of the clinic-first build); it reads the same reporting read-models (PRD-08/READ-MODELS) the dashboards do, but is a distinct analytical surface — a triangle cohort matrix and an actionable client list rather than headline tiles. The at-risk list hands off to the follow-up/recall queue (PRD-07) so a number on the report becomes a call, never a dead end. New-vs-returning and the headline retention/rebooking rates stay on BUSINESS-DASH; this story owns the cohort matrix and the at-risk/lapsed worklist. A cohort is the group of clients who first visited in the same month.

## How it works

The cohort matrix is the truest measure of whether new clients stick: each row is the clients who first visited in a given month, and reading left-to-right shows how many are still active 1, 2, 3 … months on. Newer cohorts naturally have shorter rows (less history), so the grid is a triangle; colour encodes the retained percentage so decay patterns are visible at a glance.
Alongside the grid sits the at-risk / lapsed worklist: clients past their expected return cadence for their treatment type, each showing last-seen, an at-risk reason (e.g. 'anti-wrinkle client, 14 weeks since last visit') and — owner-only — their value at risk. The list is the actionable counterpart to the headline retention rate on BUSINESS-DASH.
Acting on a client hands straight off to the recall/win-back loop: a one-click action queues a reactivation follow-up job (PRD-07) so the report drives a call rather than just describing a problem; the hand-off honours the client's marketing-consent state.
This reads from the reporting read-models (READ-MODELS) over appointment, client and visit data and is date/window-aware like the rest of Reports. Cohort membership and retained-state are operational; any lifetime-value / dollar figure is owner-gated (.fin) and stripped for non-owner roles.

## Requirements

- A cohort retention grid and an at-risk / lapsed client list I can act on.

## Acceptance Criteria

- [ ] A cohort grid shows, per first-visit month, the percentage of that cohort still active at N months since first visit (a triangle that shortens for newer cohorts).
- [ ] The grid reads from the reporting read-models, never OLTP, and is date/window aware like the rest of Reports.
- [ ] An at-risk / lapsed list surfaces clients past their expected return window, each with last-seen, value and a reason they are at-risk.
- [ ] Each at-risk client has a one-click hand-off that creates a reactivation follow-up job (PRD-07), respecting marketing consent.
- [ ] Operational signals are visible to managers; any lifetime-value / dollar figure is owner-only (.fin).

## UI designs / screenshots

- Prototype: Reports → Retention & rebooking (reports.png, goRep('retention')) — the 'Cohort retention · % still active by months since first visit' grid (repCohorts) with the explainer that each row is a first-visit-month group, and the 'At-risk & lapsed clients' card (repAtRisk) with an 'Open follow-ups →' action.
- Cohort grid: rows = first-visit month, columns = months since first visit, cell = % of that cohort still active, colour-graded; newer cohorts render as a shorter triangle.
- At-risk list: client, last-seen, at-risk reason, value-at-risk (.fin owner-only), and a per-row 'queue reactivation' hand-off into Follow-ups.
- Date presets shared with the business view; operational signals visible to managers, money owner-gated.

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) RetentionCohort** — cohort_month, months_since, cohort_size, still_active, retained_pct
  - _Projection over first-visit + subsequent-visit events; one cell per (cohort_month, months_since); operational (no money)._
- **(read) AtRiskClient** — client_id, last_seen, treatment_type, expected_cadence, at_risk_reason, value_at_risk
  - _Clients past expected return cadence; value_at_risk owner-gated (.fin); feeds the reactivation hand-off._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection: cohort retention matrix**
  Behaviour: project RetentionCohort = for each first-visit month, the percentage of that cohort still active at each months-since offset, producing the triangle matrix. Requirements: computed over the appointment/visit read-models (READ-MODELS), never OLTP; 'still active' uses a defined activity window; newer cohorts have fewer offsets (shorter rows); date/window-aware; eventual consistency acceptable; operational metric, no money.
- [ ] **Read-model / projection: at-risk & lapsed clients**
  Behaviour: project AtRiskClient = clients past the expected return cadence for their treatment type, with last-seen, an at-risk reason and (owner-only) value-at-risk. Requirements: cadence is per treatment type; value_at_risk is tagged owner-financial and stripped for non-owner roles; expose the underlying client ids so the list drills into the 360 profile.
- [ ] **Cohort grid UI (colour-graded triangle matrix)**
  Behaviour: render the cohort matrix as a colour-graded grid (rows = first-visit month, columns = months since first visit) with the explainer copy and a per-row legend. Requirements: cells colour by retained percentage; newer cohorts render shorter; horizontally scrollable at width; shares the Reports date presets; no money figures.
- [ ] **At-risk list UI + reactivation hand-off to Follow-ups**
  Behaviour: render the at-risk / lapsed list (client, last-seen, reason, value-at-risk) with a per-row 'queue reactivation' action and an 'Open follow-ups →' link. Requirements: the hand-off creates a reactivation follow-up job (PRD-07) honouring marketing consent; value-at-risk is .fin owner-only; rows deep-link into the client 360 profile; the reactivation action is idempotent (no duplicate job for the same client).
