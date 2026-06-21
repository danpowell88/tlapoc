# Public booking page: generic names, S4 prices withheld

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/BOOKING-PAGE`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P1  ·  **Estimate:** 3 pts  ·  **Area:** web
>
> **Depends on:** `PRD-02/ONLINE-BOOK`

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a owner, I want my public booking page to use generic service names and withhold S4 prices automatically, so that we don't reference S4 in public advertising.

The public booking page uses generic service names and withholds S4 prices by configuration (catalog schedule flag), with no advertising linter (REQ-NOTIF-12, C9).

## Requirements

- My public booking page to use generic service names and withhold S4 prices automatically.
- Traces to requirement(s): REQ-NOTIF-12.
- Must satisfy compliance obligation(s): C9.

## Acceptance Criteria

- [ ] The booking page renders generic service names and withholds S4 prices for any S4-flagged service (configuration-driven).
- [ ] No brands, 'anti-wrinkle injections', prices or #botox appear for S4 services.
- [ ] Configuration is driven by the catalog schedule flag (PRD-04).
- [ ] Advertising compliance beyond this is clinic-owned (external tools).

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: Angular web (admin/front-desk/public).
Architecture decisions: ADR-0014 (see docs/adr/decision-log.md).
Depends on: PRD-02/ONLINE-BOOK.

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/BOOKING-PAGE.
Phase: 1 · Priority: P1 · Estimate: 3 pts.
Compliance criteria: C9.

## Tasks (dev pickup)

- [ ] **Enforce compliance gate + audit events** — Server-side (C9); blocked path explains why.
- [ ] **Web UI** — prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
