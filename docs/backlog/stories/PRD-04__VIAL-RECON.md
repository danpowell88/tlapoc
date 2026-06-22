# Vial / unit reconciliation

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/VIAL-RECON`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

As a owner, I want vial/unit reconciliation across draws and wastage, so that stock, billing and the medicine register always agree.
Units drawn vs vial size + wastage must reconcile so stock, billing and the register agree (C8).

## How it works

Vial/unit reconciliation makes stock, billing and the medicine register agree (C8). One toxin vial treats several patients, so partial-vial handling is the norm: units drawn per patient vs vial size plus wastage must reconcile. This also supports the named-patient / no-aliquoting rules emerging in some states (REQ-MED-5).
Reconciliation is derived, not stored: every movement on a lot (receive, administer, waste, adjust) is a StockLedger entry, and on-hand is the sum. When the sum doesn't match a count, the discrepancy is surfaced.
Each administration decrements the selected lot via a StockLedger movement(administer) keyed to the administration_id; wastage and adjustments are their own movements. on_hand = received - used - wasted +/- adjustments, computed from the ledger - never edited directly.
Lot detail shows the reconciliation block: Received / Used / Wasted / On hand in the product's unit (vials for toxin, syringes for filler). The 'Used by' list attributes each draw to a client + units + date, so a partial vial's distribution across patients is visible.
Discrepancies (ledger sum vs a stocktake count, or an administration that would over-draw) are surfaced rather than silently absorbed, and feed reporting (PRD-08).

## Requirements

- Vial/unit reconciliation across draws and wastage.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Each administration decrements the selected lot; vial reconciliation tracks units drawn vs vial size + wastage.
- [ ] Discrepancies are surfaced.
- [ ] Reconciliation data feeds reporting (PRD-08).
- [ ] Partial-vial handling is supported.

## UI designs / screenshots

- Prototype screen: Stock & medicines - lot detail reconciliation (stock.png).
- Lot detail 'Vial reconciliation' block: Received 300U / Used 120U / Wasted 4U / On hand 176U (filler shows 'Syringe reconciliation' in syr).
- Stock-by-lot table columns: On hand / Used / Wasted per lot, with status; usage history chart per product.
- 'Used by' list attributes draws to clients (Sarah Mitchell 24U - 12 Mar, Amelia Ross 20U - 11 Mar, ...) - the partial-vial distribution.
- Charting finalise deducts charted units from the selected lot (see charting.png), the source of the administer movements.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **StockLedger** — id, tenant_id, lot_id, movement(receive|administer|waste|adjust), units, ref(administration_id?), at, actor_id, note
  - _Sum reconciles on_hand; partial-vial waste recorded; discrepancies flagged (C8). Mapping: rec/onhand/wasted on stock[] + the uses[] 'Used by' list._
- **ReconciliationView (read model)** — lot_id, received, used, wasted, on_hand, expected, variance
  - _Derived from StockLedger; variance vs a stocktake count surfaces a discrepancy (feeds PRD-08)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **StockLedger as the single source of on-hand (model & migration)**
  Add StockLedger: id, tenant_id, lot_id(FK), movement(receive|administer|waste|adjust), units, ref(administration_id nullable), at, actor_id, note; RLS by tenant; append-only. Make StockItem.on_hand a derived/maintained value: on_hand = sum(receive) - sum(administer) - sum(waste) +/- adjust. Build the ReconciliationView read model (received/used/wasted/on_hand/expected/variance) per lot. Support partial-vial fractional units where a product's unit requires it.
- [ ] **Reconciliation API + discrepancy surfacing**
  Endpoints: GET /lots/{id}/reconciliation (received/used/wasted/on_hand + the per-client 'used-by' attribution), GET /lots/{id}/ledger. Every administration writes an administer movement (from PRD-04/ADMIN-GATE) in the same transaction as the Administration; wastage writes a waste movement. Surface a discrepancy when the ledger sum disagrees with a stocktake count or an administration would over-draw the lot. Feed the reconciliation read model to reporting (PRD-08).
- [ ] **Over-draw guard + reconciliation audit**
  Guard in domain + DB (ADR-0008): no movement may drive on_hand negative; an administration that would over-draw is blocked (reconciles with PRD-04/ADMIN-GATE). adjust movements (corrections) are capability-gated and require a note; never silently rewrite history - the ledger is append-only and audited so stock, billing units and the register always agree (C8).
