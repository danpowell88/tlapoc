# Client privacy: collection notice, access & correction (DSAR)

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/PRIVACY-RIGHTS`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a client, I want to see a clear collection notice, access a copy of my data and request a correction, so that my privacy rights under the Privacy Act are respected.
Clients have APP 12/13 rights: a collection notice/consent at sign-up, and the ability to access and request correction of their own data (DSAR clock ≤30 days).

## How it works

Clients get APP 12/13 rights: a collection notice + consent at sign-up, the ability to view/export their own data, and to request a correction — all tracked against the DSAR <=30-day clock and audited.
Self-service lives in the client app privacy area; staff handle requests via Governance.

## Requirements

- To see a clear collection notice, access a copy of my data and request a correction.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Collection notice + consent shown and recorded at sign-up.
- [ ] A client can view/export their own personal/health data.
- [ ] A correction request is tracked to resolution against the DSAR clock.
- [ ] All access/correction actions are audited.

## UI designs / screenshots

- Client app: Account -> 'Your data & privacy' (residency note, request a copy, request correction) — client-app.png.
- Staff side: a DSAR queue in Governance with the response clock.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **PrivacyRequest** — id, tenant_id, client_id, type(access|correction|deletion), opened_at, due_at, status, resolution
  - _DSAR clock = opened_at + 30d._
- **ConsentToCollect** — id, client_id, notice_version, granted_at
  - _Captured at sign-up._

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C21); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
