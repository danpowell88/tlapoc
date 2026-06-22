# Witnessed destruction & disposal records (licensed/RUM + certificate)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/DESTRUCTION-RECORDS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/WASTAGE-DESTRUCTION`

## Background

As a owner, I want to record witnessed destruction of S4 stock via a licensed/RUM pathway with a certificate, so that we can evidence lawful disposal of prescription-only medicine.
Plainly: when expired or breached S4 (Schedule 4 prescription-only medicine) stock has to be destroyed, this records that it was disposed of lawfully — via a licensed or Return-Unwanted-Medicines (RUM) pathway, witnessed, with the certificate of destruction kept. Where it fits: a follow-up to PRD-04/WASTAGE-DESTRUCTION that adds the lawful-disposal evidence on top of plain wastage. It closes the medicines loop alongside reconciliation (PRD-04/VIAL-RECON) and feeds the compliance dashboard + audit pack (PRD-08).

## How it works

C16 requires witnessed destruction of S4 to be logged — including partial vials/ampoules — disposed via a licensed / Return-Unwanted-Medicines (RUM) pathway, with retained certificates of destruction. This follow-up adds that lawful-disposal layer on top of the basic's in-treatment wastage.
Destruction (expired or breached stock) is recorded against a lot: quantity, reason, pathway (licensed | RUM), certificate reference, witness and timestamp. Each writes a waste movement to the StockLedger so the lot's on-hand and reconciliation stay correct (PRD-04/VIAL-RECON).
In the prototype, lot detail offers a 'Destroy' action for expiring/expired lots with on-hand that zeroes on-hand to 'Depleted'. The real flow captures the licensed/RUM pathway + certificate ref + witness and is immutable once saved (ADR-0010). Destruction records surface in the back-office waste log and feed the compliance dashboard + audit pack.

## Requirements

- To record witnessed destruction of S4 stock via a licensed/RUM pathway with a certificate.

## Acceptance Criteria

- [ ] A destruction record captures quantity, reason, pathway (licensed | RUM), certificate reference and witness.
- [ ] Partial-vial destruction is supported; destruction of an expiring/expired/quarantined lot zeroes the remaining on-hand and marks it Depleted.
- [ ] Each destruction writes a StockLedger waste movement so reconciliation stays correct (PRD-04/VIAL-RECON).
- [ ] Destruction records are immutable once saved and audited; they surface in the back-office waste log + compliance dashboard.

## UI designs / screenshots

- Prototype screens: Stock & medicines lot detail (stock.png) + back-office waste log.
- For an Expiring/Expired lot with on-hand, a 'Destroy' action appears; the real flow captures reason, pathway (RUM/licensed), certificate ref and witness — immutable once saved.
- 'Destroy' zeroes on-hand and marks the lot Depleted; destruction also surfaces in the back-office waste log (backroom).

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **StockDestruction** — id, tenant_id, lot_id, units, reason, pathway(RUM|licensed), certificate_ref, witness_id, at, actor_id
  - _New entity (extends the basic's wastage). Partial-vial supported; immutable + audited (C16). Writes a StockLedger waste movement. Mapping: destroyLot() in the prototype lot detail._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **StockDestruction record + licensed/RUM pathway + ledger movement**
  Add StockDestruction: id, tenant_id, lot_id(FK), units, reason, pathway(RUM|licensed), certificate_ref, witness_id, at, actor_id; RLS by tenant; append-only. POST /lots/{id}/destruction (units, reason, pathway, certificate_ref, witness_id) writes a StockLedger waste movement; destroying an expiring/expired/quarantined lot zeroes the remaining on-hand and marks it Depleted. certificate_ref + witness_id are required. Support fractional/partial-vial units.
- [ ] **Immutability + witnessed-destruction audit**
  Behaviour: destruction records are immutable once saved (ADR-0010); a correction is an appended, linked record, never an edit. Requirements: audit every destruction with quantity, reason, pathway, certificate and witness — the lawful-disposal evidence an inspector asks for (C16); surface in the back-office waste log + compliance dashboard. Capability-gate the destroy action to stock-capable clinical roles.
