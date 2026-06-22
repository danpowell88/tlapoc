# Under-18 guardian consent & recorded second consultation

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/GUARDIAN-CONSENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/COOLING-OFF`, `PRD-03/CONSENT`

## Background

As a RN/NP, I want a guardian to co-sign consent for an under-18 and a second consultation to be recorded, so that a minor's treatment meets the additional consent and review requirements before it can proceed.
Plainly: the extra consent steps required when the patient is under 18 — a parent or guardian must co-sign, and a second consultation must be recorded — on top of the standard consent. Where it fits: a sibling of cooling-off (PRD-03/COOLING-OFF) inside Intake & Consent (PRD-03). COOLING-OFF owns the 7-day timer and the payment block; this story owns the additional consent artefacts for minors: the guardian co-signature against the dedicated 'Under-18 consent (+ guardian)' template and the recorded second consultation. It uses the same versioned-consent mechanism as PRD-03/CONSENT and the under-18 flag set at booking (PRD-02), and it feeds the treatment gate (PRD-03/GATING) so a minor cannot be treated until these exist.

## How it works

When the patient is under 18 (flag set at booking, PRD-02), standard consent is not enough: consent must be taken against the dedicated 'Under-18 consent (+ guardian)' template and co-signed by a parent or guardian. The guardian's name and relationship to the patient are captured and the co-signature binds to the exact template version, exactly like an adult signature (reuses PRD-03/CONSENT).
A second consultation must be recorded for the minor before treatment — its date and the reviewing practitioner are stored on the client timeline (this is the recorded review that pairs with the 7-day cooling-off enforced in PRD-03/COOLING-OFF).
The presence of a valid guardian-co-signed under-18 consent AND a recorded second consultation are inputs the treatment gate (PRD-03/GATING) checks for an under-18 patient, alongside the elapsed cooling-off. Adults are unaffected.

## Requirements

- A guardian to co-sign consent for an under-18 and a second consultation to be recorded.

## Acceptance Criteria

- [ ] An under-18 booking requires consent against the dedicated under-18 (+ guardian) template, co-signed by a parent/guardian.
- [ ] The guardian's identity/relationship is captured and the co-signature is bound to the template version (like any consent).
- [ ] A second consultation is recorded for the minor before treatment, with date and reviewing practitioner.
- [ ] The under-18 consent + recorded second consultation are inputs the treatment gate checks for a minor (with cooling-off from PRD-03/COOLING-OFF).

## UI designs / screenshots

- Prototype: Forms & consent (forms-consent.png) — 'Under-18 consent (+ guardian) v1.0 · 7-day cool-off' template; the under-18 flow adds a guardian co-sign step to the consent reader.
- Guardian step: capture guardian full name + relationship to patient + their type-to-sign signature, after the patient's acknowledgement.
- A recorded second-consultation entry (date + reviewing practitioner) appears on the client timeline; the patient header shows the under-18 status.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **GuardianConsent** — id, tenant_id, client_id, appointment_id, template_id, template_version, guardian_name, guardian_relationship, signed_at, signature_ref
  - _Co-signature on the under-18 (+ guardian) template; binds to template_version like any consent; required for an under-18 treatment (feeds GATING)._
- **SecondConsultation** — id, tenant_id, client_id, appointment_id, occurred_at, reviewed_by
  - _Recorded review for a minor before treatment; shown on the client timeline; paired with the cooling-off (PRD-03/COOLING-OFF)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Guardian co-signature bound to the under-18 template version**
  Behaviour: capture a parent/guardian co-signature for an under-18, against the dedicated under-18 (+ guardian) consent template. Requirements: capture guardian_name + guardian_relationship + signature_ref, signed_at; bind to the EXACT template_version (reuses PRD-03/CONSENT versioning); required for an under-18 patient and fed to GATING; retained (C18) and audited.
- [ ] **Recorded second consultation for minors**
  Behaviour: record a second consultation for an under-18 before treatment. Requirements: store occurred_at + reviewed_by on a SecondConsultation linked to client + appointment; surface it on the client timeline; it pairs with the 7-day cooling-off (PRD-03/COOLING-OFF) and is one of the inputs the treatment gate checks for a minor; audited.
- [ ] **Guardian co-sign step UI in the consent flow**
  Behaviour: add a guardian co-sign step to the consent reader when the patient is under 18. Requirements: after the patient acknowledgement, capture guardian full name, relationship to patient and a type-to-sign signature; the step appears only for the under-18 flow; show the under-18 status on the patient header and the recorded second-consultation on the timeline.
