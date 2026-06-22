# Facility accreditation & expiry alerts

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/FACILITY`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

As a owner, I want to record facility accreditation and be alerted before it expires, so that we never lapse on accreditation.
Per-location accreditation status + expiry alerts before lapse (REQ-FAC-1, C20).

## How it works

Per-location facility accreditation (e.g. ACSQHC/NSQHS where applicable) recorded with status + expiry alerts before lapse. Whether accreditation is blocking or advisory in the product is configurable (open question). Records are audited.
Evidences the clinic's facility obligations (C20).

## Requirements

- To record facility accreditation and be alerted before it expires.
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Per-location accreditation status recorded.
- [ ] Expiry alerts fire before lapse.
- [ ] Whether accreditation is blocking or advisory is configurable (open question).
- [ ] Records are audited.

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations (ops-equipment.png area) / facility profile — accreditation status per location with expiry alerts.

![ops-equipment — prototype screen](../screens/ops-equipment.png)

## Suggested data model

- **FacilityAccreditation** — id, tenant_id, location_id, scheme, status, expiry, evidence_ref
  - _Expiry alerts; blocking vs advisory configurable._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - FacilityAccreditation — id, tenant_id, location_id, scheme, status, expiry, evidence_ref (Expiry alerts; blocking vs advisory configurable.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Per-location accreditation status recorded.
  - Rule: Expiry alerts fire before lapse.
  - Rule: Whether accreditation is blocking or advisory is configurable (open question).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
- [ ] **Enforce compliance gate + audit events**
  Enforce C20 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Whether accreditation is blocking or advisory is configurable (open question).
- [ ] **Web UI**
  Build on the Angular web app: the ops-equipment per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Operations (ops-equipment.png area) / facility profile — accreditation status per location with expiry alerts.
