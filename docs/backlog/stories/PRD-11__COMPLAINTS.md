# Complaints register with AHPRA pathway (basic)

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/COMPLAINTS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web

## Background

As a manager, I want to log a complaint against a client/treatment and have the system surface the AHPRA pathway, so that complaints are logged correctly with the mandated pathway shown.
Plainly: a register for logging complaints against a client/treatment that always shows the AHPRA (Australian Health Practitioner Regulation Agency) pathway. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core; this basic slice is the complaint register + the mandated AHPRA-pathway surface, with the indefinite-retention flag and the reporting/raise-from-conversation hooks added as follow-ups. Handles complaints correctly with the mandated pathway (REQ-CLI-4, C24).

## How it works

A complaints / adverse-outcome register linked to client/treatment that surfaces complaint mechanisms including AHPRA (Australian Health Practitioner Regulation Agency) — explicitly noting an NDA (non-disclosure agreement) doesn't remove that right. Staff log, view, update status/resolution and link to client + treatment from the Governance register.
Logging a complaint sets the indefinite-retention flag (COMPLAINT-RETENTION) and feeds reporting / raise-from-conversation (COMPLAINT-REPORTING) — both added by the follow-ups. Handles complaints correctly with the mandated pathway shown (C24).

## Requirements

- To log a complaint against a client/treatment and have the system surface the AHPRA pathway.
- Compliance: [C24](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] A complaint links to the client/treatment and can be worked to resolution (log, view, update status/resolution).
- [ ] Logging surfaces complaint mechanisms incl. the right to complain to AHPRA — explicitly noting an NDA (non-disclosure agreement) doesn't remove that right.
- [ ] The register lives in Governance.
- [ ] Indefinite retention and the reporting/raise-from-conversation hooks are added by the follow-ups (COMPLAINT-RETENTION, COMPLAINT-REPORTING).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Governance → Overview (gov-overview) complaints register; raise a complaint linked to client/treatment with the AHPRA pathway surfaced.
- Retention flag + reporting/raise-from-conversation are the follow-ups (COMPLAINT-RETENTION, COMPLAINT-REPORTING).

![gov-overview — prototype screen](../screens/gov-overview.png)

## Suggested data model

- **Complaint** — id, tenant_id, client_id, treatment_ref, status, pathway(ahpra|internal), opened_at, resolution
  - _Register + AHPRA pathway; retention + reporting in the follow-ups._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Complaint entity + complaints register**
  Behaviour: a register to log a complaint/adverse-outcome against a client/treatment and work it to resolution. Requirements: model Complaint (tenant_id, client_id, treatment_ref, status, pathway[ahpra|internal], opened_at, resolution) under RLS (row-level security, the database-level tenant isolation); the Governance register lets staff log, view, update status/resolution and link to client + treatment.
- [ ] **Surface AHPRA pathway at log time**
  Behaviour: always show the external complaint pathway when a complaint is logged. Requirements: surface the complaint mechanisms including the right to complain to AHPRA (Australian Health Practitioner Regulation Agency) — explicitly noting an NDA (non-disclosure agreement) doesn't remove that right — as guidance copy on the form (C24).
