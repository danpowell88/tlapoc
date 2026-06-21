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

## Technical notes (high level)

- Stack: Flutter provider app

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C12); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
