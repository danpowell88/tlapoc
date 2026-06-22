# Client directory: segment filters (All / Members / At-risk / New)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-DIR-SEGMENTS`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-DIR`

## Background

As a front desk, I want to filter the client directory by segment, so that I can focus on members, at-risk clients or new clients quickly.
Plainly: filter chips on the client directory that narrow it to All / Members / At-risk / New. Where it fits: a follow-up to the client directory basic search & list (PRD-02/CLIENT-DIR) that adds segment filtering on top of the search/list. Segments derive from membership state, recall risk and join date. It sits in Reception (PRD-02).

## How it works

The basic directory provides search and the Clients table; this follow-up adds segment filtering. Filter chips narrow the directory to All / Members / At-risk / New.
The segments derive from membership state (Members), recency/recall risk (At-risk) and join date (New), so each chip reflects a meaningful operational cut of the client base.
Segments compose with the active search query, and the active segment persists across a refresh so the desk keeps its filtered view.

## Requirements

- To filter the client directory by segment.

## Acceptance Criteria

- [ ] Filter chips narrow the directory to All / Members / At-risk / New.
- [ ] Segments derive from membership state, recency/recall risk and join date.
- [ ] Segments compose with the search query.
- [ ] The active segment persists so a refresh keeps it.

## UI designs / screenshots

- Prototype: Clients (clients.png) — segment filter chips (All / Members / At-risk / New) above the table.
- Segments compose with the search box; the active segment persists across refresh.
- Each segment reflects membership/recall-risk/join-date.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends CLIENT-DIR)** — no new entities; derives segments from membership state, recall risk and join date
  - _Composes with the directory search query; the active segment persists in state._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Segment filters (All / Members / At-risk / New)**
  Behaviour: filter chips that narrow the directory to All / Members / At-risk / New. Requirements: segments derive from membership state, recency/recall risk and join date; compose with the search query; the active segment persists so a refresh keeps it.
