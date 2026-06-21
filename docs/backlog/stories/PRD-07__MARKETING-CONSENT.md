# Marketing consent & functional unsubscribe (Spam Act)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/MARKETING-CONSENT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a client, I want to only receive marketing I opted into, with a working unsubscribe on every message, so that my consent is respected per the Spam Act.

Opt-in for commercial electronic messages, sender identification and a functional unsubscribe that suppresses immediately on withdrawal (REQ-NOTIF-5, C23).

## Requirements

- To only receive marketing I opted into, with a working unsubscribe on every message.
- Traces to requirement(s): REQ-NOTIF-5.
- Must satisfy compliance obligation(s): C23.

## Acceptance Criteria

- [ ] Marketing sends only to opted-in clients and always include a working unsubscribe.
- [ ] Unsubscribing suppresses future marketing immediately.
- [ ] Sender identification is included.
- [ ] Suppression list is honoured across channels (and by PRD-06 reward comms).

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-07/CHANNELS.

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/MARKETING-CONSENT.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C23.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Enforce compliance gate + audit events** — Server-side (C23); blocked path explains why.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
