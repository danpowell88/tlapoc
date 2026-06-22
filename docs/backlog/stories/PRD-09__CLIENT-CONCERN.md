# Client 'report a concern' → follow-up / AE bridge

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CONCERN`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-07/FOLLOWUPS`, `PRD-05/ADVERSE-EVENT`

## Background

As a client, I want to report a concern after my treatment from the app, so that the clinic responds quickly if something's wrong.
Plainly: a safety channel in the client app — after a treatment the client reports a problem, which raises a staff follow-up and can escalate to a clinical adverse event (an unwanted medical occurrence after a treatment) or a formal complaint. Where it fits: a late, client-facing surface that reuses the follow-ups/job-queue (PRD-07) and adverse-event (PRD-05) modules, closing the loop back to the clinical core. The prototype's client app lets a client report a post-treatment concern, which bridges into staff follow-ups (and can escalate to an adverse event/complaint). A safety-critical client→clinic channel.

## How it works

A safety-critical client→clinic channel: the client reports a post-treatment concern from the app (description, urgency, optional photo handled like clinical media — signed URLs (temporary, expiring links to stored photos), no plain device retention, consent-respecting) and immediately sees an acknowledgement. Submitting raises a follow-up Job (PRD-07) with the client and treatment linked; in staff Follow-ups it appears as a job (prototype openConcern / concernCall) where staff view it, call back, resolve, or escalate to an adverse event (PRD-05) / complaint (PRD-11).
The exchange is recorded and audited; a complaint escalation pulls in the C24 AHPRA (Australian Health Practitioner Regulation Agency) pathway + indefinite retention. Bridges the client app to staff follow-ups (the concern bridge — tla_client_reports localStorage in the proto).

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

- Prototype: client-app 'Report a concern' (description, urgency, optional photo; acknowledgement on submit) → staff Follow-ups job ('View report' → openConcern; 'client called back' → concernCall).
- Escalation paths to adverse event (PRD-05) and complaint (PRD-11).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **Concern** — id, tenant_id, client_id, treatment_ref, body, urgency, photo_ref?, status, raised_at
  - _Raises a Job (PRD-07); escalate → AdverseEvent/Complaint._
- **(reuses) Job** — PRD-07 — follow-up the concern raises, linking client + treatment
  - _Staff call back / resolve / escalate._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Client app: 'Report a concern' submission + acknowledgement**
  Client-app 'Report a concern' flow: description + urgency + optional photo (handled like clinical media — request a signed upload URL, no plain device retention, consent-respecting). POST a Concern (client_id, treatment_ref, body, urgency, photo_ref?, raised_at). Show the client an immediate acknowledgement that the clinic has it.
- [ ] **Concern → follow-up Job bridge (replaces tla_client_reports)**
  Server-side: a submitted Concern raises a follow-up Job (PRD-07) linking the client and treatment, replacing the prototype's tla_client_reports localStorage bridge (ingestClientReports). The job lands in staff Follow-ups.
- [ ] **Staff Follow-ups: view / call back / resolve a concern**
  In staff Follow-ups, render the concern job (prototype openConcern 'View report'); let staff call the client back and resolve it (concernCall → 'Marked as actioned — client called back', job → done). Surface urgency.
- [ ] **Escalate a concern to adverse event / complaint**
  From the concern, allow escalation to an adverse event (PRD-05) or a complaint (PRD-11). A complaint escalation pulls in the C24 AHPRA (Australian Health Practitioner Regulation Agency) pathway and indefinite retention (C18). Record + audit the whole exchange end-to-end.
