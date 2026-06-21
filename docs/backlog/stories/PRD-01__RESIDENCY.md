# Data residency & sub-processor controls

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RESIDENCY`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/IAC`

## Background

As a compliance officer, I want assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment, so that we meet residency and cross-border obligations.
All PII/PHI storage + compute must resolve to Australia East; a sub-processor outside AU is blocked unless an APP-8 assessment + consent exists (C21/ADR-0016).

## How it works

All PII/PHI storage and compute resolve to Australia East; a sub-processor outside AU is blocked unless an APP-8 assessment + consent record exists. Sub-processor flows are kept in a register; signed-URL media enforces the same residency.
Enforced at the infra level (Sprint-0 IAC policy) and checked by integrations (PRD-10).

## Requirements

- Assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] All PII/PHI resources resolve to Australia East (verified, ties to Sprint 0 IAC policy).
- [ ] An integration to a non-AU sub-processor is blocked unless an APP-8 assessment + consent record exists.
- [ ] Sub-processor data flows are documented in a register.
- [ ] Signed-URL media access enforces the same residency.

## UI designs / screenshots

- Surfaces as a trust note ('your data stays in Australia') on client privacy screens and an admin sub-processor register in Settings.

## Suggested data model

- **SubProcessor** — id, tenant_id, name, region, app8_assessment_ref, consent_ref, status
  - _Non-AU blocked unless assessed + consented._

## Technical notes (high level)

- Architecture decisions: [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C21); blocked path explains why.
