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

- [ ] **Lead pipeline model + stages (projection over conversations)**
  Behaviour: a Lead is a thin pipeline layer over the inbox (ADR-0033) — name, contact, source (Instagram DM / Website widget / Facebook / Referral / Google), interest, stage (new / consult / won / lost), next_action, optional linked conversation, plus consent state. Staff move a lead between stages as it progresses. Requirements: tenant-scoped with RLS (row-level security); stage transitions feed the conversion read-models; an enquiry from the inbox becomes a pipeline card.
- [ ] **Convert lead -> client / booking (preserve history)**
  Behaviour: converting a lead creates or links a client and (optionally) a booking, preserving the original enquiry history. Requirements: the linked conversation/history is retained on the resulting client; converted_client_id is stamped; conversion moves the lead to 'won'.
- [ ] **Consent-gated outbound nudges (1:1 replies exempt, C23)**
  Behaviour: a 1:1 service reply to a lead is fine (not public advertising), but any proactive outbound nudge to a lead gates on marketing consent — the board shows a consent dot per lead. Requirements: outbound nudges route through MARKETING-CONSENT (consent + suppression, C23); 1:1 replies are exempt; advertising compliance (C9) for campaigns/social stays clinic-owned in external tools.
- [ ] **Lead follow-ups -> Follow-ups queue + conversion KPIs**
  Behaviour: lead follow-ups surface in the unified Follow-ups queue (e.g. 'Reply & book — Friday consult'); a conversion KPI read-model powers the cards (Open leads, Consults booked, Conversion %, Avg days). Requirements: lead Jobs project into PRD-07/FOLLOWUPS; KPI (key performance indicator) figures computed server-side from stage transitions.
- [ ] **Leads (CRM) web UI (kanban + KPIs + convert)**
  Behaviour: the Growth -> Leads screen shows KPI cards and kanban columns (New enquiry / Consult booked / Converted / Lost) with lead cards (source + consent dot), a convert-to-client/booking action, and the '1:1 replies aren't public advertising; outbound nudges need opt-in consent' note. Requirements: front-desk/owner gated; loading/empty/error states; cards reflect stage moves live.
