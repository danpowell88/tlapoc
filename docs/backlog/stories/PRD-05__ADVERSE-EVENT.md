# Adverse-event capture → DAEN pathway

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/ADVERSE-EVENT`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/IMMUTABILITY`

## Background

As a injector, I want to log an adverse event linked to the treatment, product and lot, so that it feeds the TGA report and the right follow-ups happen.
Log an adverse event/complication linked to the treatment, product and lot, classify seriousness and target the correct DAEN database (REQ-CLIN-5, C12). Includes the VO/anaphylaxis complication-response flow.

## How it works

Log an adverse event/complication linked to the treatment, product and lot; classify seriousness and target the correct DAEN database (medicine vs device) (C12). A complication-response flow (vascular occlusion / anaphylaxis -> log hyaluronidase/adrenaline) routes the AE and raises jobs.
Full prefilled DAEN submission lives in the Governance hub (PRD-08).

## Requirements

- To log an adverse event linked to the treatment, product and lot.
- Compliance: [C12](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] An adverse event captures the data a TGA report needs, classifies seriousness and targets the correct DAEN database (medicine vs device).
- [ ] It links to the treatment, product and lot.
- [ ] A complication-response flow (VO/anaphylaxis → log hyaluronidase/adrenaline) routes the AE + raises jobs.
- [ ] Full submission/prefill lives in the Governance hub (PRD-08).

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Prototype: Clinical -> Complication protocols (clinical-safety.png) — launch a protocol, log the response/kit used; an adverse-event capture linked to the treatment/product/lot.
- Routes to Governance -> Adverse events & DAEN (gov-ae) with seriousness set.

![clinical-safety — prototype screen](../screens/clinical-safety.png)

## Suggested data model

- **AdverseEvent** — id, tenant_id, client_id, chart_entry_id, product_id, lot_id, seriousness, daen_target(medicine|device), description, at
  - _Feeds DAEN prefill (PRD-08); raises jobs._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - AdverseEvent — id, tenant_id, client_id, chart_entry_id, product_id, lot_id, seriousness, daen_target(medicine|device), description, at (Feeds DAEN prefill (PRD-08); raises jobs.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: An adverse event captures the data a TGA report needs, classifies seriousness and targets the correct DAEN database (medicine vs device).
  - Rule: It links to the treatment, product and lot.
  - Rule: A complication-response flow (VO/anaphylaxis → log hyaluronidase/adrenaline) routes the AE + raises jobs.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-05/IMMUTABILITY.
- [ ] **Enforce compliance gate + audit events**
  Enforce C12 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Provider app UI (Flutter)**
  Build on the Flutter provider app: the clinical-safety per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Clinical -> Complication protocols (clinical-safety.png) — launch a protocol, log the response/kit used; an adverse-event capture linked to the treatment/product/lot.
  - Routes to Governance -> Adverse events & DAEN (gov-ae) with seriousness set.
