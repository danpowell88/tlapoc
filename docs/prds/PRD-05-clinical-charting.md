# PRD-05 — Clinical Charting: Injection Mapping & Before/After

> **▸ Option A alignment (rev 2, 2026-06-19).** Charting now **opens with product & batch (lot) selection** (step 1 — the vial being drawn from, restricted to **in-date / ARTG / in-custody** stock) **before** mapping points; charted units **deduct from that selected lot** on finalise (REQ-CLIN-2, REQ-MED-4). Injection mapping (**tap-to-add + drag**) and **before/after drag-compare** are validated. Adds **REQ-CLIN-7 treatment plans & protocols** (multi-session plans + applyable protocol templates feeding recall) and a **charting overview / "in-room now"** entry point. **"Auto-detect" injection points is advisory + human-confirmed only and deferred to Phase 2** (ADR-0020, 🔬 — *no AI in v1*; v1 ships manual mapping). Charting is now a **guided flow** — **pre-treatment review** (safety + last-treatment + consult/Rx surfaced), **treatment-type-aware** (toxin map vs a non-S4 **skin note**) and a **finalise close-out** (aftercare · recall · 2-day wellbeing call · adverse event) before checkout (**REQ-CLIN-9**, ADR-0024). See [requirements §12](../02-requirements.md#12-option-a-prototype-alignment--feasibility-register).
>
> **▸ Option A alignment (rev 4, 2026-06-20).** Charting becomes **modality-aware** (ADR-0025): beyond the toxin map, Phase 2 adds **dermal filler** (multi-area / multi-syringe / per-area lot + a mandatory **vascular-occlusion/blindness consent gate**), **energy-device** charting (per-pass settings/fluence logbook + skin-type/patch-test + safety checks, **gated by a state laser licence**), **weight-loss titration** plans, and **standardised photo capture** with **ghost-overlay** alignment; a **complication-response** flow (VO/anaphylaxis → log hyaluronidase/adrenaline → routed AE + jobs) and **outcome/revision** signal feed reporting (REQ-CLIN-10..13, REQ-FAC-4). The Clinical area in the prototype demonstrates the modality model, complication protocols, photography and outcomes.

> **Phase:** 1 · **Status:** Draft<br>
> **Requirements:** REQ-CLIN-1…6 · **Compliance:** C8, C12, C14<br>
> **ADRs:** 0009 (media/signed URLs), 0010 (immutability), 0015 (offline sync)<br>
> **Depends on:** PRD-01, PRD-03, PRD-04

## 1. Summary
The clinical record that matches the Aesthetic Record / Pabau bar: on-image/diagram **injection
mapping** (product · units · depth · site · **batch-lot**), standardised **before/after photos**
with comparison, immutable finalised notes, and adverse-event logging that feeds the TGA pathway —
all usable room-side on the provider app, even offline.

## 2. Goals & non-goals
**Goals:** templated toxin treatment note; facial-diagram + photo injection mapping with per-point
product/units/depth/lot; standardised photo capture + side-by-side compare; immutable finalisation
with audited amendments; adverse-event capture → DAEN pathway.

**Non-goals (v1):** AI scribe (far future, REQ-CLIN-6); 3D imaging; filler/other-treatment templates
(toxin first); video documentation.

## 3. Users
RN/NP (charting + mapping + photos), dermal therapist (non-S4 skin charting), client (views own photos with consent).

## 4. User stories
- As an **injector**, I chart on a **facial diagram** (and/or the patient photo), dropping injection points that each capture **product, units, depth, technique and batch-lot/expiry**.
- As an **injector**, I take **standardised before/after photos** room-side and compare against prior visits.
- As an **injector**, once I **finalise** the note it's locked; any later change is an **appended, audited amendment**.
- As an **injector** offline in the room, my notes/photos **queue locally and sync** when back online — nothing is lost.
- As an **injector**, I log an **adverse event/complication** linked to the treatment, product and lot.

## 5. Key flow
```mermaid
flowchart TD
  A[Open treatment<br/>(consult+consent verified)] --> B[Pick toxin template]
  B --> C[Map injection points<br/>product/units/depth/site/lot]
  C --> D[Capture before/after photos<br/>(consented; signed-URL upload)]
  D --> E{Online?}
  E -- no --> F[Queue locally (encrypted)]
  F --> G[Sync when connected]
  E -- yes --> H[Save draft]
  G --> H
  H --> I[Finalise → immutable<br/>+ register link (PRD-04)]
  I --> J{Adverse event?}
  J -- yes --> K[Log → DAEN pathway C12]
```

## 6. Functional scope
- **Notes** (REQ-CLIN-1): configurable toxin template; structured + free text; phrases/snippets.
- **Injection mapping** (REQ-CLIN-2, C8): annotate facial diagram and/or uploaded photo; each point = product, units, depth, technique, **batch-lot + expiry** (the per-point lot feeds PRD-04 register + recall).
- **Photos** (REQ-CLIN-3, C14): provider-app camera or upload; standardised framing/ghosting guide; side-by-side compare across visits; annotation; **secure central storage via signed URLs, never on personal devices** (ADR-0009); gated by image-use consent.
- **Immutability** (REQ-CLIN-4, ADR-0010): finalised entries locked; amendments appended + audited.
- **Adverse events** (REQ-CLIN-5, C12): log linked to treatment/product/lot; routes to DAEN-medicines (toxin) with seriousness classification; prefilled export (full pathway in PRD-08/§report).
- **AI scribe** (REQ-CLIN-6): **deferred — far future.**

## 7. Data & entities
`ChartEntry` (immutable on finalise), `InjectionPoint` (product, units, depth, technique, lot, coords),
`Photo` (Blob ref, framing meta, consent link), `Amendment`, `AdverseEvent` (seriousness, product, lot, DAEN target).

## 8. Acceptance criteria
- **AC1 (C8):** Every injection point records product, units, depth, site and **batch-lot/expiry**; the lot links to the medicine register and recall lookup.
- **AC2 (C14):** Photos require current image-use consent; they are stored centrally (signed URLs) and never persisted on the device beyond transient sync cache.
- **AC3 (ADR-0010):** A finalised note cannot be edited; an amendment creates a new linked, audited entry preserving the original.
- **AC4 (ADR-0015):** With connectivity dropped mid-visit, notes/photos are queued and later sync with no loss; finalisation occurs server-side.
- **AC5 (C12):** An adverse event captures the data a TGA report needs, classifies seriousness, and targets the correct DAEN database.
- **AC6:** Before/after photos display side-by-side across visits with consistent framing guidance.

## 9. Dependencies & sequencing
After PRD-04 (lot/register) and PRD-03 (consent/image-use). Heavy on the provider app (PRD-09) — build the mapping canvas as an early spike.

## 10. Out of scope
AI scribe; filler/laser templates; 3D/video.

## 11. Open questions
- Facial-diagram asset + mapping-canvas approach in Flutter (spike).
- Photo standardisation aids (overlay/ghosting) scope for v1.
