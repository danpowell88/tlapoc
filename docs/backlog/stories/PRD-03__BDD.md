# BDD / psychological screening instrument

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/BDD`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a RN/NP, I want a BDD/psychological screen completed and surfaced before I proceed, so that I can avoid harm for at-risk patients per the guidelines.
Cosmetic guidelines require BDD screening; a positive result must be surfaced to the prescriber before treatment (C3).

## How it works

Cosmetic guidelines require screening for Body Dysmorphic Disorder / psychological wellbeing before non-surgical cosmetic procedures (C3, AHPRA 2 Sept 2025). A validated BDD/psychological instrument is embedded inside the intake wizard as a short set of wellbeing questions (how often the client thinks about the concern, whether it affects daily life/relationships, whether expectations are realistic).
The result is scored and stored as a ScreeningResult; a positive flag is surfaced to the prescriber and recorded. A completed screen authored/reviewed by an RN or NP must be present before treatment — it is one of the inputs the server-enforced gate (GATING) checks for an S4 treatment.
Which validated instrument to embed is an open clinical question (the prototype uses placeholder wellbeing questions) — the instrument is configurable so the clinically-chosen tool can be slotted in without rework.

## Requirements

- A BDD/psychological screen completed and surfaced before I proceed.
- Compliance: [C3](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A validated BDD/psychological screening instrument is embedded in intake.
- [ ] A completed screen authored/reviewed by an RN/NP is present before treatment.
- [ ] A positive flag is surfaced to the prescriber and recorded.
- [ ] Which instrument is used is configurable (open question to confirm).

## UI designs / screenshots

- Client app: the BDD/wellbeing screen within the intake wizard (client-app.png) — 'A few wellbeing questions', radio options (Rarely/Sometimes/A lot · No/A little/A lot · Realistic/Unsure).
- Staff: Charting pre-treatment review (charting.png) shows a 'BDD screen: clear' chip (or a flagged state) to the prescriber; Forms & consent (forms-consent.png) shows the screening within the 'Medical history & screening' template.
- Instrument is configurable (open question to confirm clinically).

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ScreeningResult** — id, tenant_id, client_id, appointment_id, instrument, instrument_version, answers(json), score, flag(bool), reviewed_by, reviewed_at
  - _Positive flag surfaced to prescriber; an RN/NP-reviewed result required before treatment (C3)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Configurable BDD/psychological instrument + scoring**
  Embed a validated screening instrument in intake as a configurable, versioned question set with a scoring rule that produces a score + boolean flag. Make the instrument swappable (instrument + instrument_version) so the clinically-chosen tool slots in without rework — v1 uses the prototype's placeholder wellbeing questions. Store the answers + score as a ScreeningResult linked to client + appointment.
- [ ] **Positive-flag surfacing + RN/NP review requirement**
  On a positive score, raise the flag and surface it to the prescriber (chip on the charting pre-treatment review + a follow-up signal). Record reviewed_by/reviewed_at when an RN/NP reviews the result; the GATING evaluation requires an RN/NP-reviewed ScreeningResult to exist before an S4 treatment (C3). Audited.
- [ ] **BDD screen in the intake wizard + prescriber chip UI**
  Render the wellbeing questions inside the client-app/kiosk intake wizard step. On the staff side, render the 'BDD screen: clear' / flagged chip on the Charting pre-treatment review and the screening status within the Forms & consent 'Medical history & screening' template.
