# Charting lot picker: lot-required-before-points gate

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/PRODUCT-LOT-PICKER-GATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/PRODUCT-LOT-PICKER`

## Background

As a injector, I want point placement blocked until a valid lot is selected, with that lot wired into every point, so that every charted unit is provably traceable to the vial it came from.
Plainly: the rule that you cannot drop a single injection point until you have committed to a specific vial — and that the chosen vial automatically becomes the one every point deducts from. Where it fits: a follow-up to PRD-05/PRODUCT-LOT-PICKER that adds the hard gate on top of lot selection. Without it the picker merely suggests a lot; with it the medicine register can prove which lot every charted unit came from, because no point can exist without one (PRD-04/ADMIN-GATE, PRD-04/VIAL-RECON).

## How it works

This follow-up adds the hard gate on top of the basic's lot selection. Step 2 is deliberately a gate: the injector must commit to the exact vial before charting any point, so the medicine register can prove which lot every unit came from.
Placing a point is blocked until a valid lot is selected; once chosen, the lot becomes the default wired into every injection point's deduction and is shown as the active 'Product · lot' label on the map (e.g. 'Botox · B2245 · exp Sep 2026').
The rule is enforced on the server too (not just the UI) so a draft can't carry points without a lot; the selected_lot_id is what the finalise deduction and the lot→client register link draw against (PRD-04/ADMIN-GATE, VIAL-RECON).

## Requirements

- Point placement blocked until a valid lot is selected, with that lot wired into every point.

## Acceptance Criteria

- [ ] No injection point can be placed until a valid lot is selected.
- [ ] Once chosen, the lot becomes the default wired into every point's deduction and updates the active 'Product · lot' label on the map.
- [ ] The 'lot required before points' rule is enforced on the server, not just the UI, so a draft can't carry points without a lot.
- [ ] The selected_lot_id is what the finalise deduction and the lot→client register link draw against (PRD-04/ADMIN-GATE, VIAL-RECON).

## UI designs / screenshots

- Prototype screen: Charting — Step 2 'Product & batch' → Step 3 'Injection map' (charting.png).
- Tapping the face is blocked (with a reason) until a valid lot is selected; selecting a lot enables point placement and sets the 'Product · lot' label.
- In read-only mode the chosen product/lot renders statically with no edit controls.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry (referenced)** — selected_lot_id required before any InjectionPoint can be created
  - _Extends the basic's selection — no new entity; adds the server-enforced 'lot required before points' invariant._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Lot-selection gate on point placement + default-lot wiring**
  Behaviour: no injection point can be placed until a valid lot is selected; once chosen, the lot becomes the default wired into every point's deduction and updates the active 'Product · lot' label on the map. Requirements: enforce the 'lot required before points' rule on the server too (not just the UI) so a draft can't carry points without a lot; the selected_lot_id is what the finalise deduction and the lot→client register link draw against (PRD-04/ADMIN-GATE, VIAL-RECON).
