# MFA & step-up authentication for sensitive actions

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/MFA-STEPUP`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/SIGNIN-UI`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a security-conscious clinic, I want MFA for staff and step-up re-authentication on the most sensitive actions, so that high-risk operations can't be performed on a walk-up or hijacked session.

Staff MFA is required; sensitive clinical/medicines/financial actions (e.g. prescribing, S4 custody changes, destruction, data export) may require step-up re-auth. Client MFA policy is an open question.

## Requirements

- MFA for staff and step-up re-authentication on the most sensitive actions.
- Traces to requirement(s): REQ-TEN-2, REQ-SEC-1.
- Must satisfy compliance obligation(s): C10.

## Acceptance Criteria

- [ ] Staff sign-in enforces MFA (via Entra).
- [ ] Configured sensitive actions require a recent/step-up auth or are blocked with a clear prompt.
- [ ] Step-up events are audited.
- [ ] Client MFA policy (optional vs required for sensitive actions) is configurable (open question resolved per clinic).

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0004 (see docs/adr/decision-log.md).
Depends on: PRD-01/SIGNIN-UI.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/MFA-STEPUP.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C10.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C10); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
