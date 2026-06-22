# Reviews & reputation (request, acknowledge, flag, auto-follow-up)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REVIEWS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a owner, I want to request reviews and manage replies, with negative ones auto-raising follow-ups, so that reputation is managed and problems are caught early.
The prototype's Growth → Reviews screen (scanReviews/reviewReply/reviewFlag/reviewAck) requests reviews, replies/acknowledges, and auto-raises follow-up jobs for negative reviews (≤3★) — with a staff caution against resharing an S4-endorsing review as a prohibited testimonial.

## How it works

Post-visit review requests go to ALL eligible (consented) clients — no sentiment pre-screen (ACL). Staff can reply to, acknowledge, or flag any review. Negative reviews (≤3★) and complaint-keyword matches (unhappy/refund/rude/pain/no one called...) are auto-detected and raised as review Jobs into the Follow-ups queue (Lead Nurse for unhappy/clinical, Reception otherwise), so a bad review becomes an action, not just a notification.
The platform has no feature that reposts or embeds a review as marketing, so an S4-endorsing review can't be weaponised into a prohibited testimonial; where a review names an S4 result, staff see a caution: 'Names an S4 result — replying is fine, but don't reshare it publicly (would be a prohibited testimonial)' (C9/ADR-0032). KPIs (avg rating, review count, response rate, needs-follow-up) sit on top. Email campaigns/social posting stay in the clinic's external tools.

## Requirements

- To request reviews and manage replies, with negative ones auto-raising follow-ups.
- Deferred (Phase 2+): placeholder, design-only for now.
- Compliance: [C9](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria), [C23](https://github.com/danpowell88/tlapoc/blob/main/docs/02-requirements.md#6-compliance-requirements-auqld--restated-as-acceptance-criteria)

## Acceptance Criteria

- [ ] Review requests are sent to all eligible consented clients (no sentiment gating — ACL); reply/acknowledge supported.
- [ ] Negative reviews (≤3★) and complaint-keyword matches auto-raise review jobs into the Follow-ups queue (Lead Nurse for clinical, Reception otherwise).
- [ ] A caution warns against resharing an S4-endorsing review as a prohibited testimonial (C9); the platform has no repost-as-marketing feature.
- [ ] No sentiment-gating of who is asked (request-all).

## UI designs / screenshots

_Prototype screen: prototype.html — Comms & growth (Inbox/Automations/Campaigns), Growth (Leads/Reviews), Follow-ups, Settings → Public booking page; booking-widget.html._

- Prototype: Growth -> Reviews — KPI cards (Avg rating 4.4★, Reviews 48, Response rate 89%, Needs follow-up); 'Requests go to every eligible client (no sentiment gating — ACCC). Reply to any review and acknowledge it; negative reviews & complaints are auto-flagged for follow-up. Never repost one endorsing an S4 result.'; 'Auto-detect follow-ups' (scanReviews); per-review Reply / Acknowledge / Flag follow-up (reviewReply/reviewAck/reviewFlag); 'needs follow-up' badge on ≤3★; S4 testimonial caution banner; footer noting campaigns/social live in external tools.

![growth-reviews — prototype screen](../screens/growth-reviews.png)

## Suggested data model

- **Review** — id, tenant_id, client_id?, source(google|facebook), rating, body, names_s4(bool), status(new|acknowledged|replied|flagged), at
  - _<=3 stars or complaint-keyword -> review Job (Follow-ups); testimonial caution when names_s4 (C9/ADR-0032)._

## Technical notes (high level)

- Architecture decisions: [ADR-0032](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Review model + complaint-keyword auto-detect (migrations)**
  Model Review (tenant_id + RLS): source, rating, body, names_s4, status.
  - Request-all: review requests gate only on consent (C23), never on sentiment (ACL).
  - Auto-detect: rating <=3 OR a complaint-keyword match flags needs-follow-up.
  - No repost-as-marketing field/feature exists (prevents prohibited testimonials).
- [ ] **Reviews API: request, reply, acknowledge, flag -> Job; testimonial caution**
  Server-side.
  - Send review requests to all eligible consented clients (no gating); reply/acknowledge endpoints; flag -> create a review Job (Follow-ups) assigned Lead Nurse (clinical/unhappy) or Reception.
  - Auto-detect: scan reviews, raise review Jobs for ≤3★/complaint matches idempotently.
  - When a review names an S4 result, surface the caution (don't reshare — prohibited testimonial, C9/ADR-0032); the platform offers no repost action. KPI read-model (avg, count, response rate, needs-follow-up).
