# Administration gating & immutable record

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/ADMIN-GATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRESCRIPTION`, `PRD-04/STOCK-RECEIVE`

## Background

As a RN, I want to administer S4 only against a valid unconsumed script for this client, recording product, units, depth, site and batch-lot/expiry, so that every dose is lawful, traceable and tamper-proof.
An RN can only administer S4 against a valid, unconsumed prescription for that same client, with current consent and a selected in-date lot; the record is immutable once saved (C8).

## How it works

Administration gating is the central invariant of the moat (C8). An RN may only administer S4 when every prior link holds: a valid, unconsumed Prescription for the SAME client, current consent (incl. off-label coverage if flagged), and a selected lot that is in-date, in-custody and ARTG-verified. The resulting Administration record is immutable once saved (ADR-0010).
This is the chain end-to-end: consult -> individual Rx -> administration against a valid unconsumed script + current consent + in-date in-custody ARTG lot -> immutable register entry -> lot<->client recall link + vial reconciliation. The gate is what makes every dose provably lawful and traceable.
In the prototype, administration IS the act of finalising the injection map against the selected lot. Each charted point records product + units + depth + site + the batch-lot/expiry; finalising deducts the charted units from that lot and writes the Administration(s).
The server re-checks every precondition at finalise time (never trusting the client): the gate chips (consult, consent, screening) must be satisfied; the selected lot must be in-date, in the correct custody location and ARTG-verified; and the units drawn must not over-draw the lot's on-hand. A failed check blocks finalise with an explanatory banner and writes an audit event.
On success the Administration row is appended (immutable, ADR-0010) and the linked Prescription transitions to consumed. The record carries client, prescription, product, lot, units, site, depth, administrator, timestamp - exactly the fields the medicine register and the lot->clients recall need (C8).
Corrections never edit a saved Administration; an appended, linked correction is the only path (ADR-0010) - tamper-evident by construction.

## Requirements

- To administer S4 only against a valid unconsumed script for this client, recording product, units, depth, site and batch-lot/expiry.
- Compliance: [C8](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] An Administration cannot persist without a valid script (same client), current consent and a selected in-date lot.
- [ ] It records product, units, depth, site and batch-lot/expiry; it is immutable once saved.
- [ ] A blocked attempt shows the reason and writes an audit event.
- [ ] The administration appears in the medicine register.

## UI designs / screenshots

- Prototype screen: Charting - finalise against the selected lot (charting.png).
- Step 2 'Product & batch' confirms the vial: product selector + lot selector showing 'B2245 - exp Sep 2026', 'on hand 176U - Fridge 1 - in date'; note 'Units charted below deduct from this lot on finalise - only in-date, in-custody stock is selectable (ARTG-checked).'
- Step 3 'Injection map': per-point Units + 'Lot B2245 - exp Sep 2026'; a running 'Total units' (e.g. 28u) reconciled against the lot.
- 'Finalise & checkout' commits the administration: 'Finalising locks the note and deducts the units used from the selected lot in Stock.'
- Over-draw or any missing prerequisite (consult/consent/lot) blocks finalise with an explanatory banner; the administering-RN view carries a 'verified the consult & script' checkbox.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Administration** — id, tenant_id, client_id, prescription_id, product_id, lot_id, units, site, depth, technique, administrator_id, at, correction_of?
  - _Immutable (ADR-0010); requires valid unconsumed Rx (same client) + current consent + in-date in-custody ARTG lot (C8). correction_of links an appended correction. Appears in the register; powers lot->clients recall. Mapping: a charted InjectionPoint row at finaliseChart()._
- **ChartEntry / InjectionPoint** — chart_id, point_id, name(site), units, depth, product_id, lot_id
  - _Finalised chart entries are immutable; each point becomes an administration draw against the lot._

## Technical notes (high level)

- Architecture decisions: [ADR-0010](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Immutable Administration record + correction-by-append (model & migration)**
  Add Administration: id, tenant_id, client_id, prescription_id(FK), product_id, lot_id(FK), units, site, depth, technique, administrator_id, at, correction_of(self-FK, nullable); RLS by tenant. Make it append-only: REVOKE UPDATE/DELETE; a correction is a new row with correction_of set (ADR-0010). Index (lot_id) for the recall lookup and (client_id, at) for the register. The medicine-register row is this table - no separate mutable copy.
- [ ] **Finalise-administration endpoint + stock deduction**
  Endpoint POST /charts/{id}/finalise creates the Administration(s) from the charted points and decrements the selected lot's on-hand via the StockLedger (movement=administer, ref=administration_id) in one transaction (PRD-04/VIAL-RECON). Server recomputes totals; reject if units drawn exceed lot on-hand (over-draw). On success, transition the Prescription to consumed. Idempotent on the finalise token so an offline-queued retry can't double-administer (ADR-0015).
- [ ] **C8 administration gate invariant + blocked-attempt audit**
  Enforce the full gate in domain + DB (ADR-0008) at finalise: valid unconsumed Prescription for the SAME client; current Consent (and off-label coverage if Rx.off_label); lot in-date AND in-custody (StockLocation/custodian) AND artg_verified AND not quarantined (cold-chain breach). Any failure blocks with a specific explainable reason and writes an AuditEvent for the refusal. Successful administration also audited. This is the moat's keystone - UI checks are advisory only.
