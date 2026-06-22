# Owner-only financial (.fin) capability gating

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/FIN-GATING`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-01/RBAC`

## Background

As a owner, I want all revenue/MRR/pricing figures hidden from non-owner roles across the app and API, so that financials stay owner-only.
Project rule + prototype: revenue, MRR and pricing figures must stay gated behind the owner financial capability; non-owner roles (e.g. reception) see memberships but no money figures. The prototype tags these with a .fin class toggled by capability.

## How it works

All revenue/MRR/pricing figures are hidden from non-owner roles across the app AND the API — enforced server-side (the API never returns gated figures to unauthorised roles), not just hidden in the UI. Non-owner roles see operational data (e.g. membership status) but no money; attempted access is denied and audited.
The project's owner-only financials rule, made structural (the .fin capability).

## Requirements

- All revenue/MRR/pricing figures hidden from non-owner roles across the app and API.
- Compliance: [C4](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A financial capability gates money figures in dashboards, checkout, finance, memberships and reports.
- [ ] Non-owner roles see operational data (e.g. membership status) but no revenue/MRR/pricing.
- [ ] Gating is enforced server-side (API never returns gated figures to unauthorised roles), not just hidden in UI.
- [ ] Attempted access is denied and audited.

## UI designs / screenshots

- Prototype: money figures tagged .fin are hidden for reception/clinical roles across dashboards, checkout totals, finance, memberships and reports; visible only to the owner.
- A non-owner never sees revenue/MRR/pricing.

![finance — prototype screen](../screens/finance.png)

## Suggested data model

- **Capability finance.read** — gates money fields server-side
  - _API strips/denies gated figures; access attempts audited._

## Technical notes (high level)

- Architecture decisions: [ADR-0017](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Capability finance.read — gates money fields server-side (API strips/denies gated figures; access attempts audited.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A financial capability gates money figures in dashboards, checkout, finance, memberships and reports.
  - Rule: Non-owner roles see operational data (e.g. membership status) but no revenue/MRR/pricing.
  - Rule: Gating is enforced server-side (API never returns gated figures to unauthorised roles), not just hidden in UI.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/RBAC.
- [ ] **Enforce compliance gate + audit events**
  Enforce C4, C10 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - A financial capability gates money figures in dashboards, checkout, finance, memberships and reports.
  - Gating is enforced server-side (API never returns gated figures to unauthorised roles), not just hidden in UI.
