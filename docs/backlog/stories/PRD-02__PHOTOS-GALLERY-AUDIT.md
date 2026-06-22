# Before/after photo gallery: photo-view audit events

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/PHOTOS-GALLERY-AUDIT`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/PHOTOS-GALLERY`

## Background

As a compliance officer, I want every photo view recorded in the audit log, so that image access is demonstrable to a regulator.
Plainly: writing an audit record every time a clinical photo is viewed in the gallery. Where it fits: a follow-up to the before/after gallery basic consent-gated view (PRD-02/PHOTOS-GALLERY) that adds view-level auditing on top of the consent-gated, signed-URL photo set. It satisfies compliance criteria C10 (audited PII access) and C14 (image-use consent) by making image access demonstrable. It sits on the Client 360 profile in Reception (PRD-02).

## How it works

The basic story serves the consent-gated photo set; this follow-up adds the audit trail over it. Every time a photo is viewed, an AuditEvent (actor, client_id, photo_id, at) is written to the append-only audit stream (ADR-0010).
This makes image access demonstrable to a regulator (C10/C14) — the clinic can show exactly who viewed which client's photos and when.
Viewing while consent is withdrawn is impossible by construction (the basic issues no signed URL when consent is withdrawn), so the audit trail only ever records consent-valid views.

## Requirements

- Every photo view recorded in the audit log.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Every photo view is recorded (actor, client, photo, at) in the append-only audit stream.
- [ ] Image access is demonstrable to a regulator (C10/C14).
- [ ] Viewing while consent is withdrawn is impossible by construction (no URL issued by the basic).

## UI designs / screenshots

- No new screen — auditing is behind the gallery view in the Photos tab (client-360.png).
- Each photo view writes an AuditEvent to the append-only stream.
- No view is possible while consent is withdrawn (no signed URL issued).

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **AuditEvent (ref)** — actor, client_id, photo_id, at
  - _Append-only (ADR-0010); written on every photo view; image access demonstrable (C10/C14)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Photo-view audit events (C10/C14)**
  Behaviour: every time a photo is viewed, record it. Requirements: write an AuditEvent (actor, client_id, photo_id, at) to the append-only stream (ADR-0010) so image access is demonstrable to a regulator; viewing while consent is withdrawn is impossible by construction (no URL issued).
