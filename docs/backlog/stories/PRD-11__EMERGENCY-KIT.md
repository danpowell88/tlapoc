# Emergency kit register (basic)

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/EMERGENCY-KIT`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

As a owner, I want to track the emergency kit (what each item is for, quantity, expiry), so that we know what's on hand for a complication.
Plainly: track the emergency drugs and kit (for filler vascular occlusion and anaphylaxis) — what each item is for, quantity and expiry — so staff know what's on hand. Where it fits: part of the operational backbone (Facility/Ops) around the clinical core; this basic slice is the kit register + add/remove, with expiry alerts, the complication-protocol link + 'Start response', and the continuity-of-care contact added as follow-ups. Track the emergency kit (REQ-FAC-3, C20).

## How it works

Track the emergency kit (hyaluronidase for filler vascular occlusion, adrenaline 1:1000 for anaphylaxis, hydrocortisone, etc.) with what each item is for, quantity and expiry (add/remove via saveKit/newKit/removeKit). This register is the source of truth for what's available during a complication response.
Expiry alerts (KIT-ALERTS), surfacing the kit beside the complication protocols with 'Start response' (KIT-PROTOCOLS), and the continuity-of-care contact (CONTINUITY-CONTACT) are added by the follow-ups. Ensures the clinic knows its emergency stock (C20).

## Requirements

- To track the emergency kit (what each item is for, quantity, expiry).
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Emergency-kit items (incl. hyaluronidase, adrenaline, hydrocortisone) are recorded with what each is for, quantity and expiry.
- [ ] The register supports add/remove (saveKit/newKit/removeKit).
- [ ] It is the source of truth for what's available during a complication response.
- [ ] Expiry alerts, the complication-protocol link, and the continuity-of-care contact are added by the follow-ups (KIT-ALERTS, KIT-PROTOCOLS, CONTINUITY-CONTACT).

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Clinical → Complication protocols (clinical-safety) — Emergency kit register (Item · For · Qty · Expiry; Add item / Remove via saveKit/newKit/removeKit).
- Expiry alerts, the 'Start response' protocol link and the continuity contact are the follow-ups.

![clinical-safety — prototype screen](../screens/clinical-safety.png)

## Suggested data model

- **EmergencyKitItem** — id, tenant_id, location_id, name(hyaluronidase|adrenaline|hydrocortisone|...), for, expiry, quantity
  - _Source of truth for the kit; alerts + protocol link in the follow-ups._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **EmergencyKitItem register + add/remove**
  Behaviour: track the emergency drugs/kit (hyaluronidase for filler vascular occlusion, adrenaline 1:1000 for anaphylaxis, hydrocortisone, etc.) with what each is for, quantity and expiry. Requirements: model EmergencyKitItem (tenant_id, location_id, name, for, expiry, quantity); register UI (Item · For · Qty · Expiry) with add/remove (prototype saveKit/newKit/removeKit); this is the source of truth for what's available during a complication response.
