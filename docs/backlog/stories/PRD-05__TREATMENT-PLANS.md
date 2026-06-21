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

## Suggested data model

- **TreatmentPlan** — id, tenant_id, client_id, protocol_id, sessions[]{service, interval, status}, created_at
  - _Feeds recall; progress on Client 360._
- **Protocol** — id, tenant_id, name, steps[]
  - _Applyable template._

## Technical notes (high level)

- Stack: Flutter provider app
- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
