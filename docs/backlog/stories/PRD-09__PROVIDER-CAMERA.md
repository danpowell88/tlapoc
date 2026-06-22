# Provider app: native-camera before/after capture

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-CAMERA`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/PROVIDER-ROOMSIDE`, `PRD-05/PHOTOS`

## Background

As a injector, I want to capture before/after photos at the chair without them being stored on the device, so that the visual record is captured while staying compliant.
Plainly: the chairside camera step where the injector takes before/after photos that stream straight to central storage and never sit on the device. Where it fits: a follow-up to the room-side mapping basic (PRD-09/PROVIDER-ROOMSIDE) that adds photo capture; it reuses the photos module (PRD-05) and the signed-URL posture (ADR-0009), and capture is gated on image-use consent. No photo persists on the device after sync (C14).

## How it works

Native-camera before/after capture gated on image-use consent: request a per-image signed upload URL (a temporary, expiring link, ADR-0009), stream the image straight to central storage, and discard the local file once sync confirms — no photo persists on device after sync (C14), only a transient capture cache.
Capture is blocked when image-use consent is absent. Photos attach to the PRD-05 ChartEntry as the visit's before/after, and surface to the client via the consent-gated gallery (PHOTO-COMPARE).

## Requirements

- To capture before/after photos at the chair without them being stored on the device.

## Acceptance Criteria

- [ ] Native-camera before/after capture is gated on image-use consent — capture is blocked when consent is absent.
- [ ] Each image streams to central storage via a per-image short-lived signed URL (a temporary, expiring link to a stored photo).
- [ ] No photo persists on the device after sync (C14) — only a transient capture cache.
- [ ] Captured photos attach to the PRD-05 ChartEntry as before/after for this visit.

## UI designs / screenshots

- Prototype: treatment-room — Photos step; native-camera before/after capture.
- Capture blocked without image-use consent; none persist on device after sync (C14).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Photo** — PRD-05 — before/after via signed URLs; consent-gated; no device retention (C14)
  - _Extends PROVIDER-ROOMSIDE; transient capture cache only._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Native-camera before/after capture via signed-URL upload (no device retention)**
  Behaviour: native-camera before/after capture gated on image-use consent. Requirements: request a per-image signed upload URL (a temporary, expiring link, ADR-0009), stream the image straight to central storage, and discard the local file once sync confirms — no photo persists on device after sync (C14), only a transient capture cache; capture is blocked when image-use consent is absent.
