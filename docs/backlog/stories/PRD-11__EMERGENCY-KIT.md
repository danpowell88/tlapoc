# Emergency kit & continuity-of-care

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EMERGENCY-KIT`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

As a owner, I want to track the emergency kit with expiry alerts and record a continuity-of-care contact, so that we're prepared for complications and cover when a prescriber is unavailable.
Track the emergency kit (hyaluronidase, anaphylaxis) with expiry alerts and record a continuity-of-care contact (REQ-FAC-3, C20).

## How it works

Track the emergency kit (incl. hyaluronidase for filler vascular occlusion, anaphylaxis) with expiry alerts before lapse, plus a continuity-of-care contact for when the treating practitioner/prescriber is unavailable. Emergency/complication protocol links are surfaced (ties to PRD-05 complication response).
Ensures the clinic is prepared for complications (C20).

## Requirements

- To track the emergency kit with expiry alerts and record a continuity-of-care contact.
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Emergency-kit items (incl. hyaluronidase, anaphylaxis) raise expiry alerts before lapse.
- [ ] A continuity-of-care contact is recorded and visible when the treating practitioner/prescriber is unavailable.
- [ ] Emergency/complication protocol links are surfaced.
- [ ] Ties into the complication-response flow (PRD-05).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations + Clinical -> Complication protocols (clinical-safety.png) — emergency-kit register with expiry alerts (saveKit/newKit/removeKit); continuity-of-care contact.

![clinical-safety — prototype screen](../screens/clinical-safety.png)

## Suggested data model

- **EmergencyKitItem** — id, tenant_id, location_id, name(hyaluronidase|adrenaline|...), expiry, quantity
  - _Expiry alerts; linked from complication protocols._
- **ContinuityContact** — id, tenant_id, name, role, phone
  - _Surfaced when prescriber unavailable._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C20); blocked path explains why.
- [ ] **Web UI** — prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html.
