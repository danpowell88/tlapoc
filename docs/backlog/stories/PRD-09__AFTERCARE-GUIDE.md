# Client app: day-by-day aftercare guidance + escalation

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/AFTERCARE-GUIDE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-CARE`, `PRD-09/CLIENT-CONCERN`

## Background

As a client, I want day-by-day aftercare guidance for my treatment with a clear way to escalate if something's wrong, so that I recover well and know exactly what to do if there's a problem.
Plainly: the in-app aftercare guide that walks a client through recovery day by day after a treatment, suggests matched skincare, and gives a clear 'something's wrong' escalation. Where it fits: a client-facing surface that comes late in the build, a sibling of the My care story (PRD-09/CLIENT-CARE); it reads the visit/treatment so the right protocol shows, and its escalation hands off to the safety channel (PRD-09/CLIENT-CONCERN → PRD-07 follow-ups / PRD-05 adverse event). Aftercare is care content (transactional), not marketing, so it is always delivered.

## How it works

After a treatment the app surfaces the matching aftercare protocol and steps the client through recovery day by day (e.g. skin-needling day-1 / day-4 guidance), with reminders/check-ins arriving as care notifications. The content is keyed to the client's recent visit/treatment so the right guidance shows automatically.
Matched product picks (e.g. recovery serums) are presented as care recommendations — never S4 (Schedule 4 prescription-only medicine) and not priced/advertised in a way that breaches the AU advertising rules. A prominent 'something's wrong' affordance escalates into the Report-a-concern flow (PRD-09/CLIENT-CONCERN), which raises a staff follow-up and can escalate to an adverse event (an unwanted medical occurrence after a treatment) / complaint.
Because aftercare is transactional care content, it is always delivered regardless of the client's marketing opt-out (only offers/news are opt-out). This closes the loop from the treatment back to the client's recovery.

## Requirements

- Day-by-day aftercare guidance for my treatment with a clear way to escalate if something's wrong.

## Acceptance Criteria

- [ ] The right aftercare protocol shows for the client's recent treatment, with day-by-day recovery guidance.
- [ ] Matched product picks are suggested as care content (not S4, never priced as advertising).
- [ ] A prominent 'something's wrong' action escalates into Report-a-concern (PRD-09/CLIENT-CONCERN).
- [ ] Aftercare is treated as transactional care content and always delivered (not gated by marketing opt-out).

## UI designs / screenshots

- Prototype: client-app My care → Aftercare (caftercare) — day-by-day recovery guidance, matched product picks (aftercareRecs), and a 'something's wrong' escalation.
- Surfaced from Home as an 'Aftercare check-in' nudge and an in-progress aftercare card; notifications inbox carries day-N check-ins.
- 'Something's wrong' routes into Report a concern (creport).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **AftercareProtocol** — id, tenant_id, treatment_type, steps[]{day, guidance}, product_picks[]
  - _Keyed to treatment_type; product picks are care recommendations, never S4._
- **(reuses) Visit/Treatment** — PRD-05 — recent treatment that selects the protocol
  - _Drives which protocol + day-N the client sees._
- **(reuses) Notification** — PRD-07 — day-N aftercare check-ins, always-on transactional care content
  - _Not gated by marketing opt-out._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Day-by-day aftercare protocol matched to the recent treatment**
  Behaviour: select and render the aftercare protocol matching the client's most recent treatment, stepping through recovery day by day. Requirements: protocol is keyed to treatment_type from the visit (PRD-05); day-N check-ins arrive as transactional care notifications (PRD-07) that are always delivered regardless of marketing opt-out; the in-progress aftercare card and Home nudge deep-link in.
- [ ] **Matched product picks as care recommendations**
  Behaviour: present matched skincare/recovery product picks alongside the guidance. Requirements: picks are care recommendations only — never S4 (Schedule 4 prescription-only medicine) and never presented/priced in a way that breaches the AU advertising rules; tapping a pick routes to the retail/care item, not a prescription medicine.
- [ ] **'Something's wrong' escalation into Report-a-concern**
  Behaviour: a prominent escalation affordance hands off to the Report-a-concern flow. Requirements: it routes into PRD-09/CLIENT-CONCERN (description + urgency + optional photo handled as clinical media), which raises a staff follow-up (PRD-07) and can escalate to an adverse event (PRD-05) / complaint (PRD-11); the client gets an immediate acknowledgement.
