# Outcomes: per-treatment/practitioner aggregation & reporting feed

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/OUTCOMES-REPORTING`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/OUTCOMES`

## Background

As a owner, I want outcome and revision signals aggregated per treatment type and practitioner, so that I can measure quality and feed it to reporting.
Plainly: this rolls up the individual outcome records into the numbers that matter — touch-up rate, percent satisfied, complication rate by treatment type and by practitioner — and feeds them to reporting. Where it fits: a follow-up to PRD-05/OUTCOMES that adds the aggregation layer on top of outcome capture. The individual Outcome records already exist; this story builds the read-model and the 'Outcomes & revisions per treatment type' table, feeding quality reporting (PRD-08). Quality/money figures stay owner-gated (.fin).

## How it works

This follow-up adds the aggregation layer on top of outcome capture. The individual Outcome records (rating, satisfaction, revision_of) the basic captures are rolled into a read-model: touch-up rate (revisions/treatments), % satisfied, n and complications (from AdverseEvent) per treatment type and per practitioner.
The 'Outcomes & revisions — per treatment type' table renders the aggregates (the prototype's outcomeStats: Anti-wrinkle 8% touch-up / 96% satisfied, Filler 14% / 91%, Skin, Laser/IPL). A revision_of is never counted as a fresh success.
Aggregates feed PRD-08 quality reporting; quality/money figures stay owner-gated per the financial-gating rules (.fin).

## Requirements

- Outcome and revision signals aggregated per treatment type and practitioner.

## Acceptance Criteria

- [ ] A read-model aggregates touch-up rate (revisions/treatments), % satisfied, n and complications (from AdverseEvent) per treatment type and practitioner.
- [ ] The 'Outcomes & revisions — per treatment type' table renders the aggregates.
- [ ] A revision (revision_of) is not counted as a fresh success in the touch-up rate.
- [ ] Aggregates feed PRD-08 quality reporting; quality/money figures stay owner-gated (.fin).

## UI designs / screenshots

- 'Outcomes & revisions - per treatment type' table: Treatment - Touch-up rate - Satisfied - n - Complications (Anti-wrinkle 8% / 96% / 96 / 0; Filler 14% / 91% / 34 / 1; Skin 5% / 94% / 120 / 0; Laser/IPL 5% / 94% / 60 / 0).
- Sits alongside the standardised-photography card (shared with PHOTOS).
- Quality/money figures owner-gated (.fin).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **Derived / reporting (read model)** — per treatment type + practitioner: touch-up rate = revisions/treatments, % satisfied, n, complications (from AdverseEvent)
  - _Extends the basic's Outcome records — no new entity; the aggregation read-model for the table + PRD-08 quality reporting._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Outcome aggregation read-model + per-treatment table**
  Behaviour: a read-model aggregating touch-up rate, % satisfied, n and complications (from AdverseEvent) per treatment type/practitioner, rendered as the 'Outcomes & revisions per treatment type' table and feeding PRD-08 reporting. Requirements: a revision_of is not counted as a fresh success; quality/money figures stay owner-gated (.fin).
