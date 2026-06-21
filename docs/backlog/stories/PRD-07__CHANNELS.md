# Notification channels (SMS / email / push)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/CHANNELS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend, integration

## Background

As a developer, I want a notification abstraction over SMS, email and push with per-tenant templates, so that all messaging is consistent and provider-swappable.
An INotifier port over an AU SMS provider + email + app push, with per-tenant templates (REQ-NOTIF-1, ADR-0012).

## Requirements

- A notification abstraction over SMS, email and push with per-tenant templates.

## Acceptance Criteria

- [ ] INotifier supports SMS (AU provider), email and app push.
- [ ] Per-tenant message templates supported.
- [ ] Provider is swappable behind the port.
- [ ] All sends log to the client's comms history.

## Technical notes (high level)

- Stack: .NET API (domain/services); Ports-and-adapters integration
- Architecture decisions: [ADR-0012](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Domain logic & business rules** — Core behaviour + invariants.
- [ ] **API endpoint(s) + OpenAPI contract** — Wire request/response; regenerate clients.
- [ ] **Integration adapter + config** — Behind the port; AU / APP-8 posture.
- [ ] **Tests (unit + integration)** — Cover acceptance criteria, incl. any gate/invariant.
