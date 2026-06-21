# Client directory: search, filter, merge, soft-delete

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-DIR`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/CLIENT-360`

## Background

As a front desk, I want to search and filter clients, merge duplicates and soft-delete with audit, so that the client list stays accurate and findable.
A searchable client directory with duplicate merge and audited soft-delete keeps the record clean.

## How it works

A fast, searchable client directory with duplicate detection/merge (preserving history + audit) and audited soft-delete, so the client list stays accurate and findable.
Quick client search is reachable from the front-desk shell (the header search).

## Requirements

- To search and filter clients, merge duplicates and soft-delete with audit.
- Compliance: [C10](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Fast search/filter across the directory.
- [ ] Duplicate detection + merge that preserves history and audit.
- [ ] Soft-delete with audit; deleted clients excluded from active views.
- [ ] Quick client search is reachable from the front-desk shell.

## UI designs / screenshots

_Prototype screen: prototype.html — Schedule, 'New booking' wizard, Clients directory & 360._

- Prototype: Clients (clients.png) — searchable/filterable directory list; row -> opens Client 360; merge-duplicates and soft-delete actions.
- Global header search jumps straight to a client.

![clients — prototype screen](../screens/clients.png)

## Suggested data model

- **Client** — (as PRD-01 CLIENT-CORE) + search index
  - _Merge re-points child records; soft-delete sets deleted_at._
- **MergeLog** — id, primary_id, merged_id, at, actor_id
  - _Audited; reversible reference._

## Technical notes (high level)

- Stack: Angular web (admin/front-desk/public)

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Web UI** — prototype.html — Schedule, 'New booking' wizard, Clients directory & 360.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
