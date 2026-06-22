# Complaints register with AHPRA pathway

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/COMPLAINTS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web

## Background

As a manager, I want to log a complaint against a client/treatment and have the system surface the AHPRA pathway, so that complaints are handled correctly and retained.
A complaints/adverse-outcome register linked to client/treatment that surfaces complaint mechanisms incl. AHPRA (NDA doesn't remove the right), feeds retention (complaint → indefinite) and reporting (REQ-CLI-4, C24).

## How it works

A complaints / adverse-outcome register linked to client/treatment that surfaces complaint mechanisms including AHPRA (explicitly noting an NDA doesn't remove that right). Logging a complaint sets an indefinite-retention flag on the related record (C18, PRD-01) — exempting it from the normal destruction schedule for as long as the complaint exists — and feeds reporting (PRD-08) and Governance. A complaint can be raised directly from a conversation (PRD-07 inbox).
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

- Prototype: Governance → Overview (gov-overview) complaints register; raise a complaint linked to client/treatment with the AHPRA pathway surfaced.
- Surfaces in Governance ('Open AE cases', 'Needs attention'); can be raised from a conversation (PRD-07).

![gov-overview — prototype screen](../screens/gov-overview.png)

## Suggested data model

- **Complaint** — id, tenant_id, client_id, treatment_ref, status, pathway(ahpra|internal), opened_at, resolution
  - _Sets indefinite-retention flag (C18); feeds reporting._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Complaint entity + complaints register**
  Model Complaint (tenant_id, client_id, treatment_ref, status, pathway[ahpra|internal], opened_at, resolution) under RLS. Complaints register in Governance: log, view, update status/resolution, link to client + treatment.
- [ ] **Surface AHPRA pathway at log time**
  When a complaint is logged, surface the complaint mechanisms including the right to complain to AHPRA notwithstanding any NDA (C24) as guidance copy on the form.
- [ ] **Complaint → indefinite retention flag**
  Logging a complaint sets an indefinite-retention flag on the related record; the PRD-01 retention engine reads it and exempts that record from the normal destruction schedule while the complaint exists (C18).
- [ ] **Feed reporting + raise-from-conversation**
  Feed complaints into the register/reporting (PRD-08) and the Governance command centre. Allow a complaint to be raised directly from a PRD-07 inbox conversation, linking the thread to the new complaint.
