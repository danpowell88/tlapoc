# Client 360: Overview tab (recent activity & at-a-glance)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-360-OVERVIEW`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-360`

## Background

As a staff member, I want an Overview tab with recent activity and an at-a-glance panel on the client profile, so that I get the gist of a client the moment I open their record.
Plainly: the default tab of the Client 360 profile — recent activity and an at-a-glance panel (visits count, last seen, referred-by). Where it fits: a follow-up to the Client 360 basic aggregation & header (PRD-02/CLIENT-360) that adds the default tab on top of the header. It reads via the aggregation API and honours owner-only financial gating (lifetime spend is .fin-gated). It sits in Reception (PRD-02).

## How it works

The basic story provides the aggregation API and the header; this follow-up adds the default Overview tab. It shows recent activity (treatments, rewards, skin) and an at-a-glance panel summarising the client — visits count, last seen, referred-by.
Money figures in the at-a-glance, such as lifetime spend, are gated behind the .fin capability (owner-only) and stripped for non-owner roles, consistent with the platform's financial gating.
All data is read via the Client 360 aggregation API (this story is presentation, not a new source of truth), and each item deep-links into the relevant underlying record.

## Requirements

- An Overview tab with recent activity and an at-a-glance panel on the client profile.

## Acceptance Criteria

- [ ] The Overview tab shows recent activity (treatments, rewards, skin) and an at-a-glance panel (visits count, last seen, referred-by).
- [ ] Lifetime spend / money figures in the at-a-glance are gated behind the .fin capability (owner-only).
- [ ] It reads via the aggregation API and deep-links into the relevant record.

## UI designs / screenshots

- Prototype: Client 360 (client-360.png) — Overview tab: recent activity + at-a-glance (visits, last seen, referred-by); lifetime spend is .fin-gated.
- Money figures hidden for non-owner roles; items deep-link into the relevant record.
- Default tab on opening the profile.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(reads CLIENT-360 aggregation)** — recent activity + at-a-glance (visits, last seen, referred-by, lifetime spend[.fin])
  - _Presentation over the aggregation API; lifetime spend gated behind .fin (owner-only)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Overview tab (recent activity + at-a-glance, .fin-gated spend)**
  Behaviour: the default tab showing recent activity (treatments, rewards, skin) and an at-a-glance panel (visits count, last seen, referred-by). Requirements: lifetime spend / money figures in the at-a-glance are .fin-gated (owner-only); reads via the aggregation API; deep-links into the relevant record.
