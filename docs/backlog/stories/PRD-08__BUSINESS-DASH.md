# Business analytics dashboards

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`

## Background

As a owner, I want dashboards for revenue, retention, no-shows, conversion, at-risk, big spenders and membership MRR/churn, filterable by date and practitioner, so that I can run the business on real numbers.
Revenue, retention/churn, no-shows, cancellations, conversion, at-risk, big spenders, membership MRR/churn and per-practitioner mix, date-filterable (REQ-RPT-1/2). Money figures owner-gated.

## How it works

The owner BI the clinic already relies on: revenue, retention/churn, no-shows, cancellations, conversion, at-risk, big spenders, membership MRR/churn and per-practitioner mix — date-filterable. Reward-cost vs retention surfaces (from PRD-06). All money figures are gated behind the owner financial capability.
Rebuilds the prototype's analytics on live data and fixes the Mindbody reporting gap.

## Requirements

- Dashboards for revenue, retention, no-shows, conversion, at-risk, big spenders and membership MRR/churn, filterable by date and practitioner.

## Acceptance Criteria

- [ ] Core dashboards match the prototype's metrics on the same date range.
- [ ] Date-range presets + custom filtering; per-practitioner views.
- [ ] Reward-cost vs retention surfaces (from PRD-06).
- [ ] All money figures are gated behind the owner financial capability.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Reports (reports.png) — revenue trend, treatment mix, top treatments, new-vs-returning, retention, membership MRR; date-range presets + custom; per-practitioner.
- Money figures hidden for non-owner roles (.fin gating).

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) BusinessMetrics** — revenue, retention, churn, no_shows, cancellations, conversion, at_risk, big_spenders, mrr by date/practitioner
  - _From read-models; owner-gated._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection** — Materialised view fed by domain events.
- [ ] **Web UI** — prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack).
