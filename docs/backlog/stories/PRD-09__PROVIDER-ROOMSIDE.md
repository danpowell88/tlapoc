# Provider app: room-side charting, camera & finalise

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-ROOMSIDE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/MAPPING`, `PRD-05/PHOTOS`

## Background

As a injector, I want to map injections, capture photos and finalise the chart room-side, so that the full clinical record is captured at the chair.
Plainly: the chairside app where the injector maps each injection, photographs before/after, links the script and seals the record. Where it fits: the hero clinical workflow on the provider app, a late surface that reuses the mapping/photos (PRD-05) and prescribing (PRD-04) modules built earlier. Map injections, capture photos via signed URLs (never on device), record consult/link script and finalise — all surfacing PRD-04/05 (REQ-APP-2, C14/ADR-0009).

## How it works

Room-side charting on the provider app: tap-to-place injection mapping (drag to adjust, product/units per point), link script, native-camera before/after photos, and consult/Rx/administration — surfacing PRD-05 and PRD-04. Photos upload to central storage via short-lived signed URLs (ADR-0009); none persist on device after sync (C14) and capture requires image-use consent.
Finalisation is server-side and the entry becomes read-only once sealed (AC6). Thumb-first, gloves-on usability (UX §1). The hero clinical workflow at the chair.

## Requirements

- To map injections, capture photos and finalise the chart room-side.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Provider app surfaces PRD-05 mapping/photos and PRD-04 consult/Rx/administration.
- [ ] Photos capture to central storage via signed URLs (temporary, expiring links to stored photos); none persist on device after sync (C14).
- [ ] Finalisation is server-side; once finalised the entry is read-only.
- [ ] Thumb-first, gloves-on usability (UX §1).

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: treatment-room — steps Today · Pre-flight · Consent & script · Injection map · Photos · Complete.
- 'Treatment record' / 'Treatment settings'; tap-to-place injection map (drag to adjust), product/units per point, link script, native-camera before/after.
- Finalise locks the note; none persist on device after sync (C14).

![treatment-room — prototype screen](../screens/treatment-room.png)

## Suggested data model

- **(reuses) ChartEntry/InjectionPoint** — PRD-05 — note + mapped points (site, product, units)
  - _Same entities; provider-app surface._
- **(reuses) Photo** — PRD-05 — before/after via signed URLs; consent-gated; no device retention (C14)
  - _Transient capture cache only._
- **(reuses) Administration** — PRD-04 — product/units administered, linked script
  - _Surfaced room-side._

## Technical notes (high level)

- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Pre-flight + consent/script verification step**
  Behaviour: a room-side pre-flight read (alerts, allergies, history, goals) and a 'Consent & script' step showing signed consent + the prescriber's authorised dose, both verified before mapping. Requirements: surfaces the PRD-03/04 gate state and the linked script; the injection-map / photos / complete steps stay locked until pre-flight + consent + script pass; thumb-first, gloves-on layout (UX §1).
- [ ] **Tap-to-place injection-mapping canvas (product/units, script-linked)**
  Behaviour: a tap-to-place injection-mapping canvas on a face/body image — drag to adjust each point, capture product + units per point, with a live units total checked against the script. Requirements: accurate hit-testing on a touch canvas (highest app risk — SPIKE-CANVAS); writes to the PRD-05 ChartEntry/InjectionPoint entities via the API; surfaces PRD-04 consult/Rx/administration; gloved-hand target sizes.
- [ ] **Native-camera before/after capture via signed-URL upload (no device retention)**
  Behaviour: native-camera before/after capture gated on image-use consent. Requirements: request a per-image signed upload URL (a temporary, expiring link, ADR-0009), stream the image straight to central storage, and discard the local file once sync confirms — no photo persists on device after sync (C14), only a transient capture cache; capture is blocked when image-use consent is absent.
- [ ] **Server-side finalise → immutable record + stock decrement**
  Behaviour: 'Complete' seals the record. Requirements: finalisation is server-side — it decrements the exact batch/lot (the manufacturer's batch of a medicine vial) from inventory and pushes aftercare to the client app; the app re-fetches the sealed, read-only entry so it shows immutable (AC6); corrections are appended amendments, never edits; finalise is disabled until everything has synced (ties to PROVIDER-OFFLINE).
