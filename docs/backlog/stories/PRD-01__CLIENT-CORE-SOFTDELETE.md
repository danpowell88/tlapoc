# Client core: soft-delete with audit

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/CLIENT-CORE-SOFTDELETE`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/CLIENT-CORE`

## Background

As a system, I want to soft-delete a client so they leave active/bookable/search views but their row and history remain, so that deletion is reversible and lawful, with destruction left to the retention engine.
Plainly: deleting a client hides them from active and bookable views without ever destroying the row — the record and its history stay for retention and audit. Where it fits: a follow-up to the client core record (PRD-01/CLIENT-CORE), which ships the DOB record + age derivation; this adds the delete lifecycle. Deliberately not destruction: physically destroying records is PRD-01/RETENTION's job — here a soft-delete just excludes the client from active use and writes an audit event.

## How it works

Soft-delete stamps deleted_at so a deleted client drops out of active, bookable and search views while the row and all its history are preserved. This is the lifecycle plumbing on top of the client core record (PRD-01/CLIENT-CORE): a deleted client cannot be booked or surface in active search, but nothing is physically removed.
The boundary with retention is deliberate: this story never hard-deletes — lawful physical destruction (with the destruction register + certificate) is PRD-01/RETENTION's job, and a soft-delete does not override a legal retention period or a litigation hold. Every soft-delete writes an audit event so there is a record of who removed a client and when.

## Requirements

- To soft-delete a client so they leave active/bookable/search views but their row and history remain.

## Acceptance Criteria

- [ ] A soft-deleted client (deleted_at set) is excluded from active / bookable / search views but the row and its history remain.
- [ ] The client is never hard-deleted here — destruction is RETENTION's job.
- [ ] A soft-deleted client cannot be booked or appear in active search.
- [ ] The delete writes an audit event.

## UI designs / screenshots

- Surfaces as the delete/restore lifecycle on the client record; a soft-deleted client is excluded from active/bookable/search views (the full client directory + 360 profile are PRD-02).
- No hard-delete affordance — destruction is RETENTION's job; the delete writes an audit event.

## Suggested data model

- **Client (extends PRD-01/CLIENT-CORE)** — uses existing deleted_at
  - _No new entity — adds the soft-delete lifecycle over the Client core; never hard-deletes (destruction is RETENTION)._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Soft-delete with audit (retention/destruction stays RETENTION's job)**
  Behaviour: support soft-delete (deleted_at) so a deleted client is excluded from active/bookable/search views but the row and its history remain. Requirements: never hard-delete here — destruction is RETENTION's job; a soft-deleted client cannot be booked or appear in active search; the delete writes an audit event.
