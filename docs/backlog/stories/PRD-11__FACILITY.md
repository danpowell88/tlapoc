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

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
