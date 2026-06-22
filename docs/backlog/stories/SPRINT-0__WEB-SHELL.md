# Angular web shell: routing, auth guard, layout

> **Epic:** [SPRINT-0 — Engineering foundations & setup](../epics/SPRINT-0.md)  ·  **Key:** `SPRINT-0/WEB-SHELL`  ·  **Type:** Chore  ·  **Stage:** M0  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `SPRINT-0/AUTH-STAFF`, `SPRINT-0/DESIGN`

## Background

As a front-end developer, I want an Angular shell with the Entra auth guard, top-level routing, a role-aware navigation frame and the design-system theme applied, so that feature screens drop into a consistent, authenticated layout.
Sprint 0 (setup), web front-end: this builds the empty but working frame of the staff web app — the sign-in gate, the page routing, a navigation bar that adapts to the user's role, and the product look-and-feel — so that real screens can simply drop in later. It builds on staff sign-in and the design system, and calls one sample screen through the generated API client to prove the whole stack works together. The real navigation and home dashboard come later in the App-shell phase. The admin/front-desk web app needs a shell — auth guard, role-aware nav, layout — before feature screens land.

## How it works

The Angular shell guards every route with the Entra auth guard from AUTH-STAFF: unauthenticated users are redirected to Entra sign-in and authenticated users land in the shell. Top-level routing and a navigation frame are in place, with navigation driven by capability/role flags — a placeholder model until PRD-01 RBAC (role-based access control; ADR-0017's capabilities) lands, but structured so the real capability checks slot in without re-laying-out the shell.
The design-system theme and tokens from DESIGN are applied globally so the shell already looks like the product, and the cross-cutting UX (user-experience) patterns (banners, chips) are available to feature screens. A sample feature route renders inside the shell using the OPENAPI-generated API client, proving auth + routing + theme + API call together.
This is intentionally a shell, not features: APP-NAV builds the real left-nav/role-aware structure and TODAY the landing dashboard (see dashboard.png for where it's heading). WEB-SHELL just guarantees the authenticated, themed container exists.

## Requirements

- An Angular shell with the Entra auth guard, top-level routing, a role-aware navigation frame and the design-system theme applied.

## Acceptance Criteria

- [ ] Unauthenticated users are redirected to Entra sign-in; authenticated users land on a shell.
- [ ] Navigation is driven by capabilities/role (placeholder until PRD-01 RBAC lands).
- [ ] Design-system theme + tokens applied globally.
- [ ] A sample feature route renders inside the shell using the generated API client.

## UI designs / screenshots

_Prototype screen: Non-UI / platform scaffolding — no prototype screen._

- The authenticated app frame (later filled by PLATFORM/APP-NAV; see dashboard.png) — sign-in redirect, shell layout, themed.

## Technical notes (high level)

- Architecture decisions: [ADR-0005](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Build the Angular shell: auth guard, routing, capability-driven nav frame, themed, with a sample route**
  Stand up the authenticated, themed container feature screens drop into.
  - Entra auth guard (AUTH-STAFF): unauthenticated -> sign-in redirect; authenticated -> shell.
  - Top-level routing and a navigation frame whose items are driven by capability/role flags — a placeholder model now, structured so PRD-01 RBAC (role-based access control) capabilities slot in without re-layout.
  - Design-system theme + tokens (DESIGN) applied globally; cross-cutting patterns available to screens.
  - A sample feature route rendering inside the shell via the OPENAPI-generated client, proving auth + routing + theme + API together.
- [ ] **Document the shell structure and how feature screens plug in**
  Write the front-end shell guide so feature work is consistent and APP-NAV can extend it.
  - How routes register, how the auth guard applies, and how the capability/role nav placeholder works (and where real RBAC (role-based access control) replaces it).
  - How a feature screen consumes the generated API client and the design system inside the shell.
  - The boundary between this shell and PLATFORM/APP-NAV + TODAY.
