# Complaints: reporting feed + raise-from-conversation

> **Epic:** [PRD-11 — Facility, infection-control, emergency & complaints](../epics/PRD-11.md)  ·  **Key:** `PRD-11/COMPLAINT-REPORTING`  ·  **Type:** Story  ·  **Stage:** M6  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-11/COMPLAINTS`, `PRD-07/FOLLOWUPS`

## Background

As a manager, I want complaints to feed reporting and be raisable from a conversation, so that complaints are visible in the wider picture and easy to open from an inbox thread.
Plainly: complaints feed the wider Governance/reporting picture and can be started directly from an inbox conversation. Where it fits: a follow-up to the complaints register (PRD-11/COMPLAINTS) that adds the reporting feed and the raise-from-conversation hook; it surfaces complaints in reporting (PRD-08) and the Governance command centre, and links a PRD-07 inbox thread to a new complaint.

## How it works

Complaints feed the wider picture and can start from an inbox thread: feed complaints into the register/reporting (PRD-08) and the Governance command centre ('Open AE cases', 'Needs attention'). Allow a complaint to be raised directly from a PRD-07 inbox conversation, linking the thread to the new complaint.
This builds on the complaints register basic (PRD-11/COMPLAINTS), wiring it into reporting and the comms inbox. The conversation→complaint link is recorded and audited.

## Requirements

- Complaints to feed reporting and be raisable from a conversation.

## Acceptance Criteria

- [ ] Complaints feed the register/reporting (PRD-08) and the Governance command centre ('Open AE cases', 'Needs attention').
- [ ] A complaint can be raised directly from a PRD-07 inbox conversation.
- [ ] Raising from a conversation links the thread to the new complaint.
- [ ] The link is recorded and audited.

## UI designs / screenshots

- Prototype: Governance ('Open AE cases', 'Needs attention') surfaces complaints; raise a complaint from a PRD-07 conversation.
- Reporting (PRD-08) includes complaints; the inbox thread links to the new complaint.

![ops-openclose — prototype screen](../screens/ops-openclose.png)

## Suggested data model

- **(reuses) Complaint + Conversation** — PRD-11/COMPLAINTS complaint feeds PRD-08 reporting; PRD-07 conversation links to a new complaint
  - _Extends COMPLAINTS; reporting feed + conversation→complaint link, audited._

## Other

- Source PRD: [PRD-11-facility-complaints.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-11-facility-complaints.md)

## Tasks (dev pickup)

- [ ] **Feed reporting + raise-from-conversation**
  Behaviour: complaints feed the wider picture and can start from an inbox thread. Requirements: feed complaints into the register/reporting (PRD-08) and the Governance command centre ('Open AE cases', 'Needs attention'); allow a complaint to be raised directly from a PRD-07 inbox conversation, linking the thread to the new complaint.
