# Product catalogue: per-product on-hand cards, usage history & below-par

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/PRODUCT-CATALOGUE-CARDS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a stock-capable clinician / owner, I want a card per product showing on-hand, recent usage/wastage and a below-par warning, so that I can read each product's stock health at a glance and reorder before it runs out.
Plainly: the at-a-glance health card for each product on the main stock screen — how much is on hand, how much was used or wasted lately, and a warning when it drops below the reorder level. Where it fits: a follow-up to PRD-04/PRODUCT-CATALOGUE that adds the per-product read-model view on top of the typed catalogue. It reads on-hand and usage from the StockLedger (PRD-04/VIAL-RECON) as a projection, never a hand-maintained counter, and its below-par signal drives the reorder count shown on the stock overview (PRD-04/STOCK-OVERVIEW).

## How it works

This follow-up turns the raw catalogue into a readable health summary: a card per product on the main Medicines & stock screen showing on-hand, used and wasted over the last 90 days, a small usage sparkline and the product's S4 badge (prototype prodCards/prodAgg/spark).
When a product's on-hand drops under its par level the card shows a 'below par' state; that same signal is summed into the reorder count surfaced on the stock overview KPI strip (PRD-04/STOCK-OVERVIEW) so a near-empty product is visible without opening the catalogue.
Every figure is a projection over the StockLedger (ADR-0013) computed per product + unit only — a toxin's units and a filler's syringes are never summed into one number (ADR-0021). The figures are derived, never hand-typed counters.
Any cost or margin detail shown on a card is owner-only and stripped for non-owner roles (the .fin capability) — a non-owner sees on-hand and below-par but no money.

## Requirements

- A card per product showing on-hand, recent usage/wastage and a below-par warning.

## Acceptance Criteria

- [ ] The main stock screen renders a card per product with on-hand (in that product's unit), used/wasted over 90 days, a usage sparkline and an S4 badge.
- [ ] A 'below par' state appears when on-hand drops under the product's par level, and drives the reorder count on the KPI strip.
- [ ] Every figure is computed per product+unit from the ProductAggregate read model over the StockLedger — never a cross-unit roll-up (ADR-0021).
- [ ] Any cost or margin overlay on a card stays owner-only behind the .fin capability.

## UI designs / screenshots

- Prototype screen: Stock & medicines — per-product cards (stock.png).
- A card per product: on-hand, used/wasted (90d), a usage sparkline, an S4 badge and a 'below par' chip with the reorder count (e.g. 'reorder 2').
- Cost/margin overlays render only when the .fin capability is present.
- Non-owner stock roles see on-hand and below-par but no dollar figures.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **ProductAggregate (read model)** — product_id, unit, on_hand, used_90d, wasted_90d, below_par(bool)
  - _Extends the basic's model: a projection over the StockLedger, computed per product+unit only (ADR-0021). Mapping: prodAgg() in the prototype._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **ProductAggregate read model over the StockLedger**
  Behaviour: project on_hand, used_90d, wasted_90d and below_par per product+unit from the StockLedger (PRD-04/VIAL-RECON). Requirements: never a cross-unit roll-up (ADR-0021); below_par is on-hand < par level; figures are derived, never hand-maintained counters.
- [ ] **Per-product cards + usage sparkline + below-par (UI)**
  Behaviour: render a card per product on the main stock screen (on-hand, used/wasted 90d, usage sparkline, S4 badge, below-par chip + reorder count) (prototype prodCards/spark). Requirements: cost/margin overlays stay owner-only behind the .fin capability; the below-par count feeds the stock overview KPI strip (PRD-04/STOCK-OVERVIEW).
