# Marketing consent & functional unsubscribe (Spam Act)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/MARKETING-CONSENT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a client, I want to only receive marketing I opted into, with a working unsubscribe on every message, so that my consent is respected per the Spam Act.
Opt-in for commercial electronic messages, sender identification and a functional unsubscribe that suppresses immediately on withdrawal (REQ-NOTIF-5, C23).

## How it works

Opt-in for commercial electronic messages, sender identification, and a functional unsubscribe that suppresses immediately on withdrawal (Spam Act, C23). Marketing sends only to opted-in clients; suppression is honoured across channels (and by PRD-06 reward comms).
Transactional reminders/aftercare are exempt and always send.

## Requirements

- To only receive marketing I opted into, with a working unsubscribe on every message.
- Compliance: [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Marketing sends only to opted-in clients and always include a working unsubscribe.
- [ ] Unsubscribing suppresses future marketing immediately.
- [ ] Sender identification is included.
- [ ] Suppression list is honoured across channels (and by PRD-06 reward comms).

## UI designs / screenshots

- Client app/profile: marketing opt-in toggle + unsubscribe in every marketing message; staff see consent state on the Client 360.
- Admin: suppression list.

![settings-booking — prototype screen](../screens/settings-booking.png)

## Suggested data model

- **MarketingConsent** — id, client_id, channel, opted_in(bool), updated_at
  - _Required for marketing (C23)._
- **SuppressionList** — tenant_id, contact, reason, at
  - _Honoured across all marketing/reward comms._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - MarketingConsent — id, client_id, channel, opted_in(bool), updated_at (Required for marketing (C23).)
  - SuppressionList — tenant_id, contact, reason, at (Honoured across all marketing/reward comms.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: Marketing sends only to opted-in clients and always include a working unsubscribe.
  - Rule: Unsubscribing suppresses future marketing immediately.
  - Rule: Sender identification is included.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
  - Depends on: PRD-07/CHANNELS.
- [ ] **Enforce compliance gate + audit events**
  Enforce C23 as a server-side invariant that cannot be bypassed via the API:
  - Block the action when prerequisites are missing; return a clear reason for the blocked-action banner (what's blocked / which rule / how to resolve / who can resolve).
  - Write an immutable AuditEvent for the attempt and its outcome.
  - Marketing sends only to opted-in clients and always include a working unsubscribe.
