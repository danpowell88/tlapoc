# Notification channels (SMS / email / push)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/CHANNELS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend, integration

## Background

As a developer, I want a notification abstraction over SMS, email and push with per-tenant templates, so that all messaging is consistent and provider-swappable.
An INotifier port over an AU SMS provider + email + app push, with per-tenant templates (REQ-NOTIF-1, ADR-0012).

## How it works

An INotifier abstraction over an AU SMS provider + email + app push, with per-tenant templates (ADR-0012). All sends log to the client's comms history; the provider is swappable behind the port.
The shared delivery layer every reminder/aftercare/recall/marketing message goes through.

## Requirements

- A notification abstraction over SMS, email and push with per-tenant templates.

## Acceptance Criteria

- [ ] INotifier supports SMS (AU provider), email and app push.
- [ ] Per-tenant message templates supported.
- [ ] Provider is swappable behind the port.
- [ ] All sends log to the client's comms history.

## UI designs / screenshots

- No dedicated screen — surfaces through templates + the comms history on the Client 360; admin sets the SMS/email/push providers in Settings.
- Per-tenant message templates.

## Suggested data model

- **MessageTemplate** — id, tenant_id, channel(sms|email|push), key, body, variables[]
  - _Per-tenant; rendered per send._
- **NotificationLog** — id, tenant_id, client_id, channel, template_key, status, sent_at
  - _Comms history; swappable provider behind INotifier._

## Technical notes (high level)

- Architecture decisions: [ADR-0012](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Data model & migrations**
  Model + migrate (EF Core; every table carries tenant_id with an RLS policy):
  - MessageTemplate — id, tenant_id, channel(sms|email|push), key, body, variables[] (Per-tenant; rendered per send.)
  - NotificationLog — id, tenant_id, client_id, channel, template_key, status, sent_at (Comms history; swappable provider behind INotifier.)
  - Add the FKs/relationships above; index the columns this story filters or looks up on; make records append-only/immutable where the story requires it.
- [ ] **Backend: domain logic, rules & API endpoint(s)**
  Domain logic + the API the web/Flutter clients call; enforce every rule server-side (never trust the UI):
  - Endpoints: the commands + queries for the entities above and each action in the acceptance criteria.
  - Rule: INotifier supports SMS (AU provider), email and app push.
  - Rule: Per-tenant message templates supported.
  - Rule: Provider is swappable behind the port.
  - Emit domain events for read-models / notifications / follow-up jobs where relevant.
  - Publish the OpenAPI contract so the generated clients update.
- [ ] **Integration adapter, sync & config**
  Implement the provider behind its swappable port:
  - Connection/config (OAuth tokens stored encrypted) + the field mapping this story needs.
  - Trigger on the relevant event; idempotent sync with retries, back-off and a visible reconciliation/status.
  - Handle partial failures + replays; surface errors to the user.
  - Residency: AU-resident or APP-8-assessed + consented before any PII leaves (C21).
