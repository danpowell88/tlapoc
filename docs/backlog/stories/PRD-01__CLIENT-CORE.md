# Client core record: DOB & under-18 flag

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CLIENT-CORE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/TENANT`

## Background

As a system, I want to capture client DOB and derive an under-18 flag, so that downstream cooling-off and pricing rules can enforce age-based requirements.
The client record captures DOB and derives an under-18 flag that feeds cooling-off (C6) and advertising/pricing (C9) elsewhere.

## How it works

The core client record captures DOB and derives an under-18 flag that downstream rules consume: cooling-off (PRD-03/C6) and S4 pricing/advertising (C9). It supports soft-delete with audit and duplicate handling.
Under-18 status appears as an age chip on the patient header so staff always see it.

## Requirements

- To capture client DOB and derive an under-18 flag.
- Compliance: [C6](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] DOB captured; under-18 flag derived and exposed to PRD-03/PRD-06/PRD-07.
- [ ] The flag updates correctly across a birthday.
- [ ] Soft-delete with audit and duplicate handling supported (full CRM in PRD-02).
- [ ] Under-18 status is visible on the patient header (consumed by UX age chip).

## UI designs / screenshots

- Prototype: the Client 360 header (client-360.png) shows the age/under-18 chip alongside consent chips; DOB on the profile.
- Directory + profile are PRD-02; this story is the underlying record + age derivation.

![client-360 — prototype screen](../screens/client-360.png)

## Suggested data model

- **Client** — id, tenant_id, name, dob, contacts, flags(json), under18(derived), deleted_at
  - _under18 recomputed across birthdays; soft-delete excluded from active views._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Client — id, tenant_id, name, dob, contacts, flags(json), under18(derived), deleted_at (under18 recomputed across birthdays; soft-delete excluded from active views.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: DOB captured; under-18 flag derived and exposed to PRD-03/PRD-06/PRD-07.
  - Rule: The flag updates correctly across a birthday.
  - Rule: Soft-delete with audit and duplicate handling supported (full CRM in PRD-02).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/TENANT.
