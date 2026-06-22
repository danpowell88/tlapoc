# Spike — Postgres RLS with EF Core session context

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-RLS`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 2 pts  ·  **Area:** data

## Background

As a engineer, I want a spike proving EF Core reliably sets the Postgres session tenant for RLS under connection pooling and async, so that the RLS baseline is built on a verified pattern.
Setting the per-request tenant for RLS through EF Core's connection/session lifecycle has known sharp edges (pooling, background jobs). Prove it before building on it.

## How it works

Spike proving EF Core reliably sets the Postgres session tenant for RLS under connection pooling and async, with a safe audited elevated path for background jobs and an acceptable performance impact. De-risks the RLS baseline (ADR-0002/0003).

## Requirements

- A spike proving EF Core reliably sets the Postgres session tenant for RLS under connection pooling and async.

## Acceptance Criteria

- [ ] Prototype shows RLS isolation holds across pooled connections and async requests.
- [ ] A safe elevated/bypass path for background jobs is demonstrated and audited.
- [ ] Performance impact measured and acceptable.
- [ ] Pattern documented and feeds SPRINT-0/RLS.

## Technical notes (high level)

- Architecture decisions: [ADR-0002](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0003](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)
- Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Define spike scope, questions & success criteria**
  List the unknowns to resolve and the pass/fail bar before building; time-box it.
- [ ] **Build a throwaway prototype**
  Smallest end-to-end slice that answers the questions (not production code); measure the risky bits.
- [ ] **Write up findings + go/no-go recommendation (ADR if warranted)**
  What worked, the gotchas, the chosen approach + its impact on the dependent stories.
