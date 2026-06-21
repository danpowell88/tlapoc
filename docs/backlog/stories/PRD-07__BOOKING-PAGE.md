# Public booking page: generic names, S4 prices withheld

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/BOOKING-PAGE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a owner, I want my public booking page to use generic service names and withhold S4 prices automatically, so that we don't reference S4 in public advertising.
The public booking page uses generic service names and withholds S4 prices by configuration (catalog schedule flag), with no advertising linter (REQ-NOTIF-12, C9).

## How it works

The public booking page uses generic service names and withholds S4 prices by configuration (the catalog schedule flag), with no advertising linter (C9). No brands, 'anti-wrinkle injections', prices or #botox appear for S4 services.
Advertising compliance beyond this is clinic-owned (external tools).

## Requirements

- My public booking page to use generic service names and withhold S4 prices automatically.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] The booking page renders generic service names and withholds S4 prices for any S4-flagged service (configuration-driven).
- [ ] No brands, 'anti-wrinkle injections', prices or #botox appear for S4 services.
- [ ] Configuration is driven by the catalog schedule flag (PRD-04).
- [ ] Advertising compliance beyond this is clinic-owned (external tools).

## UI designs / screenshots

_Prototype screen: prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html._

- Prototype: Settings -> Public booking page (settings-booking.png) — toggle generic names + withhold S4 prices; the public page (public-booking.png) reflects it.
- Configuration-driven, not a linter.

![settings-booking — prototype screen](../screens/settings-booking.png)

## Suggested data model

- **PublicBookingConfig** — tenant_id, generic_names(bool), withhold_s4_prices(bool)
  - _Shared with PRD-02 ONLINE-BOOK; driven by Service.schedule (ADR-0014)._

## Technical notes (high level)

- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations** — Entities/columns + relationships; tenant_id + RLS.
- [ ] **Backend: domain logic, rules & API endpoint(s)** — Behaviour + invariants + the OpenAPI contract the UI/clients consume.
- [ ] **Enforce compliance gate + audit events** — Server-side (C9); blocked path explains why.
- [ ] **Web UI** — prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.
