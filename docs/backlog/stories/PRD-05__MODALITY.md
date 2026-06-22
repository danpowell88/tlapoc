# Other-modality charting: filler / energy / weight-loss (placeholder)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/MODALITY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** provider-app

## Background

As a injector, I want modality-aware charting for filler, energy devices and weight-loss, so that the platform covers the full treatment menu.
A Phase-2 placeholder for charting other modalities (categories of treatment beyond toxin injectables) — dermal filler, energy/laser devices and weight-loss. v1 ships only the toxin chart and a non-S4 skin note, but the charting engine is built modality-aware now so these slot in later. A deferred design-only card under PRD-05 charting (depended on by BODY-CONTOURING); nothing builds in v1 beyond the modality model already in MAPPING and NOTE-TEMPLATE. Phase 2 adds dermal filler (multi-area, per-area lot, vascular occlusion (VO)/blindness consent gate), energy-device charting (per-pass settings, laser-licence gated), weight-loss titration and ghost-overlay photo alignment (REQ-CLIN-10..13). Placeholder.

## How it works

As an injector, I want modality-aware charting for filler, energy devices and weight-loss, so that the platform covers the full treatment menu.
Placeholder / Phase 2. v1 ships toxin + a non-S4 skin note, but the charting engine is built modality-aware from day one (ADR-0025) so these extensions slot in without re-architecting the clinical record. This story captures each modality's specific gates and capture surface so the later build is a known quantity.
Treatment is modelled as a typed modality carrying {schedule, regClass, daenRoute, unit, advertisable, requires:[consult|rx|s4Lot|laserLicence|patchTest]} (ADR-0025). The modality drives the capture surface and the compliance behaviour: dermal filler is multi-area / multi-syringe with per-area lot and a mandatory vascular-occlusion / blindness consent gate; energy-device charting is a per-pass settings/fluence logbook with skin-typing + patch-test + safety checks, blocked without a state laser licence (no Schedule 4 'Prescription Only Medicine' (S4)); weight-loss is a titration protocol with Australian Register of Therapeutic Goods (ARTG)-brand enforcement (compounded GLP-1 refused); standardised photography gains ghost-overlay alignment.
Adverse-event routing is modality-derived: toxin & filler-as-medicine route to Database of Adverse Event Notifications (DAEN)-medicines; device-class filler/PDO/RF route to DAEN-devices (extends ADVERSE-EVENT / C12). The catalogue's existing s4 flag is extended (not replaced) with regClass/artg/compounded/daenRoute, and a new laserLicence credential (per state/class) gates energy-device booking and charting.
No build in v1 beyond the modality model already present in MAPPING / NOTE-TEMPLATE; this card holds the design and the gates so the Phase-2 stories (e.g. BODY-CONTOURING) extend it cleanly.

## Requirements

- Modality-aware charting for filler, energy devices and weight-loss.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — v1 ships toxin + non-S4 skin notes; the modality model (typed chart, product-class routing, licence gating) already anticipates these.
- [ ] Each modality's specific gates are captured for later build: filler VO/blindness consent gate + per-area lot; energy-device laser-licence + patch-test + per-pass fluence logbook; weight-loss titration + ARTG/compounded enforcement.
- [ ] Adverse-event routing is modality-derived (medicine vs device DAEN); standardised photography gains ghost-overlay alignment.

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Clinical -> Treatment menu: each treatment's category sets its compliance behaviour (schedule, custody, consent, adverse event (AE) routing, rewards/ads) - the modality model in action (ADR-0025).
- Body contouring + the skin note show non-toxin capture surfaces; filler/energy/weight-loss are concept cards for v1.
- Deferred - no v1 build; the model already carries the requires:[] gates so Phase-2 stories extend it.

![clinical-body — prototype screen](../screens/clinical-body.png)

## Suggested data model

- **Modality (catalogue, ADR-0025)** — schedule, regClass, daenRoute (medicine|device), unit, advertisable, requires:[consult|rx|s4Lot|laserLicence|patchTest]
  - _Extends the existing s4 flag with regClass/artg/compounded/daenRoute; drives capture surface + compliance._
- **ChartEntry.treatment_type (extended)** — + modality-specific payloads (filler areas/syringes, device passes/fluence, titration steps)
  - _Filler adds a VO/blindness consent gate + per-area lot; energy requires a laserLicence credential._
- **LaserLicence (credential)** — id, staff_id, state, class, expiry
  - _Gates energy-device booking + charting (per state/class)._

## Technical notes (high level)

- Architecture decisions: [ADR-0025](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Scope & design the modality extensions when pulled into a sprint**
  Deferred placeholder - no build in v1. The modality model (ADR-0025) already exists in the catalogue + charting; this task is to confirm it still fits scope/regulatory stance, then break down per modality: filler (multi-area/multi-syringe, per-area lot, mandatory VO/blindness consent gate), energy device (per-pass settings/fluence logbook, skin-typing + patch-test, laser-licence gate, no S4), weight-loss (titration protocol, ARTG/compounded enforcement), and ghost-overlay photo alignment. Capture each modality's DAEN routing (medicine vs device).
