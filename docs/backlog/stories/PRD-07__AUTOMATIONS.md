# Automation builder (triggers → timed messages)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/AUTOMATIONS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/REMINDERS-CARE`

## Background

As a owner / front desk, I want to configure automations that send the right message at the right time per trigger, so that reminders, aftercare and recall run hands-off.
The prototype's Comms → Automations screen (toggleAuto) configures the reminder/aftercare/recall sequences as toggleable automations. This is the management UI over PRD-07's sequence engine.

## Requirements

- To configure automations that send the right message at the right time per trigger.
- Compliance: [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Automations map a trigger (booking, visit, interval) to a timed sequence of messages.
- [ ] Each automation can be enabled/disabled and edited per treatment type.
- [ ] Marketing automations respect opt-in/unsubscribe (C23); transactional ones always send.
- [ ] Drives the same sequence engine as PRD-07/REMINDERS-CARE and PRD-07/RECALL.

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
