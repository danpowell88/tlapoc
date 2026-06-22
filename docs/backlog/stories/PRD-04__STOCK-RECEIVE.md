# Stock receipt, ARTG & lawful-supply provenance

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCK-RECEIVE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-04/PRODUCT-CATALOGUE`

## Background

As a prescriber/owner, I want to receive S4 stock and record its ARTG status, brand, sponsor and lawful supply source, so that we only hold lawfully-supplied, approved medicine.
S4 stock is received from a TGA-approved wholesaler with ARTG status, brand, sponsor and lawful supply source recorded; non-ARTG/unverified source is warned/blocked (C11). S4 POs require a prescriber signer.

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

- [ ] **StockItem (lot) + PurchaseOrder model with provenance (model & migration)**
  Add StockItem: id, tenant_id, product_id(FK), lot, expiry, received_units, on_hand, wasted, supplier, artg_verified(bool), supply_source, location_id(FK StockLocation), custodian_id, status; RLS by tenant. Add PurchaseOrder: id, tenant_id, supplier, wholesaler_approved, lines[], prescriber_signer_id, status. Index (product_id, expiry) for expiry alerts and (lot) for recall. on_hand is maintained only via StockLedger movements, never edited directly.
- [ ] **Receive-stock API + ARTG/lawful-supply validation**
  Endpoint POST /stock/receive: lot, expiry, received_units (product unit), supplier, artg status, supply_source, location_id, custodian_id. Writes a StockLedger receive movement and creates the StockItem. Validate lawful supply: warn or block non-ARTG / unverified-source per tenant config (C11). ARTG = manual entry in v1 with a hook for a future ARTG dataset lookup. Receiving into a location binds custody (PRD-04/CUSTODY-STORAGE).
- [ ] **Prescriber-signer gate on S4 POs + audit**
  Enforce that an S4 PurchaseOrder requires prescriber_signer_id (a prescribe-S4-capable staffer) and wholesaler_approved=true before it can be raised/received (GAP-3, ADR-0008); RN/EN/admin attempts are rejected. Audit every receive with full provenance (lot, ARTG, supplier, source, signer) - this is the lawful-supply evidence an inspector asks for (C11).
