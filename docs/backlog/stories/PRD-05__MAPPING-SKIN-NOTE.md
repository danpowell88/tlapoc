# Charting: non-S4 skin-note variant fields

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MAPPING-SKIN-NOTE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/MAPPING`

## Background

As a injector / dermal therapist, I want a non-S4 skin-note variant capturing areas, device, settings and consumables, so that skin treatments are charted without an irrelevant prescription/lot/deduction.
Plainly: the fields for a non-injectable skin treatment — which areas were treated, what device was used, its settings and any consumables — with no prescription, vial or stock deduction. Where it fits: a follow-up to PRD-05/MAPPING that builds the non-S4 (not Schedule 4 prescription-only medicine) skin-note body. The treatment-type toggle that shows/hides this lives in PRD-05/NOTE-TEMPLATE-TYPE-TOGGLE; this story owns the skin-note fields themselves and persists them as a SkinNote on the ChartEntry.

## How it works

This follow-up builds the non-S4 skin-note body. When treatment_type=skin (set by the toggle in PRD-05/NOTE-TEMPLATE-TYPE-TOGGLE) the toxin map + lot steps are hidden and a non-S4 skin note renders: 'Areas treated' multi-select chips (Full face / Cheeks / Under-eye / Neck / Décolletage), a Device/modality select (needling / Hydrafacial / Laser-IPL / peel), a Settings/depth input and a Consumables (non-S4) input (prototype skin-only block + applyChartType).
A skin note has no lot, no prescription (Rx) and no stock deduction on finalise — it is non-S4. It persists to a SkinNote bound to the ChartEntry.
The toggle that shows/hides this variant lives in PRD-05/NOTE-TEMPLATE-TYPE-TOGGLE; this story owns the fields.

## Requirements

- A non-S4 skin-note variant capturing areas, device, settings and consumables.

## Acceptance Criteria

- [ ] When treatment_type=skin the toxin map + lot steps are hidden and a non-S4 skin note renders.
- [ ] The skin note captures 'Areas treated' (multi-select), Device/modality, Settings/depth and Consumables (non-S4).
- [ ] There is no lot, no prescription and no stock deduction on finalise for a skin note.
- [ ] The skin note persists as a SkinNote bound to the ChartEntry.

## UI designs / screenshots

- Skin-treatment block: 'Areas treated' multi-select chips, a Device/modality select, a Settings/depth input and a Consumables (non-S4) input (skin-only block + applyChartType).
- No product/lot card, no prescription gate and no finalise deduction for a skin note.
- Read-only roles see the skin-note detail without editors.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **SkinNote (non-S4 variant)** — id, chart_entry_id, areas[] (enum), device_modality, settings_text, consumables_text
  - _New entity bound to the basic's ChartEntry. No prescription or lot; non-S4; no stock deduction on finalise._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Skin-note (non-S4) variant fields**
  Behaviour: when treatment_type=skin the toxin map+lot steps are hidden and a non-S4 skin note renders — 'Areas treated' multi-select chips (Full face / Cheeks / Under-eye / Neck / Décolletage), Device/modality select (needling / Hydrafacial / Laser-IPL / peel), a Settings/depth input and a Consumables (non-S4) input (prototype skin-only block + applyChartType). Requirements: no lot, no prescription (Rx) and no stock deduction on finalise; persist to a SkinNote bound to the ChartEntry. The treatment-type toggle that shows/hides this lives in PRD-05/NOTE-TEMPLATE-TYPE-TOGGLE.
