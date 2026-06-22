# Provider app: room-side injection mapping (basic)

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/PROVIDER-ROOMSIDE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-09/PROVIDER-DAY`, `PRD-05/MAPPING`

## Background

As a injector, I want to verify consent/script and map injections at the chair, so that the injection chart is captured room-side against the script.
Plainly: the chairside app at its core — a pre-flight read and consent/script check, then a tap-to-place injection map that records product and units per point against the script. Where it fits: the hero clinical workflow on the provider app, a late surface that reuses the mapping (PRD-05) and prescribing (PRD-04) modules built earlier; this basic slice gets the injection chart captured room-side, with native-camera before/after capture and server-side finalise added as follow-ups. Map injections at the chair surfacing PRD-04/05 (REQ-APP-2).

## How it works

Room-side charting on the provider app at its core: a pre-flight read (alerts, allergies, history, goals) and a 'Consent & script' step showing signed consent + the prescriber's authorised dose, then tap-to-place injection mapping (drag to adjust, product/units per point) with a live units total checked against the script — surfacing PRD-05 mapping and PRD-04 consult/Rx/administration. The injection-map step stays locked until pre-flight + consent + script pass.
Thumb-first, gloves-on usability (UX §1). The hero clinical workflow at the chair. Native-camera before/after capture and server-side finalise are added by the follow-ups (PROVIDER-CAMERA, PROVIDER-FINALISE).

## Requirements

- To verify consent/script and map injections at the chair.

## Acceptance Criteria

- [ ] A room-side pre-flight read and a 'Consent & script' step verify signed consent + the prescriber's authorised dose before mapping.
- [ ] A tap-to-place injection-mapping canvas captures product + units per point, with a live units total checked against the script.
- [ ] Mapping writes to the PRD-05 ChartEntry/InjectionPoint entities via the API and surfaces PRD-04 consult/Rx/administration.
- [ ] Thumb-first, gloves-on usability (UX §1).

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: treatment-room — steps Today · Pre-flight · Consent & script · Injection map.
- 'Treatment record' / 'Treatment settings'; tap-to-place injection map (drag to adjust), product/units per point, link script.
- Photos and Complete steps are added by the follow-ups (PROVIDER-CAMERA, PROVIDER-FINALISE).

![treatment-room — prototype screen](../screens/treatment-room.png)

## Suggested data model

- **(reuses) ChartEntry/InjectionPoint** — PRD-05 — note + mapped points (site, product, units)
  - _Same entities; provider-app surface._
- **(reuses) Administration** — PRD-04 — product/units administered, linked script
  - _Surfaced room-side._

## Technical notes (high level)

- Architecture decisions: [ADR-0009](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Pre-flight + consent/script verification step**
  Behaviour: a room-side pre-flight read (alerts, allergies, history, goals) and a 'Consent & script' step showing signed consent + the prescriber's authorised dose, both verified before mapping. Requirements: surfaces the PRD-03/04 gate state and the linked script; the injection-map step stays locked until pre-flight + consent + script pass; thumb-first, gloves-on layout (UX §1).
- [ ] **Tap-to-place injection-mapping canvas (product/units, script-linked)**
  Behaviour: a tap-to-place injection-mapping canvas on a face/body image — drag to adjust each point, capture product + units per point, with a live units total checked against the script. Requirements: accurate hit-testing on a touch canvas (highest app risk — SPIKE-CANVAS); writes to the PRD-05 ChartEntry/InjectionPoint entities via the API; surfaces PRD-04 consult/Rx/administration; gloved-hand target sizes.
