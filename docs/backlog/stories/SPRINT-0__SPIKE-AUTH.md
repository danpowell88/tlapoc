# Spike — Entra External ID ↔ Flutter ↔ .NET auth

> **Epic:** [SPRINT-0 — Sprint 0 — Foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-AUTH`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 2 pts  ·  **Area:** backend

## Background

Sprint 0 — Foundations & setup — Everything the team needs in place before feature work begins: repositories and solution structure, CI/CD, cloud environments in Australia East, identity wiring for staff and clients, the Postgres + RLS data baseline, the API/web/app shells, a shared design system, observability, a security baseline, and the four de-risk spikes called out in the docs index.

As a engineer, I want a time-boxed spike proving staff + client sign-in from Flutter and web through to authorised .NET API calls, so that the auth wiring stories proceed on a proven approach.

End-to-end auth across Entra (staff), Entra External ID (clients), Flutter and .NET is novel enough to de-risk before committing the auth wiring stories.

## Requirements

- A time-boxed spike proving staff + client sign-in from Flutter and web through to authorised .NET API calls.

## Acceptance Criteria

- [ ] A throwaway prototype completes Entra (staff) and External ID (client) sign-in from Flutter and web.
- [ ] An authorised call reaches a .NET endpoint with tenant + role claims usable for RLS/RBAC.
- [ ] Findings, library choices and gotchas written up; risks/decisions captured (ADR if needed).
- [ ] Outcome explicitly feeds AUTH-STAFF / AUTH-CLIENT.

## UI designs / screenshots

Non-UI / platform scaffolding — no prototype screen.

## Technical notes (high level)

Stack: .NET API (domain/services).
Architecture decisions: ADR-0004 (see docs/adr/decision-log.md).
Time-boxed spike — produce findings + a go/no-go, not production code.

## Other

Epic: SPRINT-0 — Sprint 0 — Foundations & setup.
Source PRD: docs/prds/PRD-01-foundations-tenancy.md.
Backlog key: SPRINT-0/SPIKE-AUTH.
Phase: 0 · Priority: P0 · Estimate: 2 pts.

## Tasks (dev pickup)

- [ ] **Define spike scope, questions & success criteria** — What we must learn before building.
- [ ] **Build a throwaway prototype** — Smallest thing that answers the question.
- [ ] **Evaluate results, risks & options**
- [ ] **Write up findings + go/no-go recommendation (ADR if warranted)**
