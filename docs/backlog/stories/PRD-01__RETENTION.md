# Retention policy engine & destruction register

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RETENTION`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`

## Background

As a admin, I want retention timers and a destruction register that surfaces records due for destruction and logs their destruction, so that we keep records exactly as long as the law requires, no more, no less.
Records must be retained per legal periods (adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation) and destroyed with a register + certificate (C18).

## Requirements

- Retention timers and a destruction register that surfaces records due for destruction and logs their destruction.
- Compliance: [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Retention rules: adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation.
- [ ] Records past retention surface for destruction with their retention basis.
- [ ] Destroying a record writes a destruction-register entry (patient, period, date) + certificate reference.
- [ ] A transfer log records records handed to another provider.

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C18); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
