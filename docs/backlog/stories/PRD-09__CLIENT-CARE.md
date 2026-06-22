# Client app: my care health hub (basic)

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-CARE`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-09/CLIENT-JOURNEY`, `PRD-05/PHOTOS`

## Background

As a client, I want to view my visit history, treatment plan, medicines and documents, so that I can see my own care in one place.
Plainly: the My care tab of the client app where someone reviews their own care — past visits, treatment plan, their medicines and downloadable documents. Where it fits: a late, outward-facing surface that reuses the modules built earlier (PRD-05 clinical, PRD-06 commerce); this basic slice stands up the read-only health hub, and the rewards, card-on-file, before/after gallery and aftercare are its follow-up siblings. Clients view their own care history in-app (REQ-APP-1).

## How it works

The My care health hub lists past visits, the ongoing treatment plan (what's due / course progress), the client's own medicines (S4 — Schedule 4 prescription-only medicine — record) and downloadable documents (signed consents, treatment records, receipts, aftercare PDFs). All read-only over the owning modules (PRD-05 clinical, PRD-06 commerce) via the API — no parallel app store.
The medicines view is shown privately and never priced or advertised (AU advertising rules); documents download through the secure channel. The before/after gallery, day-by-day aftercare, rewards and the card-on-file are their own follow-up siblings (PHOTO-COMPARE, AFTERCARE-GUIDE, CLIENT-REWARDS, CLIENT-ACCOUNT). Self-service for care history.

## Requirements

- To view my visit history, treatment plan, medicines and documents.

## Acceptance Criteria

- [ ] The My care tab lists past visits and the ongoing treatment plan (what's due / course progress).
- [ ] The client's own medicines (S4 record) are shown privately and never priced or advertised.
- [ ] Documents (signed consents, treatment records, receipts, aftercare PDFs) download through the secure channel.
- [ ] All read-only over the owning modules (PRD-05 clinical, PRD-06 commerce) — no app-local store.

## UI designs / screenshots

_Prototype screen: client-app.html, treatment-room.html, checkin.html, backroom.html._

- Prototype: client-app — My care (visit history, treatment plan, medicines, documents).
- Medicines shown privately, never priced/advertised; documents download via the secure channel.
- Before/after gallery + aftercare are sibling sub-screens (PHOTO-COMPARE, AFTERCARE-GUIDE).

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Visit/TreatmentPlan** — PRD-05 — visit history + ongoing treatment plan (what's due / course progress)
  - _Read-only; client sees own care only._
- **(reuses) Medicine/Document** — PRD-05/PRD-06 — client's own S4 medicine record; signed consents, treatment records, receipts, aftercare PDFs
  - _Medicines never priced/advertised; documents download via the secure channel._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **My care tab: visit history + treatment plan + medicines + documents**
  Behaviour: the My care health hub lists past visits, the ongoing treatment plan (what's due / course progress), the client's own medicines (S4 — Schedule 4 prescription-only medicine — record) and downloadable documents (signed consents, treatment records, receipts, aftercare PDFs). Requirements: all read-only over the owning modules (PRD-05 clinical, PRD-06 commerce) via the API; the medicines view is shown privately and never priced or advertised (AU advertising rules); documents download through the secure channel. The before/after gallery and the day-by-day aftercare are their own siblings (PHOTO-COMPARE, AFTERCARE-GUIDE).
