# BDD screening: positive-flag surfacing & RN/NP review requirement

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/BDD-REVIEW-GATE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/BDD`

## Background

As a RN/NP, I want a positive BDD screen surfaced to me and required to be reviewed before treatment, so that an at-risk patient is never treated without clinical review.
Plainly: surfacing a positive BDD/psychological screen to the prescriber and requiring an RN/NP (registered nurse / nurse practitioner) to review it before treatment. Where it fits: a follow-up to the BDD screening basic instrument & scoring (PRD-03/BDD) that adds the flag-and-review obligation on top of the scored result. The RN/NP-reviewed result is one of the inputs the treatment gate (PRD-03/GATING) checks for an S4 treatment (C3). It sits in Intake & Consent (PRD-03).

## How it works

The basic story scores and stores the screen; this follow-up adds the safety obligation it exists for. A positive score raises a flag the prescriber sees (a chip on the charting pre-treatment review plus a follow-up signal).
An RN/NP (registered nurse / nurse practitioner) must review the result before treatment, with reviewed_by/reviewed_at recorded on review.
The GATING evaluation requires an RN/NP-reviewed ScreeningResult before an S4 (Schedule 4 prescription-only medicine) treatment (C3, AHPRA guidance), so an at-risk patient can't be treated without clinical review. The flag and review are audited.

## Requirements

- A positive BDD screen surfaced to me and required to be reviewed before treatment.
- Compliance: [C3](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A positive score raises a flag the prescriber sees.
- [ ] An RN/NP must review the result before treatment; reviewed_by/reviewed_at are recorded.
- [ ] The GATING evaluation requires an RN/NP-reviewed ScreeningResult before an S4 treatment (C3).
- [ ] The flag and review are audited.

## UI designs / screenshots

- Staff: Charting pre-treatment review (charting.png) shows a 'BDD screen: clear' chip or a flagged state to the prescriber.
- A positive flag requires RN/NP review (reviewed_by/reviewed_at) before treatment.
- The flagged state is unmistakable; the review feeds the GATING evaluation (C3).

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ScreeningResult (extends BDD)** — flag(bool), reviewed_by, reviewed_at
  - _Positive flag surfaced to prescriber; an RN/NP-reviewed result required before an S4 treatment (C3); feeds GATING; audited._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Positive-flag surfacing + RN/NP review requirement**
  Behaviour: a positive score raises a flag the prescriber sees, and an RN/NP must review the result before treatment. Requirements: surface the flag to the prescriber (chip on the charting pre-treatment review + a follow-up signal); record reviewed_by/reviewed_at on review; the GATING evaluation requires an RN/NP-reviewed ScreeningResult before an S4 (Schedule 4 prescription-only medicine) treatment (C3); audited.
