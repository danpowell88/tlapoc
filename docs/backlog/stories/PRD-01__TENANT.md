# Tenant provisioning & staff invitation

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/TENANT`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend

## Background

As a owner, I want to provision my clinic and invite staff who then sign in with our Microsoft 365 accounts, so that my team can access the platform under one isolated tenant.
Plainly: this is where a clinic first exists in the system — one clinic becomes one isolated tenant (its own walled-off data), and its staff get accounts. It is the very first Foundations story, built right after the Sprint 0 platform plumbing. Everything else in the product hangs off it: there is no client, booking, chart or payment until a tenant and its staff exist, so this story unblocks the entire backlog. An owner provisions their clinic (tenant) and invites staff to sign in with existing Microsoft 365 accounts.

## How it works

Tenancy is the root every other record hangs off: one clinic = one Tenant, with one or more Locations (the prototype clinic switcher offers Brisbane, Gold Coast and a locum site). Provisioning is a one-time owner setup that creates the Tenant row, its first Location, and the owner StaffProfile, then opens the staff-invitation flow.
Staff join by invitation: the owner enters a work email, the platform sends an invite, and the invitee completes Microsoft Entra ID SSO (ADR-0004). On first successful SSO the invite is consumed and an Entra object id is bound to a tenant-scoped StaffProfile — there is no local password for staff. Re-inviting a pending member resends; deactivating revokes access immediately and ends live sessions, but keeps the (immutable, audited) history of what they did.
The single most important safety property lives here: every row carries tenant_id and Postgres row-level security (ADR-0003) filters on a per-request session setting (SET app.tenant_id) so a query physically cannot return another clinic's rows — even on a developer mistake. AC2: a user in Tenant A querying any record gets only Tenant-A rows, and a cross-tenant id returns not-found, never a leak. The API also sets and asserts tenant context as defence-in-depth.
Edge cases: an invite to an email that is not a valid Entra account can never complete SSO (it stays pending); a deactivated owner cannot be the last active owner (block); re-activating restores access without re-binding identity.

## Requirements

- To provision my clinic and invite staff who then sign in with our Microsoft 365 accounts.

## Acceptance Criteria

- [ ] Provisioning creates a tenant with locations and an owner account.
- [ ] Invited staff complete Entra SSO and are bound to the tenant.
- [ ] All records created carry tenant_id and are RLS-isolated.
- [ ] Re-inviting / deactivating a staff member is supported and audited.

## UI designs / screenshots

- Non-clinical setup surface (admin) — not one of the captured prototype clinical screens. Provisioning + locations + the staff invite/manage list live in Settings.
- Surfaces operationally as the sidebar clinic context (top-left 'The Lounge — Brisbane' with the location switcher) and the header user chip once a staff member has joined.
- Staff-management list: per-member row with name, work email, assigned role, and status (pending / accepted / revoked) plus resend-invite and deactivate/reactivate actions; every change writes an audit event.

## Suggested data model

- **Tenant** — id, name, status(active|suspended), created_at, settings(json)
  - _Root of isolation; every other table FKs an owning tenant_id with an RLS policy keyed off SET app.tenant_id._
- **Location** — id, tenant_id, name, address, timezone, status
  - _A tenant has 1+ locations (Brisbane, Gold Coast, locum in the proto). Scopes data + audit + reporting (see CLINIC-SWITCH)._
- **StaffProfile** — id, tenant_id, entra_object_id, display_name, work_email, role_id, status(active|deactivated)
  - _Bound to an Entra identity on first SSO; never holds a staff password. Extended by CREDENTIALS._
- **StaffInvite** — id, tenant_id, email, role_id, status(pending|accepted|revoked), invited_by, invited_at, accepted_at
  - _Invite -> Entra SSO bind -> StaffProfile; idempotent resend; revoke ends pending + live access._

## Technical notes (high level)

- Architecture decisions: [ADR-0003](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Tenancy data model, RLS & tenant-context middleware**
  Model Tenant, Location, StaffProfile and StaffInvite with tenant_id on every table and an RLS policy that filters on the per-request session tenant (SET app.tenant_id). Provide request-scoped middleware that resolves the caller's tenant from the auth token, sets the DB session variable for the connection, and asserts it server-side as defence-in-depth so a missing/incorrect tenant context fails closed (never returns rows). Prove AC2: a cross-tenant id resolves to not-found, not a leak. Provisioning command creates Tenant + first Location + owner StaffProfile atomically; guard against deactivating the last active owner.
- [ ] **Staff invitation & lifecycle (invite -> Entra SSO bind -> activate/deactivate)**
  Owner-facing invite flow: create a StaffInvite (email + role) and dispatch it; on the invitee's first successful Entra SSO (single sign-on), consume the invite and bind the Entra object id to a tenant-scoped StaffProfile (no local password). Support idempotent resend for pending invites, revoke (cancels a pending invite), and deactivate/reactivate of an active member (deactivate ends live sessions immediately and hides them from bookable/roster surfaces but preserves audited history). Every invite/bind/deactivate/reactivate writes an AuditEvent. Settings list UI: per-member row with status chip + resend/deactivate actions.
