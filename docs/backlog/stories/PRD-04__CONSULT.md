# Synchronous consult record

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/CONSULT`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-02/CONSULT-GATE`, `PRD-03/GATING`

## Background

As a prescriber, I want to record a synchronous consult (in person or from our external telehealth app) before writing any script, so that every prescription is backed by a real assessment.
A Consult (in-person or external-telehealth) records modality, prescriber, timestamp, external reference and notes — required before any script (C1).

## How it works

A synchronous Consult is the first link in the moat chain and the legal precondition for any S4 prescription (C1). Botulinum toxin is a Schedule 4 medicine: AHPRA's cosmetic-procedures guidelines (eff. 2 Sept 2025) prohibit prescribing without a real-time assessment — no async (text/email/online-only) prescribing is lawful.
The clinic runs two consult modalities: in-person (NP/designated-RN-prescriber at the clinic) and external-telehealth (a remote doctor/NP using the clinic's existing telehealth app). Per ADR-0011 the platform does NOT build video; it records the consult metadata that proves a synchronous assessment happened and binds it to the resulting script.
A Consult records modality (in_person | telehealth_ext), the prescriber identity, an exact timestamp, an external reference (the telehealth session id/notes for the remote path) and assessment notes. It is scoped to the client and the appointment.
The Consult must exist and be recent at script time: the Prescription write (PRD-04/PRESCRIPTION) fails its server-side invariant if there is no linked Consult for the same client created at or just-before the script. The 'just-before' window is a configurable staleness bound, not a UI hint.
For the remote-prescriber path the consult is conducted externally; the prescriber records that it occurred (with the external_ref) and the resulting individual script links back to this Consult — so the chain holds even though the video never touched the platform (ADR-0011).
Consult creation, edit and link are written to the append-only AuditEvent stream (ADR-0010) — who recorded the assessment, when, and from which modality is part of the audit-ready record.

## Requirements

- To record a synchronous consult (in person or from our external telehealth app) before writing any script.
- Compliance: [C1](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Consult records modality (in-person/telehealth-external), prescriber, timestamp, external reference, notes.
- [ ] A prescription cannot be saved without a linked synchronous consult at/just-before script time.
- [ ] The remote-prescriber path links the externally-conducted consult to the resulting script.
- [ ] Consult creation is audited.

## UI designs / screenshots

- Prototype screen: Charting — pre-treatment review (charting.png).
- Charting opens on the 'Pre-treatment review' step; the 'Consult & prescription' card carries a 'Record consult ✓' action and a 'Write prescription' action.
- The consult tick must be satisfied before 'Write prescription' becomes usable — the card is the visible surface of the C1 gate.
- Modality toggle (in-person / telehealth-external) with an external-reference field shown for the telehealth path; assessment notes captured inline.
- When the current user is an administering RN (not a prescriber) the card instead shows 'Administering on a valid script · Dr Lena Park (NP) · today · 30u authorised · individual (this client)' with a verify-before-administer checkbox.

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Consult** — id, tenant_id, client_id, appointment_id, prescriber_id, modality(in_person|telehealth_ext), at, external_ref, notes, created_by, created_at
  - _Required before any Prescription (C1). modality + external_ref carry the telehealth path (ADR-0011). Prototype mapping: the 'Record consult ✓' chip on the charting pre-treatment card._
- **AuditEvent** — id, tenant_id, actor_id, at, entity('consult'), entity_id, action(create|edit|link)
  - _Append-only (ADR-0010); the consult half of the consult->script linkage evidence._

## Technical notes (high level)

- Architecture decisions: [ADR-0011](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Consult entity + consult->script link (model & migration)**
  Add the Consult table: id, tenant_id, client_id, appointment_id, prescriber_id, modality(in_person|telehealth_ext), at, external_ref, notes, created_by, created_at; tenant_id RLS-scoped. FK from Prescription.consult_id -> Consult(id). Index (client_id, at desc) so the script-write gate can find the most-recent consult for a client fast. external_ref is nullable but required when modality=telehealth_ext (CHECK constraint). No edit-in-place semantics beyond notes; audit captures changes.
- [ ] **Consult API + telehealth-external path**
  Endpoints: POST /clients/{id}/consults (create), PATCH /consults/{id} (notes/external_ref only), GET /clients/{id}/consults?recent. Server sets at server-side (don't trust client clock). The remote path accepts modality=telehealth_ext + external_ref (the external telehealth session reference) — the platform stores metadata only, never video (ADR-0011). Prescriber identity must resolve to a credential-gated prescriber (NP / remote / designated-RN-prescriber); reject otherwise. Keep modality + prescriber model configurable to absorb the WATCH-1 telehealth national review.
- [ ] **C1 consult-gate invariant + audit**
  Enforce in the domain + DB (ADR-0008), not the UI: a Prescription INSERT must reference a Consult for the SAME client whose at is within the configurable 'synchronous' staleness window of the script time; otherwise reject with an explainable reason. Write an AuditEvent on consult create/edit/link to the append-only stream (ADR-0010). A blocked script attempt is itself audited so the refusal is explainable to a regulator.
