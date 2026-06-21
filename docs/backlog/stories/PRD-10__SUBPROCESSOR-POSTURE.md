# Sub-processor residency posture (APP-8)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/SUBPROCESSOR-POSTURE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** integration
>
> **Depends on:** `PRD-01/RESIDENCY`

## Background

As a owner, I want assurance that any data leaving the platform goes only to AU-resident or APP-8-assessed sub-processors, so that integrations don't breach cross-border rules.
No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists (REQ-INT-3, C21/ADR-0016).

## Requirements

- Assurance that any data leaving the platform goes only to AU-resident or APP-8-assessed sub-processors.
- Compliance: [C21](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] No integration sends PII to a non-AU sub-processor unless an APP-8 assessment + consent record exists.
- [ ] Sub-processor data flows are registered.
- [ ] All integrations are outbound and swappable.
- [ ] Ties into PRD-01/RESIDENCY enforcement.

## Technical notes (high level)

- Stack: Ports-and-adapters integration
- Architecture decisions: [ADR-0016](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C21); blocked path explains why.
- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
