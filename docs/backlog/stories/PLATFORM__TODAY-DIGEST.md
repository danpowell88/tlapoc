# Today: Follow-ups preview + needs-attention digest

> **Epic:** [PLATFORM — Platform shell, navigation & cross-cutting UX](../epics/PLATFORM.md)  ·  **Key:** `PLATFORM/TODAY-DIGEST`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PLATFORM/TODAY`

## Background

As a staff member, I want a Follow-ups preview and a needs-attention exceptions strip on Today, so that I can see and act on outstanding work without leaving the landing page.
Plainly: the Today panel that previews the clinic's job queue and — for the owner — the 'needs attention' exceptions strip (overdue recalls, unbilled visits, credential expiries, failed payments), each with one click through to fix it. Where it fits: a follow-up to the role-tailored Today dashboard (PLATFORM/TODAY) that adds the worklist preview beside the schedule. It reads the Jobs queue (ADR-0023) and mirrors the owner exceptions digest (PRD-08/ATTENTION-DIGEST); money-bearing items are gated behind the owner-only financial (.fin) capability.

## How it works

Beside the schedule, Today gains a Follow-ups preview that previews the unified Jobs queue (ADR-0023) — the next outstanding tasks — with an 'Open queue →' link into the full worklist, so the landing page shows what's waiting without making someone navigate to find it.
For the owner, a needs-attention exceptions strip surfaces the cross-platform exceptions that need a decision: overdue recalls, unbilled visits, credential expiries (REG-WATCH), failed payments. These items mirror the owner exceptions digest (PRD-08/ATTENTION-DIGEST) so Today and the Governance Overview never disagree, and each deep-links to its source module (e.g. a failed-payment item jumps to Members & billing) so the strip is a launchpad, not a dead read screen.
Items are concern-tailored — reception sees front-desk follow-ups, the owner sees the business digest — and money-bearing items (failed payments, revenue) are gated behind the owner-only financial (.fin) capability and genericised or hidden for non-owner roles.

## Requirements

- A Follow-ups preview and a needs-attention exceptions strip on Today.

## Acceptance Criteria

- [ ] Today shows a Follow-ups preview of the Jobs queue with an 'Open queue →' link.
- [ ] For the owner, a needs-attention strip surfaces exceptions (overdue recalls, unbilled visits, credential expiries from REG-WATCH, failed payments).
- [ ] Each item deep-links to its source module for action.
- [ ] Items are concern-tailored; money-bearing items (failed payments) are .fin-gated/genericised for non-owner roles.

## UI designs / screenshots

- Prototype: Today (dashboard.png) — the Follow-ups preview panel and (for the owner) the 'Needs attention' exceptions strip; each item has a Fix/Open action that deep-links (e.g. failed membership payment → goSub('memberships','members')).
- Concern-tailored per active role; money-bearing items (failed payments) hidden/genericised for non-owner roles.

![dashboard — prototype screen](../screens/dashboard.png)

## Suggested data model

- **(read) TodayBoard (extends PLATFORM/TODAY)** — + Follow-ups preview from the Jobs queue (ADR-0023), + needs-attention items mirroring PRD-08/ATTENTION-DIGEST
  - _Reads existing signals (Jobs queue + ATTENTION-DIGEST); no new write model. Each item carries a source deep-link and an owner_financial flag for gating._

## Other

- Source PRD: [README.md](https://github.com/danpowell88/tlapoc/blob/main/docs/ux/README.md)

## Tasks (dev pickup)

- [ ] **Follow-ups preview panel (Jobs queue) on Today**
  Behaviour: render a Follow-ups preview previewing the unified Jobs queue (ADR-0023) — the next outstanding tasks — with an 'Open queue →' link to the full worklist. Requirements: reads the Jobs queue (no new write model); concern-tailored so reception sees front-desk items; loading/empty states; keep it actionable — every item has a next step.
- [ ] **Owner needs-attention exceptions strip + deep links**
  Behaviour: render the owner needs-attention strip (overdue recalls, unbilled visits, credential expiries from REG-WATCH, failed payments) with per-item Fix/Open actions that deep-link to the source module. Requirements: the items mirror PRD-08/ATTENTION-DIGEST so Today and Governance Overview agree; money-bearing items (failed payments) are .fin-gated/genericised for non-owner roles; concern-tailored per active role.
