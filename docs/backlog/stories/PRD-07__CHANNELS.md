# Notification channels (SMS / email / push)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/CHANNELS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend, integration

## Background

Communications, reminders & recall — The engine that keeps the book full and clients coming back at the right cadence: reminders, pre-/after-care sequences, and recall (~12-week toxin re-care) over SMS/email/push — with Spam Act consent/unsubscribe baked in.

As a developer, I want a notification abstraction over SMS, email and push with per-tenant templates, so that all messaging is consistent and provider-swappable.

An INotifier port over an AU SMS provider + email + app push, with per-tenant templates (REQ-NOTIF-1, ADR-0012).

## Requirements

- A notification abstraction over SMS, email and push with per-tenant templates.
- Traces to requirement(s): REQ-NOTIF-1.

## Acceptance Criteria

- [ ] INotifier supports SMS (AU provider), email and app push.
- [ ] Per-tenant message templates supported.
- [ ] Provider is swappable behind the port.
- [ ] All sends log to the client's comms history.

## UI designs / screenshots

prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html.

## Technical notes (high level)

Stack: .NET API (domain/services); Ports-and-adapters integration.
Architecture decisions: ADR-0012 (see docs/adr/decision-log.md).

## Other

Epic: PRD-07 — Communications, reminders & recall.
Source PRD: docs/prds/PRD-07-comms-reminders-recall.md.
Backlog key: PRD-07/CHANNELS.
Phase: 1 · Priority: P0 · Estimate: 5 pts.

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
