# Stocktake & discrepancy surfacing (MVP)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCKTAKE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

As a owner, I want to run a stocktake and have discrepancies surfaced with a loss/theft reporting path, so that stock integrity is provable and losses are reported.
Plainly: this is the periodic count. Staff physically count the stock of S4 (Schedule 4 prescription-only medicine), the system compares it against what the records say should be there, and any difference is flagged — with a path to report a loss or theft. Where it fits: it closes the medicines-governance loop in the moat. It sits on secure storage (PRD-04/CUSTODY-STORAGE), cross-references cabinet access anomalies, and feeds discrepancies and loss/theft reports to the compliance dashboard (PRD-08).  Stocktakes and discrepancy handling, with loss/theft reporting, close the medicines-governance loop (C17).

## How it works

Periodic S4 reconciliation (C17) proves stock integrity: a stocktake compares expected (the ledger sum) against a physical count per lot, records variances, and gives a path to report loss/theft. Near-expiry lots surface via expiry alerts. Results feed the compliance dashboard (PRD-08), and an unexplained count variance near a cabinet-access anomaly (PRD-04/CUSTODY-STORAGE) is the signal for a loss/theft report.
A Stocktake captures, per lot, the expected on-hand (from the StockLedger) and the counted quantity; variance = counted - expected. A non-zero variance is recorded as a discrepancy; the stocktaker can trigger a LossReport (loss|theft) from a discrepancy.
Expiry alerts surface near-expiry lots (the prototype's 'Expiring soon' tile and the per-lot 'Expiring' status) so they can be used FEFO or destroyed before they lapse.
Stocktake results, discrepancies and loss/theft reports feed the compliance dashboard and audit pack - keeping stock integrity provable and losses reported.

## Requirements

- To run a stocktake and have discrepancies surfaced with a loss/theft reporting path.
- Compliance: [C17](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A stocktake compares expected vs counted stock per lot.
- [ ] Discrepancies are recorded; a discrepancy can trigger a loss/theft report.
- [ ] Expiry alerts surface near-expiry lots.
- [ ] Stocktake results feed the compliance dashboard (PRD-08).

## UI designs / screenshots

- Prototype screen: Stock & medicines (stock.png).
- KPI tiles include 'Expiring soon - 1 lot (Botox B2188 - 40U)' and 'Below par - 2 reorder'; the stock-by-lot table flags an 'Expiring' status per lot.
- A stocktake action compares counted vs expected per lot; a variance is highlighted as a discrepancy with a loss/theft report path.
- The 'Reduce waste & lift margin' panel nudges FEFO use of near-expiry lots (e.g. 'Lot B2188 expiring (~6 wks - 40u)').
- Stocktake results feed the governance/compliance dashboard.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **Stocktake** — id, tenant_id, at, actor_id, lines[]{lot_id, expected, counted, variance}
  - _expected from the StockLedger; variance -> discrepancy (C17)._
- **LossReport** — id, tenant_id, stocktake_id, lot_id, units, kind(loss|theft), reported_at, reported_by, note
  - _Triggerable from a discrepancy (C17); cross-referenced with cabinet AccessLog anomalies._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Stocktake model + expiry alerting (model & migration)**
  Add Stocktake: id, tenant_id, at, actor_id, lines[]{lot_id, expected, counted, variance}; RLS by tenant. expected is snapshotted from the StockLedger at count time. Add an expiry-alert query/threshold over StockItem.expiry to surface near-expiry lots (drives the 'Expiring soon' tile and the per-lot Expiring status).
- [ ] **Stocktake API + discrepancy surfacing + audit**
  Endpoint POST /stocktake (per-lot counted); the server computes expected from the ledger and variance per line, and records a non-zero variance as a discrepancy. Surface discrepancies and near-expiry lots on the stock view and the compliance dashboard (PRD-08); FEFO nudge near-expiry lots before they lapse. Audit every stocktake and recorded variance - periodic reconciliation is the C17 evidence. Capability-gate stocktake to stock-capable clinical roles + owner.
