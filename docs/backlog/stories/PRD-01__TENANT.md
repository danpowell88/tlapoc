# Tenant provisioning & staff invitation

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/TENANT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend

## Background

As a owner, I want to provision my clinic and invite staff who then sign in with our Microsoft 365 accounts, so that my team can access the platform under one isolated tenant.
An owner provisions their clinic (tenant) and invites staff to sign in with existing Microsoft 365 accounts.

## Requirements

- To provision my clinic and invite staff who then sign in with our Microsoft 365 accounts.

## Acceptance Criteria

- [ ] Provisioning creates a tenant with locations and an owner account.
- [ ] Invited staff complete Entra SSO and are bound to the tenant.
- [ ] All records created carry tenant_id and are RLS-isolated.
- [ ] Re-inviting / deactivating a staff member is supported and audited.

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0003](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
