# Mode B pharmacy-dispensing model (placeholder)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/MODE-B`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** backend

## Background

As a owner, I want a pharmacy-dispensing mode for clinics without on-site custody, so that the platform fits a pharmacy-partner arrangement.
An alternative dispensing model where a pharmacy partner holds/dispenses stock. No pharmacy partner yet — deferred, placeholder. (DispensedItem entity reserved.)

## How it works

Placeholder (Phase 2): a pharmacy-dispensing model where a pharmacy partner holds/dispenses stock, for clinics without on-site custody. v1 is Mode A only; the tenant mode switch already anticipates Mode B (DispensedItem entity reserved).

## Requirements

- A pharmacy-dispensing mode for clinics without on-site custody.
- Deferred (Phase 2+): placeholder, design-only for now.
- Compliance: [C7](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Placeholder — v1 is Mode A only; tenant mode switch already anticipates Mode B.
- [ ] Captured so the medicines model stays mode-aware.

## Suggested data model

- **MedicineMode** — tenant_id, mode(A_onsite|B_pharmacy)
  - _v1 = A only._
- **DispensedItem** — (reserved for Mode B)
  - _Placeholder._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint**
  Deferred placeholder — no build in v1; confirm it still fits scope/regulatory stance, then break down.
