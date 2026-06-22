# Treatment plans & protocol templates

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/TREATMENT-PLANS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/NOTE-TEMPLATE`

## Background

As a injector, I want to build multi-session treatment plans from protocol templates, so that ongoing care is structured and drives recall.
Multi-session treatment plans + applyable protocol templates feed recall and structure ongoing care (REQ-CLIN-7).

## How it works

Multi-session treatment plans built from applyable protocol templates structure ongoing care and feed the recall worklist (PRD-07). Plan progress shows on the Client 360; a charting overview / 'in-room now' entry lists active plans.
Lets the clinic plan courses (e.g. a skin program) and keep clients on cadence.

## Requirements

- To build multi-session treatment plans from protocol templates.

## Acceptance Criteria

- [ ] Protocol templates can be applied to create a multi-session plan.
- [ ] Plans feed the recall worklist (PRD-07).
- [ ] Plan progress is visible on the client 360.
- [ ] A charting overview / 'in-room now' entry point lists active plans.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Prototype: Charting (charting.png) — apply a protocol to create a multi-session plan; plan progress on Client 360 (client-360.png).
- Active plans listed on the charting overview / in-room entry.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **TreatmentPlan** — id, tenant_id, client_id, protocol_id, sessions[]{service, interval, status}, created_at
  - _Feeds recall; progress on Client 360._
- **Protocol** — id, tenant_id, name, steps[]
  - _Applyable template._

## Technical notes (high level)

- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - TreatmentPlan — id, tenant_id, client_id, protocol_id, sessions[]{service, interval, status}, created_at (Feeds recall; progress on Client 360.)
  - Protocol — id, tenant_id, name, steps[] (Applyable template.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Protocol templates can be applied to create a multi-session plan.
  - Rule: Plans feed the recall worklist (PRD-07).
  - Rule: Plan progress is visible on the client 360.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-05/NOTE-TEMPLATE.
- [ ] **Provider app UI (Flutter)**
  Build on the Flutter provider app: the charting per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Charting (charting.png) — apply a protocol to create a multi-session plan; plan progress on Client 360 (client-360.png).
  - Active plans listed on the charting overview / in-room entry.
