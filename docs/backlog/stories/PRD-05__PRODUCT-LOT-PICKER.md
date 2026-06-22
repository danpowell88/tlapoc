# Charting product & batch (lot) selector (MVP)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/PRODUCT-LOT-PICKER`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/MAPPING`

## Background

As a injector, I want to choose the exact product and the in-date, in-custody, ARTG-verified lot I am drawing from before I place any injection point, so that every charted point is traceable to a lawfully-held vial and the units deduct from the right lot on finalise.
Plainly: this is Step 2 of charting — the dropdown pair where the injector picks the product and the precise batch (lot) of medicine they are about to use, before they can map a single point. Where it fits: it is a substantial, self-contained feature of the injection-map screen (PRD-05/MAPPING) and the bridge between the medicines moat and the clinical record. It reads only lawfully-held, in-date, ARTG (Australian Register of Therapeutic Goods)-checked, in-custody lots from inventory (PRD-04/STOCK-RECEIVE, PRD-04/CUSTODY-STORAGE, PRD-04/COLD-CHAIN), and the lot it selects is the one the finalise deduction draws against (PRD-04/ADMIN-GATE, PRD-04/VIAL-RECON). Without a valid lot selected here, no point can be placed and no S4 (Schedule 4 prescription-only medicine) dose is possible.

## How it works

Step 2 sits between the pre-treatment review and the injection map, and it is deliberately a hard gate: the injector must commit to the exact vial before charting any point, so the medicine register can prove which lot every unit came from. The Product dropdown lists chartable products (toxins for the toxin path); selecting a product filters the Batch/lot dropdown to that product's lots (prototype setChartProd/setChartLot/renderChartProduct).
The lot list is filtered to lawfully-usable stock only: on-hand > 0 and not Depleted/Expired, in-date, in the correct custody location, ARTG-verified and not quarantined by a cold-chain breach (PRD-04/COLD-CHAIN). A lot-info line summarises the chosen lot — on-hand · location · in-date or expiring · S4 vs non-S4 — and the helper notes that 'units charted below deduct from this lot on finalise · only in-date, in-custody stock is selectable (ARTG-checked).'
The selected lot is load-bearing: it is the default lot wired into every injection point's deduction and shown as the active 'Product · lot' label on the map (e.g. 'Botox · B2245 · exp Sep 2026'). Placing a point is blocked until a valid lot is selected.
When a product has no usable lot, the picker shows a 'no in-date stock — receive or pick another product' empty state rather than offering an unusable vial — the selectable set is exactly the lots the administration gate (PRD-04/ADMIN-GATE) would accept, so the injector never charts against stock that finalise will reject.

## Requirements

- To choose the exact product and the in-date, in-custody, ARTG-verified lot I am drawing from before I place any injection point.

## Acceptance Criteria

- [ ] A Product dropdown lists chartable products; choosing one filters the Batch/lot dropdown to that product's lots with on-hand > 0, excluding Depleted/Expired/quarantined lots.
- [ ] Only in-date, in-custody, ARTG-verified, non-quarantined lots are selectable; a lot-info line shows on-hand · location · in-date/expiring · S4 vs non-S4.
- [ ] No injection point can be placed until a valid lot is selected; the chosen lot becomes the default lot wired into every point's deduction and updates the 'Product · lot' label on the map.
- [ ] A 'no in-date stock — receive or pick another product' empty state appears when a product has no usable lot.

## UI designs / screenshots

- Prototype screen: Charting — Step 2 'Product & batch' card (charting.png).
- Product dropdown + Batch/lot dropdown (chartProdSel / chartLotSel), a lot-info line (on hand · location · in-date|expiring · S4), and the helper 'Units charted below deduct from this lot on finalise · only in-date, in-custody stock is selectable (ARTG-checked).'
- The lot dropdown shows 'B2245 · exp Sep 2026' style options with an ⚠ on expiring lots; an empty state 'no in-date stock' when none qualify.
- Selecting a lot updates the 'Product · lot' label on the injection map; in read-only mode the chosen product/lot renders statically with no edit controls.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry (referenced)** — selected_product_id, selected_lot_id (the default lot for this chart's points)
  - _The picked lot is wired into InjectionPoint deductions; finalise draws against it (PRD-04/ADMIN-GATE / VIAL-RECON)._
- **SelectableLot (derived view over StockItem)** — lot_id, product_id, lot, expiry, on_hand, location, schedule(S4|non-S4), in_date(bool), in_custody(bool), artg_verified(bool), quarantined(bool)
  - _Filtered to the exact set the administration gate would accept: on-hand>0, in-date, in-custody, ARTG-verified, not quarantined. Mapping: stock.filter(onhand>0) + renderChartProduct() in the prototype._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Selectable-lot query (in-date · in-custody · ARTG · not quarantined)**
  Behaviour: given a product, return only its lawfully-usable lots — on-hand > 0, not Depleted/Expired, in-date, in the correct custody location, ARTG (Australian Register of Therapeutic Goods)-verified and not quarantined by a cold-chain breach (PRD-04/COLD-CHAIN). Requirements: the selectable set must be exactly the set the administration gate (PRD-04/ADMIN-GATE) would accept, so a chartable lot can never be one finalise will reject; reads inventory (PRD-04/STOCK-RECEIVE, CUSTODY-STORAGE) server-side; tenant-scoped (RLS, the per-tenant database isolation).
- [ ] **Product → lot dropdowns + lot-info line + empty state**
  Behaviour: a Product dropdown filters the Batch/lot dropdown to the selected product's selectable lots, each labelled 'lot · exp …' with an expiring warning; a lot-info line summarises on-hand · location · in-date/expiring · S4 vs non-S4; a 'no in-date stock — receive or pick another product' empty state shows when none qualify (prototype setChartProd/renderChartProduct). Requirements: the helper copy states units deduct from this lot on finalise and only in-date/in-custody/ARTG stock is selectable; read-only roles see the chosen product/lot statically.
- [ ] **Selected-lot persistence on the ChartEntry**
  Behaviour: choosing a lot sets ChartEntry.selected_product_id + selected_lot_id and shows the active 'Product · lot' label on the map. Requirements: persist the selection on the draft so it survives sync; the selected_lot_id is what the finalise deduction and the lot→client register link draw against (PRD-04/ADMIN-GATE, VIAL-RECON). The hard 'lot required before any point' enforcement is a follow-up (PRD-05/PRODUCT-LOT-PICKER-GATE).
