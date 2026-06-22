# Business analytics dashboards (core: metrics read-model + headline tiles)

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/READ-MODELS`

## Background

As a owner, I want dashboards for revenue, retention, no-shows, conversion, at-risk, big spenders and membership MRR/churn, filterable by date and practitioner, so that I can run the business on real numbers.
This is the owner's business-intelligence screen: the revenue, retention and membership numbers needed to run the clinic, shown as live tiles with targets and variance. It sits in the Reporting layer (step 6 of the clinic-first build): it reads entirely from the reporting read-models (READ-MODELS), so it depends on those being in place, and the practitioner Scorecard (SCORECARD) is built on top of it. All money figures stay owner-only. Revenue, retention/churn, no-shows, cancellations, conversion, at-risk, big spenders, membership MRR (Monthly Recurring Revenue)/churn and per-practitioner mix, date-filterable (REQ-RPT-1/2). Money figures owner-gated.

## How it works

The owner business-intelligence surface, rebuilt on live data from the reporting read-models (READ-MODELS) — the analytics the clinic relied on in Mindbody but never got cleanly. It carries the prototype's structure: an Insights strip of plain-language callouts (Opportunity / Watch / On-track), then three metric bands — GROWTH (MRR, active members, net member change, new members MTD), PERFORMANCE (conversion, retention, rebooking, no-show) and FINANCE (revenue last month + MoM, prepaid liability, to-reactivate value, autopay success) — each tile showing value, target and variance.
Every figure is computed against a comparison window (prior period or an owner-set target) and is date-filterable via presets (7d / 30d / 90d) plus a custom range, with a per-practitioner breakdown. Owner-set Targets (MRR target, active-member target, conversion %, retention %, rebooking %, no-show ceiling) drive the variance colouring and the Insights callouts; targets are saved per clinic. Reward-cost vs retention surfaces from the rewards engine (PRD-06) so the owner can see whether loyalty spend is buying retention.
All money figures — revenue, MRR, prepaid liability, ARPU (average revenue per client), reward cost — are gated behind the owner financial capability (the .fin capability / applyFin() in the prototype). Non-owner roles such as Reception may see membership counts and operational metrics (no-show, rebooking) but never dollar figures.

## Requirements

- Dashboards for revenue, retention, no-shows, conversion, at-risk, big spenders and membership MRR/churn, filterable by date and practitioner.

## Acceptance Criteria

- [ ] Core dashboards reproduce the prototype's metrics (GROWTH, PERFORMANCE, FINANCE bands) on the same date range.
- [ ] Date-range presets (7d/30d/90d) + custom range, with per-practitioner breakdown.
- [ ] Owner Targets drive variance colouring and the Insights callouts; targets persist per clinic.
- [ ] Reward-cost vs retention surfaces (from PRD-06 rewards).
- [ ] All money figures are gated behind the owner financial capability; non-owner roles see counts/ops metrics but no dollars.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Reports (reports.png). Pill tabs Scorecard | Revenue | Retention & rebooking | Memberships | Capacity; the business view spans the Revenue/Retention/Memberships tabs.
- Header date presets (7d / 30d / 90d) + custom range; sub-header 'last 30 days · figures synthetic'.
- Insights strip: Opportunity / Watch / On-track cards in plain language (e.g. 'Conversion is 38% vs your 40% target — closing that gap is about 1 more member a month').
- Metric bands — GROWTH: MRR, Active members, Net member change, New members MTD · PERFORMANCE: Conversion, Retention, Rebooking, No-show · FINANCE: Revenue last month (+MoM), Prepaid liability, To reactivate, Autopay success. Each tile: value, target, variance.
- Targets editor row (MRR target, Active members, Conversion %, Retention %, Rebooking %, No-show max) with Apply targets / Reset.
- Money tiles hidden for non-owner roles (.fin gating).

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) BusinessMetrics** — period, practitioner_id?, revenue, mrr, active_members, net_member_change, conversion, retention, rebooking, no_show_rate, prepaid_liability, reactivation_value, autopay_success
  - _Projection over payments/memberships/appointments events; money fields owner-gated._
- **(read) RewardCostVsRetention** — period, reward_cost, retained_clients, cost_per_retained
  - _Joins PRD-06 reward ledger to retention; owner-gated._
- **ClinicTarget** — tenant_id, mrr_target, active_member_target, conversion_target, retention_target, rebooking_target, no_show_ceiling
  - _Owner-set; drives variance + Insights._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Read-model / projection: business metrics (period + comparison window)**
  Behaviour: project the core business metrics from the payments, membership, appointment and lifecycle events into BusinessMetrics keyed by period (+ optional practitioner), each with its value and a comparison window (prior period) for variance. Requirements: compute variance server-side; tag money fields owner-financial so the gate can strip them for non-owner roles; query over the read schema (READ-MODELS), never OLTP scans; eventual consistency acceptable. (The GROWTH/PERFORMANCE/FINANCE band breakdowns, the reward-cost-vs-retention join, the Insights strip and Targets are follow-ups.)
- [ ] **Headline metric tiles + 7d/30d/90d date presets**
  Behaviour: render the headline business tiles (value + prior-period variance) reading the BusinessMetrics projection, with a header date-preset control (7d / 30d / 90d) that re-scopes every tile and a sub-header echoing the active window ('last 30 days · figures synthetic'). Requirements: changing the preset re-queries the read-models (not OLTP) and re-computes against the matching comparison window; money tiles are .fin-gated (owner-only) — non-owner roles see counts/ops metrics but no dollars; the date selection is the single source of truth the follow-up bands read from. (Custom range + per-practitioner slicing is the follow-up BUSINESS-DASH-FILTERS.)
