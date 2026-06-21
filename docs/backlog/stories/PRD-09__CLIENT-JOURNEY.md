# Client app: book → intake → consent journey

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/CLIENT-JOURNEY`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** client-app
>
> **Depends on:** `PRD-02/ONLINE-BOOK`, `PRD-03/CONSENT`

## Background

As a client, I want to book, complete intake and e-sign consent entirely in the app, so that I'm ready for my visit without paperwork.
A client can complete the full pre-visit journey entirely in-app (REQ-APP-1).

## Requirements

- To book, complete intake and e-sign consent entirely in the app.

## Acceptance Criteria

- [ ] A client completes book → intake → consent (incl. image-use) fully in-app.
- [ ] Surfaces PRD-02 booking and PRD-03 intake/consent.
- [ ] Sign-in via social/email/OTP, tenant-scoped.
- [ ] Reminders/recall (PRD-07) are received in-app.

## UI designs / screenshots

client-app.html, treatment-room.html, checkin.html, backroom.html.

## Technical notes (high level)

- Stack: Flutter client app
- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Client app UI (Flutter)**
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
