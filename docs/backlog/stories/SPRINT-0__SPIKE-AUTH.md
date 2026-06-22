# Spike — Entra External ID ↔ Flutter ↔ .NET auth

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/SPIKE-AUTH`  ·  **Type:** Spike  ·  **Stage:** M0  ·  **Priority:** P0  ·  **Estimate:** 2 pts  ·  **Area:** backend

## Background

As a engineer, I want a time-boxed spike proving staff + client sign-in from Flutter and web through to authorised .NET API calls, so that the auth wiring stories proceed on a proven approach.
End-to-end auth across Entra (staff), Entra External ID (clients), Flutter and .NET is novel enough to de-risk before committing the auth wiring stories.

## How it works

A throwaway prototype completes staff sign-in (Entra ID) and client sign-in (External ID) from both Flutter and web, and makes an authorised call into a minimal .NET endpoint that reads tenant + role claims usable for RLS/RBAC. The point is to surface the real gotchas — redirect/PKCE handling on device, token refresh, claim mapping, and the maturity of the Flutter auth libraries for both audiences.
Go/no-go bar: both audiences sign in from both surfaces, the .NET endpoint receives a token carrying a usable tenant id and role claim, and refresh/sign-out behave. If a library or flow proves unworkable, the spike names the alternative (or escalates to an ADR) rather than letting AUTH-STAFF/AUTH-CLIENT discover it mid-build.
This is a spike: produce findings and a recommendation, not production code. The throwaway prototype is discarded; what carries forward is the proven pattern, the chosen libraries and the documented claim contract.

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

- [ ] **Define the spike scope, questions and go/no-go criteria**
  Frame exactly what must be proven and what 'pass' means before building.
  - Questions: can Flutter + web complete Entra (staff) AND External ID (client) sign-in; does an authorised .NET call receive usable tenant + role claims; do refresh/sign-out work; which auth libraries are viable?
  - Go/no-go bar: both audiences sign in from both surfaces and the .NET endpoint reads a tenant id + role claim usable for RLS/RBAC, with working refresh/sign-out.
  - Time-box and the explicit hand-off targets (AUTH-STAFF, AUTH-CLIENT).
- [ ] **Build the throwaway end-to-end prototype**
  Prove the full path with disposable code.
  - Staff (Entra) + client (External ID) sign-in from Flutter and web.
  - An authorised call into a minimal .NET endpoint that surfaces tenant + role claims for RLS/RBAC.
  - Exercise the sharp edges: device redirect/PKCE, token refresh, claim mapping, sign-out. This is throwaway — measure feasibility, don't productionise.
- [ ] **Write up findings, library choices and a go/no-go (ADR if warranted)**
  Capture the decision so the wiring stories proceed on a proven approach.
  - Findings, chosen libraries, the documented claim contract (what tokens must carry for RLS/RBAC), and gotchas.
  - A clear go/no-go; raise an ADR if a real decision/alternative emerged.
  - Explicitly state how AUTH-STAFF and AUTH-CLIENT should build on the result.
