# BDD screening: prescriber/staff screening chip UI

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/BDD-STAFF-CHIP`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/BDD`

## Background

As a RN/NP, I want the BDD screening outcome shown as a chip on the charting and forms screens, so that I can see a client's screening state at a glance.
Plainly: showing the BDD screening outcome to staff as a chip — 'BDD screen: clear' or a flagged state — on the charting pre-treatment review and within the Forms & consent template. Where it fits: a follow-up to the BDD screening basic instrument & scoring (PRD-03/BDD) that adds the staff-facing chip on top of the scored result. It is the at-a-glance read the prescriber makes before charting. It sits in Intake & Consent (PRD-03).

## How it works

The basic story scores the screen; this follow-up surfaces that outcome to staff. A 'BDD screen: clear' or flagged chip renders on the Charting pre-treatment review.
The screening status also shows within the Forms & consent 'Medical history & screening' template, so staff can see it from both the clinical and the forms surfaces.
The flagged state is rendered unmistakably so the prescriber can never miss a positive screen before charting.

## Requirements

- The BDD screening outcome shown as a chip on the charting and forms screens.

## Acceptance Criteria

- [ ] A 'BDD screen: clear' or flagged chip renders on the Charting pre-treatment review.
- [ ] The screening status shows within the Forms & consent 'Medical history & screening' template.
- [ ] The flagged state is unmistakable to the prescriber.

## UI designs / screenshots

- Staff: a 'BDD screen: clear' or flagged chip on the Charting pre-treatment review (charting.png).
- The screening status within the Forms & consent 'Medical history & screening' template (forms-consent.png).
- The flagged state is unmistakable to the prescriber.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **(reads BDD)** — no new entities; renders ScreeningResult.flag as a chip
  - _Presentation of the scored result on the charting and forms surfaces._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Prescriber/staff screening chip UI**
  Behaviour: show the screening outcome to staff. Requirements: render a 'BDD screen: clear' or flagged chip on the Charting pre-treatment review, and the screening status within the Forms & consent 'Medical history & screening' template; the flagged state is unmistakable to the prescriber.
