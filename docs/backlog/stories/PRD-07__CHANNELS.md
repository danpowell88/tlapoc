# Notification channels (SMS / email / push)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/CHANNELS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P0  ·  **Estimate:** 5 pts  ·  **Area:** backend, integration

## Background

As a developer, I want a notification abstraction over SMS, email and push with per-tenant templates, so that all messaging is consistent and provider-swappable.
An INotifier port over an AU SMS provider + email + app push, with per-tenant templates (REQ-NOTIF-1, ADR-0012).

## How it works

INotifier exposes send(channel, recipient, templateKey, variables) across three channels: SMS via an AU provider (MessageMedia/ClickSend/Twilio — chosen in the spike), transactional email, and app push (Flutter). Each tenant owns its MessageTemplate set: a body with named variables ({{first_name}}, {{appt_time}}, {{rebook_link}}), rendered per send. Adapters sit behind the port (ADR-0012), so swapping an SMS provider is one new adapter, not a checkout-of changes across features.
Every send writes a NotificationLog row (channel, template_key, status, sent_at) that surfaces on the Client 360 comms history — including delivery/failure callbacks from the provider. The port itself is channel-and-provider agnostic; the consent gate (marketing vs transactional) and the suppression list live in MARKETING-CONSENT and are applied by the callers, not baked into the transport.

## Requirements

- A notification abstraction over SMS, email and push with per-tenant templates.

## Acceptance Criteria

- [ ] INotifier supports SMS (AU provider), email and app push behind one port.
- [ ] Per-tenant MessageTemplates render with named variables per send.
- [ ] The provider is swappable behind the port (ADR-0012) — one new adapter, no caller changes.
- [ ] Every send (and its delivery/failure callback) logs to the client's comms history.

## UI designs / screenshots

- No dedicated screen — surfaces through templates and the comms history on the Client 360; admin sets the SMS/email/push providers in Settings -> Integrations.
- Per-tenant message templates with named variables.

## Suggested data model

- **MessageTemplate** — id, tenant_id, channel(sms|email|push), key, body, variables[]
  - _Per-tenant; rendered per send._
- **NotificationLog** — id, tenant_id, client_id, channel, template_key, status(queued|sent|delivered|failed), provider_ref, sent_at
  - _Client-360 comms history; swappable provider behind INotifier (ADR-0012)._

## Technical notes (high level)

- Architecture decisions: [ADR-0012](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **INotifier port + MessageTemplate/NotificationLog model (migrations)**
  Define the INotifier port and model MessageTemplate + NotificationLog (tenant_id + RLS).
  - Port: send(channel, recipient, templateKey, variables) returning a queued NotificationLog with a provider_ref.
  - MessageTemplate per tenant per channel with named variables; render step substitutes variables safely.
  - NotificationLog status lifecycle queued -> sent -> delivered|failed, updated by provider callbacks; joined to the client for the comms history.
  - The port is consent-agnostic; callers apply the consent/suppression gate (MARKETING-CONSENT).
- [ ] **Notification API: render, send, comms-history query**
  Server-side.
  - Endpoints: CRUD per-tenant templates; send via INotifier; query a client's comms history (NotificationLog).
  - Render templates with variables; queue + dispatch through the channel adapter; record the log.
  - Email/SMS/push share the same send contract.
- [ ] **Channel adapters (AU SMS / email / push) + delivery callbacks**
  Adapters behind the port (ADR-0012).
  - AU SMS adapter (provider chosen in spike) with sender-ID; email adapter; app-push adapter (Flutter tokens).
  - Provider credentials stored encrypted in Settings -> Integrations config.
  - Handle inbound delivery/failure webhooks/callbacks and update NotificationLog idempotently; retries with back-off on transient failures.
