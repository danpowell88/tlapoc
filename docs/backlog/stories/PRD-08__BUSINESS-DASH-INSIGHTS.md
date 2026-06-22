# Business dashboards: Insights strip + reward-cost-vs-retention

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/BUSINESS-DASH-INSIGHTS`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-08/BUSINESS-DASH`

## Background

As a owner, I want plain-language insight callouts and a reward-cost-vs-retention read on my dashboard, so that I know what to act on and whether loyalty spend is buying retention.
Plainly: the strip of plain-language callouts above the metric bands that translate the numbers into action ('Conversion is 38% vs your 40% target — about 1 more member a month'), tagged Opportunity / Watch / On-track, plus the reward-cost-vs-retention figure that says whether loyalty spend is buying retention. Where it fits: a follow-up to the business analytics core (PRD-08/BUSINESS-DASH) that sits on the same BusinessMetrics + targets the tiles use. The callouts are generated server-side so they never disagree with a tile; money-bearing callouts (reward cost) stay owner-only (.fin).

## How it works

The Insights strip translates the dashboard numbers into action: plain-language cards above the metric bands ('Conversion is 38% vs your 40% target — closing that gap is about 1 more member a month'), each tagged Opportunity, Watch or On-track. They are generated server-side from target / prior-period variance (not hand-authored copy) and derived from the same BusinessMetrics + ClinicTarget the tiles use, so a callout never disagrees with a tile. Ordering surfaces the most material gap first.
Alongside it, the reward-cost-vs-retention surface joins the PRD-06 reward ledger to retention (RewardCostVsRetention) so the owner can see whether loyalty spend is actually buying retention — cost per retained client. The reward-cost figures are money and stay owner-gated behind the owner-only financial (.fin) capability.

## Requirements

- Plain-language insight callouts and a reward-cost-vs-retention read on my dashboard.

## Acceptance Criteria

- [ ] An Insights strip of plain-language cards sits above the bands, each tagged Opportunity, Watch or On-track.
- [ ] Callouts are generated server-side from target/prior-period variance (not hand-authored), derived from the same BusinessMetrics + ClinicTarget the tiles use, so they never disagree with a tile.
- [ ] Ordering surfaces the most material gap first.
- [ ] A reward-cost-vs-retention surface (from PRD-06 rewards) shows whether loyalty spend buys retention; money figures are owner-only (.fin).

## UI designs / screenshots

- Prototype: Reports — the Insights strip of Opportunity / Watch / On-track cards in plain language above the metric bands.
- Callouts generated server-side from the same BusinessMetrics + ClinicTarget the tiles use (never disagree with a tile); most material gap first.
- Reward-cost vs retention surfaces (from PRD-06 rewards); reward-cost money figures .fin-gated (owner-only).

![reports — prototype screen](../screens/reports.png)

## Suggested data model

- **(read) RewardCostVsRetention** — period, reward_cost, retained_clients, cost_per_retained
  - _Joins PRD-06 reward ledger to retention; owner-gated (.fin)._
- **(derived) Insight callout** — from BusinessMetrics + ClinicTarget variance → {tag(opportunity|watch|on_track), copy, materiality}
  - _Generated server-side from the same metrics+targets the tiles use; never disagrees with a tile._

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Insights strip (Opportunity / Watch / On-track callouts)**
  Behaviour: a strip of plain-language cards above the bands that translate the numbers into action ('Conversion is 38% vs your 40% target — closing that gap is about 1 more member a month'), each tagged Opportunity, Watch or On-track. Requirements: generated server-side from target/prior-period variance (not hand-authored copy); cards are derived from the same BusinessMetrics + ClinicTarget the tiles use so they never disagree with a tile; ordering surfaces the most material gap first.
- [ ] **Read-model / projection: reward-cost vs retention**
  Behaviour: project RewardCostVsRetention by joining the PRD-06 reward ledger to retention so the owner sees whether loyalty spend buys retention (cost per retained client). Requirements: tag the reward-cost money fields owner-financial so the gate strips them for non-owner roles; read over the read schema (READ-MODELS), never OLTP; eventual consistency acceptable.
