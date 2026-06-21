# Complication protocol library & response kits

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/COMPLICATION-LIBRARY`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-05/ADVERSE-EVENT`

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a clinician, I want a library of complication protocols with guided response steps and kit links, so that in an emergency I follow the correct, documented steps.

The prototype's Clinical → Complication protocols (openComplication/completeComplication) provides step-by-step VO/anaphylaxis protocols and links the emergency kit — the reference side of the adverse-event response.

## Requirements

- A library of complication protocols with guided response steps and kit links.
- Traces to requirement(s): REQ-CLIN-13, REQ-FAC-3.
- Must satisfy compliance obligation(s): C12, C20.

## Acceptance Criteria

- [ ] Protocols (e.g. vascular occlusion, anaphylaxis) present guided steps and required kit items.
- [ ] Launching a protocol logs the response and can raise an adverse event (PRD-05/ADVERSE-EVENT).
- [ ] Completion is recorded with timing and outcome.
- [ ] Links to the emergency-kit register (PRD-11/EMERGENCY-KIT).

## UI designs / screenshots

prototype.html — Clinical → Complication protocols.

## Technical notes (high level)

Stack: Flutter provider app.
Depends on: PRD-05/ADVERSE-EVENT.

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/COMPLICATION-LIBRARY.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C12, C20.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C12, C20); blocked path explains why.
- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
