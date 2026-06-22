# Before/after photo gallery: compare & grouping UI

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/PHOTOS-GALLERY-COMPARE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/PHOTOS-GALLERY`

## Background

As a clinician, I want to view before/after pairs side-by-side and grouped by treatment/date, so that I can read a client's treatment progress at a glance.
Plainly: the gallery's presentation — grouping images by treatment/date and showing before/after pairs side-by-side. Where it fits: a follow-up to the before/after gallery basic consent-gated view (PRD-02/PHOTOS-GALLERY) that adds the compare/grouping presentation on top of the consent-gated, signed-URL photo set. It still renders only when image-use consent is granted (the basic's gate). It sits on the Client 360 profile in Reception (PRD-02).

## How it works

The basic story serves the consent-gated photo set via signed URLs; this follow-up adds the presentation a clinician reads. The Photos tab groups images by treatment/date and lets the clinician view before/after pairs side-by-side.
Pairs are matched on kind(before|after) + treatment_ref so the right before and after sit together, and there is no download/save affordance — images stay served via the basic's short-lived signed URLs.
It renders only when image-use consent is currently granted, inheriting the basic's consent gate; nothing here weakens the consent or no-local-storage rules.

## Requirements

- To view before/after pairs side-by-side and grouped by treatment/date.

## Acceptance Criteria

- [ ] Before/after pairs can be compared side-by-side and are grouped by treatment/date.
- [ ] Pairs are matched on kind(before|after) + treatment_ref.
- [ ] There is no download/save affordance.
- [ ] It renders only when image-use consent is granted (the basic's gate).

## UI designs / screenshots

- Prototype: Client 360 (client-360.png) Photos tab — the before/after gallery grid grouped by treatment/date with side-by-side compare.
- Pairs matched on kind(before|after) + treatment_ref; no download/save affordance.
- Renders only when image-use consent is on file.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends PHOTOS-GALLERY)** — no new entities; groups the consent-gated GalleryView by treatment_ref/date and pairs kind(before|after)
  - _Presentation only; still gated on current image-use consent and served via signed URLs._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Before/after compare + grouping UI**
  Behaviour: a Photos-tab grid that groups images by treatment/date and lets a clinician view before/after pairs side-by-side. Requirements: pairs are matched on kind(before|after) + treatment_ref; no download/save affordance; renders only when consent is granted.
