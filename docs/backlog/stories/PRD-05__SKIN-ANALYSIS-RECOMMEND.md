# Skin analysis: recommended-plan chips feeding treatment plans

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/SKIN-ANALYSIS-RECOMMEND`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/SKIN-ANALYSIS`

## Background

As a dermal therapist / injector, I want below-threshold concerns to surface recommended-plan chips that jump to the matching treatment, so that a skin assessment turns into a structured plan rather than a number.
Plainly: this turns a skin assessment into next steps — the concerns that scored worst become tappable suggestions that jump straight to the matching treatment, so a low score becomes a booked plan. Where it fits: a follow-up to PRD-05/SKIN-ANALYSIS that adds the recommendation layer on top of the scored assessment, feeding the treatment-plan engine (PRD-05/TREATMENT-PLANS).

## How it works

This follow-up adds the recommendation layer on top of the scored assessment. Concerns scoring below a threshold (the prototype's 'score < 60') drive recommended-plan chips — tappable focus areas that jump to the matching treatment.
Each chip maps a low-scoring concern to a recommended_service_id; selecting it can seed a TreatmentPlan (PRD-05/TREATMENT-PLANS), so an assessment becomes structured ongoing care rather than a one-off number.
The recommendation reads the SkinZoneScore values the basic records.

## Requirements

- Below-threshold concerns to surface recommended-plan chips that jump to the matching treatment.

## Acceptance Criteria

- [ ] Concerns scoring below a threshold surface 'recommended plan — focus areas' chips.
- [ ] Each chip maps to a recommended service and jumps to the matching treatment.
- [ ] Selecting a chip can seed a treatment plan (PRD-05/TREATMENT-PLANS).
- [ ] The recommendation reads the assessment's zone scores (PRD-05/SKIN-ANALYSIS).

## UI designs / screenshots

- 'Recommended plan - focus areas (score < 60)' chips that jump to the matching treatment (feed TREATMENT-PLANS).
- Each chip maps a concern to a recommended service.
- Selecting a chip can seed a treatment plan.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **SkinZoneScore (extended)** — + recommended_service_id
  - _Extends the basic's SkinZoneScore: below-threshold concerns map to a recommended service that drives the chips (TREATMENT-PLANS)._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Recommended-plan chips from below-threshold concerns**
  Behaviour: below-threshold concerns surface 'recommended plan - focus areas' chips that map to a recommended service and jump to the matching treatment; selecting a chip can seed a TreatmentPlan (PRD-05/TREATMENT-PLANS). Requirements: read the assessment's SkinZoneScore values; the chip-to-service mapping is the recommended_service_id.
