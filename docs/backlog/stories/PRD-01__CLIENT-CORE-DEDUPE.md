# Client core: duplicate detection & reviewed merge

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CLIENT-CORE-DEDUPE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/CLIENT-CORE`

## Background

As a system, I want duplicate client records surfaced as merge candidates and a reviewed, audited merge, so that duplicates are cleaned up without ever falsely merging two real people.
Plainly: spotting two records that look like the same person (matching name, DOB and contact) and offering a reviewed merge — never silently merging, because a false merge of two real people is dangerous. Where it fits: a follow-up to the client core record (PRD-01/CLIENT-CORE) that adds duplicate handling on top of the core record. Merge is a reviewed action that re-points history to the surviving record and is audited; the full client directory and 360 profile remain PRD-02.

## How it works

Duplicate handling surfaces merge candidates — records matching on name + DOB (date of birth) + contact — as advisory suggestions only. It never auto-merges, because falsely merging two real people who happen to share details is far worse than leaving a suspected duplicate flagged.
Merge is therefore a reviewed action: an operator confirms, the merge re-points clinical/booking history onto the surviving record, and the action writes an audit event. Merged-away records (and soft-deleted ones, PRD-01/CLIENT-CORE-SOFTDELETE) stay out of active views. The full client directory, search and 360 profile that host this in everyday use are PRD-02.

## Requirements

- Duplicate client records surfaced as merge candidates and a reviewed, audited merge.

## Acceptance Criteria

- [ ] Duplicate / merge candidates (matching name + DOB + contact) are surfaced as suggestions, never auto-merged.
- [ ] Merge is a reviewed action that re-points history to the surviving record.
- [ ] A merge writes an audit event.
- [ ] Merged-away (and soft-deleted) records stay out of active views (full directory + 360 profile are PRD-02).

## UI designs / screenshots

- Surfaces as a merge-candidates suggestion (matching name + DOB + contact) with a reviewed confirm-merge action; never an automatic merge.
- Merge re-points history to the surviving record and writes an audit event; merged-away records stay out of active views (full directory + 360 profile are PRD-02).

## Suggested data model

- **Client (extends PRD-01/CLIENT-CORE)** — merge re-points history to the surviving Client; merged-away records excluded from active views
  - _No new entity — adds advisory duplicate detection + a reviewed merge over the Client core; never auto-merges._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Duplicate detection & reviewed merge**
  Behaviour: surface duplicate/merge candidates (matching name + DOB (date of birth) + contact) as suggestions, never auto-merging two real people. Requirements: merge is a reviewed action that re-points history to the surviving record and writes an audit event; soft-deleted and merged-away records stay out of active views (full client directory + 360 profile are PRD-02).
