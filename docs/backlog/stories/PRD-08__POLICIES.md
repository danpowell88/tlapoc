# Policies & procedures sign-off

> **Epic:** [PRD-08 — Reporting & compliance dashboards (Governance hub)](../epics/PRD-08.md)  ·  **Key:** `PRD-08/POLICIES`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-08/INSPECTION-PACK`

## Background

As a owner / compliance officer, I want to publish policies and track staff sign-off, so that I can evidence that the team has read current procedures.
The prototype's Governance → Policies screen (signPolicy) tracks staff acknowledgement/sign-off of clinic policies and procedures, part of the Governance hub.

## How it works

Policies & procedures sign-off: versioned policies published to relevant roles, with staff sign-off recorded per version + date; outstanding sign-offs surface and a policy change requires re-acknowledgement. Sign-off status is included in the inspection pack.
Evidences that the team has read current procedures (part of the Governance hub).

## Requirements

- To publish policies and track staff sign-off.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Policies are versioned and published to relevant roles.
- [ ] Staff sign-off is recorded per policy version with date; outstanding sign-offs surface.
- [ ] Sign-off status is included in the inspection-readiness pack.
- [ ] Changes to a policy require re-acknowledgement.

## UI designs / screenshots

_Prototype screen: prototype.html — Reports, Governance (Overview/AE & DAEN/Policies/Audit pack)._

- Prototype: Governance -> Policies (gov-policies.png) — policy list with versions + per-staff sign-off status (signPolicy); outstanding highlighted.

![gov-policies — prototype screen](../screens/gov-policies.png)

## Suggested data model

- **Policy** — id, tenant_id, name, version, body, roles[]
  - _Re-ack required on change._
- **PolicySignoff** — id, policy_version, staff_id, signed_at
  - _Feeds inspection pack._

## Technical notes (high level)

- Architecture decisions: [ADR-0030](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-08-reporting-compliance.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-08-reporting-compliance.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Policy — id, tenant_id, name, version, body, roles[] (Re-ack required on change.)
  - PolicySignoff — id, policy_version, staff_id, signed_at (Feeds inspection pack.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Policies are versioned and published to relevant roles.
  - Rule: Staff sign-off is recorded per policy version with date; outstanding sign-offs surface.
  - Rule: Sign-off status is included in the inspection-readiness pack.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-08/INSPECTION-PACK.
- [ ] **Enforce compliance gate + audit events**
  Enforce C10, C20 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Web UI**
  Build on the Angular web app: the gov-policies per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Governance -> Policies (gov-policies.png) — policy list with versions + per-staff sign-off status (signPolicy); outstanding highlighted.
