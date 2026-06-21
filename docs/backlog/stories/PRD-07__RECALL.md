# Recall / recare worklist

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/RECALL`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a front desk, I want a recall worklist of clients due to rebook and automatic recall nudges at the treatment interval, so that clients return on cadence and the book stays full.

Recare at the treatment interval (toxin ~12 weeks) + unbooked-rebook prompts, with a recall worklist for front desk (REQ-NOTIF-3).

## Requirements

- A recall worklist of clients due to rebook and automatic recall nudges at the treatment interval.
- Traces to requirement(s): REQ-NOTIF-3.

## Acceptance Criteria

- [ ] A toxin client with no future booking enters the recall worklist at the configured interval and receives the nudge.
- [ ] Unbooked recommended sessions prompt a rebook.
- [ ] Front desk can work the recall/rebook worklist.
- [ ] Recall integrates with treatment plans (PRD-05) and rebooking (PRD-06).

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: .NET API (domain/services).
Depends on: PRD-07/CHANNELS.

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/RECALL.
Phase: 1 · Priority: P1 · Estimate: 3 pts.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
