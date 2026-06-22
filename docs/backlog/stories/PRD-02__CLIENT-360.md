# Client 360° profile

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-360`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-01/CLIENT-CORE`

## Background

As a staff member, I want a single 360° client profile pulling together history, medical flags, consents, photos, memberships, balances and comms, so that I have the full picture in one place.
Any staff member can open a client's full profile: history, contacts, medical flags, consents, photos, memberships, balances, comms and complaints.

## How it works

A single 360-degree client profile pulls together everything any staff member needs: overview, medical/contraindications, consents, photos, visit history, memberships, balance, comms and complaints — surfacing data owned by PRD-03/04/05/06/11 via the API.
Access is RBAC-scoped (reception sees limited clinical info) and audited.

## Requirements

- A single 360° client profile pulling together history, medical flags, consents, photos, memberships, balances and comms.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Profile aggregates overview, medical/contraindications, consents, photos, visits, memberships, balance, comms, complaints.
- [ ] Consent/age chips render on the header (consent ✓ / image-use ✓ / under-18 cooling-off).
- [ ] Access is RBAC-scoped (reception sees limited clinical info) and audited.
- [ ] Surfaces data owned by PRD-03/04/05/06/11 via the API.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Client 360 (client-360.png) — header with consent/age chips (consent / image-use / under-18 cooling-off), tabbed sections for medical, consents, photos, visits, memberships, balance, comms, complaints.
- Quick links into charting, checkout and follow-ups.

![client-360 — prototype screen](../screens/client-360.png)

## Suggested data model

- **Client (aggregate view)** — joins Client + IntakeResponse + ConsentSignature + Photo + Appointment + Membership + AccountBalance + Complaint
  - _Read aggregation; each part owned by its module. RBAC filters fields._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - Client (aggregate view) — joins Client + IntakeResponse + ConsentSignature + Photo + Appointment + Membership + AccountBalance + Complaint (Read aggregation; each part owned by its module. RBAC filters fields.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Profile aggregates overview, medical/contraindications, consents, photos, visits, memberships, balance, comms, complaints.
  - Rule: Consent/age chips render on the header (consent ✓ / image-use ✓ / under-18 cooling-off).
  - Rule: Access is RBAC-scoped (reception sees limited clinical info) and audited.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-01/CLIENT-CORE.
- [ ] **Web UI**
  Build on the Angular web app: the client-360 per the UI spec. Wire to the API with loading/empty/error states; capability-gate controls; responsive; show the blocked-action banner / gate chips where gated; respect owner-only .fin gating for money figures.
  Key elements (from the prototype):
  - Prototype: Client 360 (client-360.png) — header with consent/age chips (consent / image-use / under-18 cooling-off), tabbed sections for medical, consents, photos, visits, memberships, balance, comms, complaints.
  - Quick links into charting, checkout and follow-ups.
