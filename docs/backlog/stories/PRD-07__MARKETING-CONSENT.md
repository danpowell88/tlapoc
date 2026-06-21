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

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C23); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
