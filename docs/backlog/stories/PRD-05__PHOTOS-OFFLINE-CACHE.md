# Clinical photos: on-device transient cache & post-sync purge

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/PHOTOS-OFFLINE-CACHE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/PHOTOS`

## Background

As a injector, I want photos taken offline to queue encrypted on the device and be purged after upload, so that I never lose a photo mid-treatment and no clinical image lingers on the device.
Plainly: when a photo is taken in a room with no Wi-Fi, it is held in a locked, temporary spot on the device just long enough to upload — then wiped, so no clinical image ever lingers on a personal device. Where it fits: a follow-up to PRD-05/PHOTOS that adds the offline-capture path on top of signed-URL storage, riding the charting offline queue (PRD-05/OFFLINE). It enforces the privacy rule (C14/ADR-0009) that nothing persists on the device beyond a transient, encrypted pre-sync copy.

## How it works

This follow-up adds the offline-capture path on top of signed-URL storage. Photos captured offline go to an encrypted on-device queue with the rest of the chart (PRD-05/OFFLINE) and upload via signed URL on reconnect.
The device cache holds nothing beyond the transient pre-sync copy and is purged after a confirmed upload (ADR-0009/0015) — no image is ever written to the device gallery or persisted long-term on the device. This is the privacy invariant (C14) made true on the device, not just the server.
A photo's pending/uploaded state is shown alongside the chart's sync indicator so the clinician knows the image is safe.

## Requirements

- Photos taken offline to queue encrypted on the device and be purged after upload.

## Acceptance Criteria

- [ ] Photos captured offline go to an encrypted on-device queue with the rest of the chart (PRD-05/OFFLINE) and upload via signed URL on reconnect.
- [ ] The device cache holds nothing beyond the transient pre-sync copy and is purged after a confirmed upload.
- [ ] No image is ever written to the device gallery or persisted long-term on the device (C14/ADR-0009).
- [ ] A photo's pending/uploaded state is visible alongside the chart's sync state.

## UI designs / screenshots

- A pending-photo affordance alongside the chart's sync/offline indicator; the photo clears 'pending' once uploaded.
- No device-gallery write; nothing persists beyond the transient encrypted pre-sync copy.
- Primarily a provider-app surface (PRD-09).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **LocalQueue (device, referenced)** — pending photos held encrypted at rest with the chart; purged after a confirmed signed-URL upload
  - _Extends the basic's Photo pipeline onto the device — rides the charting offline queue (PRD-05/OFFLINE); no long-term device persistence (C14/ADR-0009)._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **On-device transient cache + post-sync purge**
  Provider app: photos captured offline go to an encrypted on-device queue with the rest of the chart (see PRD-05/OFFLINE) and upload via signed URL on reconnect; the device cache holds nothing beyond the transient pre-sync copy and is purged after a confirmed upload (ADR-0009/0015). No image is ever written to the device gallery or persisted long-term on the device.
