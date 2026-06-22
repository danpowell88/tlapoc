# Aftercare instruction sequences (day-0 + day-3, per treatment type)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/AFTERCARE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/REMINDERS-CARE`

## Background

As a client, I want aftercare instructions after my treatment, tailored to what I had, so that I recover well and know what to watch for.
Plainly: care tips sent after a treatment — a day-0 and a day-3 touch tailored to the treatment — to reduce worry and complications. Where it fits: a follow-up to the basic appointment reminders/confirmations (PRD-07/REMINDERS-CARE) that adds aftercare sequences on the same sequence engine, triggered by a completed visit. Aftercare is transactional (Spam Act exempt) so it sends regardless of marketing opt-in, but it still must not name or price S4 (Schedule 4 prescription-only medicine) items (C9). Keyed by treatment type. All sends log to the comms history.

## How it works

Aftercare (day-0 + day-3 care tips) is a Sequence keyed by treatment type, triggered by a completed visit, running on the sequence engine from the basic reminders/confirmations story (PRD-07/REMINDERS-CARE). A multi-touch day-0 and day-3 cadence reduces worry and complications, with the right content per treatment type.
Aftercare is transactional (Spam Act exempt) so it sends regardless of marketing opt-in and has no unsubscribe-gating — but it still must not name or price S4 (Schedule 4 prescription-only medicine) items (C9). All sends log to the comms history.

## Requirements

- Aftercare instructions after my treatment, tailored to what I had.

## Acceptance Criteria

- [ ] An aftercare Sequence keyed by treatment type sends a day-0 and a day-3 touch after a completed visit, on the existing sequence engine (PRD-07/REMINDERS-CARE).
- [ ] Aftercare is transactional (Spam Act exempt) — it sends regardless of marketing opt-in (no unsubscribe-gating).
- [ ] Aftercare content must not name or price S4 (Schedule 4 prescription-only medicine) items (C9).
- [ ] All sends log to the comms history.

## UI designs / screenshots

- Prototype: Comms -> Automations — 'Aftercare sequence — Day 0 + day 3 care tips after each visit · SMS · Post-treatment'; sends appear in the client's comms history.

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Sequence (extends PRD-07/REMINDERS-CARE)** — trigger=visit, treatment_type, kind=transactional, steps at day-0 + day-3
  - _No new entity; aftercare content; transactional (opt-in exempt); no S4 references (C9)._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Aftercare sequences (day-0 + day-3, per treatment type, transactional, no S4)**
  Behaviour: an aftercare Sequence keyed by treatment type sends a day-0 and a day-3 care touch after a completed visit on the engine from PRD-07/REMINDERS-CARE. Requirements: transactional (Spam Act exempt, no unsubscribe-gating); content must not name/price S4 (Schedule 4 prescription-only medicine) (C9); all sends log to the comms history.
