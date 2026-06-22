# Wastage, disposal & destruction records

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/WASTAGE-DESTRUCTION`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

As a owner, I want to record wastage, disposal and destruction (including partial vials) with certificates, so that we evidence lawful disposal of S4 medicine.
Plainly: this records medicine that is thrown away or destroyed — a leftover part-vial after a treatment, or expired/spoiled stock — and proves it was disposed of lawfully with a certificate. Where it fits: it closes the medicines loop in the moat alongside reconciliation (PRD-04/VIAL-RECON): every unit received is accounted for as administered, wasted or destroyed. It sits on secure storage (PRD-04/CUSTODY-STORAGE) and feeds the compliance dashboard and audit pack (PRD-08).  Wastage and destruction (incl. partial vials) must be recorded via a licensed/RUM pathway with certificates (C16).

## How it works

C16 requires witnessed destruction/wastage of S4 to be logged - including partial vials/ampoules - disposed via a licensed / Return-Unwanted-Medicines (RUM) pathway, with retained certificates of destruction. This closes the medicines loop alongside reconciliation and stocktake: every unit received is accounted for as administered, wasted or destroyed.
Wastage (a partial-vial remainder discarded after a treatment) and destruction (expired or breached stock) are recorded against a lot: quantity, reason, pathway (RUM|licensed), certificate reference, witness and timestamp. Each writes a waste movement to the StockLedger so the lot's on-hand and reconciliation stay correct (PRD-04/VIAL-RECON).
In the prototype, lot detail offers 'Record wastage' (units + reason) and, for expiring/expired lots with on-hand, a 'Destroy' action that zeroes on-hand to 'Depleted'. The real flow captures the licensed/RUM pathway + certificate ref and is immutable once saved (ADR-0010).
Destruction records are surfaced in the back-office waste log and feed the compliance dashboard and audit pack.

## Requirements

- To record wastage, disposal and destruction (including partial vials) with certificates.
- Compliance: [C16](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Wastage/destruction records capture quantity, reason, pathway and certificate reference.
- [ ] Partial-vial destruction is supported.
- [ ] Licensed/RUM disposal pathway is recorded.
- [ ] Records are immutable and audited.

## UI designs / screenshots

- Prototype screens: Stock & medicines lot detail (stock.png) + back-office waste log.
- Lot detail has a wastage row: a units input + 'Record wastage' button; for an Expiring/Expired lot with on-hand, a 'Destroy' action appears.
- Recording wastage increments the lot's Wasted figure and decrements On hand in the reconciliation block; 'Destroy' zeroes on-hand and marks the lot Depleted.
- The real destruction flow additionally captures reason, pathway (RUM/licensed), certificate ref and witness - immutable once saved.
- Destruction also surfaces in the back-office waste log (backroom).

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **StockDestruction** — id, tenant_id, lot_id, units, reason, pathway(RUM|licensed), certificate_ref, witness_id, at, actor_id
  - _Partial-vial supported; immutable + audited (C16). Writes a StockLedger waste movement. Mapping: recordWastage()/destroyLot() in the prototype lot detail._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **StockDestruction record + ledger waste movement (model & migration)**
  Add StockDestruction: id, tenant_id, lot_id(FK), units, reason, pathway(RUM|licensed), certificate_ref, witness_id, at, actor_id; RLS by tenant; append-only (no UPDATE/DELETE). Each destruction/wastage writes a StockLedger waste movement so reconciliation stays correct (PRD-04/VIAL-RECON). Support fractional/partial-vial units. certificate_ref + witness_id are required for a destruction (vs an in-treatment wastage).
- [ ] **Wastage/destruction API + licensed/RUM pathway**
  Endpoints: POST /lots/{id}/wastage (units, reason) and POST /lots/{id}/destruction (units, reason, pathway, certificate_ref, witness_id). Wastage decrements on_hand via the ledger; destruction of an expiring/expired/quarantined lot zeroes the remaining on-hand and marks it Depleted. Capture the licensed/RUM pathway + certificate so disposal is provably lawful (C16). Surface in the back-office waste log + compliance dashboard.
- [ ] **Immutability + witnessed-destruction audit**
  Records are immutable once saved (ADR-0010); a correction is an appended, linked record, never an edit. Audit every wastage/destruction with quantity, reason, pathway, certificate and witness - the lawful-disposal evidence an inspector asks for (C16). Capability-gate the destroy action to stock-capable clinical roles.
