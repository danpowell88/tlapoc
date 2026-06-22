# Pre-care instruction sequences (per treatment type)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/PRECARE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/REMINDERS-CARE`

## Background

As a client, I want pre-care instructions before my treatment, tailored to what I'm having, so that I arrive properly prepared.
Plainly: timed pre-treatment instructions — for example, avoid blood thinners before toxin — sent ahead of a booked visit and tailored to the treatment. Where it fits: a follow-up to the basic appointment reminders/confirmations (PRD-07/REMINDERS-CARE) that adds pre-care sequences on the same sequence engine. Pre-care is transactional (Spam Act exempt) so it sends regardless of marketing opt-in, but it still must not name or price S4 (Schedule 4 prescription-only medicine) items (C9). Keyed by treatment type so a filler client and a skin-needling client get the right cadence and content. All sends log to the comms history.

## How it works

Pre-care (e.g. avoid blood thinners before toxin) is a Sequence keyed by treatment type and timed ahead of the booked visit, running on the sequence engine from the basic reminders/confirmations story (PRD-07/REMINDERS-CARE). A filler client and a skin-needling client get the right pre-care content.
Pre-care is transactional (Spam Act exempt) so it sends regardless of marketing opt-in and has no unsubscribe-gating — but it still must not name or price S4 (Schedule 4 prescription-only medicine) items (C9). All sends log to the comms history.

## Requirements

- Pre-care instructions before my treatment, tailored to what I'm having.

## Acceptance Criteria

- [ ] A pre-care Sequence is keyed by treatment type and timed ahead of the booked visit, sent on the existing sequence engine (PRD-07/REMINDERS-CARE).
- [ ] Pre-care is transactional (Spam Act exempt) — it sends regardless of marketing opt-in (no unsubscribe-gating).
- [ ] Pre-care content must not name or price S4 (Schedule 4 prescription-only medicine) items (C9).
- [ ] All sends log to the comms history.

## UI designs / screenshots

- Prototype: Comms -> Automations — a pre-care sequence per treatment type (timed before the visit); sends appear in the client's comms history.

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Sequence (extends PRD-07/REMINDERS-CARE)** — trigger=booking, treatment_type, kind=transactional, steps timed before the visit
  - _No new entity; pre-care content; transactional (opt-in exempt); no S4 references (C9)._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Pre-care sequences per treatment type (transactional, no S4)**
  Behaviour: a pre-care Sequence keyed by treatment type sends timed pre-treatment instructions ahead of the booked visit on the engine from PRD-07/REMINDERS-CARE. Requirements: transactional (Spam Act exempt, no unsubscribe-gating); content must not name/price S4 (Schedule 4 prescription-only medicine) (C9); all sends log to the comms history.
