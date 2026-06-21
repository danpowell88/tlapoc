# Retention policy engine & destruction register

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RETENTION`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a admin, I want retention timers and a destruction register that surfaces records due for destruction and logs their destruction, so that we keep records exactly as long as the law requires, no more, no less.

Records must be retained per legal periods (adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation) and destroyed with a register + certificate (C18).

## Requirements

- Retention timers and a destruction register that surfaces records due for destruction and logs their destruction.
- Traces to requirement(s): REQ-SEC-4.
- Must satisfy compliance obligation(s): C18.

## Acceptance Criteria

- [ ] Retention rules: adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation.
- [ ] Records past retention surface for destruction with their retention basis.
- [ ] Destroying a record writes a destruction-register entry (patient, period, date) + certificate reference.
- [ ] A transfer log records records handed to another provider.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-01/AUDIT.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/RETENTION.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C18.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C18); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
