# Provider app: server-side finalise → immutable record

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-FINALISE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/PROVIDER-ROOMSIDE`, `PRD-05/MAPPING`

## Background

As a injector, I want to finalise the chart at the chair so it's sealed and stock is deducted, so that the clinical record is complete, immutable and inventory stays accurate.
Plainly: the 'Complete' action at the chair that seals the chart, deducts the exact stock used and makes the record read-only. Where it fits: a follow-up to the room-side mapping basic (PRD-09/PROVIDER-ROOMSIDE) that adds finalisation; finalisation is server-side (PRD-04/05) and ties to the offline guard (PROVIDER-OFFLINE) — finalise stays disabled until everything has synced. Once sealed the entry is immutable; corrections are appended amendments.

## How it works

'Complete' seals the record. Finalisation is server-side — it decrements the exact batch/lot (the manufacturer's batch of a medicine vial) from inventory and pushes aftercare to the client app; the app re-fetches the sealed, read-only entry so it shows immutable (AC6).
Corrections are appended amendments, never edits. Finalise is disabled until everything has synced (ties to PROVIDER-OFFLINE), protecting the server-side immutability guarantee — a chart can't be sealed with edits or photos still pending.

## Requirements

- To finalise the chart at the chair so it's sealed and stock is deducted.

## Acceptance Criteria

- [ ] 'Complete' seals the record server-side and decrements the exact batch/lot from inventory.
- [ ] Once finalised the entry is read-only; corrections are appended amendments, never edits.
- [ ] Finalise pushes aftercare to the client app.
- [ ] Finalise is disabled until everything has synced (ties to PROVIDER-OFFLINE).

## UI designs / screenshots

- Prototype: treatment-room — Complete step; finalise locks the note.
- Finalise disabled until synced; the sealed entry is read-only (AC6).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) ChartEntry** — PRD-05 — sealed, read-only after finalise; amendments appended
  - _Extends PROVIDER-ROOMSIDE; server-side finalise + stock decrement (PRD-04)._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Server-side finalise → immutable record + stock decrement**
  Behaviour: 'Complete' seals the record. Requirements: finalisation is server-side — it decrements the exact batch/lot (the manufacturer's batch of a medicine vial) from inventory and pushes aftercare to the client app; the app re-fetches the sealed, read-only entry so it shows immutable (AC6); corrections are appended amendments, never edits; finalise is disabled until everything has synced (ties to PROVIDER-OFFLINE).
