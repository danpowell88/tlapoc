# Client app: consent-gated before/after gallery with drag-to-compare

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PHOTO-COMPARE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-CARE`, `PRD-02/PHOTOS-GALLERY`

## Background

As a client, I want to view my before/after photos with a drag-to-compare slider, only while my image-use consent is on, so that I can see my own progress without my photos ever being exposed without consent.
Plainly: the before/after photo section inside the client app's My care tab, where someone reviews their own progress photos with a drag-to-compare slider — shown only while their image-use consent is current. Where it fits: a client-facing surface that comes late in the build, a sibling of the My care story (PRD-09/CLIENT-CARE); it is the client-side display of photos captured and owned during charting (PRD-05) and must honour the separate, withdrawable image-use consent from Intake & Consent (PRD-03/IMAGE-CONSENT). It mirrors the staff-side gallery (PRD-02/PHOTOS-GALLERY) on the client's own phone, so the same consent + signed-URL (a temporary, expiring link to a stored photo) rules apply.

## How it works

The before/after gallery is the client-facing display of their own clinical photos inside My care. It is strictly downstream of consent: it re-checks the client's current image-use consent server-side and only renders when consent is granted — when consent is withdrawn the gallery hides (or shows an empty 'image-use consent withdrawn' state) and the server issues no new signed URLs, so a withdrawal immediately stops further display (C14, ADR-0009).
Images are never on the device: each thumbnail/full view is fetched through a short-lived signed URL (a temporary, expiring link to a stored photo) and held only in a transient cache — nothing is downloaded to the device photo library. A drag-to-compare slider overlays a before and after image so the client reads progress at a glance; pairs are grouped by treatment/date.
Photos are captured and owned by charting (PRD-05); this surface composes and displays them on the client's phone and enforces the consent + audit rules. The client sees only their own photos and every view writes an AuditEvent.

## Requirements

- To view my before/after photos with a drag-to-compare slider, only while my image-use consent is on.

## Acceptance Criteria

- [ ] The gallery renders only when current image-use consent is granted; when withdrawn it is hidden/empty with a clear note.
- [ ] Each image is fetched through a short-lived signed URL and never written to device storage or the photo library.
- [ ] Before/after pairs compare side-by-side via a drag-to-compare slider, grouped by treatment/date.
- [ ] The client sees only their own photos; every view is audited.

## UI designs / screenshots

- Prototype: client-app My care → 'Before & after' (cphotos) — consent-gated progress photos with a drag-to-compare slider.
- When image-use consent is off, the section is hidden / shows an empty 'image-use consent withdrawn' state rather than any image.
- Pairs grouped by treatment/date; full view served via a signed URL, no save-to-device.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Photo** — PRD-05 — before/after; viewed via short-lived signed URL (ADR-0009); image-use-consent-gated
  - _Client sees own photos only; never persisted/cached to the device photo library._
- **(reuses) ImageConsent** — PRD-03/IMAGE-CONSENT — status(granted|withdrawn), re-checked server-side per view
  - _Withdrawal hides the gallery and stops new signed URLs (C14)._
- **(reuses) AuditEvent** — actor(client), photo, at
  - _Every view audited (C10/C14)._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Consent-gated gallery with server-side image-use re-check**
  Behaviour: render the before/after gallery in My care only when the client's current image-use consent is granted; when withdrawn, hide it or show an empty 'image-use consent withdrawn' state. Requirements: re-check ImageConsent.status server-side (PRD-03/IMAGE-CONSENT) on entry and per view; on withdrawal the server issues NO new signed URLs so display stops immediately (C14, ADR-0009); the client sees only their own photos.
- [ ] **Signed-URL fetch with no device retention**
  Behaviour: each thumbnail and full view streams from a short-lived signed URL (a temporary, expiring link to a stored photo). Requirements: nothing is written to the device photo library or persisted between sessions — only a transient in-memory cache; save/share-to-device is disabled; URLs expire quickly and are re-requested per view.
- [ ] **Drag-to-compare slider + treatment/date grouping + audit**
  Behaviour: a drag-to-compare slider overlays a before and after image; pairs are grouped by treatment/date. Requirements: smooth gloved/touch dragging; the pairing reads PRD-05 photo metadata; every view writes an AuditEvent (actor=client, photo, at) for compliance (C10/C14).
