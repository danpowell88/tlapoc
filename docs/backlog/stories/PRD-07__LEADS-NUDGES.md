# Leads: consent-gated outbound nudges (1:1 replies exempt, C23)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/LEADS-NUDGES`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/LEADS-CRM`

## Background

As a front desk / owner, I want outbound nudges to leads to respect marketing consent, so that we follow up compliantly while 1:1 replies stay free.
Plainly: a 1:1 reply to a lead is fine (not public advertising), but any proactive outbound nudge to a lead must respect marketing consent — so the board shows a consent dot per lead and nudges route through the consent + suppression gate. Where it fits: a follow-up to the leads core (PRD-07/LEADS-CRM), which tracks and converts leads; this adds the compliant outbound-nudge path. Outbound nudges route through MARKETING-CONSENT (consent + suppression, C23); 1:1 service replies are exempt; advertising compliance (C9) for campaigns/social stays clinic-owned in external tools.

## How it works

A 1:1 service reply to a lead is fine (not public advertising), but any proactive outbound nudge to a lead gates on marketing consent — the board shows a consent dot per lead. This extends the leads core (PRD-07/LEADS-CRM).
Outbound nudges route through MARKETING-CONSENT (consent + suppression, C23); 1:1 replies are exempt; advertising compliance (C9) for campaigns/social stays clinic-owned in external tools.

## Requirements

- Outbound nudges to leads to respect marketing consent.

## Acceptance Criteria

- [ ] A 1:1 service reply to a lead is exempt (not public advertising); any proactive outbound nudge gates on marketing consent.
- [ ] Outbound nudges route through MARKETING-CONSENT (consent + suppression, C23).
- [ ] The board shows a consent dot per lead.
- [ ] Advertising compliance (C9) for campaigns/social stays clinic-owned in external tools.

## UI designs / screenshots

- Prototype: Growth -> Leads (CRM) — a consent dot per lead card; 'outbound nudges need opt-in consent' note; outbound nudge action gated on consent.

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **Lead (extends PRD-07/LEADS-CRM)** — consent(bool) drives the nudge gate + consent dot
  - _No new entity; nudges route via PRD-07/MARKETING-CONSENT (C23); 1:1 replies exempt._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Consent-gated outbound nudges + per-lead consent dot (C23)**
  Behaviour: proactive outbound nudges to a lead gate on marketing consent (consent + suppression via PRD-07/MARKETING-CONSENT); 1:1 replies are exempt; the board shows a consent dot per lead. Requirements: never nudge a non-consented/suppressed lead (C23); advertising compliance (C9) for campaigns/social stays clinic-owned in external tools.
