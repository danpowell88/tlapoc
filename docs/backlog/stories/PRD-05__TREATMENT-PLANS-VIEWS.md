# Treatment plans: protocol builder, Client 360 progress & in-room list

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/TREATMENT-PLANS-VIEWS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/TREATMENT-PLANS`

## Background

As a injector / clinic admin, I want a protocol builder, a plan-progress view on the Client 360, and an in-room list of active plans, so that the clinic curates its protocols and clinicians pick up clients mid-course.
Plainly: the screens around treatment plans — a builder for the clinic to design its protocol templates, a progress tab on the client's record, and a 'who's mid-course today' list for the clinician. Where it fits: a follow-up to PRD-05/TREATMENT-PLANS that adds the management and review surfaces on top of the plan engine. The plan data and apply flow already exist; this story makes them visible and curatable.

## How it works

This follow-up adds the management and review surfaces on top of the plan engine. A Protocol template builder lets the clinic curate named courses with ordered steps (service + recommended interval) for reuse.
Plan progress becomes visible on the Client 360 (a treatment-plan tab showing sessions done / next-due and the cadence), and a charting overview / 'in-room now' entry point lists the day's active plans so the clinician can pick up where a client is in their course.
These surfaces read the plan engine (PRD-05/TREATMENT-PLANS) and its progress queries; the skin-analysis recommendations (PRD-05/SKIN-ANALYSIS) and outcomes (PRD-05/OUTCOMES) feed into and read from plans.

## Requirements

- A protocol builder, a plan-progress view on the Client 360, and an in-room list of active plans.

## Acceptance Criteria

- [ ] A Protocol template builder lets the clinic create/edit named courses with ordered steps (service + recommended interval).
- [ ] The Client 360 shows a treatment-plan tab with sessions done / next-due and the cadence.
- [ ] A charting overview / 'in-room now' entry point lists the day's active plans so the clinician picks up mid-course.
- [ ] These surfaces read the plan engine (PRD-05/TREATMENT-PLANS); capability-gated to clinical / admin roles.

## UI designs / screenshots

- Protocol template builder (named course, ordered steps = service + interval).
- Client 360: a treatment-plan tab showing sessions done / next-due and the cadence.
- A charting overview / 'in-room now' entry point listing the day's active plans so the clinician picks up mid-course.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Protocol / TreatmentPlan / PlanSession (referenced)** — read for the builder, Client-360 progress and in-room list
  - _Extends the basic's plan engine with management/review surfaces — no new entity._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Protocol builder + Client-360 progress + in-room list (UI)**
  Build the Protocol template builder, the plan-progress view on the Client 360 (sessions done / next-due) and the charting overview / 'in-room now' list of active plans. Wire to the plan engine (PRD-05/TREATMENT-PLANS) with loading/empty/error states; capability-gate to clinical / admin roles.
