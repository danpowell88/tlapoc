# Reviews: auto-detect negative reviews / complaint keywords → Job

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REVIEWS-AUTODETECT`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/REVIEWS`

## Background

As a owner, I want negative reviews to auto-raise follow-up jobs, so that a bad review becomes an action and problems are caught early.
Plainly: catch the bad reviews automatically — anything ≤3 stars or matching complaint keywords gets a 'needs follow-up' badge and raises a Job so it becomes an action, not just a notification. Where it fits: a follow-up to the reviews core (PRD-07/REVIEWS), which handles request/reply/acknowledge/flag; this closes the loop by auto-raising follow-up Jobs for negative reviews. Jobs route into the unified Follow-ups queue (PRD-07/FOLLOWUPS) with the same Lead-Nurse/Reception split, and raising is idempotent. An 'Auto-detect follow-ups' action sweeps on demand.

## How it works

Negative reviews (≤3★) and complaint-keyword matches (unhappy/refund/rude/pain/no one called...) are auto-detected and shown with a 'needs follow-up' badge, raising review Jobs into the Follow-ups queue (PRD-07/FOLLOWUPS) so a bad review becomes an action, not just a notification; an 'Auto-detect follow-ups' action sweeps on demand. This extends the reviews core (PRD-07/REVIEWS).
Rating ≤3 OR a keyword match flags needs-follow-up; raising Jobs is idempotent; routing follows the same Lead-Nurse (clinical/unhappy) / Reception (otherwise) split as the core's manual flag.

## Requirements

- Negative reviews to auto-raise follow-up jobs.

## Acceptance Criteria

- [ ] Negative reviews (≤3★) and complaint-keyword matches (unhappy/refund/rude/pain/no one called...) are auto-detected and shown with a 'needs follow-up' badge.
- [ ] Detected reviews raise review Jobs into the Follow-ups queue (PRD-07/FOLLOWUPS) with the same Lead-Nurse/Reception routing as the core.
- [ ] An 'Auto-detect follow-ups' action sweeps on demand.
- [ ] Raising Jobs is idempotent (no duplicate for an already-open review job).

## UI designs / screenshots

- Prototype: Growth -> Reviews — 'needs follow-up' badge on ≤3★ and complaint matches; 'Auto-detect follow-ups' (scanReviews).

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Review (extends PRD-07/REVIEWS)** — rating/keyword match → needs-follow-up + review Job (PRD-07/FOLLOWUPS)
  - _No new entity; auto-detect over the core Review; idempotent Job raising._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Auto-detect negative reviews / complaint keywords -> Job**
  Behaviour: negative reviews (≤3★) and complaint-keyword matches are auto-detected, shown with a 'needs follow-up' badge, and raise review Jobs into Follow-ups (PRD-07/FOLLOWUPS); an 'Auto-detect follow-ups' action sweeps on demand. Requirements: rating ≤3 OR keyword match flags needs-follow-up; idempotent Job raising; same Lead-Nurse/Reception routing as the core.
