# Spike — Entra External ID ↔ Flutter ↔ .NET auth

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-AUTH`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 2 pts  ·  **Area:** backend

## Background

As a engineer, I want a time-boxed spike proving staff + client sign-in from Flutter and web through to authorised .NET API calls, so that the auth wiring stories proceed on a proven approach.
End-to-end auth across Entra (staff), Entra External ID (clients), Flutter and .NET is novel enough to de-risk before committing the auth wiring stories.

## How it works

Time-boxed spike proving end-to-end auth: staff (Entra) + client (External ID) sign-in from Flutter and web through to an authorised .NET call carrying tenant + role claims usable for RLS/RBAC. De-risks the highest-uncertainty plumbing before the AUTH wiring stories; output is findings + an ADR if needed.

## Requirements

- A time-boxed spike proving staff + client sign-in from Flutter and web through to authorised .NET API calls.

## Acceptance Criteria

- [ ] A throwaway prototype completes Entra (staff) and External ID (client) sign-in from Flutter and web.
- [ ] An authorised call reaches a .NET endpoint with tenant + role claims usable for RLS/RBAC.
- [ ] Findings, library choices and gotchas written up; risks/decisions captured (ADR if needed).
- [ ] Outcome explicitly feeds AUTH-STAFF / AUTH-CLIENT.

## Technical notes (high level)

- Architecture decisions: [ADR-0004](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)
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
