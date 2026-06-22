# Under-18 guardian consent: recorded second consultation

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/GUARDIAN-CONSENT-SECOND-CONSULT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/GUARDIAN-CONSENT`

## Background

As a RN/NP, I want a second consultation recorded for an under-18 before treatment, so that a minor's treatment meets the additional review requirement.
Plainly: recording a second consultation for an under-18 — its date and the reviewing practitioner — before treatment. Where it fits: a follow-up to the under-18 guardian consent basic guardian co-signature (PRD-03/GUARDIAN-CONSENT) that adds the recorded second consultation alongside the guardian co-signature. It pairs with the 7-day cooling-off (PRD-03/COOLING-OFF) and is one of the inputs the treatment gate (PRD-03/GATING) checks for a minor. It sits in Intake & Consent (PRD-03).

## How it works

The basic story captures the guardian co-signature; this follow-up adds the second-consultation record that pairs with it for minors. A second consultation must be recorded for the under-18 before treatment.
Its date (occurred_at) and the reviewing practitioner (reviewed_by) are stored on a SecondConsultation linked to client + appointment and surfaced on the client timeline.
It pairs with the 7-day cooling-off (PRD-03/COOLING-OFF) — the recorded review that accompanies the mandatory wait — and is one of the inputs the treatment gate (PRD-03/GATING) checks for an under-18 patient. It is audited.

## Requirements

- A second consultation recorded for an under-18 before treatment.

## Acceptance Criteria

- [ ] A second consultation is recorded for the minor before treatment, with date and reviewing practitioner.
- [ ] It is stored on a SecondConsultation linked to client + appointment and surfaced on the client timeline.
- [ ] It pairs with the 7-day cooling-off (PRD-03/COOLING-OFF) and is one of the inputs the treatment gate checks for a minor.
- [ ] The recorded second consultation is audited.

## UI designs / screenshots

- A recorded second-consultation entry (date + reviewing practitioner) appears on the client timeline (forms-consent.png).
- It pairs with the under-18 cooling-off; the patient header shows the under-18 status.
- Audited; fed to GATING as an input for a minor.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **SecondConsultation** — id, tenant_id, client_id, appointment_id, occurred_at, reviewed_by
  - _Recorded review for a minor before treatment; shown on the client timeline; paired with the cooling-off (PRD-03/COOLING-OFF); feeds GATING._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Recorded second consultation for minors**
  Behaviour: record a second consultation for an under-18 before treatment. Requirements: store occurred_at + reviewed_by on a SecondConsultation linked to client + appointment; surface it on the client timeline; it pairs with the 7-day cooling-off (PRD-03/COOLING-OFF) and is one of the inputs the treatment gate checks for a minor; audited.
