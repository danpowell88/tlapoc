# Stock at-a-glance: KPI tiles (MVP)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCK-OVERVIEW`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/STOCK-RECEIVE`

## Background

As a stock-capable clinician / owner, I want an at-a-glance medicines dashboard with on-hand, expiry and below-par signals plus FEFO waste-reduction nudges, so that I can see stock health in seconds and act before a lot expires or runs out.
Plainly: this is the top of the Medicines & stock screen — the read-only picture of stock health (what's on hand, what's expiring, what's below par) plus the lawful nudges to use near-expiry stock before it is written off. Where it fits: it is the at-a-glance surface of the medicines moat, a sibling of the receive/provenance story (PRD-04/STOCK-RECEIVE) and a read aggregation over the same lots. It reads on-hand and usage from the StockLedger (PRD-04/VIAL-RECON), expiry from the lots, and its 'reduce waste & lift margin' panel coordinates with the schedule's quiet-window fill (PRD-02/QUIET-WINDOWS) so a near-expiry S4 (Schedule 4 prescription-only medicine) lot can be consumed first-expiry-first-out (FEFO) — using only non-S4 incentives, because S4 medicines may never be discounted or advertised (TGA, the Therapeutic Goods Administration).

## How it works

The screen already holds the lots; this story is the read-only health summary on top of them. KPI tiles report products tracked, active lots (on-hand > 0), expiring-soon lots with their detail (e.g. 'Botox B2188 · 40U'), and the below-par reorder count — every figure computed per product+unit, never rolled up across a toxin's units and a filler's syringes (ADR-0021).
Per-product cards (prototype prodCards/prodAgg) show on-hand, used/wasted over 90 days, a usage sparkline and a 'below par' state; a usage-history chart trends units used per week per product. These are projections over the StockLedger (PRD-04/VIAL-RECON), not hand-maintained counters.
The 'Reduce waste & lift margin' panel turns the data into action: a near-expiry lot is framed as a write-off to avoid ('Lot B2188 expiring ~6 wks · 40u — avoid a ~$440 write-off'), nudged FEFO (first-expiry-first-out), with a tie-in to the schedule's quiet windows that could absorb it (PRD-02/QUIET-WINDOWS). It also nudges clearing slow-moving retail.
Two hard constraints frame the panel: S4 medicines can never be discounted or advertised, so every lever uses non-S4 incentives sent privately to consented clients (TGA); and every dollar/margin figure is owner-only and stripped for non-owner roles (the .fin capability) — a non-owner sees the lot-health prompt to act, but no money.

## Requirements

- An at-a-glance medicines dashboard with on-hand, expiry and below-par signals plus FEFO waste-reduction nudges.

## Acceptance Criteria

- [ ] KPI tiles surface products tracked, active lots, expiring-soon lots (with the lot detail) and below-par reorder count, computed per product+unit.
- [ ] Per-product cards show on-hand, used/wasted (90d), a usage sparkline and a below-par state; a usage-history chart trends units used per week.
- [ ] A 'reduce waste & lift margin' panel nudges FEFO use of near-expiry lots and slow-moving retail using only non-S4 incentives, with any dollar/margin figure gated owner-only (.fin).
- [ ] The panel cross-links to the schedule's quiet windows (PRD-02/QUIET-WINDOWS) so a near-expiry lot can be absorbed before it must be written off.

## UI designs / screenshots

- Prototype screen: Stock & medicines top section (stock.png).
- KPI tiles: 'Products tracked', 'Active lots', 'Expiring soon' (count + the lot detail line, amber) and 'Below par' (reorder count, amber).
- Per-product cards (on-hand, used/wasted 90d, sparkline, S4 badge, below-par state) and a 'Usage history · units used / week' chart with a per-product toggle.
- 'Reduce waste & lift margin' panel: a near-expiry-lot card ('Lot B2188 expiring (~6 wks · 40u) · avoid a ~$440 write-off · FEFO · 3 quiet windows could absorb it · See quiet windows →'), a 'pull bookings into the window' non-S4 member-offer card and a slow-moving-retail bundle card, with the footnote that S4 medicines can't be discounted/advertised (TGA).
- Owner-only ($) figures rendered only when the .fin capability is present.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **ProductAggregate (read model)** — product_id, unit, on_hand, used_90d, wasted_90d, below_par(bool); projected from StockLedger
  - _Per product+unit only (ADR-0021); drives the cards + KPI tiles. Mapping: prodAgg() in the prototype._
- **ExpiryAlert (derived)** — lot_id, product_id, expiry, on_hand, weeks_to_expiry, est_writeoff_value(.fin)
  - _Surfaces near-expiry lots for the FEFO nudge; the dollar value is owner-only (.fin). Ties to PRD-02/QUIET-WINDOWS for absorption._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Stock KPI tiles (products, active lots, expiring soon, below par)**
  Behaviour: a KPI strip over the lots — products tracked, active lots (on-hand > 0), expiring-soon lots with the lot detail line, and the below-par reorder count (prototype kProducts/kLots/kExpLots/kReorder). Requirements: every figure is a per-product+unit projection over the StockLedger (PRD-04/VIAL-RECON), never a cross-unit roll-up (ADR-0021); below-par is on-hand < par level; expiring-soon reads the expiry alert query.
- [ ] **Expiry-alert query behind the tiles**
  Behaviour: the 'expiring soon' tile reads a near-expiry-lot query that returns each lot with weeks-to-expiry and on-hand. Requirements: tenant-scoped over StockItem.expiry; this same query is reused by the FEFO waste nudges follow-up (PRD-04/STOCK-OVERVIEW-NUDGES) and the stocktake expiry surfacing.
