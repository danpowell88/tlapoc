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

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - PrivacyRequest — id, tenant_id, client_id, type(access|correction|deletion), opened_at, due_at, status, resolution (DSAR clock = opened_at + 30d.)
  - ConsentToCollect — id, client_id, notice_version, granted_at (Captured at sign-up.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Collection notice + consent shown and recorded at sign-up.
  - Rule: A client can view/export their own personal/health data.
  - Rule: A correction request is tracked to resolution against the DSAR clock.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/TENANT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C21 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Collection notice + consent shown and recorded at sign-up.
