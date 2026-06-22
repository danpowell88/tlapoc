# Consent: status chip & blocked-action banner

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/CONSENT-STATUS-CHIP`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/CONSENT`

## Background

As a RN/NP, I want consent state shown as a chip and a banner that names what's missing, so that I can see at a glance whether consent is current before charting.
Plainly: surfacing consent state to staff — a 'Consent ✓' or version-mismatch chip on the patient/charting header, and a blocked-action banner that names exactly what's missing and links the fix. Where it fits: a follow-up to the versioned e-signed consent basic signature capture (PRD-03/CONSENT) that adds the staff-facing status surface on top of the signature. It is driven by the treatment gate and reuses the shared GATING banner (PRD-03/GATING). It sits in Intake & Consent (PRD-03).

## How it works

The basic story records the signature; this follow-up surfaces its state to staff. A 'Consent ✓' or version-mismatch chip renders on the patient/charting header, driven by the treatment gate.
When consent is missing or superseded, the blocked-action banner names exactly what is missing and links the fix (send consent link), so the path forward is always clear.
It reuses the shared GATING banner (PRD-03/GATING) rather than re-implementing one, keeping the blocked-action experience consistent across the gates.

## Requirements

- Consent state shown as a chip and a banner that names what's missing.
- Compliance: [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A 'Consent ✓' or version-mismatch chip renders on the patient/charting header, driven by the gate.
- [ ] When consent is missing or superseded the blocked-action banner names exactly what is missing and links the fix (send consent link).
- [ ] It reuses the shared GATING banner.

## UI designs / screenshots

- Staff: a 'Consent ✓' or version-mismatch chip on the patient / charting header (charting.png).
- When consent is missing/superseded the blocked-action banner names what's missing and links the fix (send consent link).
- Reuses the shared GATING banner.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **(reads CONSENT + GATING)** — no new entities; renders the gate's consent state as a chip + banner
  - _Driven by the treatment gate; reuses the shared GATING blocked-action banner._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Consent status chip + blocked-action banner**
  Behaviour: surface consent state to staff. Requirements: render a 'Consent ✓' or version-mismatch chip on the patient / charting header driven by the gate; when consent is missing or superseded the blocked-action banner names exactly what is missing and links the fix (send consent link); reuses the shared GATING banner.
