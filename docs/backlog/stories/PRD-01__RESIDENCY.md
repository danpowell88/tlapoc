# Data residency & sub-processor controls

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RESIDENCY`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** infra
>
> **Depends on:** `SPRINT-0/IAC`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a compliance officer, I want assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment, so that we meet residency and cross-border obligations.

All PII/PHI storage + compute must resolve to Australia East; a sub-processor outside AU is blocked unless an APP-8 assessment + consent exists (C21/ADR-0016).

## Requirements

- Assurance and enforcement that PII/PHI stays in Australia and never flows to a non-AU sub-processor without an APP-8 assessment.
- Traces to requirement(s): REQ-SEC-1, REQ-SEC-2, REQ-SEC-6.
- Must satisfy compliance obligation(s): C21.

## Acceptance Criteria

- [ ] All PII/PHI resources resolve to Australia East (verified, ties to Sprint 0 IAC policy).
- [ ] An integration to a non-AU sub-processor is blocked unless an APP-8 assessment + consent record exists.
- [ ] Sub-processor data flows are documented in a register.
- [ ] Signed-URL media access enforces the same residency.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: Azure / CI-CD / IaC.
Architecture decisions: ADR-0016 (see docs/adr/decision-log.md).
Depends on: SPRINT-0/IAC.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/RESIDENCY.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C21.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C21); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
