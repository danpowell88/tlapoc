# Guided toxin note: pre-treatment review & gate (MVP)

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/NOTE-TEMPLATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

As a injector, I want a guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template, so that I chart quickly and safely with the right context in front of me.
The guided clinical note an injector fills in during a toxin treatment: it surfaces safety and prescription context first, then a templated note. Charting (the clinical record of what was actually done) is the clinical heart of the platform and sits straight after the S4 (Schedule 4 'Prescription Only Medicine') consult/prescribing moat (PRD-04) on the clinic-first build spine; this story is the entry point to the whole PRD-05 charting flow (depends on PRD-04/ADMIN-GATE; depended on by MAPPING, TREATMENT-PLANS, SKIN-ANALYSIS). Charting is a guided, treatment-type-aware flow: a pre-treatment review (safety + last-treatment + consult/prescription (Rx) surfaced) then a configurable toxin note (structured + free text + snippets) (REQ-CLIN-1/9).

## How it works

As an injector, I want a guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template, so that I chart quickly and safely with the right context in front of me.
Charting at The Lounge is not a blank text box — it is a guided, treatment-type-aware flow that puts the safety- and compliance-critical context in front of the clinician before they touch a single field. The note itself is templated (structured fields + free text + reusable phrases) so a routine anti-wrinkle treatment can be charted in under a minute without losing the medico-legal detail an Australian Health Practitioner Regulation Agency (AHPRA) inspection expects.
Step 1 is a Pre-treatment review card the injector reads before anything is editable: safety flags (allergies, contraindications, BDD-screen result), the linked consult/prescription status, and a one-line Last treatment summary (e.g. '24u · 12 Mar · forehead + glabella · Bella RN') with a 'Copy last map' shortcut. These are read-only chips pulled from PRD-03 (intake/consent/screening) and PRD-04 (consult/Rx) — the injector confirms them, the system does not let them be edited here.
A treatment-type toggle (Anti-wrinkle (toxin) / Skin treatment) selects which template renders. The toxin template is a configurable NoteTemplate: structured fields (indication, areas, technique notes, aftercare) plus a free-text area and a library of reusable phrases/snippets the clinic curates. Selecting 'Skin treatment' swaps in a non-S4 skin-note variant (areas / device / settings / consumables) with no prescription or lot — built in PRD-05/MAPPING's skin-note story.
Charting cannot open at all unless the consult + consent gate (PRD-03/PRD-04) is satisfied — the safe path is the only path. The gate state is shown as header chips ('Consult ✓ · Consent ✓ · screening clear'); when it is not satisfied the entry point is blocked with a reason rather than opening a half-usable note.
The same NoteTemplate model is what later modalities (filler, energy, weight-loss) extend, so the template engine is built generically now even though v1 only ships the toxin template and the non-S4 skin variant.

## Requirements

- A guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template.

## Acceptance Criteria

- [ ] Step 1 'Pre-treatment review' surfaces safety flags, the last-treatment summary and the linked consult/Rx as read-only context the injector confirms before the note becomes editable.
- [ ] The toxin template is configurable per tenant: structured fields, free text and reusable phrases/snippets, all versioned.
- [ ] A treatment-type toggle switches between the toxin template and the non-S4 skin-note variant; the rendered fields change accordingly.
- [ ] Charting cannot open unless the consult + consent gate (PRD-03/04) is satisfied; a blocked entry point states why and who can resolve it.
- [ ] 'Copy last map' / copy-last-note pre-fills from the client's previous matching treatment for editing (never auto-finalised).

## UI designs / screenshots

_Prototype screen: prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html._

