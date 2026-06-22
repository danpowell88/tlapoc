# Loss / theft reporting from a stock discrepancy

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCK-LOSS-THEFT`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/STOCKTAKE`

## Background

As a owner, I want to raise a loss/theft report from an unexplained stock discrepancy, so that losses of S4 medicine are formally reported and evidenced.
Plainly: when a stocktake turns up missing stock that can't be explained, this is the path to formally report it as a loss or theft — especially when it lines up with an odd cabinet access. Where it fits: a follow-up to PRD-04/STOCKTAKE that adds the loss/theft reporting workflow on top of discrepancy surfacing. It cross-references cabinet access anomalies from secure storage (PRD-04/CUSTODY-CABINET-MONITOR) and feeds the compliance dashboard + audit pack (PRD-08), closing the medicines-governance loop (C17).

## How it works

This follow-up adds the loss/theft reporting workflow on top of the basic's discrepancy surfacing. A non-zero stocktake variance is the trigger: the stocktaker can raise a LossReport (loss | theft) from a discrepancy, capturing the lot, units and a note.
An unexplained count variance near a cabinet-access anomaly (PRD-04/CUSTODY-CABINET-MONITOR) is exactly the signal for a loss/theft report — the two are cross-referenced so an unattributed open near a count variance is easy to spot.
Loss/theft reports feed the compliance dashboard and audit pack — periodic reconciliation + loss reporting is the C17 evidence that keeps stock integrity provable and losses reported. Each report is audited.

## Requirements

- To raise a loss/theft report from an unexplained stock discrepancy.

## Acceptance Criteria

- [ ] A loss/theft report can be raised from a recorded stocktake discrepancy, capturing the lot, units, kind (loss | theft) and a note.
- [ ] An unexplained count variance near a cabinet-access anomaly (PRD-04/CUSTODY-CABINET-MONITOR) is highlighted as the signal for a loss/theft report.
- [ ] Loss/theft reports feed the compliance dashboard (PRD-08).
- [ ] Each loss/theft report is audited.

## UI designs / screenshots

- Prototype screen: Stock & medicines (stock.png) + the compliance dashboard.
- A recorded stocktake variance is highlighted as a discrepancy with a loss/theft report path.
- A loss/theft report captures lot, units, kind (loss/theft) and a note; it cross-references cabinet access anomalies and feeds the governance/compliance dashboard.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **LossReport** — id, tenant_id, stocktake_id, lot_id, units, kind(loss|theft), reported_at, reported_by, note
  - _New entity (extends the basic's Stocktake). Triggerable from a discrepancy (C17); cross-referenced with cabinet AccessLog anomalies (PRD-04/CUSTODY-CABINET-MONITOR)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **LossReport model + raise-from-discrepancy API**
  Add LossReport: id, tenant_id, stocktake_id, lot_id, units, kind(loss|theft), reported_at, reported_by, note; RLS by tenant. POST /stocktake/{id}/loss-report raises a LossReport(loss|theft) from a recorded discrepancy. Capability-gate to stock-capable clinical roles + owner.
- [ ] **Cabinet-anomaly cross-reference + audit + dashboard feed**
  Behaviour: cross-reference cabinet AccessLog anomalies (PRD-04/CUSTODY-CABINET-MONITOR) so an unexplained open near a count variance is easy to spot; feed loss/theft reports to the compliance dashboard (PRD-08). Requirements: audit every loss/theft report — loss reporting is the C17 evidence.
