# Standardised before/after photos + compare

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/PHOTOS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-03/IMAGE-CONSENT`

## Background

As a injector, I want to capture standardised before/after photos and compare them against prior visits, so that I can track outcomes consistently.
Capture standardised before/after photos room-side (framing/ghosting guide), compare side-by-side across visits; media stored centrally via signed URLs, never on personal devices, gated by image-use consent (REQ-CLIN-3, C14/ADR-0009).

## How it works

As an injector, I want to capture standardised before/after photos and compare them against prior visits, so that I can track outcomes consistently.
Clinical photography is both an outcomes tool and a privacy hazard. The Lounge captures standardised before/after images room-side with a framing/ghosting guide so shots are comparable across visits, but every image is PHI: it is stored centrally via short-lived signed URLs, never persisted on a personal device, and cannot be captured without current image-use consent (C14/ADR-0009).
Capture is gated on image-use consent (PRD-03): if the client's separate image-use consent is missing or withdrawn, the camera/upload control is blocked with a reason, and any downstream use stops when consent is withdrawn. With consent present, the clinician captures via the provider-app camera (or uploads) using a fixed pose preset and a ghost overlay of the matching prior photo, so the new shot aligns and before/afters differ only by the treatment.
Images are written straight to private central storage (Azure Blob, AU-resident) and only ever surfaced through short-lived signed URLs — never embedded as bytes in the clinical record and never left on the device beyond a transient, encrypted sync cache that is cleared after upload (ADR-0009). Each Photo carries framing metadata (pose preset), the capturing consent reference and the link to its ChartEntry/client.
The before/after view is a drag-to-compare slider across visits (the prototype shows '12 weeks apart · stored securely, never on device'); a gallery groups a client's photos by pose so the same angle compares cleanly. Lightweight annotation is supported on a copy, never destroying the original.
This story owns the capture + compare + storage rules; the standardised-pose presets and outcomes table live in the Clinical → Photography & outcomes screen (shared with OUTCOMES).

## Requirements

- To capture standardised before/after photos and compare them against prior visits.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Camera/upload offers a standardised framing/ghosting guide (pose preset + ghost overlay of the matching prior photo); before/after compares side-by-side across visits.
- [ ] Capture is blocked without current image-use consent (PRD-03); a withdrawn consent stops downstream use of the image.
- [ ] Photos are stored centrally and only served via short-lived signed URLs; nothing persists on the device beyond a transient encrypted sync cache that is cleared after upload.
- [ ] Lightweight annotation is supported on a copy; the original capture is preserved.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Charting right rail 'Before / after · drag to compare': an overlaid pair with a draggable divider (initBA), 'Before'/'After' labels, and the caption '12 weeks apart · stored securely, never on device'.
- Photography & outcomes: 'Standardised photography' card with pose-preset chips (Frontal / Left 45° / Right 45° / Smile dynamic — addPose/removePose) and a 'Live + ghost overlay' figure (the prior photo at low opacity to align the new shot).
- Capture/upload control is gated: when image-use consent is missing or withdrawn it is disabled with the reason and who can resolve it.
- New vs the prototype (build these): the real camera/upload pipeline with signed-URL writes, the consent gate, the per-pose gallery across visits, and copy-based annotation.

![clinical-imaging — prototype screen](../screens/clinical-imaging.png)

## Suggested data model

- **Photo** — id, tenant_id, client_id, chart_entry_id (nullable), blob_ref (private), pose_preset, framing_meta (json), taken_at, captured_by, image_consent_id (FK), annotated_copy_ref (nullable)
  - _Central private storage; served only via short-lived signed URLs; never on device (C14/ADR-0009)._
- **ImageConsent (PRD-03, referenced)** — id, client_id, scope, granted_at, withdrawn_at
  - _Capture checks granted & not withdrawn; withdrawal stops downstream use._
- **PosePreset** — id, tenant_id, name (Frontal / Left 45° / ...), order
  - _Drives the ghost-overlay alignment and groups the compare gallery by angle._

## Technical notes (high level)

- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations: Photo + PosePreset**
  EF Core: Photo (client_id, chart_entry_id, blob_ref to private storage, pose_preset, framing_meta json, taken_at, captured_by, image_consent_id FK, annotated_copy_ref) + PosePreset (tenant-scoped pose list). Every table tenant_id + RLS. The clinical record stores only the blob reference + metadata — never image bytes. Index Photo by client and by pose for the compare gallery.
- [ ] **Media pipeline: signed-URL upload/serve + consent gate**
  Server-issued short-lived signed URLs for both upload (write to private AU-resident Blob, ADR-0009) and read; no public URLs, no bytes through the API. The capture/serve endpoints check current image-use consent (PRD-03) and refuse when missing/withdrawn; a consent-withdrawal event revokes downstream access. Write an AuditEvent for capture, view and annotation. Enforce these as server-side invariants (C14) — never trust the client.
- [ ] **Capture + before/after compare UI**
  Provider/web UI: camera/upload with a pose preset + ghost overlay of the matching prior photo for alignment; the drag-to-compare before/after slider; a per-pose gallery across visits; copy-based annotation that preserves the original. Gate the capture control on image-use consent with a clear blocked-action reason. Loading/empty/error states; capability-gated to clinical roles.
- [ ] **On-device transient cache + post-sync purge**
  Provider app: photos captured offline go to an encrypted on-device queue with the rest of the chart (see OFFLINE) and upload via signed URL on reconnect; the device cache holds nothing beyond the transient pre-sync copy and is purged after a confirmed upload (ADR-0009/0015). No image is ever written to the device gallery or persisted long-term on the device.
