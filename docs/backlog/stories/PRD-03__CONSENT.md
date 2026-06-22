# Versioned e-signed consent with mandated content

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/CONSENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a client, I want to read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it, so that I give genuinely informed consent.
Consent must be versioned, e-signed, plain-language and contain mandated content (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, complaint mechanisms incl. AHPRA-despite-NDA) (C5).

## How it works

Consent must be versioned, e-signed, plain-language, and contain the mandated content: procedure nature, risks/benefits/alternatives, the practitioner's qualifications, costs, realistic-outcome language and complaint mechanisms (including the right to AHPRA despite any NDA).
Treatment is blocked until a current, version-matched consent is signed; changing a template creates a new version and previously signed consents stay bound to the version they were signed against. Versions are retained per the retention policy.

## Requirements

- To read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it.
- Compliance: [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Consent is versioned, e-signed and contains all mandated content.
- [ ] Treatment is blocked until a current, version-matched consent is signed; the block states what's missing.
- [ ] Changing a template creates a new version; previously signed consents stay bound to their version.
- [ ] Consent versions are retained per the retention policy (C18).

## UI designs / screenshots

- Client app: plain-language consent reader + e-signature (client-app.png); staff see consent status in Forms & consent (forms-consent.png) and as a chip on the charting/patient header (charting.png).
- Mandated-content sections are explicit; the block states exactly what is missing.

![forms-consent — prototype screen](../screens/forms-consent.png)

## Suggested data model

- **ConsentTemplate** — id, tenant_id, treatment_type, version, content(sections), mandated_fields[]
  - _New version on change; old signatures stay bound._
- **ConsentSignature** — id, client_id, appointment_id, template_version, signed_at, signature_ref, verbal_confirmed
  - _Retained (C18); drives the treatment gate._

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - ConsentTemplate — id, tenant_id, treatment_type, version, content(sections), mandated_fields[] (New version on change; old signatures stay bound.)
  - ConsentSignature — id, client_id, appointment_id, template_version, signed_at, signature_ref, verbal_confirmed (Retained (C18); drives the treatment gate.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Consent is versioned, e-signed and contains all mandated content.
  - Rule: Treatment is blocked until a current, version-matched consent is signed; the block states what's missing.
  - Rule: Changing a template creates a new version; previously signed consents stay bound to their version.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-03/INTAKE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C5, C18 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Consent is versioned, e-signed and contains all mandated content.
  - Treatment is blocked until a current, version-matched consent is signed; the block states what's missing.
  - Changing a template creates a new version; previously signed consents stay bound to their version.
