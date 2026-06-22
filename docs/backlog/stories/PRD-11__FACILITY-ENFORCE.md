# Facility: blocking-vs-advisory enforcement

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/FACILITY-ENFORCE`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/FACILITY`

## Background

As a owner, I want to choose whether a lapsed accreditation blocks or merely warns, so that enforcement matches our clinic's regulatory posture.
Plainly: let each clinic choose whether a lapsed accreditation blocks operations or merely warns. Where it fits: a follow-up to the facility accreditation register (PRD-11/FACILITY) that adds the enforcement decision; per RECON-2 (non-surgical injectables) accreditation is optional/conditional, so this is a per-clinic config flag read at the relevant guard points, defaulting advisory (the open question).

## How it works

Let each clinic choose whether a lapsed accreditation blocks or merely warns: a per-clinic config flag (blocking | advisory) read at the relevant guard points. It defaults advisory per RECON-2 (accreditation optional/conditional for non-surgical injectables — the open question).
When set to blocking, a lapsed accreditation gates the guarded operation; when advisory, it surfaces a warning only. Accreditation changes are audited. This builds on the register (PRD-11/FACILITY) and complements the warning alerts (FACILITY-ALERTS).

## Requirements

- To choose whether a lapsed accreditation blocks or merely warns.

## Acceptance Criteria

- [ ] A per-clinic config flag (blocking | advisory) is read at the relevant guard points.
- [ ] It defaults advisory per RECON-2 (accreditation optional/conditional for non-surgical injectables — the open question).
- [ ] When blocking, a lapsed accreditation gates the guarded operation; when advisory, it warns only.
- [ ] Accreditation changes are audited.

## UI designs / screenshots

- Prototype: Operations / facility profile — blocking-vs-advisory setting per clinic (defaults advisory).
- Read at the relevant guard points; accreditation changes audited.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) FacilityAccreditation + clinic config** — per-clinic flag accreditation_enforcement(blocking|advisory)
  - _Extends FACILITY; read at guard points; defaults advisory (RECON-2 open question)._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Blocking-vs-advisory config flag**
  Behaviour: let each clinic choose whether a lapsed accreditation blocks or merely warns. Requirements: a per-clinic config flag (blocking | advisory) read at the relevant guard points, defaulting advisory per RECON-2 (accreditation optional/conditional for non-surgical injectables — the open question); audit accreditation changes.
