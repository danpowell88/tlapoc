# Stock receipt, ARTG & lawful-supply provenance

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCK-RECEIVE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a prescriber/owner, I want to receive S4 stock and record its ARTG status, brand, sponsor and lawful supply source, so that we only hold lawfully-supplied, approved medicine.
Plainly: this is how medicine comes in the door and gets logged. When an S4 (Schedule 4 prescription-only medicine) arrives, the clinic records exactly which approved product it is, who supplied it and that it was lawfully ordered — so the clinic can prove it only holds legitimate stock. Where it fits: this is where provenance enters the moat. It sits on the product catalogue (PRD-04/PRODUCT-CATALOGUE) and feeds the administration gate (PRD-04/ADMIN-GATE), which will only let a nurse draw from a lot whose lawful supply was recorded here.  S4 stock is received from a TGA-approved wholesaler with ARTG status, brand, sponsor and lawful supply source recorded; non-ARTG/unverified source is warned/blocked (C11). S4 POs require a prescriber signer.

## How it works

Lawful supply is a top TGA enforcement target (penalties to $1.65M/breach for individuals): importing or using unapproved/counterfeit injectables is exactly what C11 guards against. Every S4 lot received must record its ARTG registration/approval status, brand, sponsor and the lawful supply source (ordered by an authorised prescriber from a TGA-approved wholesaler).
S4 purchase orders require a prescriber signer - RNs/ENs/admin cannot buy S4 (GAP-3). The receive flow is where provenance enters the system and where non-ARTG / unverified-source stock is warned or blocked per tenant config.
Receiving creates a StockItem (lot) under a product: lot number, expiry, units received (in the product's unit), supplier, ARTG status, supply source, the storage location and the custodian. On-hand starts at received and is decremented by administrations/wastage via the StockLedger.
The server validates lawful supply: ARTG status is recorded (manual entry in v1; dataset lookup is an open option), and non-ARTG or unverified-source stock is warned or blocked per tenant config. An S4 PO must carry a prescriber signer and a TGA-approved wholesaler.
The received lot then surfaces in the stock-by-lot table with on-hand / used / wasted / status, and in lot detail with expiry, supplier, storage+temp, custody, the ARTG badge and vial reconciliation. The provenance recorded here is what makes the lot selectable at administration.

## Requirements

- To receive S4 stock and record its ARTG status, brand, sponsor and lawful supply source.
- Compliance: [C11](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Receiving records ARTG status, brand, sponsor and supply source per lot.
- [ ] Receiving non-ARTG or unverified-source stock is warned/blocked per config.
- [ ] S4 purchase orders require a prescriber signer + TGA-approved wholesaler.
- [ ] ARTG validation supports manual entry (lookup against an ARTG dataset is an open option).

## UI designs / screenshots

- Prototype screen: Stock & medicines - 'Receive stock' (stock.png).
- 'Receive stock' opens a modal capturing lot, expiry, units received, supplier, ARTG status, and the destination location ('Receive into Fridge 1').
- The received lot appears in the 'Stock by lot' table: product, lot, expiry, on-hand, used, wasted, status (OK/Expiring/Depleted/Expired).
- Lot detail shows the ARTG badge ('ARTG' verified vs 'unapproved'), supplier (e.g. 'Allergan AU'), storage ('Fridge 1 - 4.2C') and custody ('Dr Lee NP').
- ARTG validation is manual entry in v1; a dataset lookup is flagged as an open option.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **StockItem** — id, tenant_id, product_id, lot, expiry, received_units, on_hand, wasted, supplier, artg_verified(bool), supply_source, location_id, custodian_id, status(OK|Expiring|Depleted|Expired)
  - _Provenance per lot (C11); on_hand decremented by administrations via StockLedger. Mapping: the stock[] lot objects + doReceive()._
- **PurchaseOrder** — id, tenant_id, supplier, wholesaler_approved(bool), lines[]{product_id,qty}, prescriber_signer_id, status
  - _S4 POs require a prescriber signer + TGA-approved wholesaler (GAP-3). RNs/ENs/admin cannot sign an S4 PO._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Receive-stock modal (lot, expiry, units, supplier, ARTG, destination)**
  Behaviour: 'Receive stock' opens a modal capturing the lot number, expiry, units received (in the product's unit), supplier, ARTG (Australian Register of Therapeutic Goods) status and the destination location ('Receive into Fridge 1'); on save the lot appears at the top of the 'Stock by lot' table and is auto-selected for its detail (prototype openReceive/doReceive). Requirements: received_units seeds on_hand via a StockLedger receive movement (on_hand is never typed directly); receiving into a location binds the lot to that secure StockLocation and its custodian (PRD-04/CUSTODY-STORAGE).
- [ ] **ARTG status + lawful-supply provenance per lot**
  Behaviour: every received S4 (Schedule 4 prescription-only medicine) lot records its ARTG registration status, brand, sponsor and lawful supply source; the lot detail shows the ARTG badge ('ARTG ✓' vs 'unapproved') alongside supplier and custody. Requirements: a non-ARTG or unverified-source lot is warned or blocked per tenant config (C11) — lawful supply is a top TGA (Therapeutic Goods Administration) enforcement target; ARTG is manual entry in v1 with a hook for a future ARTG-dataset lookup. The provenance recorded here is exactly what makes a lot selectable at the administration gate (PRD-04/ADMIN-GATE).
- [ ] **Prescriber-signer gate on S4 purchase orders**
  Behaviour: an S4 purchase order can only be raised/received by a prescriber signer from a TGA-approved wholesaler. Requirements: enforce in domain + DB (ADR-0008) that an S4 PurchaseOrder carries prescriber_signer_id (a prescribe-S4-capable staffer) AND wholesaler_approved=true before it commits (GAP-3); RN/EN/admin attempts are rejected with an explainable reason. RNs/ENs/admin cannot buy S4.
- [ ] **Receive-provenance audit trail**
  Behaviour: each receive writes an immutable audit record of the full provenance — lot, ARTG status, supplier, supply source, destination, custodian and the prescriber signer. Requirements: append-only AuditEvent stream (ADR-0010); a blocked receive (non-ARTG / unverified source / non-prescriber signer) is itself audited so the refusal is explainable. This is the lawful-supply evidence an inspector asks for (C11).
