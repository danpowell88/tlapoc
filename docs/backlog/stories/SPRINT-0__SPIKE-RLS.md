# Spike — Postgres RLS with EF Core session context

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-RLS`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 2 pts  ·  **Area:** data

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a engineer, I want a spike proving EF Core reliably sets the Postgres session tenant for RLS under connection pooling and async, so that the RLS baseline is built on a verified pattern.

Setting the per-request tenant for RLS through EF Core's connection/session lifecycle has known sharp edges (pooling, background jobs). Prove it before building on it.

## Requirements

- A spike proving EF Core reliably sets the Postgres session tenant for RLS under connection pooling and async.

## Acceptance Criteria

- [ ] Prototype shows RLS isolation holds across pooled connections and async requests.
- [ ] A safe elevated/bypass path for background jobs is demonstrated and audited.
- [ ] Performance impact measured and acceptable.
- [ ] Pattern documented and feeds SPRINT-0/RLS.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: Postgres + EF Core (RLS).
Architecture decisions: ADR-0002, ADR-0003 (see docs/adr/decision-log.md).
Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/SPIKE-RLS.
Phase: 0 · Priority: P0 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Define spike scope, questions & success criteria** — What we must learn before building.
- [ ] **Build a throwaway prototype** — Smallest thing that answers the question.
- [ ] **Evaluate results, risks & options**
- [ ] **Write up findings + go/no-go recommendation (ADR if warranted)**
