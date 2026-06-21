# Staff credentials + canInject compliance gate

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CREDENTIALS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

As a owner, I want structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject, so that only registered, insured, in-scope staff can be booked and can treat.
Staff profiles hold AHPRA reg #, type, status/expiry, conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII; these derive a single canInject gate. Must accept the new designated RN prescriber role.

## Requirements

- Structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C19](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Profiles capture AHPRA reg/type/status/expiry/conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII.
- [ ] A practitioner whose PII excludes cosmetic, or whose registration has lapsed, is flagged not-cleared.
- [ ] The designated RN prescriber role is supported (endorsement + recorded partnered prescriber).
- [ ] canInject is a single derived signal consumed by booking (PRD-02) and treatment gates.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0028](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0029](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C19); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
