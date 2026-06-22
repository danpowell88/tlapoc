# Multi-role staff & active-role context

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/MULTI-ROLE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

As a staff member with multiple roles, I want to be assigned more than one role and act under a chosen active role, so that my permissions reflect what I'm doing without separate logins.
Some users legitimately hold several roles (e.g. an NP who is also the business owner, or a lead nurse covering reception). The model must allow multiple role assignments and an active-role context that the authorisation pipeline honours.

## How it works

Some staff legitimately hold several roles (an NP who is also the owner; a lead nurse covering reception). The model allows multiple role assignments and an active-role context the authorisation pipeline honours, with the active role recorded on actions.
Owner-only financial capability is independent of clinical roles — an NP is not automatically the owner.

## Requirements

- To be assigned more than one role and act under a chosen active role.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A staff profile can hold multiple roles; the union/active-role model is well-defined.
- [ ] The authorisation pipeline evaluates capabilities for the active role (consumed by PLATFORM/ROLE-CONTEXT).
- [ ] Switching active role is recorded; actions capture the role used.
- [ ] Owner-only financial capability is independent of clinical roles (an NP isn't automatically owner).

## UI designs / screenshots

- Header shows the active role + scope; a switch-active-role control for multi-role users (extends the prototype persona display).

## Suggested data model

- **StaffRole** — staff_id, role_id, is_default
  - _Many-to-many; active role chosen per session and stamped on actions._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - StaffRole — staff_id, role_id, is_default (Many-to-many; active role chosen per session and stamped on actions.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A staff profile can hold multiple roles; the union/active-role model is well-defined.
  - Rule: The authorisation pipeline evaluates capabilities for the active role (consumed by PLATFORM/ROLE-CONTEXT).
  - Rule: Switching active role is recorded; actions capture the role used.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/RBAC.
- [ ] **Enforce compliance gate + audit events**
  Enforce C4 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Owner-only financial capability is independent of clinical roles (an NP isn't automatically owner).
