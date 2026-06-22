# Concern: escalate to adverse event / complaint

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CONCERN-ESCALATE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-CONCERN`, `PRD-05/ADVERSE-EVENT`

## Background

As a clinic staff, I want to escalate a concern to an adverse event or a complaint, so that serious concerns enter the right clinical / regulatory pathway.
Plainly: from a reported concern, staff can escalate to a clinical adverse event (an unwanted medical occurrence after a treatment) or a formal complaint. Where it fits: a follow-up to the concern basic (PRD-09/CLIENT-CONCERN) that adds escalation; it hands off to the adverse-event (PRD-05) and complaints (PRD-11) modules, and a complaint escalation pulls in the AHPRA (Australian Health Practitioner Regulation Agency) pathway and indefinite retention. The whole exchange is recorded and audited end-to-end.

## How it works

From the concern, allow escalation to an adverse event (an unwanted medical occurrence after a treatment, PRD-05) or a complaint (PRD-11). A complaint escalation pulls in the C24 AHPRA (Australian Health Practitioner Regulation Agency) pathway and indefinite retention (C18).
The escalation links the originating Concern to the new adverse event / complaint so the thread is traceable; the whole exchange is recorded and audited end-to-end. This is the most serious arm of the safety channel, beyond a routine call-back (CONCERN-TRIAGE).

## Requirements

- To escalate a concern to an adverse event or a complaint.

## Acceptance Criteria

- [ ] From the concern, staff can escalate to an adverse event (PRD-05) or a complaint (PRD-11).
- [ ] A complaint escalation pulls in the C24 AHPRA pathway and indefinite retention (C18).
- [ ] The escalation links the originating concern to the new adverse event / complaint.
- [ ] The whole exchange is recorded and audited end-to-end.

## UI designs / screenshots

- Prototype: staff Follow-ups — escalation actions from a concern to adverse event (PRD-05) and complaint (PRD-11).
- Complaint escalation surfaces the AHPRA pathway + indefinite retention; exchange audited end-to-end.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) AdverseEvent/Complaint** — PRD-05 adverse event / PRD-11 complaint, linked from the originating Concern
  - _Extends CLIENT-CONCERN; complaint sets indefinite-retention (C18) + AHPRA pathway (C24)._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Escalate a concern to adverse event / complaint**
  From the concern, allow escalation to an adverse event (PRD-05) or a complaint (PRD-11). A complaint escalation pulls in the C24 AHPRA (Australian Health Practitioner Regulation Agency) pathway and indefinite retention (C18). Record + audit the whole exchange end-to-end.
