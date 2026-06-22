# Infection-control & waste logs

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/IPC-LOGS`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web

## Background

As a staff member, I want to keep infection-control logs for sterilisation/single-use and sharps/clinical-waste disposal, so that we evidence safe practice.
Sterilisation/single-use, sharps & clinical-waste disposal logs, all audited (REQ-FAC-2, C20). Fuller v2 adds manifests + sterilisation register.

## How it works

Infection-control logs: sterilisation/single-use and sharps/clinical-waste disposals, each with detail, timestamp and actor, tenant/location-scoped and audited, retrievable as an inspection trail (feeds the PRD-08 pack). The cold-chain dimension (twice-daily fridge log + breach pathway, links PRD-04) lives in the OPENCLOSE/TEMP-MONITORS stories and reconciles into one cold-chain record.
Waste manifests (NSW CA+TC / QLD WTC) and a sterilisation register are captured at the model level for v2 expansion. Day-to-day evidence of safe practice (C20).

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

- Prototype: Operations → Open/close & fridge log (ops-openclose) + back-office waste log (backroom) — sterilisation/single-use, sharps & clinical-waste entries (detail, time, actor).
- Logs retrievable as an inspection trail.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **InfectionControlLog** — id, tenant_id, location_id, kind(sterilisation|single_use|sharps|clinical_waste), detail, at, actor_id
  - _Audited; feeds inspection pack._
- **WasteManifest** — id, tenant_id, stream(clinical|sharps), carrier, certificate_ref, at
  - _NSW CA+TC / QLD WTC (v2 expansion)._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **InfectionControlLog entity (append-only, audited)**
  Model InfectionControlLog (tenant_id, location_id, kind[sterilisation|single_use|sharps|clinical_waste], detail, at, actor_id) as an append-only, audited log under RLS.
- [ ] **IPC log entry UI (sterilisation/single-use + sharps/clinical-waste)**
  Quick-entry surface on Operations / back-office waste log to record sterilisation/single-use cycles and sharps/clinical-waste disposals (detail, auto time + actor).
- [ ] **IPC log retrieval / inspection trail**
  Retrieve and filter IPC logs (by kind, date, location) as an inspection trail; expose them to the PRD-08 inspection-readiness pack.
- [ ] **WasteManifest model stub for v2**
  Define WasteManifest (stream[clinical|sharps], carrier, certificate_ref, at) at the model level so the data model anticipates the v2 manifest workflow (NSW CA+TC / QLD WTC); v1 surface only captures disposals, no full carrier/certificate workflow.
