# Mode B pharmacy-dispensing model (placeholder)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/MODE-B`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** backend

## Background

As a owner, I want a pharmacy-dispensing mode for clinics without on-site custody, so that the platform fits a pharmacy-partner arrangement.
An alternative dispensing model where a pharmacy partner holds/dispenses stock. No pharmacy partner yet — deferred, placeholder. (DispensedItem entity reserved.)

## How it works

Mode B is an alternative dispensing model (REQ-MED-3, deferred) where a pharmacy partner holds and dispenses per-patient stock for clinics without on-site prescriber custody - an RN holds/administers only dispensed items, never bulk stock. There is no pharmacy partner yet, so v1 is Mode A only; this story keeps the medicines model mode-aware.
A tenant MedicineMode switch (A_onsite | B_pharmacy) already anticipates Mode B; v1 = A only. The DispensedItem entity is reserved so the per-patient dispensing model can be added later without a schema rework. WATCH-1 (single-product telehealth prescribing under national review) could elevate the on-site-NP and designated-RN-prescriber models and change Mode-B economics.

## Requirements

- A pharmacy-dispensing mode for clinics without on-site custody.
- Deferred (Phase 2+): placeholder, design-only for now.
- Compliance: [C7](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Placeholder — v1 is Mode A only; tenant mode switch already anticipates Mode B.
- [ ] Captured so the medicines model stays mode-aware.

## UI designs / screenshots

- No dedicated screen in v1; the Mode-A custody header ('On-site stock') is the visible mode today. Mode B would add a per-patient dispensed-item surface in a later phase.

## Suggested data model

- **MedicineMode** — tenant_id, mode(A_onsite|B_pharmacy)
  - _v1 = A only; the mode-aware switch._
- **DispensedItem** — (reserved for Mode B) client_id, pharmacy_ref, product, lot, dispensed_at
  - _Placeholder - per-patient dispensed items tied to the client; RN holds/administers dispensed-only, never bulk (REQ-MED-3)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Scope & design Mode B when pulled into a sprint**
  Placeholder (Phase 2+). When a pharmacy partner exists, design the per-patient dispensing model: MedicineMode=B_pharmacy, the reserved DispensedItem entity (client-tied dispensed items from the pharmacy), and the rule that an RN holds/administers dispensed-only and never bulk S4 (REQ-MED-3, C7). Re-check against WATCH-1 (telehealth prescribing national review). v1 ships Mode A only; this task is intentionally not built now.
