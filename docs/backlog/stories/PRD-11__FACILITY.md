# Facility accreditation & expiry alerts

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/FACILITY`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

As a owner, I want to record facility accreditation and be alerted before it expires, so that we never lapse on accreditation.
Plainly: record each location's accreditation and get warned before it lapses, so the clinic never operates out of accreditation. Where it fits: Facility/Ops is the operational backbone around the clinical core, built after the clinical and reporting layers; accreditation status feeds the inspection pack (PRD-08) and Governance. Per-location accreditation status + expiry alerts before lapse (REQ-FAC-1, C20).

## How it works

Per-location facility accreditation recorded with scheme (ACSQHC (Australian Commission on Safety and Quality in Health Care)/NSQHS (National Safety and Quality Health Service standards) where applicable, or a state licence), status, expiry and evidence reference; expiry alerts fire ahead of lapse. Per RECON-2 (non-surgical injectables), accreditation is treated as optional/conditional, so blocking-vs-advisory is configurable per clinic (the open question), defaulting advisory.
Records are audited and current status feeds the inspection pack (PRD-08) and Governance ('Registrations & indemnity: current'). Evidences the clinic's facility obligations (C20).

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

- Prototype: Operations (ops-equipment area) / facility profile — accreditation status per location (scheme, status, expiry, evidence) with expiry alerts.

![ops-equipment — prototype screen](../screens/ops-equipment.png)

## Suggested data model

- **FacilityAccreditation** — id, tenant_id, location_id, scheme, status, expiry, evidence_ref
  - _Expiry alerts; blocking-vs-advisory configurable; audited._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **FacilityAccreditation entity + per-location record**
  Behaviour: record each location's accreditation with its scheme, status, expiry and evidence. Requirements: model FacilityAccreditation (tenant_id, location_id, scheme, status, expiry, evidence_ref) tenant-scoped under RLS (row-level security, the database-level tenant isolation); CRUD the per-location record and attach the certificate as evidence_ref (media).
- [ ] **Facility profile: per-location accreditation UI**
  Behaviour: a facility-profile view listing each location's accreditation (scheme, status, expiry, evidence link) with an edit/renew action. Requirements: surfaces on the operations view; feeds Governance's 'Registrations & indemnity: current' status; current status flows into the PRD-08 inspection pack.
- [ ] **Accreditation expiry alerts (scheduled)**
  Behaviour: warn ahead of an accreditation lapsing. Requirements: schedule expiry alerts (configurable lead-time before expiry) via the jobs scheduler, raising a job/notification so renewal happens in time; never operate silently out of accreditation.
- [ ] **Blocking-vs-advisory config flag**
  Behaviour: let each clinic choose whether a lapsed accreditation blocks or merely warns. Requirements: a per-clinic config flag (blocking | advisory) read at the relevant guard points, defaulting advisory per RECON-2 (accreditation optional/conditional for non-surgical injectables — the open question); audit accreditation changes.
