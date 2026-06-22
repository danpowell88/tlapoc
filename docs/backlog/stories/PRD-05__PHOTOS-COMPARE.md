# Clinical photos: before/after compare, per-pose gallery & annotation

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/PHOTOS-COMPARE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/PHOTOS`

## Background

As a injector, I want to compare before/after photos across visits, browse them by pose, and annotate a copy, so that I can track outcomes consistently without altering the original images.
Plainly: this lets the clinician line up a new photo against an earlier one and drag a slider to see the difference, browse a client's shots grouped by camera angle, and mark up a copy without touching the original. Where it fits: a follow-up to PRD-05/PHOTOS that adds the comparison and review layer on top of capture + storage. It reads the same signed-URL stored photos (never on device) and respects image-use consent (C14), and it underpins outcomes tracking (PRD-05/OUTCOMES).

## How it works

This follow-up adds the comparison and review layer on top of capture + storage. At capture, a ghost overlay of the matching prior photo (at low opacity) helps the clinician align the new shot so before/afters differ only by the treatment.
The before/after view is a drag-to-compare slider across visits (the prototype shows '12 weeks apart · stored securely, never on device'); a per-pose gallery groups a client's photos by pose so the same angle compares cleanly (initBA + PosePreset grouping).
Lightweight annotation is supported on a copy, never destroying the original. Every served image still flows through short-lived signed URLs and respects image-use consent (C14/ADR-0009) — the compare/gallery never embeds bytes or persists to the device.

## Requirements

- To compare before/after photos across visits, browse them by pose, and annotate a copy.

## Acceptance Criteria

- [ ] A ghost overlay of the matching prior photo aids alignment at capture so before/afters differ only by the treatment.
- [ ] A drag-to-compare before/after slider compares photos side-by-side across visits.
- [ ] A per-pose gallery groups a client's photos by angle so the same angle compares cleanly.
- [ ] Lightweight annotation is supported on a copy; the original capture is preserved, and any served image still uses short-lived signed URLs (C14).

## UI designs / screenshots

- Charting right rail 'Before / after · drag to compare': an overlaid pair with a draggable divider (initBA), 'Before'/'After' labels, and the caption '12 weeks apart · stored securely, never on device'.
- Photography & outcomes: a 'Live + ghost overlay' figure (the prior photo at low opacity to align the new shot) and a per-pose gallery across visits.
- Copy-based annotation that preserves the original; any served image uses short-lived signed URLs.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Photo (referenced)** — annotated_copy_ref (the annotation copy; original preserved); grouped by pose_preset for the gallery
  - _Extends the basic's Photo — no new entity; the compare slider + per-pose gallery + copy-based annotation read the stored photos via signed URLs._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Ghost overlay + before/after compare + per-pose gallery + annotation (UI)**
  Behaviour: a ghost overlay of the matching prior photo at capture, a drag-to-compare before/after slider across visits, a per-pose gallery grouping a client's photos by angle, and copy-based annotation that preserves the original (initBA + PosePreset grouping). Requirements: every served image uses short-lived signed URLs and respects image-use consent (C14/ADR-0009); annotation writes a copy, never the original; capability-gated to clinical roles.
