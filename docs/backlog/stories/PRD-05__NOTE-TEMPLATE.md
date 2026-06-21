# Guided toxin treatment note & pre-treatment review

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/NOTE-TEMPLATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

Clinical charting: injection mapping & before/after — The clinical record that matches the Aesthetic Record / Pabau bar: a guided charting flow opening with product & lot selection, on-image/diagram injection mapping (product · units · depth · site · batch-lot), standardised before/after photos with comparison, immutable finalised notes with audited amendments, and adverse-event logging that feeds the TGA/DAEN pathway

As a injector, I want a guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template, so that I chart quickly and safely with the right context in front of me.

Charting is a guided, treatment-type-aware flow: a pre-treatment review (safety + last-treatment + consult/Rx surfaced) then a configurable toxin note (structured + free text + snippets) (REQ-CLIN-1/9).

## Requirements

- A guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template.
- Traces to requirement(s): REQ-CLIN-1, REQ-CLIN-9.

## Acceptance Criteria

- [ ] Pre-treatment review surfaces safety flags, last treatment and the linked consult/Rx (verified before opening).
- [ ] Configurable toxin template with structured fields, free text and reusable phrases/snippets.
- [ ] A non-S4 skin note variant exists (treatment-type-aware).
- [ ] Charting cannot open unless the consult+consent gate is satisfied (PRD-03/04).

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0024 (see docs/adr/decision-log.md).
Depends on: PRD-04/ADMIN-GATE.

## Other

Epic: PRD-05 — Clinical charting: injection mapping & before/after.
Source PRD: docs/prds/PRD-05-clinical-charting.md.
Backlog key: PRD-05/NOTE-TEMPLATE.
Phase: 1 · Priority: P0 · Estimate: 5 pts.

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
