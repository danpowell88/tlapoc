# Lead / prospect CRM

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/LEADS-CRM`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a front desk / owner, I want to track leads/prospects through to booking, so that enquiries don't get lost and convert better.
Most enquiries arrive asking the one thing a clinic can't answer publicly ('how much is Botox?'), via IG/FB DM, the website widget or phone. A 1:1 reply isn't public advertising, so a lead pipeline lets reception convert privately and stops enquiries getting lost. This is a thin CRM over the inbox: track prospects who haven't booked, move them to consult/won/lost, and convert to a client/booking preserving history. Phase 2 in scope, with real pipeline mechanics.  The prototype's Growth → Leads (CRM) screen tracks enquiries who haven't booked yet, over the inbox (ADR-0033).

## How it works

A Lead is a thin pipeline layer over the inbox (ADR-0033): name, contact, source (Instagram DM / Website widget / Facebook / Referral / Google), interest, stage (new / consult / won / lost), next_action, an optional linked conversation and converted_client_id, plus consent state. Stage transitions feed conversion read-models (KPIs: open leads, consults booked, conversion %, avg days). Converting a lead creates/links the client and preserves the enquiry history.
The advertising line is respected: 1:1 service replies are fine (not public advertising), but any outbound nudge to a lead gates on marketing consent (C23) — the board shows a consent dot per lead. Lead follow-ups surface in the unified Follow-ups queue ('Reply & book — Friday consult'). Advertising compliance (C9) for campaigns/social stays clinic-owned in external tools.

## Requirements

- To track leads/prospects through to booking.
- Deferred (Phase 2+): placeholder, design-only for now.
- Compliance: [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Leads are captured with source, stage and next action (over the inbox).
- [ ] A lead can convert to a client/booking, preserving the enquiry history.
- [ ] Lead follow-ups surface in the Follow-ups queue.
- [ ] Outbound marketing to leads respects Spam-Act consent (C23); 1:1 service replies are exempt.

## UI designs / screenshots

_Prototype screen: prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html._

- Prototype: Growth -> Leads (CRM) — KPI cards (Open leads, Consults booked, Conversion %, Avg days); kanban columns New enquiry / Consult booked / Converted / Lost; lead cards with source + a consent dot; 'Enquiries from the inbox become pipeline cards. Pricing questions stay private (1:1 replies aren't public advertising); outbound nudges need opt-in consent.'

![growth-leads — prototype screen](../screens/growth-leads.png)

## Suggested data model

- **Lead** — id, tenant_id, name, contact, source, interest, stage(new|consult|won|lost), next_action, conversation_id?, converted_client_id?, consent(bool)
  - _Projection over conversations (ADR-0033); convert preserves history; outbound nudges gate on consent (C23)._

## Technical notes (high level)

- Architecture decisions: [ADR-0033](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Lead model as a projection over conversations (migrations)**
  Model Lead (tenant_id + RLS (row-level security)) per ADR-0033: name, contact, source, interest, stage, next_action, optional conversation_id + converted_client_id, consent.
  - A thin pipeline layer over the inbox; stage transitions feed conversion read-models.
- [ ] **Leads API: pipeline stages, convert-to-client, consent-gated nudges, Follow-ups**
  Server-side.
  - CRUD leads; move stage (new/consult/won/lost); convert -> create/link a client + (optional) booking, preserving enquiry history.
  - Outbound nudges gate on marketing consent (C23); 1:1 service replies exempt.
  - Lead follow-ups raise Jobs into Follow-ups; conversion KPI (key performance indicator) read-model (open, consults, conversion %, avg days).
- [ ] **Leads (CRM) web UI: kanban + KPIs + convert**
  Angular per the screenshot.
  - Kanban columns (New enquiry / Consult booked / Converted / Lost) with lead cards (source + consent dot); KPI (key performance indicator) cards; convert-to-client/booking action; the 1:1-vs-public-advertising note.
  - Front-desk/owner gated; loading/empty/error states.
