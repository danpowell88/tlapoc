# Reminders, confirmations & care sequences

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REMINDERS-CARE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** backend
>
> **Depends on:** `PRD-07/CHANNELS`

## Background

As a client, I want timely reminders I can confirm/decline and pre-/after-care instructions for my treatment, so that I'm prepared and cared for around my visit.
Appointment reminders/confirmations plus pre-care and aftercare sequences (multi-touch, timed per treatment type) (REQ-NOTIF-2). Transactional messages are exempt from opt-in.

## Requirements

- Timely reminders I can confirm/decline and pre-/after-care instructions for my treatment.

## Acceptance Criteria

- [ ] Appointment reminders/confirmations send per template; confirm/decline updates the appointment (PRD-02).
- [ ] Pre-care + aftercare sequences are multi-touch and timed per treatment type.
- [ ] Transactional messages send regardless of marketing opt-in and avoid S4 references.
- [ ] Sends are logged to comms history.

## Technical notes (high level)

- Stack: .NET API (domain/services)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
