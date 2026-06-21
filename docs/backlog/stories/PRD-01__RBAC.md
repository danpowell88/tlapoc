# RBAC + scope-of-practice matrix enforcement

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/RBAC`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a owner, I want roles mapped to capabilities so the system blocks any action outside a user's scope of practice, so that people can only do what they're trained and legally allowed to do.
Roles map to the §3 scope matrix; the auth pipeline blocks actions outside a user's scope. Capabilities gate API actions, concerns drive role-tailored dashboards (ADR-0017).

## How it works

Authorisation is capabilities x concerns (ADR-0017): capabilities gate API actions; concerns drive role-tailored dashboards. Each persona (NP, Lead RN, RN, dermal, reception, owner-business) maps to a capability set mirroring the legal scope-of-practice matrix.
Every API action checks a capability server-side; an out-of-scope attempt is blocked with a reason + audit event. This makes 'only allowed people can act' true by construction, not by screen-hiding.

## Requirements

- Roles mapped to capabilities so the system blocks any action outside a user's scope of practice.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C19](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Capabilities × concerns model implemented; each API action checks a capability.
- [ ] The persona set (NP, Lead RN, RN, dermal, reception, owner-business) maps to the matrix.
- [ ] An out-of-scope action is blocked with a clear reason and an audit event.
- [ ] Owner-business is read-only for clinical/stock unless they hold the credential.

## UI designs / screenshots

- Surfaces as the persona/role + scope tooltip in the header (prototype 'Switch user' + scope note), and nav entries showing/hiding per role.
- Blocked actions show the calm blocked-action banner: what is blocked, which rule, how to resolve, who can resolve.

## Suggested data model

- **Role** — id, tenant_id, name, capabilities[]
  - _Preset roles map to the scope matrix; custom builder is later._
- **Capability** — key, description
  - _e.g. chart.write, stock.custody, finance.read; checked per API action._
- **Concern** — key
  - _Drives which dashboard widgets a role sees._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C4, C19); blocked path explains why.
