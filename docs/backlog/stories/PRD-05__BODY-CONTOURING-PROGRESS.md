# Body contouring: standardised body photos & measurements over the course

> **Epic:** [PRD-05 — Clinical charting: injection mapping & before/after](../epics/PRD-05.md)  ·  **Key:** `PRD-05/BODY-CONTOURING-PROGRESS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-05/BODY-CONTOURING`

## Background

As a therapist, I want standardised body photos and objective measurements tracked over the course, shareable with the client, so that non-facial progress is evidenced and the client can see results.
Plainly: this tracks how a body-contouring course is going — standardised before/after body photos and objective measurements like waist circumference across visits — and can share that progress with the client. Where it fits: a follow-up to PRD-05/BODY-CONTOURING that adds the outcome-tracking layer on top of the body-map chart. It rides the clinical-photo storage rules (PRD-05/PHOTOS) and feeds plans (PRD-05/TREATMENT-PLANS) and outcomes (PRD-05/OUTCOMES).

## How it works

This follow-up adds the outcome-tracking layer on top of the body-map chart. Standardised before/after body photos ride the PHOTOS storage rules (PRD-05/PHOTOS) — signed URLs, never on device, image-use consent (C14) — and objective measurements (e.g. waist circumference) are recorded over the course (Baseline / +4 wks / +8 wks).
Sessions feed multi-session plans (PRD-05/TREATMENT-PLANS) and outcomes (PRD-05/OUTCOMES); progress photos + measurements can be pushed to the client app (consent-respecting).
It adds the BodyMeasurement entity and pairs it with the standardised body photos.

## Requirements

- Standardised body photos and objective measurements tracked over the course, shareable with the client.

## Acceptance Criteria

- [ ] Standardised before/after body photos ride the PHOTOS storage rules (signed URLs, never on device, image-use consent — C14).
- [ ] Objective measurements (e.g. waist circumference) are recorded over the course (Baseline / +4 wks / +8 wks).
- [ ] Sessions feed multi-session plans (PRD-05/TREATMENT-PLANS) and outcomes (PRD-05/OUTCOMES).
- [ ] Progress photos + measurements can be pushed to the client app, consent-respecting.

## UI designs / screenshots

- Before/after standardised body photos + a waist-circumference progress chart over the course (Baseline / +4 wks / +8 wks).
- 'Send progress to client' action (consent-respecting).
- Measurements + photos feed plans (TREATMENT-PLANS) + outcomes (OUTCOMES).

![charting — prototype screen](../screens/charting.png)

## Suggested data model

- **BodyMeasurement** — id, chart_entry_id / plan_id, kind (e.g. waist_circumference), value, taken_at
  - _New entity (extends the basic's BodyChart). Objective progress over the course; pairs with standardised body photos (PRD-05/PHOTOS)._

## Other

- Source PRD: [PRD-05-clinical-charting.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-05-clinical-charting.md)

## Tasks (dev pickup)

- [ ] **Body measurements + standardised body photos over the course**
  Behaviour: standardised before/after body photos (PHOTOS rules) and objective measurements (e.g. waist circumference) over the course (Baseline / +4 wks / +8 wks); progress can be pushed to the client app (consent-respecting). Requirements: photos ride PRD-05/PHOTOS (signed URLs, never on device, image-use consent — C14); add BodyMeasurement; feed sessions into plans (PRD-05/TREATMENT-PLANS) + outcomes (PRD-05/OUTCOMES).
