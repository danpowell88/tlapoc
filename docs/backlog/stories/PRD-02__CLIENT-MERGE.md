# Client merge — basic duplicate detection & review

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-MERGE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-DIR`

## Background

As a front desk, I want to find duplicate client records and merge them into one without losing any history, so that a client has a single accurate record and no visit, consent or invoice is orphaned.
Plainly: the tool that spots when the same person exists twice in the client list and merges the duplicates into one surviving record, re-pointing all their history onto it. Where it fits: a sibling of the client directory (PRD-02/CLIENT-DIR) in Reception (PRD-02); the directory is how staff find a client, and this is how staff keep that list clean. It is deliberately separate from deletion: a merge preserves and re-homes history rather than removing it, and like soft-delete it never hard-deletes anything (true destruction is governed by PRD-01/RETENTION). Because a merge moves clinical and consent records between identities, it is audited and reversible by reference.

## How it works

Duplicate detection surfaces candidate pairs using name / date-of-birth / phone / email heuristics so the desk can review and confirm a merge rather than guessing. A confirmed merge nominates a surviving primary and a merged record.
The merge runs as a single server-side transaction that re-points EVERY child record — appointments/visits, consents and image-consent, photos, invoices, memberships, rewards and follow-up jobs — from the merged client onto the primary, preserving all history; nothing is deleted. It writes a MergeLog capturing primary_id, merged_id, actor, timestamp and the counts re-pointed per type, giving an audited, reversible reference.
Merge never hard-deletes: the merged identity is retired but its history lives on under the primary, consistent with retention obligations (PRD-01/RETENTION). The action is capability-gated and audited.

## Requirements

- To find duplicate client records and merge them into one without losing any history.

## Acceptance Criteria

- [ ] Candidate duplicates are surfaced from name/DOB/phone/email heuristics.
- [ ] A merge re-points ALL child records (appointments, consents, image-consent, photos, invoices, memberships, rewards, jobs) to the surviving primary, preserving history.
- [ ] A MergeLog records primary/merged/actor/timestamp and per-type re-pointed counts (audited, reversible reference).
- [ ] Merge is server-enforced in one transaction and capability-gated.

## UI designs / screenshots

- Prototype: Clients (clients.png) — a 'merge duplicates' action surfaced from the directory; candidate-duplicate review showing the two records side-by-side with the fields that match.
- Merge confirmation names the surviving primary, lists what will be re-pointed (counts per type), and warns that the action is logged.
- Post-merge, the merged record is retired from active views; a MergeLog entry is viewable for audit/reversal reference.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **MergeLog** — id, tenant_id, primary_id, merged_id, at, actor_id, repointed_counts(json)
  - _Audited; merge re-points child records to the primary and preserves history; reversible reference (never a hard delete)._
- **(derived) DuplicateCandidate** — = pairs of Clients scored by name/dob/phone/email match heuristics
  - _Surfaced for desk review; a merge is only ever staff-confirmed, never automatic._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Duplicate detection heuristics + candidate review**
  Behaviour: surface candidate duplicate pairs for the desk to review. Requirements: score pairs on name / date-of-birth / phone / email match heuristics; present the two records side-by-side with matching fields highlighted; a merge is always staff-confirmed, never automatic; tenant-scoped. The merge transaction and the confirmation/retirement UI are follow-ups.
