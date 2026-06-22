# Follow-ups: rules/keyword auto-categorisation (no AI)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/FOLLOWUPS-AUTOCAT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a staff member, I want inbound comms auto-sorted into the right kind of follow-up Job, so that enquiries land with the right person without manual triage.
Plainly: read inbound comms and turn them into the right kind of Job automatically by rules and keywords — a complaint becomes a Lead-Nurse callback, a booking enquiry a Reception reply — with no AI. Where it fits: a follow-up to the unified queue core (PRD-07/FOLLOWUPS), which merges signals and supports lifecycle actions; this adds automatic categorisation of inbound comms into jobs. Auto-categorisation is a UX aid, not a safety control — jobs are advisory and human-actioned. Idempotent. An 'Auto-detect from inbox' action triggers a sweep.

## How it works

Inbound comms auto-categorise into jobs by rules/keyword (NO AI) — e.g. a 'Complaint' conversation → a Lead-Nurse callback job; a 'Booking' enquiry → a Reception reply-&-book job; a 'Pricing' enquiry → a Reception reply job; an 'Auto-detect from inbox' action triggers a sweep. This extends the unified queue core (PRD-07/FOLLOWUPS).
Rules/keyword only — auto-categorisation is a UX aid, not a safety control; jobs are advisory and human-actioned. Auto-creation is idempotent (don't double-create for an already-open conversation job); the assigned role follows the category.

## Requirements

- Inbound comms auto-sorted into the right kind of follow-up Job.

## Acceptance Criteria

- [ ] Inbound comms auto-categorise into jobs by rules/keyword (NO AI) — e.g. 'Complaint' → Lead-Nurse callback; 'Booking' → Reception reply-&-book; 'Pricing' → Reception reply.
- [ ] An 'Auto-detect from inbox' action triggers a sweep.
- [ ] Categorisation is a UX aid, not a safety control — jobs are advisory and human-actioned.
- [ ] Auto-creation is idempotent — it doesn't double-create for an already-open conversation job; the assigned role follows the category.

## UI designs / screenshots

- Prototype: Follow-ups — an 'Auto-detect from inbox' button; auto-created job rows carry an 'auto-detected' source tag.

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Job (extends PRD-07/FOLLOWUPS)** — source=auto; type/assignee from the matched rule/keyword
  - _No new entity; rules/keyword only (no AI); idempotent._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Rules/keyword auto-categorisation (no AI) + 'Auto-detect from inbox' sweep**
  Behaviour: inbound comms auto-categorise into jobs by rules/keyword (NO AI); an 'Auto-detect from inbox' action sweeps on demand. Requirements: rules/keyword only (UX aid, not a safety control — advisory, human-actioned); idempotent (don't double-create for an already-open conversation job); the assigned role follows the category.
