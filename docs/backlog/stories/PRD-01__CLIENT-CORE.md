# Client core record: DOB & under-18 flag

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CLIENT-CORE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/TENANT`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a system, I want to capture client DOB and derive an under-18 flag, so that downstream cooling-off and pricing rules can enforce age-based requirements.

The client record captures DOB and derives an under-18 flag that feeds cooling-off (C6) and advertising/pricing (C9) elsewhere.

## Requirements

- To capture client DOB and derive an under-18 flag.
- Traces to requirement(s): REQ-CLI-3.

## Acceptance Criteria

- [ ] DOB captured; under-18 flag derived and exposed to PRD-03/PRD-06/PRD-07.
- [ ] The flag updates correctly across a birthday.
- [ ] Soft-delete with audit and duplicate handling supported (full CRM in PRD-02).
- [ ] Under-18 status is visible on the patient header (consumed by UX age chip).

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-01/TENANT.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/CLIENT-CORE.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C6.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
