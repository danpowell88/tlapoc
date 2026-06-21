# Automation builder (triggers → timed messages)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/AUTOMATIONS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/REMINDERS-CARE`

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a owner / front desk, I want to configure automations that send the right message at the right time per trigger, so that reminders, aftercare and recall run hands-off.

The prototype's Comms → Automations screen (toggleAuto) configures the reminder/aftercare/recall sequences as toggleable automations. This is the management UI over PRD-07's sequence engine.

## Requirements

- To configure automations that send the right message at the right time per trigger.
- Traces to requirement(s): REQ-NOTIF-2, REQ-NOTIF-3.

## Acceptance Criteria

- [ ] Automations map a trigger (booking, visit, interval) to a timed sequence of messages.
- [ ] Each automation can be enabled/disabled and edited per treatment type.
- [ ] Marketing automations respect opt-in/unsubscribe (C23); transactional ones always send.
- [ ] Drives the same sequence engine as PRD-07/REMINDERS-CARE and PRD-07/RECALL.

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Depends on: PRD-07/REMINDERS-CARE.

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/AUTOMATIONS.
Phase: 1 · Priority: P2 · Estimate: 2 pts.
Compliance criteria: C23.

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
