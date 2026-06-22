# Client merge: confirmation UI & post-merge retirement

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-MERGE-CONFIRM-UI`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-MERGE`, `PRD-02/CLIENT-MERGE-TRANSACTION`

## Background

As a front desk, I want a clear confirmation before a merge and the merged record retired afterwards, so that I can see exactly what a merge will do and trust it's logged.
Plainly: the confirmation step shown before a merge commits, and the retired state of the merged record afterwards. Where it fits: a follow-up to the client merge basic duplicate detection & review (PRD-02/CLIENT-MERGE) that adds the safety UI around the merge transaction (PRD-02/CLIENT-MERGE-TRANSACTION). It surfaces the per-type counts that will be re-pointed and the MergeLog for audit/reversal reference. It sits in Reception (PRD-02).

## How it works

The transaction follow-up does the merge; this follow-up wraps it in a safe, legible UI. A confirmation step before committing names the surviving primary, lists the per-type counts that will be re-pointed, and warns that the action is logged.
After the merge the merged identity drops from active views while its full history shows under the surviving primary, so the desk sees one clean record.
The MergeLog entry written by the transaction is viewable for audit and reversal reference, closing the loop on a legible, accountable merge.

## Requirements

- A clear confirmation before a merge and the merged record retired afterwards.

## Acceptance Criteria

- [ ] A confirmation step before committing names the surviving primary and lists the per-type counts that will be re-pointed, warning the action is logged.
- [ ] After merge the merged identity drops from active views while its history shows under the primary.
- [ ] The MergeLog entry is viewable for audit/reversal reference.

## UI designs / screenshots

- Prototype: Clients (clients.png) — a merge confirmation naming the surviving primary, the per-type re-pointed counts, and a 'this action is logged' warning.
- Post-merge, the merged record is retired from active views; history shows under the primary.
- The MergeLog entry is viewable for audit/reversal reference.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(reads CLIENT-MERGE-TRANSACTION)** — no new entities; reads the planned re-point counts pre-commit and the MergeLog post-commit
  - _Presentation/safety layer over the merge transaction; the merged identity is retired, not deleted._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Merge confirmation UI + post-merge retirement**
  Behaviour: a confirmation step before committing and a retired state after. Requirements: the confirmation names the surviving primary, lists the per-type counts that will be re-pointed, and warns the action is logged; after merge the merged identity drops from active views while its history shows under the primary; the MergeLog entry is viewable for audit/reversal reference.
