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

## Technical notes (high level)

- Stack: Flutter client app

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C12, C24); blocked path explains why.
- [ ] **Client app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
