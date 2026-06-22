# Lead / prospect CRM — pipeline, stages & convert (core)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/LEADS-CRM`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a front desk / owner, I want to track leads/prospects through stages and convert them to a client/booking, so that enquiries don't get lost and convert better.
Most enquiries arrive asking the one thing a clinic can't answer publicly ('how much is Botox?'), via IG/FB DM, the website widget or phone. A 1:1 reply isn't public advertising, so a lead pipeline lets reception convert privately and stops enquiries getting lost. This is the minimal end-to-end core — a thin CRM over the inbox: track prospects who haven't booked, move them through stages, and convert to a client/booking preserving history. The consent-gated outbound nudges and the conversion KPIs / Follow-ups-queue projection are each added as their own follow-ups. Phase 2 in scope, with real pipeline mechanics (ADR-0033).

## How it works

A Lead is a thin pipeline layer over the inbox (ADR-0033): name, contact, source (Instagram DM / Website widget / Facebook / Referral / Google), interest, stage (new / consult / won / lost), next_action, an optional linked conversation and converted_client_id, plus consent state. Stage transitions feed conversion read-models (KPIs: open leads, consults booked, conversion %, avg days). Converting a lead creates/links the client and preserves the enquiry history.
The advertising line is respected: 1:1 service replies are fine (not public advertising), but any outbound nudge to a lead gates on marketing consent (C23) — the board shows a consent dot per lead. Lead follow-ups surface in the unified Follow-ups queue ('Reply & book — Friday consult'). Advertising compliance (C9) for campaigns/social stays clinic-owned in external tools.

## Requirements

- To track leads/prospects through stages and convert them to a client/booking.
- Deferred (Phase 2+): placeholder, design-only for now.
- Compliance: [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Leads are captured with source, interest, stage (new / consult / won / lost) and next action, as a projection over the inbox (ADR-0033).
- [ ] A lead can be moved between stages; an enquiry from the inbox becomes a pipeline card.
- [ ] A lead can convert to a client/booking, preserving the enquiry history (converted_client_id stamped, stage → won).
- [ ] Outbound nudges (consent-gated) and conversion KPIs / Follow-ups projection are added by follow-ups.

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
  Behaviour: a Lead is a thin pipeline layer over the inbox (ADR-0033) — name, contact, source (Instagram DM / Website widget / Facebook / Referral / Google), interest, stage (new / consult / won / lost), next_action, optional linked conversation, plus consent state. Staff move a lead between stages as it progresses. Requirements: tenant-scoped with RLS (row-level security); an enquiry from the inbox becomes a pipeline card. (Conversion read-models ship with the KPI follow-up.)
- [ ] **Convert lead -> client / booking (preserve history)**
  Behaviour: converting a lead creates or links a client and (optionally) a booking, preserving the original enquiry history. Requirements: the linked conversation/history is retained on the resulting client; converted_client_id is stamped; conversion moves the lead to 'won'.
- [ ] **Leads (CRM) web UI (kanban + convert)**
  Behaviour: the Growth -> Leads screen shows kanban columns (New enquiry / Consult booked / Converted / Lost) with lead cards (source), a convert-to-client/booking action, and the '1:1 replies aren't public advertising' note. Requirements: front-desk/owner gated; loading/empty/error states; cards reflect stage moves live. (KPI cards and the per-lead consent dot ship with their follow-ups.)
