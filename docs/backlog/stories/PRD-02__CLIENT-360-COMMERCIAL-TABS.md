# Client 360: commercial tabs (Membership & rewards / Billing / Notes & comms)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-360-COMMERCIAL-TABS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-360`

## Background

As a staff member, I want tabs for membership & rewards, billing and notes & comms on the client profile, so that I can see a client's commercial and communication history in one place.
Plainly: the commercial tabs of the Client 360 profile — membership & rewards, billing, and notes & comms. Where it fits: a follow-up to the Client 360 basic aggregation & header (PRD-02/CLIENT-360) that adds the commercial tabs on top of the header. It honours owner-only financial gating: the Billing tab and money figures sit behind the .fin capability, stripped for non-owner roles such as Reception (who may see memberships but no money). It sits in Reception (PRD-02).

## How it works

The basic story provides the aggregation API and the header; this follow-up adds the commercial tabs. Tabs render membership & rewards, billing, and notes & comms.
Financial gating is the key constraint: the Billing tab and any money figures are gated behind the .fin capability (owner-only) and stripped for non-owner roles — Reception may see memberships but no money figures.
All data is read via the Client 360 aggregation API, and the commercial tabs deep-link into checkout.

## Requirements

- Tabs for membership & rewards, billing and notes & comms on the client profile.

## Acceptance Criteria

- [ ] Tabs render membership & rewards, billing, and notes & comms.
- [ ] The Billing tab and any money figures are gated behind the .fin capability (owner-only) and stripped for non-owner roles such as Reception (who may see memberships but no money).
- [ ] Reads via the aggregation API and deep-links into checkout.

## UI designs / screenshots

- Prototype: Client 360 (client-360.png) — Membership & rewards, Billing (.fin), and Notes & comms tabs.
- Billing tab and money figures gated behind .fin (owner-only); reception sees memberships but no money.
- Reads via the aggregation API; deep-links into checkout.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(reads CLIENT-360 aggregation)** — Membership & rewards, Billing[.fin], Notes & comms (owned by PRD-06/07)
  - _Presentation over the aggregation API; Billing/money gated behind .fin (owner-only)._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Commercial tabs (Membership & rewards / Billing[.fin] / Notes & comms)**
  Behaviour: tabs for membership & rewards, billing, and notes & comms. Requirements: the Billing tab and any money figures are gated behind the .fin capability (owner-only) and stripped for non-owner roles such as Reception (who may see memberships but no money); reads via the aggregation API; deep-links into checkout.
