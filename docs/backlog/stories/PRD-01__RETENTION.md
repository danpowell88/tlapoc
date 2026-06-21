# Retention policy engine & destruction register

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RETENTION`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/AUDIT`

## Background

As a admin, I want retention timers and a destruction register that surfaces records due for destruction and logs their destruction, so that we keep records exactly as long as the law requires, no more, no less.
Records must be retained per legal periods (adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation) and destroyed with a register + certificate (C18).

## How it works

A retention engine keeps records exactly as long as the law requires: adults >=7y from last contact, minors to age 25, indefinite where a complaint/litigation flag is set. Records past their period surface for destruction; destroying one writes a register entry (patient, period, date) + certificate reference.
A transfer log records records handed to another provider.

## Requirements

- Retention timers and a destruction register that surfaces records due for destruction and logs their destruction.
- Compliance: [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Retention rules: adults ≥7y from last contact; minors to age 25; indefinite on complaint/litigation.
- [ ] Records past retention surface for destruction with their retention basis.
- [ ] Destroying a record writes a destruction-register entry (patient, period, date) + certificate reference.
- [ ] A transfer log records records handed to another provider.

## UI designs / screenshots

- Surfaces in Governance: a 'records due for destruction' list (with retention basis) and the destruction register + certificates.

## Suggested data model

- **RetentionPolicy** — id, tenant_id, record_type, basis(adult7y|minor25|indefinite_on_flag), period
- **DestructionRecord** — id, tenant_id, record_ref, patient, period, destroyed_at, certificate_ref
  - _Immutable + audited._
- **TransferLog** — id, record_ref, to_provider, at

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C18); blocked path explains why.
