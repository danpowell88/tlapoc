# Facility accreditation register (basic)

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/FACILITY`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

As a owner, I want to record each location's facility accreditation, so that I have an evidenced record of our accreditation status.
Plainly: record each location's accreditation — scheme, status, expiry and evidence — so the clinic knows where it stands. Where it fits: Facility/Ops is the operational backbone around the clinical core, built after the clinical and reporting layers; this basic slice is the accreditation record + its UI, with expiry alerts and the blocking-vs-advisory enforcement added as follow-ups. Accreditation status feeds the inspection pack (PRD-08) and Governance (REQ-FAC-1, C20).

## How it works

Per-location facility accreditation recorded with scheme (ACSQHC (Australian Commission on Safety and Quality in Health Care)/NSQHS (National Safety and Quality Health Service standards) where applicable, or a state licence), status, expiry and evidence reference; the certificate attaches as evidence_ref (media).
Records are audited and current status feeds the inspection pack (PRD-08) and Governance ('Registrations & indemnity: current'). Expiry alerts (FACILITY-ALERTS) and the blocking-vs-advisory enforcement (FACILITY-ENFORCE) are added by the follow-ups. Evidences the clinic's facility obligations (C20).

## Requirements

- To record each location's facility accreditation.
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Per-location accreditation status recorded (scheme, status, expiry, evidence).
- [ ] The certificate attaches as evidence (media).
- [ ] Records are audited and feed Governance ('Registrations & indemnity: current') + the PRD-08 inspection pack.
- [ ] Expiry alerts and the blocking-vs-advisory enforcement are added by the follow-ups (FACILITY-ALERTS, FACILITY-ENFORCE).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations (ops-equipment area) / facility profile — accreditation status per location (scheme, status, expiry, evidence) with an edit/renew action.
- Expiry alerts + blocking-vs-advisory are the follow-ups (FACILITY-ALERTS, FACILITY-ENFORCE).

![ops-equipment — prototype screen](../screens/ops-equipment.png)

## Suggested data model

- **FacilityAccreditation** — id, tenant_id, location_id, scheme, status, expiry, evidence_ref
  - _Per-location record; audited._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **FacilityAccreditation entity + per-location record**
  Behaviour: record each location's accreditation with its scheme, status, expiry and evidence. Requirements: model FacilityAccreditation (tenant_id, location_id, scheme, status, expiry, evidence_ref) tenant-scoped under RLS (row-level security, the database-level tenant isolation); CRUD the per-location record and attach the certificate as evidence_ref (media).
- [ ] **Facility profile: per-location accreditation UI**
  Behaviour: a facility-profile view listing each location's accreditation (scheme, status, expiry, evidence link) with an edit/renew action. Requirements: surfaces on the operations view; feeds Governance's 'Registrations & indemnity: current' status; current status flows into the PRD-08 inspection pack.
