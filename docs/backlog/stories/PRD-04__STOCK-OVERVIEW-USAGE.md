# Stock overview: usage-history chart

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCK-OVERVIEW-USAGE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/STOCK-OVERVIEW`

## Background

As a stock-capable clinician / owner, I want a usage-history chart trending units used per week per product, so that I can see demand trends and plan reorders ahead of need.
Plainly: a chart that trends how many units of each product were used per week, so the owner can see demand moving over time rather than just today's on-hand. Where it fits: a follow-up to PRD-04/STOCK-OVERVIEW that adds a trend chart beneath the KPI tiles, and a sibling of the per-product cards (PRD-04/PRODUCT-CATALOGUE-CARDS). It trends the same StockLedger movements (PRD-04/VIAL-RECON) the cards and tiles read.

## How it works

This follow-up adds a trend view on top of the at-a-glance tiles: a 'units used / week' chart (prototype usagechart) with a per-product toggle so the owner can read demand for each product over time.
The series trends StockLedger administer and waste movements per product (PRD-04/VIAL-RECON); it is a projection, never a hand-maintained counter.
Any cost or margin overlay on the chart is owner-only and stripped for non-owner roles (the .fin capability).

## Requirements

- A usage-history chart trending units used per week per product.

## Acceptance Criteria

- [ ] A 'units used / week' usage-history chart trends administer/waste movements per product, with a per-product toggle.
- [ ] The chart reads StockLedger movements (PRD-04/VIAL-RECON) — not a hand-maintained counter.
- [ ] Any cost/margin overlay on the chart stays owner-only (.fin).

## UI designs / screenshots

- Prototype screen: Stock & medicines — usage-history chart (stock.png).
- A 'Usage history · units used / week' chart with a per-product toggle, beneath the KPI tiles and per-product cards.
- Cost/margin overlays render only when the .fin capability is present.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **UsageSeries (read model)** — product_id, week, units_used, units_wasted; projected from StockLedger
  - _Extends the basic's model: trends administer/waste movements per product per week (ADR-0013). Mapping: usagechart in the prototype._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Usage-history series + per-product chart (UI)**
  Behaviour: trend a 'units used / week' series per product from StockLedger administer/waste movements and render it as a chart with a per-product toggle (prototype usagechart). Requirements: the series is a projection over the ledger (PRD-04/VIAL-RECON); cost/margin overlays stay owner-only (.fin).
