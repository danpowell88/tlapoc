# Client directory: audited soft-delete

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-DIR-SOFT-DELETE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-DIR`

## Background

As a front desk, I want to soft-delete a client with an audit trail, so that the active list stays clean without destroying history.
Plainly: removing a client from active views without destroying their history, with an audit entry. Where it fits: a follow-up to the client directory basic search & list (PRD-02/CLIENT-DIR) that adds audited soft-delete on top of the directory. It deliberately never hard-deletes — true destruction is governed by the retention policy in Foundations (PRD-01/RETENTION). It sits in Reception (PRD-02).

## How it works

The basic directory finds and lists clients; this follow-up adds audited soft-delete to keep the list clean. Soft-deleting a client sets deleted_at and writes an audit entry.
A soft-deleted client is excluded from search and active lists (the basic already excludes deleted_at rows) but is retained — nothing is destroyed.
Soft-delete never hard-deletes: true destruction is governed solely by the retention policy in Foundations (PRD-01/RETENTION), respecting the clinic's retention obligations. The action is capability-gated.

## Requirements

- To soft-delete a client with an audit trail.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Soft-deleting a client sets deleted_at and writes an audit entry.
- [ ] Deleted clients are excluded from search/active lists but retained.
- [ ] True destruction is governed by PRD-01 RETENTION only, never here.
- [ ] The action is capability-gated.

## UI designs / screenshots

- Prototype: Clients (clients.png) — a soft-delete action on a client.
- Deleted clients drop from active views; the action writes an audit entry.
- Capability-gated; never a hard delete.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **Client (extends CLIENT-DIR)** — deleted_at
  - _Soft-delete sets deleted_at and excludes from active views; never hard-deleted (PRD-01 RETENTION governs destruction)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Soft-delete (audited) + active-view exclusion**
  Behaviour: soft-deleting a client removes them from active views without destroying history. Requirements: set deleted_at and write an audit entry; deleted clients are excluded from search/active lists but retained (true destruction is governed by PRD-01 RETENTION only, never here); capability-gated.
