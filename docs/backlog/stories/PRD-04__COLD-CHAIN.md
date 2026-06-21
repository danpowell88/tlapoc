# Temperature logging & excursion alerts

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/COLD-CHAIN`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend, integration
>
> **Depends on:** `PRD-04/CUSTODY-STORAGE`

## Background

As a owner, I want temperature logging for the medicine fridge with excursion alerts, so that we never use medicine that breached cold-chain.
Toxin must stay 2–8°C; temperature logging raises excursion alerts and flags affected stock (C13). Integrates with the optional ESP32 cold-chain monitor.

## Requirements

- Temperature logging for the medicine fridge with excursion alerts.
- Compliance: [C13](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Temperature can be logged (manual + via the device API) for storage locations.
- [ ] An excursion raises an alert and flags affected stock for quarantine.
- [ ] A breach pathway can quarantine a lot and raise a job (links PRD-11).
- [ ] Excursion history is retained and visible.

## Technical notes (high level)

- Stack: .NET API (domain/services); Ports-and-adapters integration

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C13); blocked path explains why.
- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
