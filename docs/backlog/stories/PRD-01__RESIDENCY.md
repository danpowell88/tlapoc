# Data residency & sub-processor controls

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RESIDENCY`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/IAC`

## Background

As a compliance officer, I want assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment, so that we meet residency and cross-border obligations.
Plainly: this guarantees the clinic's personal and health data stays in Australia and never flows to an overseas supplier without a proper cross-border assessment and consent. It is a Foundations story built on the Sprint 0 infrastructure policy. It is the check the later integrations epic calls before any data leaves to a third party, and the trust note clients see — the clinic's assurance that data stays in-country. All PII/PHI (personal and personal-health information) storage + compute must resolve to Australia East; a sub-processor outside AU is blocked unless an APP-8 (Australian Privacy Principle 8, governing cross-border disclosure) assessment + consent exists (C21/ADR-0016).

## How it works

All PII/PHI storage and compute must resolve to Azure Australia East (ADR-0001/0016, C10/C21, REQ-SEC-1/2/6). This is enforced primarily at the infra level by the Sprint-0 IaC policy (region pinning + policy guardrails that fail a deploy outside AU East) — the application story is the runtime + integration controls that sit on top, plus the human-facing evidence.
A sub-processor outside Australia (payment, SMS, accounting, any integration handling PII) is blocked unless an APP-8 cross-border assessment + client consent record exists (AC8). Integrations (PRD-10) check the sub-processor's region/assessment status before any PII leaves; an AU-resident processor passes, a non-AU one without an assessment+consent is refused with a clear reason. The sub-processor register documents every data flow (who, region, what data, assessment + consent references) so the clinic can evidence its cross-border posture.
Signed-URL media access (clinical photos, credential evidence, data exports — ADR-0009) enforces the same residency: blobs live in AU-resident storage and are reached only via short-lived signed URLs, never copied to a non-AU location or retained on devices.
Surfaces to clients as the 'your data stays in Australia' trust note (client app privacy) and to staff as the sub-processor register in Settings. The register is the artefact an auditor asks for under APP 8 (Australian Privacy Principle 8, governing cross-border disclosure).

## Requirements

- Assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] All PII/PHI resources resolve to Australia East (verified, ties to Sprint 0 IAC policy).
- [ ] An integration to a non-AU sub-processor is blocked unless an APP-8 assessment + consent record exists.
- [ ] Sub-processor data flows are documented in a register.
- [ ] Signed-URL media access enforces the same residency.

## UI designs / screenshots

- Surfaces as a client-facing trust note ('Your data is stored securely in Australia') on the client app privacy screen, and an admin sub-processor register in Settings listing each integration with its region, data categories, APP-8 assessment reference and consent reference.
- A blocked non-AU integration shows a clear reason (no APP-8 assessment + consent) rather than silently failing.

## Suggested data model

- **SubProcessor** — id, tenant_id, name, purpose, region, data_categories, app8_assessment_ref, consent_ref, status(active|blocked)
  - _Non-AU is blocked unless app8_assessment_ref AND consent_ref are present; the register documents every cross-border flow._

## Technical notes (high level)

- Architecture decisions: [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Residency verification + APP-8 sub-processor gate**
  Verify (and assert at runtime, tying to the Sprint-0 IaC region policy) that PII/PHI (personal and personal-health information) storage + compute resolve to Australia East. Model SubProcessor (region, purpose, data categories, app8_assessment_ref, consent_ref, status) and enforce the gate: any integration sending PII to a non-AU sub-processor is blocked unless an APP-8 (Australian Privacy Principle 8, governing cross-border disclosure) assessment AND a consent record both exist, returning a clear reason. This is the check PRD-10 integrations call before any PII leaves.
- [ ] **Signed-URL media residency enforcement**
  Ensure clinical photos, credential evidence and data exports live in AU-resident storage and are accessed only via short-lived signed URLs (ADR-0009), gated by role + consent, never copied to a non-AU location or persisted on devices. Apply the same residency rule to export deliveries (PRIVACY-RIGHTS).
- [ ] **Sub-processor register UI (Settings) + client trust note**
  Build the admin sub-processor register in Settings: a row per integration with region, data categories, APP-8 (Australian Privacy Principle 8, governing cross-border disclosure) assessment reference, consent reference and active/blocked status, with the block reason visible. Surface the client-facing 'your data stays in Australia' trust note on the client app privacy screen. Capability-gate the register to owner/configure.
