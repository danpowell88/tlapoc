# Tenant provisioning & staff invitation

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/TENANT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend

## Background

As a owner, I want to provision my clinic and invite staff who then sign in with our Microsoft 365 accounts, so that my team can access the platform under one isolated tenant.
An owner provisions their clinic (tenant) and invites staff to sign in with existing Microsoft 365 accounts.

## How it works

Tenancy is the foundation every other record hangs off: one clinic = one tenant, with one or more locations. Provisioning creates the tenant, its first location and the owner account, then invites staff who sign in with the clinic's existing Microsoft 365 accounts.
Every row carries tenant_id and is isolated by Postgres row-level security (ADR-0003), so a query can never cross tenants even on a developer mistake — the single most important safety property of the data layer.

## Requirements

- To provision my clinic and invite staff who then sign in with our Microsoft 365 accounts.

## Acceptance Criteria

- [ ] Provisioning creates a tenant with locations and an owner account.
- [ ] Invited staff complete Entra SSO and are bound to the tenant.
- [ ] All records created carry tenant_id and are RLS-isolated.
- [ ] Re-inviting / deactivating a staff member is supported and audited.

## UI designs / screenshots

- Surfaces as the clinic switcher (sidebar) and Settings; staff invitation/management is an admin screen.
- Owner provisions the clinic, sets locations, and invites staff by email; they complete Entra SSO to join.

## Suggested data model

- **Tenant** — id, name, status, created_at, settings(json)
  - _Root of isolation; everything FKs an owning tenant_id._
- **Location** — id, tenant_id, name, address, timezone
  - _A tenant has 1+ locations (Brisbane, Gold Coast in the proto)._
- **StaffInvite** — id, tenant_id, email, role, status(pending|accepted|revoked), invited_at
  - _Invite -> Entra SSO bind -> StaffProfile._

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0003](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
