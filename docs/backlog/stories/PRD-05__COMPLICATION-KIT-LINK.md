# Complication protocols: emergency-kit register linkage & expiry surfacing

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/COMPLICATION-KIT-LINK`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/COMPLICATION-LIBRARY`

## Background

As a clinician, I want each protocol's required kit shown with quantity and expiry, and a response to record kit used, so that the emergency kit is verified on-hand and in-date before I need it.
Plainly: this connects each emergency protocol to the actual kit it needs — high-dose hyaluronidase, adrenaline — so the clinic can see at a glance that the right items are on hand and in date, and a response can record which items it used. Where it fits: a follow-up to PRD-05/COMPLICATION-LIBRARY that links the protocols to the emergency-kit register (PRD-11/EMERGENCY-KIT). The protocol library and response checklist already exist; this story surfaces kit availability/expiry and lets a response consume kit items.

## How it works

This follow-up links the protocols to the emergency-kit register. Each ComplicationProtocol's required kit items (e.g. vascular occlusion -> high-dose hyaluronidase; anaphylaxis -> adrenaline 1:1000) are shown with quantity + expiry, read from the emergency-kit register (PRD-11/EMERGENCY-KIT), so the items a protocol needs are known to be on hand with in-date expiry.
Missing or expired kit is flagged so the clinic restocks before it matters; a completed ComplicationResponse can record which kit items it consumed.
The kit register itself lives in PRD-11 — this story reads from it and does not relocate it.

## Requirements

- Each protocol's required kit shown with quantity and expiry, and a response to record kit used.

## Acceptance Criteria

- [ ] Each protocol shows its required kit items with quantity + expiry, read from the emergency-kit register (PRD-11/EMERGENCY-KIT).
- [ ] Missing or expired kit is flagged so the clinic restocks.
- [ ] A completed response can record which kit items were consumed.
- [ ] The kit register is read, not relocated — it lives in PRD-11.

## UI designs / screenshots

- Emergency kit register table: Item - For - Qty - Expiry (Hyaluronidase 1500IU / Adrenaline 1:1000 / Hydrocortisone) - links protocols to the kit (PRD-11).
- Each protocol card shows its required items with qty + expiry; missing/expired kit is flagged.
- A response records which kit items were consumed.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **EmergencyKitItem (PRD-11, referenced)** — item, for, qty, expiry
  - _Extends the basic's ComplicationProtocol.required_kit refs — no new entity here; protocols link required kit and a response records kit consumed. Expiry/availability surfaced so the kit is ready._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Emergency-kit register linkage + expiry surfacing**
  Wire protocols to the emergency-kit register (PRD-11/EMERGENCY-KIT): show each protocol's required items with qty + expiry, flag missing/expired kit so the clinic restocks, and let a response record which kit items were consumed. Read from the kit register; don't relocate it.
