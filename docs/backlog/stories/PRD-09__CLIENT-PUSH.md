# Client app: push token + notification inbox

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-PUSH`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/CLIENT-JOURNEY`, `PRD-07/FOLLOWUPS`

## Background

As a client, I want to receive reminders and recall as push notifications and in an in-app inbox, so that I don't miss appointments or follow-up messages.
Plainly: the client app registers for push notifications and shows reminders and recall messages in an in-app inbox. Where it fits: a follow-up to the client-app basic (PRD-09/CLIENT-JOURNEY) that adds push + the inbox; the messages themselves are sent by the comms module (PRD-07) — this surface only receives and displays them. Transactional appointment/care messages are always shown.

## How it works

Register a push token at sign-in and render reminders / recall (PRD-07) as push plus an in-app inbox. Notifications are delivered by PRD-07 — this surface only receives and displays them; transactional care/appointment messages are always shown regardless of the client's marketing opt-out (only offers/news are opt-out).
Tapping a notification deep-links to the relevant screen (e.g. the pre-visit forms or the next-appointment card). The inbox is the in-app home for everything the clinic sends the client.

## Requirements

- To receive reminders and recall as push notifications and in an in-app inbox.

## Acceptance Criteria

- [ ] A push token is registered at sign-in and reminders/recall render as push plus an in-app inbox.
- [ ] Notifications are delivered by PRD-07 — this surface only receives and displays them.
- [ ] Transactional care/appointment messages are always shown (not gated by marketing opt-out).
- [ ] Tapping a notification deep-links to the relevant screen.

## UI designs / screenshots

- Prototype: client-app — Messages / notifications inbox; reminders and recall arrive as push + in-app entries.
- Tapping a notification deep-links to the relevant screen; transactional messages always shown.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) Notification** — PRD-07 push token + in-app inbox
  - _Extends CLIENT-JOURNEY; PRD-07 sends, this surface receives/displays only._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Push token registration + in-app notification inbox (PRD-07)**
  Behaviour: register a push token at sign-in and render reminders / recall as push plus an in-app inbox. Requirements: notifications are delivered by PRD-07 (this surface only receives and displays them); transactional care/appointment messages are always shown; tapping a notification deep-links to the relevant screen.
