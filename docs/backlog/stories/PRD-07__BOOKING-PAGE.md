# Public booking page: generic names, S4 prices withheld

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/BOOKING-PAGE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

As a owner, I want my public booking page to use generic service names and withhold S4 prices automatically, so that we don't reference S4 in public advertising.
The public booking page uses generic service names and withholds S4 prices by configuration (catalog schedule flag), with no advertising linter (REQ-NOTIF-12, C9).

## How it works

A PublicBookingConfig (shared with PRD-02 ONLINE-BOOK) holds two toggles: generic_names and withhold_s4_prices. When on, any service flagged S4 in the catalog (PRD-04/ADR-0014) renders with a generic name and no price on the public page — e.g. 'Anti-wrinkle treatment — Pricing discussed at consult', while non-S4 services show normally ('Skin treatment — from $180', 'Cosmetic consultation — $50 · 30 min'). No brands, 'anti-wrinkle injections', prices or hashtags appear for S4 services.
This is configuration-driven, not a linter: the schedule flag is the single source of truth, the same flag that governs rewards eligibility (ADR-0014). The settings screen states the policy plainly: 'Service names stay generic, S4 prices withheld and no S4 imagery — set by clinic policy when configuring the page & its SEO metadata.' Advertising compliance beyond this public page (campaigns, social) is clinic-owned (Mailchimp, Meta Business Suite).

## Requirements

- My public booking page to use generic service names and withhold S4 prices automatically.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] The booking page renders generic service names and withholds S4 prices for any S4-flagged service (configuration-driven).
- [ ] No brands, 'anti-wrinkle injections', prices or #botox appear for S4 services (e.g. 'Pricing discussed at consult').
- [ ] Configuration is driven by the catalog schedule flag (PRD-04/ADR-0014), shared with PRD-02 ONLINE-BOOK.
- [ ] There is no advertising linter; compliance beyond this page is clinic-owned (external tools).

## UI designs / screenshots

_Prototype screen: prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html._

- Prototype: Settings -> Public booking page — 'Public booking widget · Service names stay generic, S4 prices withheld and no S4 imagery — set by clinic policy when configuring the page & its SEO metadata'; a live Preview (e.g. 'Cosmetic consultation $50 · 30 min', 'Anti-wrinkle treatment — Pricing discussed at consult', 'Skin treatment from $180', 'Book a consultation').
- Configuration-driven, not a linter; the public page reflects it (public-booking).

![settings-booking — prototype screen](../screens/settings-booking.png)

## Suggested data model

- **PublicBookingConfig** — tenant_id, generic_names(bool), withhold_s4_prices(bool), no_s4_imagery(bool)
  - _Shared with PRD-02 ONLINE-BOOK; driven by Service.schedule (ADR-0014). No linter._

## Technical notes (high level)

- Architecture decisions: [ADR-0014](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **PublicBookingConfig model (shared with PRD-02) (migrations)**
  Model PublicBookingConfig (tenant-scoped): generic_names, withhold_s4_prices, no_s4_imagery.
  - Shared with PRD-02 ONLINE-BOOK; the catalog Service.schedule flag (PRD-04/ADR-0014) is the source of truth for which services are affected.
- [ ] **Public booking-page render: schedule-driven generic names + withheld prices**
  Server-side render of the public booking page/feed.
  - For each service, if S4-flagged AND config on: emit a generic name, suppress price ('Pricing discussed at consult'), suppress S4 imagery; non-S4 services render name + price normally.
  - Applies to the page and its SEO metadata. Configuration-driven, not a linter — driven entirely by the schedule flag + the toggles.
- [ ] **Enforce no-public-S4 as a server-side invariant + audit**
  C9 invariant on the public surface the app owns.
  - The public render must never expose an S4 service's brand/clinical name/price/imagery when the policy is on; assert this server-side so a UI/client change can't leak it.
  - Audit config changes (ADR-0010). (No advertising linter — external advertising is clinic-owned, ADR-0034.)
- [ ] **Settings -> Public booking page web UI + live preview**
  Angular per the screenshot.
  - Public-booking-widget panel with the policy toggles (generic names / withhold S4 prices / no S4 imagery) and SEO metadata fields.
  - Live Preview showing how S4 vs non-S4 services render (price withheld for S4).
  - Owner/admin gated; loading/empty/error states.
