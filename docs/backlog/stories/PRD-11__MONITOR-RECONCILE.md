# Cold-chain: reconcile device + manual readings

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/MONITOR-RECONCILE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/TEMP-MONITORS`, `PRD-11/OPENCLOSE-FRIDGE`

## Background

As a owner / staff, I want device and manual fridge readings merged into one cold-chain record, so that an inspector sees a single unbroken chain regardless of source.
Plainly: merge the automated monitor readings with the manual fridge-log entries into one evidenced cold-chain (the unbroken temperature-controlled storage required for medicines) history per fridge, so an inspector sees a single unbroken chain. Where it fits: a follow-up to the monitor basic (PRD-11/TEMP-MONITORS) that adds reconciliation; it joins the device feed with the manual log (PRD-11/OPENCLOSE-FRIDGE) and the medicines cold-chain (PRD-04) into one record that feeds the inspection pack.

## How it works

Merge device readings with the manual FridgeLog entries (PRD-11/OPENCLOSE-FRIDGE) into a single evidenced cold-chain (the unbroken temperature-controlled storage required for medicines) record per fridge: one history regardless of source (C13). The reconciled record is what feeds the inspection pack and demonstrates an unbroken chain to a regulator.
Breaches raised from either the monitor (PRD-11/TEMP-MONITORS) or the manual log remain in the one record so nothing is lost. This is the reconciliation arm that completes the cold-chain evidence picture across both basics.

## Requirements

- Device and manual fridge readings merged into one cold-chain record.

## Acceptance Criteria

- [ ] Device readings and the manual FridgeLog entries (OPENCLOSE-FRIDGE) merge into a single evidenced cold-chain record per fridge.
- [ ] There is one history regardless of source (C13).
- [ ] The reconciled record feeds the PRD-08 inspection pack and demonstrates an unbroken chain to a regulator.
- [ ] Breaches from either source remain in the one record.

## UI designs / screenshots

- Prototype: Operations → Temperature monitors / Open-close fridge log — one reconciled cold-chain history per fridge.
- One history regardless of source; feeds the PRD-08 inspection pack.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) TempLog/FridgeLog** — PRD-04 device readings + PRD-11/OPENCLOSE-FRIDGE manual entries reconciled into one record
  - _Extends TEMP-MONITORS; one cold-chain history per fridge (C13); feeds inspection pack._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Reconcile device + manual readings into one cold-chain record**
  Behaviour: merge device readings with the manual FridgeLog entries (OPENCLOSE-FRIDGE) into a single evidenced cold-chain (the unbroken temperature-controlled storage required for medicines) record per fridge. Requirements: one history regardless of source (C13); the reconciled record is what feeds the inspection pack and demonstrates an unbroken chain to a regulator.
