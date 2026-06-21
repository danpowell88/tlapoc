# Data residency & sub-processor controls

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RESIDENCY`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/IAC`

## Background

As a compliance officer, I want assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment, so that we meet residency and cross-border obligations.
All PII/PHI storage + compute must resolve to Australia East; a sub-processor outside AU is blocked unless an APP-8 assessment + consent exists (C21/ADR-0016).

## Requirements

- Assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] All PII/PHI resources resolve to Australia East (verified, ties to Sprint 0 IAC policy).
- [ ] An integration to a non-AU sub-processor is blocked unless an APP-8 assessment + consent record exists.
- [ ] Sub-processor data flows are documented in a register.
- [ ] Signed-URL media access enforces the same residency.

## Technical notes (high level)

- Stack: Azure / CI-CD / IaC
- Architecture decisions: [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C21); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
