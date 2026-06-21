# Versioned e-signed consent with mandated content

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/CONSENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/INTAKE`

## Background

As a client, I want to read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it, so that I give genuinely informed consent.
Consent must be versioned, e-signed, plain-language and contain mandated content (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, complaint mechanisms incl. AHPRA-despite-NDA) (C5).

## Requirements

- To read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it.
- Compliance: [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Consent is versioned, e-signed and contains all mandated content.
- [ ] Treatment is blocked until a current, version-matched consent is signed; the block states what's missing.
- [ ] Changing a template creates a new version; previously signed consents stay bound to their version.
- [ ] Consent versions are retained per the retention policy (C18).

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C5, C18); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
