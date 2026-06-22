# Injection map: finalise → transactional stock deduction + register link

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MAPPING-FINALISE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/MAPPING`

## Background

As a injector, I want to finalise the injection map so the charted units deduct from the selected lot and the dose is recorded, so that the treatment is committed as a lawful, traceable administration.
Plainly: the moment the injector commits the charted map — it locks the note and subtracts the units used from the chosen vial, writing the official record that links the batch to the client. Where it fits: a follow-up to PRD-05/MAPPING that adds the finalise/commit step on top of the saved-draft canvas. This is the administration act for the toxin path: a single transaction re-checks the S4 (Schedule 4 prescription-only medicine) gate, deducts the units from the selected lot (PRD-04/ADMIN-GATE, PRD-04/VIAL-RECON) and writes the lot→client register link for recall (PRD-04/RECALL-LOOKUP). The immutability/close-out UI lives in PRD-05/IMMUTABILITY.

## How it works

This follow-up adds the commit step on top of the saved-draft canvas (PRD-05/MAPPING). 'Finalise & checkout' commits the administration: a single DB transaction re-validates the S4 gate, locks the ChartEntry, deducts the charted Σunits from the selected lot via a StockLedger administration movement, and writes the lot→client register link (PRD-04) for recall + vial reconciliation (prototype finaliseChart).
It is rejected if Σunits exceed the lot's on-hand (over-draw), with an explainable reason, and is idempotent on a finalise token so a retried or offline-queued finalise never double-deducts (ADR-0015).
This story owns the deduction + register link only; the close-out modal, the locking semantics and the post-finalise amendment trail live in PRD-05/IMMUTABILITY, and the full administration-gate invariant lives in PRD-04/ADMIN-GATE — finalise here re-checks that gate server-side rather than re-implementing it.

## Requirements

- To finalise the injection map so the charted units deduct from the selected lot and the dose is recorded.

## Acceptance Criteria

- [ ] 'Finalise & checkout' commits the administration in a single transaction: it re-validates the gate, locks the ChartEntry and deducts the charted Σunits from the selected lot via a StockLedger administration movement.
- [ ] Finalise writes the lot→client register link (PRD-04) for recall + vial reconciliation.
- [ ] Finalise is rejected if Σunits exceed the lot's on-hand (over-draw), with an explainable reason.
- [ ] Finalise is idempotent on a finalise token so a retried/offline-queued finalise never double-deducts.

## UI designs / screenshots

- Right rail 'Finalise & checkout' button (locks the note, deducts units) — hidden in read-only.
- Helper: 'Finalising locks the note and deducts the units used from the selected lot in Stock.'
- Over-draw or any missing prerequisite blocks finalise with an explanatory banner.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **InjectionPoint → StockLedger (derived)** — finalise writes one StockLedger administration movement per lot, decrements on-hand, and writes the lot→client register link (PRD-04)
  - _Extends the basic's InjectionPoint/ChartEntry — no new entity; the transactional deduction + register link at finalise. total_units = Σ InjectionPoint.units reconciled on finalise._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Finalise → transactional stock deduction + register link**
  Behaviour: 'Finalise & checkout' commits the administration — it locks the note and deducts the charted Σunits from the selected lot in Stock (prototype finaliseChart). Requirements: a single DB transaction re-validates the gate, locks the ChartEntry, deducts Σunits via a StockLedger administration movement, and writes the lot→client register link (PRD-04) for recall + vial reconciliation; reject if Σunits > on-hand (over-draw); an idempotency key so a retried/offline-queued finalise never double-deducts. Post-finalise edits route to Amendment (PRD-05/IMMUTABILITY); the immutability/close-out UI itself lives in PRD-05/IMMUTABILITY.
