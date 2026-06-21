# Server-enforced treatment gating

> **Epic:** [PRD-03 — Intake, consent & compliance gating](../epics/PRD-03.md)  ·  **Key:** `PRD-03/GATING`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-03/CONSENT`, `PRD-03/BDD`

## Background

As a RN/NP, I want the system to block treatment until required intake and consent are complete and current, telling me exactly what's missing, so that the compliant path is the only path.
Treatment cannot start unless required intake + consent are complete and current — enforced server-side, surfaced via the blocked-action banner (ADR-0008).

## How it works

The shared treatment gate: charting/treatment cannot start unless required intake + a current consent (and BDD screen) exist — enforced server-side, surfaced via the calm blocked-action banner ('what is missing, how to fix, who can resolve'). Never a dead-end.
This is the mechanism PRD-04 (consult/Rx) and PRD-05 (charting) consume; gate decisions are audited.

## Requirements

- The system to block treatment until required intake and consent are complete and current, telling me exactly what's missing.
- Compliance: [C5](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Treatment is blocked server-side unless required intake + current consent exist.
- [ ] The block states what's missing and how to resolve it (never a dead-end).
- [ ] The gate is the shared mechanism consumed by PRD-04/05.
- [ ] Gate decisions are audited.

## UI designs / screenshots

- Prototype: the Charting pre-treatment review (charting.png) shows the gate chips and blocks opening the map until satisfied; the banner explains and links the fix.
- Same gate reused on the provider app (treatment-room.png).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **(derived) TreatmentGate** — = required IntakeResponse present AND current ConsentSignature AND ScreeningResult present (AND consult/Rx for S4)
  - _Server-enforced; evaluated before charting opens (ADR-0008)._

## Technical notes (high level)

- Stack: .NET API (domain/services)
- Architecture decisions: [ADR-0008](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-03-intake-consent-gating.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-03-intake-consent-gating.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C5); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
