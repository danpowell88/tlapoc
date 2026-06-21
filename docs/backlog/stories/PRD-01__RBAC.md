# RBAC + scope-of-practice matrix enforcement

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RBAC`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/TENANT`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a owner, I want roles mapped to capabilities so the system blocks any action outside a user's scope of practice, so that people can only do what they're trained and legally allowed to do.

Roles map to the §3 scope matrix; the auth pipeline blocks actions outside a user's scope. Capabilities gate API actions, concerns drive role-tailored dashboards (ADR-0017).

## Requirements

- Roles mapped to capabilities so the system blocks any action outside a user's scope of practice.
- Traces to requirement(s): REQ-TEN-3, REQ-TEN-4.
- Must satisfy compliance obligation(s): C4, C19.

## Acceptance Criteria

- [ ] Capabilities × concerns model implemented; each API action checks a capability.
- [ ] The persona set (NP, Lead RN, RN, dermal, reception, owner-business) maps to the matrix.
- [ ] An out-of-scope action is blocked with a clear reason and an audit event.
- [ ] Owner-business is read-only for clinical/stock unless they hold the credential.

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0017 (see docs/adr/decision-log.md).
Depends on: PRD-01/TENANT.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/RBAC.
Phase: 0 · Priority: P0 · Estimate: 5 pts.
Compliance criteria: C4, C19.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C19); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
