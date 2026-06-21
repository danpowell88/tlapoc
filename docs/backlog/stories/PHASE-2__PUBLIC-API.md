# Public API & webhooks (placeholder)

> **Epic:** [PHASE-2 — Phase 2+ / scale (cross-cutting placeholders)](../epics/PHASE-2.md)  ·  **Key:** `PHASE-2/PUBLIC-API`  ·  **Type:** Story  ·  **Stage:** M7  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** integration

## Background

As a integrator, I want a public API and webhooks, so that third-party tools can integrate.
Outbound/inbound public API + webhooks for third parties (PRD-10 deferred; Phase 3).

## How it works

Placeholder (Phase 3): an outbound/inbound public API + webhooks for third parties. The internal API is already OpenAPI-described and contract-first, so this is auth/rate-limit/versioning + webhook delivery on top.

## Requirements

- A public API and webhooks.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 3; internal API is OpenAPI-described already.
- [ ] Captured so the API stays contract-first.

## Suggested data model

- **(future) ApiKey / Webhook** — tenant_id, scopes, secret / url, events[]
  - _Phase 3._

## Technical notes (high level)

- Stack: Ports-and-adapters integration

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint** — Deferred placeholder — no build yet.
- [ ] **Confirm it still fits scope / regulatory stance**
