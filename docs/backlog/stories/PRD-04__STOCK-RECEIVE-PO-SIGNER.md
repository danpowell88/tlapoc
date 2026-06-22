# S4 purchase orders: prescriber-signer & approved-wholesaler gate

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/STOCK-RECEIVE-PO-SIGNER`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/STOCK-RECEIVE`

## Background

As a prescriber/owner, I want S4 purchase orders restricted to a prescriber signer from a TGA-approved wholesaler, so that only an authorised person can lawfully order S4 medicine.
Plainly: the rule that only an authorised prescriber may actually buy S4 (Schedule 4 prescription-only medicine) stock, and only from a TGA (Therapeutic Goods Administration)-approved wholesaler — a nurse or admin cannot place that order. Where it fits: a follow-up to PRD-04/STOCK-RECEIVE that adds the purchase-order layer in front of receiving. Receiving a lot already records provenance; this adds the upstream control that the order itself was lawfully placed (GAP-3, C11).

## How it works

This follow-up adds the purchase-order control that sits upstream of receiving. The basic (PRD-04/STOCK-RECEIVE) records that a lot arrived with lawful provenance; this story enforces that the order which brought it in was lawfully placed.
An S4 purchase order requires a prescriber signer — RNs/ENs/admin cannot buy S4 (GAP-3). Enforce in domain + DB (ADR-0008) that an S4 PurchaseOrder carries prescriber_signer_id (a prescribe-S4-capable staffer) AND wholesaler_approved=true before it commits; an RN/EN/admin attempt is rejected with an explainable reason.
The purchase order, its prescriber signer and approved wholesaler are part of the lawful-supply evidence an inspector asks for (C11); a blocked attempt is itself audited so the refusal is explainable.

## Requirements

- S4 purchase orders restricted to a prescriber signer from a TGA-approved wholesaler.

## Acceptance Criteria

- [ ] An S4 PurchaseOrder must carry a prescriber_signer_id (a prescribe-S4-capable staffer) and wholesaler_approved=true before it can commit.
- [ ] An RN / EN / admin attempt to raise or sign an S4 purchase order is rejected with an explainable reason.
- [ ] A non-approved wholesaler on an S4 line is rejected.
- [ ] The purchase order and any blocked attempt are audited.

## UI designs / screenshots

- Prototype screen: Stock & medicines — purchase order / receive flow (stock.png).
- Raising an S4 purchase order requires selecting a prescriber signer and an approved wholesaler; non-prescriber roles see the action disabled with the reason.
- A blocked PO attempt (non-prescriber signer / non-approved wholesaler) shows an explainable banner and is audited.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **PurchaseOrder** — id, tenant_id, supplier, wholesaler_approved(bool), lines[]{product_id,qty}, prescriber_signer_id, status
  - _New entity (extends the receive flow). S4 POs require a prescriber signer + TGA-approved wholesaler (GAP-3). RNs/ENs/admin cannot sign an S4 PO._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **PurchaseOrder entity + prescriber-signer / approved-wholesaler invariant**
  Behaviour: an S4 purchase order can only be raised/received by a prescriber signer from a TGA-approved wholesaler. Requirements: enforce in domain + DB (ADR-0008) that an S4 PurchaseOrder carries prescriber_signer_id (a prescribe-S4-capable staffer) AND wholesaler_approved=true before it commits (GAP-3); RN/EN/admin attempts are rejected with an explainable reason.
- [ ] **PO audit (signer, wholesaler, blocked attempts)**
  Behaviour: each S4 purchase order writes an audit record of its prescriber signer and approved wholesaler; a blocked attempt is itself audited. Requirements: append-only AuditEvent stream (ADR-0010); this is part of the lawful-supply evidence an inspector asks for (C11).
