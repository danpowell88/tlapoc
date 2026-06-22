# Treatment plans & protocol templates

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/TREATMENT-PLANS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a injector, I want to build multi-session treatment plans from protocol templates, so that ongoing care is structured and drives recall.
Treatment plans: multi-session courses of care built from clinic-curated protocol templates, scheduling and tracking ongoing treatment and driving the recall worklist. A care-structuring capability under PRD-05 charting on the clinic-first spine; it depends on the guided note (NOTE-TEMPLATE), feeds the recall worklist in comms (PRD-07), and reads from skin analysis (SKIN-ANALYSIS) and outcomes (OUTCOMES). Multi-session treatment plans + applyable protocol templates feed recall and structure ongoing care (REQ-CLIN-7).

## How it works

As an injector, I want to build multi-session treatment plans from protocol templates, so that ongoing care is structured and drives recall.
Much aesthetic care is a course, not a one-off: a needling program, an anti-ageing maintenance cadence, a skin protocol over several visits. Treatment plans turn that into structured, trackable care — a clinician applies a protocol template and the platform schedules the sessions, tracks progress and keeps the client on cadence via recall.
A Protocol is a reusable, clinic-curated template: a named course with ordered steps (service + recommended interval). Applying a protocol to a client instantiates a TreatmentPlan whose sessions inherit the steps, each with its own due date and status (planned / done / skipped). Plans can also be built ad hoc without a template.
Plans feed the recall worklist (PRD-07): each upcoming session projects a recall Job at its due date, so reception/comms can rebook the client at the right cadence rather than relying on memory. As sessions are charted (a ChartEntry is finalised against a plan session), the session is marked done and the next becomes the active recall.
Plan progress is visible on the Client 360 (a treatment-plan tab showing sessions done/next-due), and a charting overview / 'in-room now' entry point lists the day's active plans so the clinician can pick up where a client is in their course. The skin-analysis recommendations (SKIN-ANALYSIS) and outcomes (OUTCOMES) feed into and read from plans.

## Requirements

- To build multi-session treatment plans from protocol templates.

## Acceptance Criteria

- [ ] A protocol template (ordered steps: service + interval) can be applied to a client to create a multi-session plan; ad hoc plans are also supported.
- [ ] Each plan session has a due date and status; finalising a charted session marks it done and advances the next.
- [ ] Plans feed the recall worklist (PRD-07) — upcoming sessions project recall Jobs at their due dates.
- [ ] Plan progress is visible on the Client 360, and a charting overview / 'in-room now' entry lists active plans.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Charting: apply a protocol template to create a multi-session plan for the client; the close-out's recall toggle already projects the rebook Job (closeoutGo).
- Client 360: a treatment-plan tab showing sessions done / next-due and the cadence.
- A charting overview / 'in-room now' entry point listing the day's active plans so the clinician picks up mid-course.
- New vs the prototype (build these): the Protocol template builder, the plan instantiation + session scheduling, and the recall projection per upcoming session.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Protocol** — id, tenant_id, name, steps[]{service_id, recommended_interval, order}, active
  - _Reusable, clinic-curated template (e.g. anti-ageing maintenance, needling course)._
- **TreatmentPlan** — id, tenant_id, client_id, protocol_id (nullable for ad hoc), created_at, status
  - _Instantiated from a protocol or built ad hoc; progress shown on Client 360._
- **PlanSession** — id, plan_id (FK), service_id, due_date, status (planned|done|skipped), chart_entry_id (nullable)
  - _Finalising the linked ChartEntry marks done + advances the next; upcoming sessions project recall Jobs (PRD-07)._

## Technical notes (high level)

- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations: Protocol + TreatmentPlan + PlanSession**
  EF Core: Protocol (named template with ordered steps = service + recommended interval), TreatmentPlan (client_id, optional protocol_id, status), PlanSession (due_date, status, optional chart_entry_id link). tenant_id + Row-Level Security (RLS, the per-tenant database isolation); index plans by client and sessions by due_date for the recall projection.
- [ ] **Plan API: apply protocol, schedule sessions, track progress**
  Apply-protocol command instantiates a plan with sessions dated off the step intervals; support ad hoc plans. Finalising a charted ChartEntry against a session marks it done and advances the next active session. Project upcoming sessions as recall Jobs (ADR-0023) into the PRD-07 worklist. Expose plan-progress queries for the Client 360. Emit domain events; publish OpenAPI.
- [ ] **Plan UI: protocol builder, apply + progress + in-room list**
  Build the Protocol template builder, the apply-to-client flow in Charting, the plan-progress view on the Client 360 (sessions done / next-due) and the charting overview / 'in-room now' list of active plans. Wire to the API with loading/empty/error states; capability-gate to clinical roles.
