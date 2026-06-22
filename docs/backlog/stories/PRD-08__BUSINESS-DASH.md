# Business analytics dashboards

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

- [ ] **Date-range presets, custom range & per-practitioner filter**
  Behaviour: a header period control (7d / 30d / 90d presets plus a custom range) and a per-practitioner switch that re-scope every tile on the screen; a sub-header echoes the active window ('last 30 days · figures synthetic'). Requirements: changing the period or practitioner re-queries the read-models (not OLTP) and re-computes every band against the matching comparison window; the selection persists per user and is the single source of truth all three bands and the Insights strip read from.
- [ ] **Insights strip (Opportunity / Watch / On-track callouts)**
  Behaviour: a strip of plain-language cards above the bands that translate the numbers into action ('Conversion is 38% vs your 40% target — closing that gap is about 1 more member a month'), each tagged Opportunity, Watch or On-track. Requirements: generated server-side from target/prior-period variance (not hand-authored copy); cards are derived from the same BusinessMetrics + ClinicTarget the tiles use so they never disagree with a tile; ordering surfaces the most material gap first.
- [ ] **GROWTH band tiles (MRR, active members, net change, new members MTD)**
  Behaviour: the GROWTH band renders MRR (monthly recurring revenue), Active members, Net member change and New members MTD, each tile showing value, target and a coloured variance. Requirements: MRR is money and owner-gated (.fin) — stripped server-side for non-owner roles, who still see the member counts; variance colouring is driven by ClinicTarget; each tile drills into the underlying members/appointments.
- [ ] **PERFORMANCE band tiles (conversion, retention, rebooking, no-show)**
  Behaviour: the PERFORMANCE band renders Conversion, Retention, Rebooking and No-show, each with value / target / variance and a green state when the target is met (no-show uses a ceiling, not a floor). Requirements: these are operational metrics visible to managers without .fin; computed over the appointment/lifecycle projections; each drills into its underlying client/appointment list.
- [ ] **FINANCE band tiles (revenue + MoM, prepaid liability, to-reactivate, autopay success)**
  Behaviour: the FINANCE band renders Revenue last month (+ month-on-month), Prepaid liability, To-reactivate value and Autopay success. Requirements: every dollar figure here is owner-only (.fin) and stripped for non-owner roles; revenue/MoM read the payments projection, prepaid liability the package/membership projection, autopay success the dunning signal (PRD-06); the autopay-success rate may show to a payments role per the gating rule while the dollar figures stay owner-only.
- [ ] **Owner Targets editor (set, apply, reset; persisted per clinic)**
  Behaviour: an editable row of owner targets (MRR target, Active members, Conversion %, Retention %, Rebooking %, No-show max) with Apply targets / Reset. Requirements: persists ClinicTarget per tenant; applying re-colours every tile's variance and regenerates the Insights callouts; the editor is owner-only and the note states figures are saved per clinic (the prototype's 'saved in this browser only' becomes real per-tenant persistence).
- [ ] **Read-model / projection: business metrics + reward-cost-vs-retention**
  Behaviour: project GROWTH/PERFORMANCE/FINANCE metrics from the payments, membership, appointment and lifecycle events into BusinessMetrics keyed by period (+ optional practitioner), plus the RewardCostVsRetention join over the PRD-06 reward ledger so the owner can see whether loyalty spend buys retention. Requirements: compute variance vs target/prior-period server-side; tag money fields owner-financial so the gate can strip them; support the 7d/30d/90d/custom windows and per-practitioner slicing as query parameters over the read schema, never OLTP scans; eventual consistency acceptable.
