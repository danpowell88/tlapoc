# Complication protocol library & response kits

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/COMPLICATION-LIBRARY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/ADVERSE-EVENT`

## Background

As a clinician, I want a library of complication protocols with guided response steps and kit links, so that in an emergency I follow the correct, documented steps.
The prototype's Clinical → Complication protocols (openComplication/completeComplication) provides step-by-step VO/anaphylaxis protocols and links the emergency kit — the reference side of the adverse-event response.

## Requirements

- A library of complication protocols with guided response steps and kit links.
- Compliance: [C12](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C20](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Protocols (e.g. vascular occlusion, anaphylaxis) present guided steps and required kit items.
- [ ] Launching a protocol logs the response and can raise an adverse event (PRD-05/ADVERSE-EVENT).
- [ ] Completion is recorded with timing and outcome.
- [ ] Links to the emergency-kit register (PRD-11/EMERGENCY-KIT).

## UI designs / screenshots

prototype.html — Clinical → Complication protocols.

## Technical notes (high level)

- Stack: Flutter provider app

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C12, C20); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
