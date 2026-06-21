# Staff credentials + canInject compliance gate

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CREDENTIALS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a owner, I want structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject, so that only registered, insured, in-scope staff can be booked and can treat.

Staff profiles hold AHPRA reg #, type, status/expiry, conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII; these derive a single canInject gate. Must accept the new designated RN prescriber role.

## Requirements

- Structured credential + CPD + cosmetic-cover-insurance records that derive whether each practitioner is cleared to treat/inject.
- Traces to requirement(s): REQ-TEN-6, REQ-TEN-7, REQ-TEN-8, REQ-TEN-9.
- Must satisfy compliance obligation(s): C4, C19.

## Acceptance Criteria

- [ ] Profiles capture AHPRA reg/type/status/expiry/conditions, ≥1yr-experience flag, CPD and cosmetic-cover PII.
- [ ] A practitioner whose PII excludes cosmetic, or whose registration has lapsed, is flagged not-cleared.
- [ ] The designated RN prescriber role is supported (endorsement + recorded partnered prescriber).
- [ ] canInject is a single derived signal consumed by booking (PRD-02) and treatment gates.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0028, ADR-0029 (see docs/adr/decision-log.md).
Depends on: PRD-01/RBAC.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/CREDENTIALS.
Phase: 0 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C4, C19.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C19); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
