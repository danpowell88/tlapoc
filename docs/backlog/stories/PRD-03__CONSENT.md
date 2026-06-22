# Versioned e-signed consent with mandated content

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/CONSENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a client, I want to read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it, so that I give genuinely informed consent.
Versioned e-signed consent is the heart of Intake & Consent (PRD-03): the legally informed agreement a client must give before treatment. It sits after intake (PRD-03/INTAKE) and feeds the treatment gate (PRD-03/GATING), which blocks treatment until a current, version-matched consent is signed. In the flow it is what stands between booking (PRD-02) and the clinical work in the consult (PRD-04) and charting (PRD-05); it also seeds the separate image-use consent (PRD-03/IMAGE-CONSENT) and the under-18 cooling-off timer (PRD-03/COOLING-OFF), whose clock starts from the consent timestamp.  Consent must be versioned, e-signed, plain-language and contain mandated content (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, complaint mechanisms incl. AHPRA-despite-NDA) (C5).

## How it works

Treatment consent must be versioned, e-signed, plain-language and contain the AHPRA-mandated content: the nature of the procedure, risks/benefits/alternatives, the practitioner's qualifications, costs, realistic-outcome language (no minimising/overstating), and complaint mechanisms — including the explicit right to complain to AHPRA despite any NDA. The prototype consent text models exactly this for anti-wrinkle treatment.
Each ConsentTemplate is per-treatment-type and versioned. Changing a template creates a NEW version; previously signed consents stay bound to the version they were signed against (a ConsentSignature references template_version, not the live template). Treatment is blocked until a current, version-matched consent is e-signed for the treatment type; the block states exactly what is missing (GATING).
Capture is verbal + written: the client reads the plain-language reader and e-signs (types their full name); a verbal_confirmed flag records the practitioner's confirmation. Signed consents and templates are retained per the retention policy (C18, PRD-01 RETENTION).

## Requirements

- To read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it.
- Compliance: [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Consent is versioned, e-signed and contains all mandated content.
- [ ] Treatment is blocked until a current, version-matched consent is signed; the block states what's missing.
- [ ] Changing a template creates a new version; previously signed consents stay bound to their version.
- [ ] Consent versions are retained per the retention policy (C18).

## UI designs / screenshots

- Client app: plain-language consent reader + e-signature within the intake wizard (client-app.png) — risk/benefit/alternative/cost text, 'I've read and understood…', and 'Type your full name to sign'; includes the AHPRA-despite-NDA complaint line.
- Staff: Forms & consent (forms-consent.png) lists consent templates with version + status (e.g. 'Anti-wrinkle consent v3.2 · Current'; 'Under-18 consent (+ guardian) v1.0 · 7-day cool-off'); the patient header / charting (charting.png) shows a 'Consent ✓' chip.
- Mandated-content sections are explicit; the block states exactly what is missing.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ConsentTemplate** — id, tenant_id, treatment_type, version, content(sections), mandated_fields[], status(current|superseded)
  - _New version on change; old signatures stay bound to their version (immutable content per version)._
- **ConsentSignature** — id, tenant_id, client_id, appointment_id, template_id, template_version, signed_at, signature_ref, verbal_confirmed
  - _References the version signed; retained (C18); drives the treatment gate (GATING)._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **E-signature capture bound to template_version (+ verbal)**
  Behaviour: an endpoint that records a client's e-signature against the exact consent version they read. Requirements: create a ConsentSignature referencing the EXACT template_version, with signature_ref (typed full name / signature), signed_at and a verbal_confirmed flag (practitioner confirmation); a later template change does NOT invalidate or rebind an existing signature; retained per C18 (PRD-01 RETENTION); audited; feeds the GATING evaluation (current, version-matched).
- [ ] **Plain-language consent reader + type-to-sign (client/kiosk)**
  Behaviour: the client-app/kiosk consent step — a scrollable plain-language reader of the mandated content (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, AHPRA-despite-NDA complaint line), an 'I've read and understood' acknowledgement, and a type-your-full-name-to-sign field. Requirements: renders the exact template_version being signed; the same flow runs in the client app and at the reception check-in tablet; submitting calls the e-signature endpoint.
- [ ] **Consent status chip + blocked-action banner**
  Behaviour: surface consent state to staff. Requirements: render a 'Consent ✓' or version-mismatch chip on the patient / charting header driven by the gate; when consent is missing or superseded the blocked-action banner names exactly what is missing and links the fix (send consent link); reuses the shared GATING banner.
