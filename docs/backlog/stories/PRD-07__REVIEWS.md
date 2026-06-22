# Reviews & reputation (request, acknowledge, flag, auto-follow-up)

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REVIEWS`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** web
>
> **Depends on:** `PRD-07/FOLLOWUPS`

## Background

As a owner, I want to request reviews and manage replies, with negative ones auto-raising follow-ups, so that reputation is managed and problems are caught early.
Reputation matters, but in Australia a review feature is a compliance trap: review gating (only asking happy clients) is misleading conduct under the ACL, and reposting a review that endorses an S4 result becomes a prohibited testimonial (National Law s133, TGA Code). So this feature is built request-all (no sentiment gating), reply-yes, repost-S4-no, and it closes the loop by auto-raising follow-up jobs for negative reviews. (Phase 2 in scope, but with real mechanics — request, acknowledge, reply, flag, auto-detect.)  The prototype's Growth → Reviews screen (scanReviews/reviewReply/reviewFlag/reviewAck) requests reviews, replies/acknowledges, and auto-raises follow-up jobs for negative reviews (≤3★) — with a staff caution against resharing an S4-endorsing review as a prohibited testimonial.

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

- [ ] **Request-all review requests (no sentiment gating - ACL)**
  Behaviour: post-visit review requests go to ALL eligible (consented) clients — there is NO sentiment pre-screen ('Requests go to every eligible client (no sentiment gating — ACCC)'). Requirements: gate only on marketing consent (C23), never on predicted happiness; review gating (asking only happy clients) is misleading conduct under the ACL (Australian Consumer Law) and must not be implementable. Model Review (source, rating, body, names_s4, status) tenant-scoped with RLS (row-level security).
- [ ] **Reply / acknowledge / flag a review**
  Behaviour: staff can Reply to, Acknowledge, or Flag any review (reviewReply / reviewAck / reviewFlag). Flagging a review raises a review Job into the Follow-ups queue (PRD-07/FOLLOWUPS) assigned Lead Nurse for clinical/unhappy reviews, Reception otherwise. Requirements: reply/acknowledge update the review status; flag -> Job is idempotent; actions audited.
- [ ] **Auto-detect negative reviews / complaint keywords -> Job**
  Behaviour: negative reviews (≤3★) and complaint-keyword matches (unhappy/refund/rude/pain/no one called...) are auto-detected and shown with a 'needs follow-up' badge, raising review Jobs into Follow-ups so a bad review becomes an action, not just a notification; an 'Auto-detect follow-ups' action sweeps on demand. Requirements: rating ≤3 OR keyword match flags needs-follow-up; raising Jobs is idempotent; routing follows the same Lead-Nurse/Reception split.
- [ ] **S4 testimonial caution (C9) - no repost-as-marketing feature**
  Behaviour: where a review names an S4 (Schedule 4 prescription-only medicine) result, staff see a caution: 'Names an S4 result — replying is fine, but don't reshare it publicly (would be a prohibited testimonial)'. Requirements: the platform offers NO feature to repost/embed a review as marketing, so an S4-endorsing review can't be weaponised into a prohibited testimonial (National Law s133 / TGA Code, C9/ADR-0032); names_s4 drives the caution; replying is always allowed.
- [ ] **Reviews screen UI + reputation KPIs**
  Behaviour: the Growth -> Reviews screen shows KPI cards (Avg rating, Reviews, Response rate, Needs follow-up), the request-all/no-gating explainer, per-review Reply/Acknowledge/Flag actions, the 'needs follow-up' badge on ≤3★, the S4 testimonial caution banner, and a footer noting campaigns/social live in external tools (Mailchimp, Meta Business Suite). Requirements: KPI read-model (avg, count, response rate, needs-follow-up); owner/staff gated; loading/empty/error states.
