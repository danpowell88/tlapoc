# Reviews: screen UI + reputation KPIs

> **Epic:** [PRD-07 — Communications, reminders & recall](../epics/PRD-07.md)  ·  **Key:** `PRD-07/REVIEWS-SCREEN-KPI`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-07/REVIEWS`

## Background

As a owner, I want a Reviews screen with reputation KPIs and per-review actions, so that I can manage reputation at a glance.
Plainly: the Growth → Reviews screen — KPI cards (avg rating, review count, response rate, needs-follow-up), the request-all explainer, per-review actions and the S4 caution banner. Where it fits: a follow-up to the reviews core (PRD-07/REVIEWS), which holds the request/reply/flag mechanics and the S4 caution, and surfaces the auto-detect badge (PRD-07/REVIEWS-AUTODETECT); this is the management screen and reputation read-model on top. Campaigns/social posting stay in the clinic's external tools.

## How it works

The Growth -> Reviews screen shows KPI cards (Avg rating, Reviews, Response rate, Needs follow-up), the request-all/no-gating explainer, per-review Reply/Acknowledge/Flag actions (from PRD-07/REVIEWS), the 'needs follow-up' badge on ≤3★ (from PRD-07/REVIEWS-AUTODETECT), the S4 testimonial caution banner, and a footer noting campaigns/social live in external tools (Mailchimp, Meta Business Suite).
A KPI read-model computes avg rating, review count, response rate and needs-follow-up. Owner/staff gated; loading/empty/error states handled. This is the presentation/read-model layer over the reviews core (PRD-07/REVIEWS).

## Requirements

- A Reviews screen with reputation KPIs and per-review actions.

## Acceptance Criteria

- [ ] The Growth -> Reviews screen shows KPI cards (Avg rating, Reviews, Response rate, Needs follow-up) and the request-all/no-gating explainer.
- [ ] Per-review Reply/Acknowledge/Flag actions and the 'needs follow-up' badge on ≤3★ are shown, plus the S4 testimonial caution banner.
- [ ] A footer notes campaigns/social live in external tools (Mailchimp, Meta Business Suite).
- [ ] KPI read-model (avg, count, response rate, needs-follow-up); owner/staff gated; loading/empty/error states.

## UI designs / screenshots

- Prototype: Growth -> Reviews — KPI cards (Avg rating 4.4★, Reviews 48, Response rate 89%, Needs follow-up); 'Requests go to every eligible client (no sentiment gating — ACCC). Reply to any review and acknowledge it; negative reviews & complaints are auto-flagged for follow-up. Never repost one endorsing an S4 result.'; per-review Reply / Acknowledge / Flag; 'needs follow-up' badge on ≤3★; S4 testimonial caution banner; footer noting campaigns/social live in external tools.

![marketing-inbox — prototype screen](../screens/marketing-inbox.png)

## Suggested data model

- **(KPI read-model over PRD-07/REVIEWS)** — avg rating, review count, response rate, needs-follow-up count
  - _No new entity; read-model over the core Review; owner/staff gated._

## Other

- Source PRD: [PRD-07-comms-reminders-recall.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-07-comms-reminders-recall.md)

## Tasks (dev pickup)

- [ ] **Reviews screen UI + reputation KPIs**
  Behaviour: the Growth -> Reviews screen shows KPI cards (Avg rating, Reviews, Response rate, Needs follow-up), the request-all/no-gating explainer, per-review Reply/Acknowledge/Flag, the 'needs follow-up' badge on ≤3★, the S4 (Schedule 4 prescription-only medicine) testimonial caution banner, and a footer noting campaigns/social live in external tools. Requirements: KPI read-model (avg, count, response rate, needs-follow-up); owner/staff gated; loading/empty/error states.
