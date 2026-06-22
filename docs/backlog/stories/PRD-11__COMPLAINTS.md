# Complaints register with AHPRA pathway

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/COMPLAINTS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web

## Background

As a manager, I want to log a complaint against a client/treatment and have the system surface the AHPRA pathway, so that complaints are handled correctly and retained.
A complaints/adverse-outcome register linked to client/treatment that surfaces complaint mechanisms incl. AHPRA (NDA doesn't remove the right), feeds retention (complaint → indefinite) and reporting (REQ-CLI-4, C24).

## How it works

A complaints/adverse-outcome register linked to client/treatment that surfaces complaint mechanisms including AHPRA (noting an NDA doesn't remove that right). A complaint flag drives indefinite retention of the related record (C18, PRD-01) and feeds reporting (PRD-08). A complaint can be raised from a conversation (PRD-07).
Handles complaints correctly and retains them (C24).

## Requirements

- To log a complaint against a client/treatment and have the system surface the AHPRA pathway.
- Compliance: [C24](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C18](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A complaint links to the client/treatment and surfaces complaint mechanisms incl. AHPRA (noting NDA doesn't remove the right).
- [ ] A complaint flag drives indefinite retention of the related record (C18, PRD-01).
- [ ] Complaints feed the register/reporting (PRD-08).
- [ ] A complaint can be raised from a conversation (links PRD-07).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Governance -> Overview (gov-overview.png) complaints register; raise a complaint linked to client/treatment with the AHPRA pathway surfaced.

![gov-overview — prototype screen](../screens/gov-overview.png)

## Suggested data model

- **Complaint** — id, tenant_id, client_id, treatment_ref, status, pathway(ahpra|internal), opened_at, resolution
  - _Sets indefinite retention flag (C18); feeds reporting._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Complaint — id, tenant_id, client_id, treatment_ref, status, pathway(ahpra|internal), opened_at, resolution (Sets indefinite retention flag (C18); feeds reporting.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: A complaint links to the client/treatment and surfaces complaint mechanisms incl. AHPRA (noting NDA doesn't remove the right).
  - Rule: A complaint flag drives indefinite retention of the related record (C18, PRD-01).
  - Rule: Complaints feed the register/reporting (PRD-08).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
- [ ] **Enforce compliance gate + audit events**
  Enforce C24, C18 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Web UI**
  Build on the Angular web app: the gov-overview per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Governance -> Overview (gov-overview.png) complaints register; raise a complaint linked to client/treatment with the AHPRA pathway surfaced.
