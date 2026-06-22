# Back-office tablet: stock + S4 register + waste panels

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/BACKOFFICE-STOCK`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/BACKOFFICE-TABLET`, `PRD-11/OPENCLOSE`

## Background

As a clinic staff, I want stock-on-hand, S4-register and waste-log panels on the bench tablet, so that I can manage stock, reconcile the controlled-drug register and log waste at the bench.
Plainly: the back-office tablet panels for stock on hand, the Schedule 4 (S4, prescription-only medicine) controlled-drug register, and the waste/disposal log. Where it fits: a follow-up to the back-office tablet basic (PRD-09/BACKOFFICE-TABLET) that adds the medicines panels; they reuse the PRD-04 stock/register/destruction entities rather than re-implementing them. Money figures stay owner-only (.fin).

## How it works

The Stock panel shows on-hand levels with par lines, expiry watch and one-tap reorder/receive; the S4 (Schedule 4 prescription-only medicine) register reconciles received vs administered vs wasted against a physical count; the Waste log records witnessed disposal of partial/expired S4 vials. All reuse the PRD-04 StockItem/StockLedger/S4 register/StockDestruction entities (batch + expiry tracked) — no parallel store.
The register is append-only and reconciled; witnessed-disposal capture is required for traceability. No money figures are shown to non-owner roles — owner-only money stays behind the .fin capability. Expiring-stock state feeds the hub's morning attention items (BACKOFFICE-TABLET).

## Requirements

- Stock-on-hand, S4-register and waste-log panels on the bench tablet.

## Acceptance Criteria

- [ ] The Stock panel shows on-hand levels with par lines, expiry watch and one-tap reorder/receive.
- [ ] The S4 register reconciles received vs administered vs wasted against a physical count (append-only).
- [ ] The Waste log records witnessed disposal of partial/expired S4 vials.
- [ ] Reuses the PRD-04 StockItem/StockLedger/S4 register/StockDestruction entities; no money figures shown to non-owner roles (.fin).

## UI designs / screenshots

- Prototype: backroom — tabs Stock, S4 register, Waste log.
- Stock par lines + expiry + reorder/receive; S4 register reconciled append-only; witnessed waste disposal; money owner-only (.fin).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) StockItem/StockLedger/S4 register/StockDestruction** — PRD-04 — stock on hand, S4 register, waste/disposal
  - _Extends BACKOFFICE-TABLET; batch + expiry tracked; register append-only; money gated (.fin)._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Stock-on-hand + S4 register + waste-log panels (PRD-04)**
  Behaviour: the Stock panel shows on-hand levels with par lines, expiry watch and one-tap reorder/receive; the S4 register reconciles received vs administered vs wasted against a physical count; the Waste log records witnessed disposal of partial/expired S4 (Schedule 4 prescription-only medicine) vials. Requirements: reuses the PRD-04 StockItem/StockLedger/S4 register/StockDestruction entities (batch + expiry tracked); the register is append-only and reconciled; witnessed-disposal capture is required for traceability; no money figures shown to non-owner roles (.fin).
