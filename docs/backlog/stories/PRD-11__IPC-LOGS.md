# Infection-control & waste logs

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/IPC-LOGS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

As a staff member, I want to keep infection-control logs for sterilisation/single-use and sharps/clinical-waste disposal, so that we evidence safe practice.
Sterilisation/single-use, sharps & clinical-waste disposal logs, all audited (REQ-FAC-2, C20). Fuller v2 adds manifests + sterilisation register.

## How it works

Infection-control logs: sterilisation/single-use and sharps/clinical-waste disposal, all audited and retrievable for inspection. A twice-daily cold-chain log with a breach pathway is supported (links PRD-04 cold-chain); waste manifests + a sterilisation register are captured for v2 expansion.
Day-to-day evidence of safe practice (C20).

## Requirements

- To keep infection-control logs for sterilisation/single-use and sharps/clinical-waste disposal.
- Compliance: [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Sterilisation/single-use and sharps/clinical-waste disposals can be logged and are audited.
- [ ] Logs are retrievable for inspection (feeds PRD-08 pack).
- [ ] A twice-daily cold-chain log with a breach pathway is supported (links PRD-04 cold-chain).
- [ ] Waste manifests/sterilisation register are captured for v2 expansion.

## UI designs / screenshots

_Prototype screen: prototype.html — Front desk/Operations (Open/close & fridge log, Temperature monitors, Rooms & devices, Equipment, Call log); backroom.html._

- Prototype: Operations -> Open/close & fridge log (ops-openclose.png) + the back-office waste log (backroom.png) — sterilisation/single-use, sharps & clinical-waste entries.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **InfectionControlLog** — id, tenant_id, location_id, kind(sterilisation|single_use|sharps|clinical_waste), detail, at, actor_id
  - _Audited; feeds inspection pack._
- **WasteManifest** — id, tenant_id, stream(clinical|sharps), carrier, certificate_ref, at
  - _NSW CA+TC / QLD WTC (v2 expansion)._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - InfectionControlLog — id, tenant_id, location_id, kind(sterilisation|single_use|sharps|clinical_waste), detail, at, actor_id (Audited; feeds inspection pack.)
  - WasteManifest — id, tenant_id, stream(clinical|sharps), carrier, certificate_ref, at (NSW CA+TC / QLD WTC (v2 expansion).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Sterilisation/single-use and sharps/clinical-waste disposals can be logged and are audited.
  - Rule: Logs are retrievable for inspection (feeds PRD-08 pack).
  - Rule: A twice-daily cold-chain log with a breach pathway is supported (links PRD-04 cold-chain).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
- [ ] **Enforce compliance gate + audit events**
  Enforce C20 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Web UI**
  Build on the Angular web app: the ops-openclose per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Operations -> Open/close & fridge log (ops-openclose.png) + the back-office waste log (backroom.png) — sterilisation/single-use, sharps & clinical-waste entries.
