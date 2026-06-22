# Continuity-of-care contact

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/CONTINUITY-CONTACT`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/EMERGENCY-KIT`

## Background

As a owner, I want to record a continuity-of-care contact for when a prescriber is unavailable, so that there's cover and a named fallback when the treating practitioner can't be reached.
Plainly: record a backup contact for when the treating practitioner/prescriber is unavailable, satisfying the AHPRA (Australian Health Practitioner Regulation Agency) continuity-of-care obligation. Where it fits: a follow-up to the emergency kit register (PRD-11/EMERGENCY-KIT) that adds continuity-of-care; the contact is surfaced when the prescriber is unavailable, beside the complication-response flow.

## How it works

Record a backup contact for when the prescriber is unavailable: model ContinuityContact (name, role, phone) and surface it when the treating practitioner/prescriber is unavailable, satisfying the AHPRA (Australian Health Practitioner Regulation Agency) continuity-of-care obligation (C20).
It sits beside the complication-response flow (PRD-05) so cover is to hand in an emergency. This complements the emergency kit register (PRD-11/EMERGENCY-KIT) as the people-side of being prepared.

## Requirements

- To record a continuity-of-care contact for when a prescriber is unavailable.

## Acceptance Criteria

- [ ] A continuity-of-care contact (name, role, phone) is recorded.
- [ ] It is visible when the treating practitioner/prescriber is unavailable.
- [ ] It satisfies the AHPRA continuity-of-care obligation (C20).
- [ ] Records are audited.

## UI designs / screenshots

- Prototype: Clinical → Complication protocols (clinical-safety) — continuity-of-care contact surfaced when the prescriber is unavailable.
- Name · Role · Phone; audited.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **ContinuityContact** — id, tenant_id, name, role, phone
  - _New entity; surfaced when the prescriber is unavailable; complements EMERGENCY-KIT._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **ContinuityContact record + visibility**
  Behaviour: record a backup contact for when the prescriber is unavailable. Requirements: model ContinuityContact (name, role, phone) and surface it when the treating practitioner/prescriber is unavailable, satisfying the AHPRA (Australian Health Practitioner Regulation Agency) continuity-of-care obligation (C20).