- Header: 'Charting — {client}' with a green gate chip ('Consult ✓ · Consent ✓ · screening clear') and a 'Read-only view' chip for oversight roles.
- Treatment-type toggle pills: 'Anti-wrinkle (toxin)' (default) / 'Skin treatment' (renderChartReview + applyChartType swap the template).
- Step 1 'Pre-treatment review' card: safety chips (Allergies: none · Contraindications: none · BDD screen: clear · Consent ✓ · Consult ✓), a 'Last treatment' row ('24u · 12 Mar · forehead + glabella · Bella RN') with a 'Copy last map' button, and a 'Consult & prescription' panel that surfaces the synchronous-consult + individual-Rx chain inline (prescriber writes / administrator verifies).
- The toxin note template lives in the same flow; a finalise close-out (aftercare · recall · 2-day wellbeing call · adverse event) captures the wrap-up before checkout (closeoutGo).
- New vs the prototype (build these): the template builder/admin (fields + snippets), template versioning, and the non-S4 skin-note variant toggle wired to its own fields.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **ChartEntry** — id, tenant_id, client_id, appointment_id, consult_id, treatment_type (toxin|skin|...), status (draft|final), author_id, finalised_at, locked
  - _Shared spine with MAPPING; one per treatment. Immutable once final (ADR-0010)._
- **NoteTemplate** — id, tenant_id, treatment_type, version, fields (json schema of structured fields), snippets[] (reusable phrases), active
  - _Configurable per tenant + versioned; the toxin template and the non-S4 skin variant are two instances of the same model._
- **NoteValue** — id, chart_entry_id, template_version, structured (json keyed to template fields), free_text
  - _Captured note content bound to the template version used, so a finalised note always renders against the schema it was written with._

## Technical notes (high level)

- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Gate chips header + blocked entry point**
  Behaviour: the charting header reads 'Charting — {client}' with a live gate chip ('Consult ✓ · Consent ✓ · screening clear') and a 'Read-only view' chip for oversight roles; the charting screen will not open at all unless the consult+consent gate is satisfied. Requirements: the gate is re-checked server-side on open-draft (reject unless PRD-03 consent + PRD-04 consult/Rx are satisfied — never trust the UI, ADR-0008); an unmet gate shows a calm blocked-action banner stating what's missing and who can resolve it rather than a half-usable note. The safe path is the only path.
- [ ] **Pre-treatment review card (safety flags + last-treatment + copy-last)**
  Behaviour: Step 1 is a read-only review the injector confirms before anything becomes editable — safety chips (Allergies / Contraindications / BDD (Body Dysmorphic Disorder) screen result / Consent / Consult), and a 'Last treatment' summary row (e.g. '24u · 12 Mar · forehead + glabella · Bella RN') with a 'Copy last map' / copy-last-note shortcut (prototype renderChartReview/copyLast). Requirements: these chips are pulled from PRD-03 (intake/consent/screening) and PRD-04 (consult/Rx) and are not editable here; 'copy last' pre-fills from the client's previous matching ChartEntry for editing and is never auto-finalised.
- [ ] **Consult & prescription card (role-aware)**
  Behaviour: the pre-treatment card surfaces the synchronous-consult + individual-prescription (Rx) chain inline. For a prescriber (NP/solo) it shows 'Record consult ✓' then 'Write prescription'; for an administering RN it instead shows 'Administering on a valid script · Dr Lena Park (NP) · today · 30u authorised · individual (this client)' with a verify-before-administer checkbox (prototype renderChartReview rx branch). Requirements: this card is the visible surface of the S4 (Schedule 4 prescription-only medicine) gate — the consult tick must be satisfied before 'Write prescription' is usable; the actual consult/Rx records and invariants live in PRD-04 (CONSULT/PRESCRIPTION).
- [ ] **Basic toxin note fields + ChartEntry/NoteValue (model & flow)**
  Behaviour: after the pre-treatment review is confirmed, a basic toxin note renders — a fixed set of structured fields (indication, areas, technique notes, aftercare) plus a free-text area — captured against the ChartEntry. Requirements: add ChartEntry (id, tenant_id, client_id, appointment_id, consult_id, treatment_type, status(draft|final), author_id, finalised_at, locked) and NoteValue (structured json + free_text) bound to the note; tenant_id + Row-Level Security (RLS, the per-tenant database isolation). The configurable/versioned template engine and the type toggle are follow-ups (NOTE-TEMPLATE-ENGINE, NOTE-TEMPLATE-TYPE-TOGGLE) — v1 basic ships a single fixed toxin note.
