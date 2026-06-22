# Consent: plain-language reader & type-to-sign

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/CONSENT-READER-UI`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-03/CONSENT`

## Background

As a client, I want to read the plain-language consent and type my name to sign it, so that I give genuinely informed consent before treatment.
Plainly: the client-app/kiosk consent step — a scrollable plain-language reader of the mandated content with an acknowledgement and a type-your-full-name-to-sign field. Where it fits: a follow-up to the versioned e-signed consent basic signature capture (PRD-03/CONSENT) that adds the client-facing reader on top of the signature endpoint. It renders the exact template_version being signed and submits to the basic's e-signature endpoint. It sits in Intake & Consent (PRD-03), in the client app and the reception check-in tablet.

## How it works

The basic story records the binding signature; this follow-up adds the client-facing reading-and-signing experience. A scrollable plain-language reader presents the mandated content — the nature of the procedure, risks/benefits/alternatives, the practitioner's qualifications, costs, realistic-outcome language, and the explicit right to complain to AHPRA despite any NDA.
An 'I've read and understood' acknowledgement and a type-your-full-name-to-sign field complete the step, which renders the exact template_version being signed so the reader and the binding signature always match.
The same flow runs in the client app and at the reception check-in tablet, and submitting calls the basic's e-signature endpoint.

## Requirements

- To read the plain-language consent and type my name to sign it.
- Compliance: [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A scrollable plain-language reader presents the mandated content (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, AHPRA-despite-NDA complaint line).
- [ ] An 'I've read and understood' acknowledgement and a type-your-full-name-to-sign field.
- [ ] It renders the exact template_version being signed; submitting calls the e-signature endpoint.
- [ ] The same flow runs in the client app and at the reception check-in tablet.

## UI designs / screenshots

- Client app: plain-language consent reader + e-signature within the intake wizard (client-app.png) — risk/benefit/alternative/cost text, 'I've read and understood…', 'Type your full name to sign'; includes the AHPRA-despite-NDA complaint line.
- Renders the exact template_version being signed; the same flow runs in the client app and the reception check-in tablet.
- Submitting calls the e-signature endpoint.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **(reads CONSENT)** — renders ConsentTemplate.content(sections) for the exact template_version; submits a ConsentSignature
  - _Presentation over the basic signature endpoint; same flow in client app and kiosk._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Plain-language consent reader + type-to-sign (client/kiosk)**
  Behaviour: the client-app/kiosk consent step — a scrollable plain-language reader of the mandated content (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, AHPRA-despite-NDA complaint line), an 'I've read and understood' acknowledgement, and a type-your-full-name-to-sign field. Requirements: renders the exact template_version being signed; the same flow runs in the client app and at the reception check-in tablet; submitting calls the e-signature endpoint.
