# Multi-role staff & active-role context

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/MULTI-ROLE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

Foundations & tenancy (auth, RBAC, audit, data model) — The domain backbone on top of the Sprint 0 plumbing: tenant provisioning, RBAC + scope-of-practice enforcement, the credential/PII compliance gate that decides who can inject, the exportable audit trail, retention & destruction, the data-breach workflow, and client privacy rights.

As a staff member with multiple roles, I want to be assigned more than one role and act under a chosen active role, so that my permissions reflect what I'm doing without separate logins.

Some users legitimately hold several roles (e.g. an NP who is also the business owner, or a lead nurse covering reception). The model must allow multiple role assignments and an active-role context that the authorisation pipeline honours.

## Requirements

- To be assigned more than one role and act under a chosen active role.
- Traces to requirement(s): REQ-TEN-3, REQ-TEN-4.
- Must satisfy compliance obligation(s): C4.

## Acceptance Criteria

- [ ] A staff profile can hold multiple roles; the union/active-role model is well-defined.
- [ ] The authorisation pipeline evaluates capabilities for the active role (consumed by PLATFORM/ROLE-CONTEXT).
- [ ] Switching active role is recorded; actions capture the role used.
- [ ] Owner-only financial capability is independent of clinical roles (an NP isn't automatically owner).

## UI designs / screenshots

prototype.html — header 'Switch user' (sign-in/persona), Team → People & credentials / Compliance board, Settings.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0017 (see docs/adr/decision-log.md).
Depends on: PRD-01/RBAC.

## Other

Epic: PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model).
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: PRD-01/MULTI-ROLE.
Phase: 0 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C4.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C4); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
