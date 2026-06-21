# Versioned e-signed consent with mandated content

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/CONSENT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/INTAKE`

## Background

Intake, consent & compliance gating — Turns AHPRA's patient-safety rules into enforced workflow: pre-visit intake (medical history, contraindications, BDD/psychological screen), versioned e-signed consent with mandated content, separate withdrawable image-use consent, and cooling-off + payment blocks for under-18s.

As a client, I want to read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it, so that I give genuinely informed consent.

Consent must be versioned, e-signed, plain-language and contain mandated content (nature, risks/benefits/alternatives, practitioner qualifications, costs, realistic-outcome language, complaint mechanisms incl. AHPRA-despite-NDA) (C5).

## Requirements

- To read plain-language consent covering the procedure, risks, alternatives, the practitioner's qualifications and costs, and e-sign it.
- Traces to requirement(s): REQ-CONS-1.
- Must satisfy compliance obligation(s): C5, C18.

## Acceptance Criteria

- [ ] Consent is versioned, e-signed and contains all mandated content.
- [ ] Treatment is blocked until a current, version-matched consent is signed; the block states what's missing.
- [ ] Changing a template creates a new version; previously signed consents stay bound to their version.
- [ ] Consent versions are retained per the retention policy (C18).

## UI designs / screenshots

prototype.html — Forms & consent; client-app.html intake/consent; checkin.html.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-03/INTAKE.

## Other

Epic: PRD-03 — Intake, consent & compliance gating.
Source PRD: docs/prds/PRD-03-intake-consent-gating.md.
Backlog key: PRD-03/CONSENT.
Phase: 1 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C5, C18.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C5, C18); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
