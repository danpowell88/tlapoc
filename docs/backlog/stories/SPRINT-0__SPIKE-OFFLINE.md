# Spike — offline queue & sync integrity (provider app)

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-OFFLINE`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 2 pts  ·  **Area:** provider-app

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a mobile engineer, I want a spike proving an encrypted local queue for drafts/photos that syncs with no data loss and last-write-wins drafts, so that the offline-tolerant charting design is viable.

Treatment rooms drop Wi-Fi; the provider app must queue notes/photos encrypted and sync without loss, with server-side finalisation (ADR-0015/0010). De-risk before PRD-05/09.

## Requirements

- A spike proving an encrypted local queue for drafts/photos that syncs with no data loss and last-write-wins drafts.

## Acceptance Criteria

- [ ] Prototype queues drafts + a photo offline (encrypted) and syncs cleanly on reconnect with no loss.
- [ ] Conflict handling (last-write-wins for drafts) demonstrated; finalisation is server-side.
- [ ] Photos never persist on device beyond a transient sync cache (C14/ADR-0009).
- [ ] Approach documented; feeds PRD-05 / PRD-09.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Flutter provider app.
Architecture decisions: ADR-0009, ADR-0010, ADR-0015 (see docs/adr/decision-log.md).
Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/SPIKE-OFFLINE.
Phase: 0 · Priority: P1 · Estimate: 2 pts.
Compliance criteria: C14.

## Tasks (dev pickup)

- [ ] **Define spike scope, questions & success criteria** — What we must learn before building.
- [ ] **Build a throwaway prototype** — Smallest thing that answers the question.
- [ ] **Evaluate results, risks & options**
- [ ] **Write up findings + go/no-go recommendation (ADR if warranted)**
