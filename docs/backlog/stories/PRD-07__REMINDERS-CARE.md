# Reminders, confirmations & care sequences

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REMINDERS-CARE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a client, I want timely reminders I can confirm/decline and pre-/after-care instructions for my treatment, so that I'm prepared and cared for around my visit.

Appointment reminders/confirmations plus pre-care and aftercare sequences (multi-touch, timed per treatment type) (REQ-NOTIF-2). Transactional messages are exempt from opt-in.

## Requirements

- Timely reminders I can confirm/decline and pre-/after-care instructions for my treatment.
- Traces to requirement(s): REQ-NOTIF-2.

## Acceptance Criteria

- [ ] Appointment reminders/confirmations send per template; confirm/decline updates the appointment (PRD-02).
- [ ] Pre-care + aftercare sequences are multi-touch and timed per treatment type.
- [ ] Transactional messages send regardless of marketing opt-in and avoid S4 references.
- [ ] Sends are logged to comms history.

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-07/CHANNELS.

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/REMINDERS-CARE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
