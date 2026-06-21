# Guided toxin treatment note & pre-treatment review

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/NOTE-TEMPLATE`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** provider-app
>
> **Depends on:** `PRD-04/ADMIN-GATE`

## Background

As a injector, I want a guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template, so that I chart quickly and safely with the right context in front of me.
Charting is a guided, treatment-type-aware flow: a pre-treatment review (safety + last-treatment + consult/Rx surfaced) then a configurable toxin note (structured + free text + snippets) (REQ-CLIN-1/9).

## Requirements

- A guided note that first surfaces safety, last treatment and the consult/Rx, then a toxin template.

## Acceptance Criteria

- [ ] Pre-treatment review surfaces safety flags, last treatment and the linked consult/Rx (verified before opening).
- [ ] Configurable toxin template with structured fields, free text and reusable phrases/snippets.
- [ ] A non-S4 skin note variant exists (treatment-type-aware).
- [ ] Charting cannot open unless the consult+consent gate is satisfied (PRD-03/04).

## UI designs / screenshots

prototype.html — Charting + Clinical (Skin analysis, Body contouring, Complication protocols, Photography & outcomes); treatment-room.html.

## Technical notes (high level)

- Stack: Flutter provider app
- Architecture decisions: [ADR-0024](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Provider app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
