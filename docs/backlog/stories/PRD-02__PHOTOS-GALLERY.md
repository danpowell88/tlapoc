# Before/after photo gallery (image-use-gated)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/PHOTOS-GALLERY`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-360`, `PRD-03/IMAGE-CONSENT`

## Background

As a clinician, I want a before/after photo gallery on the client profile that only opens when image-use consent is on file, so that I can review treatment progress without ever exposing photos the client hasn't consented to.
Plainly: the before/after photo section of the Client 360 profile — the place staff view a client's progress images, gated so it only shows when the client's image-use consent is currently granted. Where it fits: a sibling of the Client 360 profile (PRD-02/CLIENT-360) in Reception (PRD-02); it is the read/display surface for photos that are captured and owned during charting (PRD-05), and it must honour the separate, withdrawable image-use consent defined in Intake & Consent (PRD-03/IMAGE-CONSENT). Because image-use consent can be withdrawn at any time and that must immediately stop further use (C14), this gallery is the place that enforcement is most visible to staff.

## How it works

The before/after gallery is the staff-facing display surface for a client's clinical photos on the Client 360 profile. It is strictly downstream of consent: it queries current ImageConsent.status server-side and only renders when consent is granted — when consent is withdrawn the gallery hides (or shows an empty 'image-use consent withdrawn' state) and the server issues no new signed URLs, so withdrawal immediately stops further use (C14, ADR-0009).
Images are never on the device: each thumbnail/full view is fetched through a short-lived signed URL (a temporary, expiring link), so nothing is downloaded or cached locally. The gallery supports grouping by treatment/date and side-by-side before/after comparison so a clinician can read progress at a glance.
Photos themselves are captured and owned by charting (PRD-05); this story composes and displays them on the profile and enforces the consent + audit rules. Every view writes an AuditEvent.

## Requirements

- A before/after photo gallery on the client profile that only opens when image-use consent is on file.

## Acceptance Criteria

- [ ] The gallery renders only when current image-use consent is granted; when withdrawn it is hidden/empty with a clear 'image-use consent withdrawn' note.
- [ ] Photos are served via short-lived signed URLs, never downloaded to the device or stored locally.
- [ ] Before/after pairs can be compared side-by-side and are grouped by treatment/date.
- [ ] Every photo view is audited (actor, client, photo, at) for compliance (C10/C14).

## UI designs / screenshots

- Prototype: Client 360 (client-360.png) Photos tab + the 'Before / after gallery (image-use consent on file)' grid — a grid of paired thumbnails noting 'image-use consent on file'.
- When image-use consent is withdrawn the gallery is hidden/empty with an 'image-use consent withdrawn' note instead of thumbnails.
- Side-by-side before/after compare; grouped by treatment/date; full view served via a signed URL, no download/save affordance.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Photo (ref, owned by PRD-05)** — id, tenant_id, client_id, appointment_id, treatment_ref, taken_at, storage_ref, kind(before|after)
  - _Owned/captured by charting (PRD-05); this story reads + displays only; never stored on the device._
- **(derived) GalleryView** — = Photos for client WHERE ImageConsent.status==granted; served via signed URL; grouped by treatment/date
  - _Gated on current image-use consent (PRD-03/IMAGE-CONSENT); hidden when withdrawn; every view audited (C10/C14)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Consent-gated gallery query + withdrawn state**
  Behaviour: build the gallery only from photos the client has current image-use consent for. Requirements: query ImageConsent.status server-side before composing the gallery; when granted, return the photo set grouped by treatment/date; when withdrawn, return an empty/hidden state so the UI shows an 'image-use consent withdrawn' note and no thumbnails — withdrawal immediately stops display (C14).
- [ ] **Signed-URL serving (no local storage)**
  Behaviour: serve each thumbnail/full image through a short-lived signed URL (a temporary, expiring link). Requirements: no photo is downloaded, cached or stored on the device (ADR-0009); on a consent-withdrawn event no new signed URLs are issued; URLs expire quickly and are per-view.
- [ ] **Before/after compare + grouping UI**
  Behaviour: a Photos-tab grid that groups images by treatment/date and lets a clinician view before/after pairs side-by-side. Requirements: pairs are matched on kind(before|after) + treatment_ref; no download/save affordance; renders only when consent is granted.
- [ ] **Photo-view audit events (C10/C14)**
  Behaviour: every time a photo is viewed, record it. Requirements: write an AuditEvent (actor, client_id, photo_id, at) to the append-only stream (ADR-0010) so image access is demonstrable to a regulator; viewing while consent is withdrawn is impossible by construction (no URL issued).
