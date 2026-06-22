# Temperature logging & excursion alerts

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/COLD-CHAIN`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend, integration
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

As a owner, I want temperature logging for the medicine fridge with excursion alerts, so that we never use medicine that breached cold-chain.
Toxin must stay 2–8°C; temperature logging raises excursion alerts and flags affected stock (C13). Integrates with the optional ESP32 cold-chain monitor.

## How it works

Toxin must stay 2-8C. Temperature can be logged manually and via the device API (ESP32 monitor); an excursion raises an alert and flags affected stock for quarantine, and the breach pathway can quarantine a lot and raise a job (links PRD-11).
Excursion history is retained and visible — evidence that cold-chain held for every lot used (C13).

## Requirements

- Temperature logging for the medicine fridge with excursion alerts.
- Compliance: [C13](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Temperature can be logged (manual + via the device API) for storage locations.
- [ ] An excursion raises an alert and flags affected stock for quarantine.
- [ ] A breach pathway can quarantine a lot and raise a job (links PRD-11).
- [ ] Excursion history is retained and visible.

## UI designs / screenshots

- Prototype: Front desk/Operations -> Temperature monitors (ops-monitors.png) — live/charted fridge temps per location, breach alerts; the stock table shows a per-lot temp (e.g. '4.2C').
- An excursion visibly quarantines the lot and raises a follow-up job.

![ops-monitors — prototype screen](../screens/ops-monitors.png)

## Suggested data model

- **TempLog** — id, tenant_id, location_id, monitor_id, temp, at, source(manual|device)
  - _2-8C range; out-of-range -> Excursion._
- **Excursion** — id, location_id, started_at, ended_at, min, max, affected_lots[], action(quarantine)
  - _Raises alert + job; flags stock (C13)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - TempLog — id, tenant_id, location_id, monitor_id, temp, at, source(manual|device) (2-8C range; out-of-range -> Excursion.)
  - Excursion — id, location_id, started_at, ended_at, min, max, affected_lots[], action(quarantine) (Raises alert + job; flags stock (C13).)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Temperature can be logged (manual + via the device API) for storage locations.
  - Rule: An excursion raises an alert and flags affected stock for quarantine.
  - Rule: A breach pathway can quarantine a lot and raise a job (links PRD-11).
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-04/CUSTODY-STORAGE.
- [ ] **Enforce compliance gate + audit events**
  Enforce C13 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
- [ ] **Integration adapter, sync & config**
  Implement the provider behind its swappable port:
  - Connection/config (OAuth tokens stored encrypted) + the field mapping this story needs.
  - Trigger on the relevant event; idempotent sync with retries, back-off and a visible reconciliation/status.
  - Handle partial failures + replays; surface errors to the user.
  - Residency: AU-resident or APP-8-assessed + consented before any PII leaves (C21).
