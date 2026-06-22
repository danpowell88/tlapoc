# Client merge: re-point all child records + MergeLog

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-MERGE-TRANSACTION`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-MERGE`

## Background

As a front desk, I want merging two clients to move all their history onto one surviving record, so that no visit, consent or invoice is orphaned when duplicates are merged.
Plainly: the transaction that actually merges two client records — nominating a surviving primary and re-pointing every child record onto it, with an audit log. Where it fits: a follow-up to the client merge basic duplicate detection & review (PRD-02/CLIENT-MERGE) that adds the merge engine on top of the candidate review. Because a merge moves clinical and consent records between identities it is server-enforced in one transaction, capability-gated and audited; it never hard-deletes (PRD-01/RETENTION governs destruction). It sits in Reception (PRD-02).

## How it works

The basic story surfaces candidate duplicate pairs; this follow-up runs the merge. A confirmed merge nominates a surviving primary and a merged record, then re-homes everything.
The merge runs as a single server-side transaction that re-points EVERY child record — appointments/visits, consents and image-consent, photos, invoices, memberships, rewards and follow-up jobs — from the merged client onto the primary, preserving all history; nothing is deleted.
It writes a MergeLog capturing primary_id, merged_id, actor, timestamp and the counts re-pointed per type, giving an audited, reversible reference. The merged identity is retired but its history lives on under the primary (PRD-01/RETENTION governs any true destruction). The action is capability-gated.

## Requirements

- Merging two clients to move all their history onto one surviving record.

## Acceptance Criteria

- [ ] A merge nominates a surviving primary and re-points ALL child records (appointments/visits, consents, image-consent, photos, invoices, memberships, rewards, jobs) to it, preserving history.
- [ ] A MergeLog records primary_id, merged_id, actor, timestamp and per-type re-pointed counts (audited, reversible reference).
- [ ] The merge is server-enforced in one transaction and capability-gated.
- [ ] Nothing is hard-deleted (PRD-01/RETENTION governs destruction).

## UI designs / screenshots

- Prototype: Clients (clients.png) — the merge runs from the confirmed candidate pair.
- The merge re-points all child records onto the surviving primary in one transaction.
- A MergeLog entry is written for audit/reversal reference.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **MergeLog** — id, tenant_id, primary_id, merged_id, at, actor_id, repointed_counts(json)
  - _Audited; merge re-points child records to the primary and preserves history; reversible reference (never a hard delete)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Merge transaction: re-point all child records + MergeLog**
  Behaviour: merging nominates a surviving primary and re-homes everything from the merged record. Requirements: in a single server-side transaction, re-point ALL child records (appointments/visits, consents, image-consent, photos, invoices, memberships, rewards, jobs) to the primary, preserving history; write a MergeLog (primary_id, merged_id, actor, at, repointed_counts per type); server-enforced and capability-gated; nothing is hard-deleted (PRD-01/RETENTION governs destruction).
