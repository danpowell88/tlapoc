# Spike — Postgres RLS with EF Core session context

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-RLS`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 2 pts  ·  **Area:** data

## Background

As a engineer, I want a spike proving EF Core reliably sets the Postgres session tenant for RLS under connection pooling and async, so that the RLS baseline is built on a verified pattern.
Setting the per-request tenant for Postgres RLS through EF Core's connection/session lifecycle has known sharp edges — connection pooling can leak a session setting between requests, and async/await can cross connection boundaries. Because RLS is the platform's most important safety property (ADR-0002/0003), the pattern is proven in a spike before RLS builds on it.  Output feeds SPRINT-0/RLS directly: the verified session-context pattern, the audited bypass path for jobs, and the measured performance impact.

## How it works

A prototype demonstrates that RLS isolation holds across pooled connections and async requests: the session tenant set for request A never leaks into request B sharing the pool, and the setting follows the connection correctly through async execution. This is the exact failure mode that would silently break tenant isolation if assumed rather than proven.
It also demonstrates a safe elevated/bypass path for background jobs — how a worker legitimately operates cross-tenant without that capability being reachable from request handling — and that the elevation is audited. And it measures the performance impact of issuing the per-request SET so the team knows the cost is acceptable before standardising on it.
Go/no-go bar: isolation provably holds under pooling + async, the bypass path works and is audited, and the overhead is acceptable. The documented pattern (where the SET happens in the connection lifecycle, how it's cleared, how the bypass is gated) is what RLS implements; the prototype itself is discarded.

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

- [ ] **Define the spike scope, questions and go/no-go criteria**
  Frame the pooling/async risk precisely and what proving it requires.
  - Questions: does the per-request session tenant leak across pooled connections; does it follow the connection through async; can a job bypass safely + audited; what's the performance cost?
  - Go/no-go bar: isolation holds under pooling + async, the audited bypass works, overhead acceptable.
  - Time-box and the hand-off target (SPRINT-0/RLS (row-level security)).
- [ ] **Build the throwaway prototype and stress the failure modes**
  Prove the pattern under the conditions that actually break it.
  - Exercise concurrent requests over a shared connection pool and assert no cross-request session-tenant leak; assert the setting survives async boundaries.
  - Demonstrate a background-job bypass path that's unreachable from request code and emits an audit event.
  - Measure the overhead of the per-request SET. Disposable code — measuring, not productionising.
- [ ] **Write up the verified pattern, bypass path and perf, with go/no-go**
  Document exactly what RLS (row-level security) should implement.
  - Where in the EF Core connection lifecycle the SET happens, how it's cleared on return, and how the job bypass is gated + audited.
  - The measured performance impact and the go/no-go.
  - ADR only if a real alternative/decision surfaced (e.g. against a particular pooling config).
