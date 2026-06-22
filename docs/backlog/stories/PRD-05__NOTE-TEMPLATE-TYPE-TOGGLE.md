# Charting: treatment-type toggle (toxin / non-S4 skin)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/NOTE-TEMPLATE-TYPE-TOGGLE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a injector, I want a toggle that switches charting between the toxin note and the non-S4 skin note, so that I chart the right kind of treatment with the right fields and gates.
Plainly: a switch at the top of charting that flips the note between an anti-wrinkle (toxin) treatment and a non-S4 (not Schedule 4 prescription-only medicine) skin treatment, showing the right fields for each. Where it fits: a follow-up to PRD-05/NOTE-TEMPLATE that adds the modality switch on top of the basic toxin note. The toxin path requires the product/lot and prescription steps; the non-S4 skin path requires neither, and its actual fields are built in PRD-05/MAPPING's skin-note task — this story owns the toggle that shows/hides each.

## How it works

This follow-up adds the modality switch on top of the basic toxin note. A treatment-type toggle (Anti-wrinkle (toxin) / Skin treatment) selects which template renders and shows or hides the toxin-only map + lot steps versus the non-S4 skin note (prototype setChartType/applyChartType).
Switching swaps the rendered fields and the pre-treatment chips: the toxin path requires product/lot and an individual prescription (the S4 gate); the non-S4 skin path has neither consult nor lot requirement, so the gate chips change accordingly.
The toggle sets ChartEntry.treatment_type (toxin | skin). The skin-note fields themselves (areas / device / settings / consumables) are built in PRD-05/MAPPING's skin-note variant task; this story owns only the toggle and the show/hide wiring.

## Requirements

- A toggle that switches charting between the toxin note and the non-S4 skin note.

## Acceptance Criteria

- [ ] A treatment-type toggle (Anti-wrinkle (toxin) / Skin treatment) selects which template renders and shows/hides the toxin-only map + lot steps vs the non-S4 skin note.
- [ ] Switching swaps the rendered fields and the pre-treatment chips: skin has no consult/prescription requirement; the toxin path requires product/lot and prescription, the non-S4 skin path has neither.
- [ ] The toggle sets ChartEntry.treatment_type accordingly.
- [ ] The skin-note fields themselves are owned by PRD-05/MAPPING's skin-note task; this story owns the show/hide toggle.

## UI designs / screenshots

- Treatment-type toggle pills: 'Anti-wrinkle (toxin)' (default) / 'Skin treatment' (setChartType/applyChartType swap the template).
- Selecting 'Skin treatment' hides the toxin map + lot steps and the prescription gate chips; selecting 'Anti-wrinkle (toxin)' restores them.
- The pre-treatment chips re-render to match the selected type.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry (referenced)** — treatment_type (toxin|skin) set by the toggle
  - _Extends the basic's ChartEntry — no new entity; the toggle drives treatment_type and the shown/hidden steps._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Treatment-type toggle + show/hide wiring**
  Behaviour: a toggle (Anti-wrinkle (toxin) / Skin treatment) selects which template renders and shows/hides the toxin-only map+lot steps vs the non-S4 skin note (prototype setChartType/applyChartType). Requirements: switching swaps the rendered fields and the pre-treatment chips (skin has no consult/prescription requirement) and sets ChartEntry.treatment_type; the skin-note fields themselves are built in PRD-05/MAPPING's skin-note task.
