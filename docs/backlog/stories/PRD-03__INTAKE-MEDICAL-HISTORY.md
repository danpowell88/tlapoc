# Pre-visit intake: medical-history step & quick safety check

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/INTAKE-MEDICAL-HISTORY`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a client, I want to complete a medical-history step and get a quick safety check before my visit, so that my practitioner is alerted to any contraindication.
Plainly: the intake wizard's medical-history checkboxes (pregnancy, blood thinners, cold-sore history, allergies, etc.) and the 'quick safety check' summary that flags contraindications for the nurse. Where it fits: a follow-up to the pre-visit intake basic capture (PRD-03/INTAKE) that adds the medical-history step on top of the basic submission. The selections derive the contraindication flags the basic stores. It sits in Intake & Consent (PRD-03), rendered in both the client app and the reception check-in tablet.

## How it works

The basic story captures an intake response; this follow-up adds the structured medical-history step that produces the safety signal. It presents checkboxes for pregnancy/breastfeeding, blood thinners, cold-sore history, latex/lidocaine allergies and a 'None of the above' option.
The selections derive the contraindication_flags the basic IntakeResponse stores, and a 'quick safety check' summary follows the step, summarising for the nurse whether any contraindication was flagged.
The same step renders identically in the client app and at the reception check-in tablet, so the experience is consistent wherever intake is completed.

## Requirements

- To complete a medical-history step and get a quick safety check before my visit.

## Acceptance Criteria

- [ ] A medical-history step with checkboxes (pregnancy/breastfeeding, blood thinners, cold-sore history, latex/lidocaine allergies, 'None of the above').
- [ ] A 'quick safety check' summary follows the step.
- [ ] Selections derive contraindication_flags; the safety check summarises whether any contraindication was flagged for the nurse.
- [ ] Rendered identically in the client app and at the reception check-in tablet.

## UI designs / screenshots

- Client app / kiosk: the medical-history step (checkboxes incl. 'None of the above') → quick safety check summary (client-app.png / checkin.png).
- Selections derive contraindication_flags; the safety check summarises flags for the nurse.
- Rendered identically in the client app and the reception check-in tablet.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **IntakeResponse (extends INTAKE)** — answers(json) → contraindication_flags[]
  - _Medical-history selections derive the contraindication flags; the safety check summarises them for the nurse._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Medical-history step + quick safety check**
  Behaviour: the intake wizard's medical-history step (checkboxes incl. pregnancy/breastfeeding, blood thinners, cold-sore history, latex/lidocaine allergies, and 'None of the above') followed by a 'quick safety check' summary. Requirements: selections derive contraindication_flags; the safety check summarises whether any contraindication was flagged for the nurse; rendered identically in the client app and at the reception check-in tablet.
