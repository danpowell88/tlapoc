# Recall / recare worklist

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/RECALL`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a front desk, I want a recall worklist of clients due to rebook and automatic recall nudges at the treatment interval, so that clients return on cadence and the book stays full.
Recare at the treatment interval (toxin ~12 weeks) + unbooked-rebook prompts, with a recall worklist for front desk (REQ-NOTIF-3).

## Requirements

- A recall worklist of clients due to rebook and automatic recall nudges at the treatment interval.

## Acceptance Criteria

- [ ] A toxin client with no future booking enters the recall worklist at the configured interval and receives the nudge.
- [ ] Unbooked recommended sessions prompt a rebook.
- [ ] Front desk can work the recall/rebook worklist.
- [ ] Recall integrates with treatment plans (PRD-05) and rebooking (PRD-06).

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
