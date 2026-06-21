# Provider app: room-side charting, camera & finalise

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-ROOMSIDE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/MAPPING`, `PRD-05/PHOTOS`

## Background

As a injector, I want to map injections, capture photos and finalise the chart room-side, so that the full clinical record is captured at the chair.
Map injections, capture photos via signed URLs (never on device), record consult/link script and finalise — all surfacing PRD-04/05 (REQ-APP-2, C14/ADR-0009).

## How it works

Room-side charting on the provider app: map injections, capture photos via signed URLs (never on device), record consult/link script and finalise — surfacing PRD-04/05. Thumb-first, gloves-on usability; finalisation is server-side and the entry becomes read-only once final.
The hero clinical workflow at the chair.

## Requirements

- To map injections, capture photos and finalise the chart room-side.
- Compliance: [C14](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Provider app surfaces PRD-05 mapping/photos and PRD-04 consult/Rx/administration.
- [ ] Photos capture to central storage via signed URLs; none persist on device after sync (C14).
- [ ] Finalisation is server-side; once finalised the entry is read-only.
- [ ] Thumb-first, gloves-on usability (UX §1).

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: provider app (treatment-room.png) — 'Treatment record', 'Treatment settings', the injection map + camera; finalise locks the note.
- Photos capture to central storage; none persist on device after sync (C14).

![treatment-room — prototype screen](../screens/treatment-room.png)

## Suggested data model

- **(reuses)** — ChartEntry/InjectionPoint/Photo (PRD-05), Administration (PRD-04)
  - _Same entities; provider-app surface._

## Technical notes (high level)

- Stack: Flutter provider app
- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C14); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
