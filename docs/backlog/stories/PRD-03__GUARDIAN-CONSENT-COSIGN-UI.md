# Under-18 guardian consent: co-sign step in the consent flow

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/GUARDIAN-CONSENT-COSIGN-UI`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/GUARDIAN-CONSENT`

## Background

As a RN/NP, I want a guardian co-sign step added to the consent reader for under-18 patients, so that a parent or guardian can co-sign in the same flow.
Plainly: adding a guardian co-sign step to the consent reader when the patient is under 18 — capturing the guardian's name, relationship and signature after the patient's acknowledgement. Where it fits: a follow-up to the under-18 guardian consent basic guardian co-signature (PRD-03/GUARDIAN-CONSENT) that adds the client-facing co-sign UI on top of the co-signature record. It appears only for the under-18 flow and reuses the consent reader (PRD-03/CONSENT-READER-UI). It sits in Intake & Consent (PRD-03).

## How it works

The basic story records the guardian co-signature; this follow-up adds the client-facing step that captures it. A guardian co-sign step is added to the consent reader when the patient is under 18.
After the patient's acknowledgement, the step captures the guardian's full name, relationship to the patient, and a type-to-sign signature, then submits the co-signature the basic story records.
The step appears only for the under-18 flow (adults are unaffected), and the under-18 status shows on the patient header with the recorded second-consultation on the timeline.

## Requirements

- A guardian co-sign step added to the consent reader for under-18 patients.

## Acceptance Criteria

- [ ] A guardian co-sign step is added to the consent reader when the patient is under 18.
- [ ] After the patient acknowledgement, it captures guardian full name, relationship to patient and a type-to-sign signature.
- [ ] The step appears only for the under-18 flow.
- [ ] The under-18 status shows on the patient header and the recorded second-consultation on the timeline.

## UI designs / screenshots

- Prototype: the under-18 flow adds a guardian co-sign step to the consent reader (forms-consent.png).
- Guardian step: capture guardian full name + relationship to patient + their type-to-sign signature, after the patient's acknowledgement.
- The step appears only for the under-18 flow; the patient header shows the under-18 status.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **GuardianConsent (reads GUARDIAN-CONSENT)** — captured via the co-sign step: guardian_name, guardian_relationship, signature_ref
  - _Client-facing step over the basic co-signature record; appears only for the under-18 flow._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Guardian co-sign step UI in the consent flow**
  Behaviour: add a guardian co-sign step to the consent reader when the patient is under 18. Requirements: after the patient acknowledgement, capture guardian full name, relationship to patient and a type-to-sign signature; the step appears only for the under-18 flow; show the under-18 status on the patient header and the recorded second-consultation on the timeline.
