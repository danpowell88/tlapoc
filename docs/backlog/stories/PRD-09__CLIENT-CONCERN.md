# Client 'report a concern' → follow-up / AE bridge

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CONCERN`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-07/FOLLOWUPS`, `PRD-05/ADVERSE-EVENT`

## Background

As a client, I want to report a concern after my treatment from the app, so that the clinic responds quickly if something's wrong.
The prototype's client app lets a client report a post-treatment concern, which bridges into staff follow-ups (and can escalate to an adverse event/complaint). A safety-critical client→clinic channel.

## How it works

A safety-critical client->clinic channel: the client reports a post-treatment concern (with optional photo, consent-respecting) from the app, raising a follow-up job for staff with the client/treatment linked. Staff can call back, resolve, or escalate to an adverse event (PRD-05) / complaint (PRD-11). The client sees acknowledgement; the exchange is recorded and audited.
Bridges the client app to staff follow-ups (the concern bridge, localStorage in the proto).

## Requirements

- To report a concern after my treatment from the app.
- Compliance: [C12](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C24](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A client can submit a concern (with optional photo, consent-respecting) from the app.
- [ ] The concern raises a follow-up job for staff (PRD-07) with the client/treatment linked.
- [ ] Staff can call back, resolve, or escalate to an adverse event (PRD-05) / complaint (PRD-11).
- [ ] The client sees acknowledgement; the exchange is recorded and audited.

## UI designs / screenshots

_Prototype screen: client-app.html — Report a concern; prototype Follow-ups._

- Prototype: client app 'Report a concern' (client-app.png) -> appears in staff Follow-ups (followups.png) as a job (openConcern/concernCall).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **Concern** — id, tenant_id, client_id, treatment_ref, body, photo_ref?, status, raised_at
  - _Raises a Job (PRD-07); escalate -> AdverseEvent/Complaint._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Concern — id, tenant_id, client_id, treatment_ref, body, photo_ref?, status, raised_at (Raises a Job (PRD-07); escalate -> AdverseEvent/Complaint.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A client can submit a concern (with optional photo, consent-respecting) from the app.
  - Rule: The concern raises a follow-up job for staff (PRD-07) with the client/treatment linked.
  - Rule: Staff can call back, resolve, or escalate to an adverse event (PRD-05) / complaint (PRD-11).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-07/FOLLOWUPS, PRD-05/ADVERSE-EVENT.
- [ ] **Enforce compliance gate + audit events**
  Enforce C12, C24 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - A client can submit a concern (with optional photo, consent-respecting) from the app.
- [ ] **Client app UI (Flutter)**
  Build on the Flutter client app: the client-app per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: client app 'Report a concern' (client-app.png) -> appears in staff Follow-ups (followups.png) as a job (openConcern/concernCall).
