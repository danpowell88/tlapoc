# Per-tenant white-label theming (placeholder)

> **Epic:** [PHASE-2 — Phase 2+ / scale (cross-cutting placeholders)](../epics/PHASE-2.md)  ·  **Key:** `PHASE-2/WHITE-LABEL`  ·  **Type:** Story  ·  **Stage:** M7  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** design

## Background

As a clinic owner, I want to brand the platform with my clinic's look, so that clients see my brand.
Plainly: this would let each clinic skin the web and mobile apps with its own logo, colours and name. Where it fits: a deferred Phase 2+ placeholder — v1 ships one clinic's brand, so per-tenant theming waits until there are multiple clinics to brand.  Placeholder (Phase 2+): per-tenant branding/theming of web and apps (a PRD-01 non-goal).

## How it works

Placeholder (Phase 2+): per-tenant branding/theming of web and apps. The design system is token-driven, so theming is a matter of per-tenant token sets (colours, logo, type) applied to web + Flutter apps — a per-tenant theme store + application layer, no component redesign. Captured so the design system stays token-driven.

## Requirements

- To brand the platform with my clinic's look.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2+; design tokens are themeable by construction.
- [ ] Captured so the design system stays token-driven.

## UI designs / screenshots

Future — not built in the prototype (some shown as concept cards in Settings → Integrations).

## Suggested data model

- **(future) TenantTheme** — tenant_id, tokens(json)
  - _Design system already token-driven._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Placeholder: per-tenant white-label theming (Phase 2+)**
  Deferred. Per-tenant token sets (colours, logo, type) applied to web + Flutter apps via a TenantTheme store + application layer; the design system is already token-driven. Not built in v1.
