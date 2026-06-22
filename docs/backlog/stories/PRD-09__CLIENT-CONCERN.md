# Client 'report a concern' → follow-up bridge (basic)

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CONCERN`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a client, I want to report a concern after my treatment from the app and know the clinic has it, so that the clinic is alerted quickly if something's wrong.
Plainly: the core of the client-app safety channel — after a treatment the client reports a problem and immediately sees an acknowledgement, and a staff follow-up is raised. Where it fits: a late, client-facing surface that reuses the follow-ups/job-queue (PRD-07) module, closing the loop back to the clinical core; this basic slice is the submission + acknowledgement + the job bridge, with the staff view/resolve and the adverse-event/complaint escalation as follow-ups. A safety-critical client→clinic channel.

## How it works

A safety-critical client→clinic channel at its core: the client reports a post-treatment concern from the app (description, urgency, optional photo handled like clinical media — signed URLs (temporary, expiring links to stored photos), no plain device retention, consent-respecting) and immediately sees an acknowledgement. Submitting raises a follow-up Job (PRD-07) with the client and treatment linked, which lands in staff Follow-ups.
The submission is recorded and audited; it replaces the prototype's tla_client_reports localStorage bridge (ingestClientReports). The staff view/call-back/resolve workflow and the escalation to an adverse event / complaint are added by the follow-ups (CONCERN-TRIAGE, CONCERN-ESCALATE).

## Requirements

- To report a concern after my treatment from the app and know the clinic has it.
- Compliance: [C12](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C24](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A client can submit a concern (description + urgency + optional photo, consent-respecting) from the app and immediately sees an acknowledgement.
- [ ] The optional photo is handled like clinical media — signed URLs, no plain device retention.
- [ ] Submitting raises a follow-up Job (PRD-07) with the client and treatment linked, landing in staff Follow-ups.
- [ ] The submission is recorded and audited (replaces the prototype's tla_client_reports localStorage bridge).

## UI designs / screenshots

_Prototype screen: client-app.html — Report a concern; prototype Follow-ups._

- Prototype: client-app 'Report a concern' (description, urgency, optional photo; acknowledgement on submit) → raises a staff Follow-ups job.
- Replaces the tla_client_reports localStorage bridge; staff triage + escalation are the follow-ups.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **Concern** — id, tenant_id, client_id, treatment_ref, body, urgency, photo_ref?, status, raised_at
  - _Raises a Job (PRD-07); staff triage + escalation in the follow-ups._
- **(reuses) Job** — PRD-07 — follow-up the concern raises, linking client + treatment
  - _Lands in staff Follow-ups._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Client app: 'Report a concern' submission + acknowledgement**
  Client-app 'Report a concern' flow: description + urgency + optional photo (handled like clinical media — request a signed upload URL, no plain device retention, consent-respecting). POST a Concern (client_id, treatment_ref, body, urgency, photo_ref?, raised_at). Show the client an immediate acknowledgement that the clinic has it.
- [ ] **Concern → follow-up Job bridge (replaces tla_client_reports)**
  Server-side: a submitted Concern raises a follow-up Job (PRD-07) linking the client and treatment, replacing the prototype's tla_client_reports localStorage bridge (ingestClientReports). The job lands in staff Follow-ups.
