# Waitlist: offer lifecycle (offered → accepted / expired)

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/WAITLIST-OFFER-LIFECYCLE`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/WAITLIST`, `PRD-02/WAITLIST-MATCHING`

## Background

As a front desk, I want an offered slot to be held briefly then accepted or rolled on to the next client, so that a freed slot is filled fairly and never left in limbo.
Plainly: the lifecycle of a waitlist offer — it holds the slot for a short window, then either books it (accepted) or rolls on to the next matching client (expired). Where it fits: a follow-up to the waitlist basic entries & management (PRD-02/WAITLIST) that adds offer state handling on top of the matching engine (PRD-02/WAITLIST-MATCHING). Accepting books via the same scope/conflict checks as any booking. It sits in Reception (PRD-02).

## How it works

The matching engine creates an offer; this follow-up runs its lifecycle. An offer holds the freed slot for a short window so the offered client has time to respond, then resolves one of two ways.
On accept, the slot is booked via the create endpoint with full scope/conflict checks (so a backfilled booking still honours the rules) and the entry is marked accepted. On expiry, the entry is marked expired and the offer rolls on to the next matching waiting entry.
Every state — offered, accepted, expired, with timestamps — is tracked per entry so the desk can see who was offered what and when, giving a clear audit of how a slot was filled.

## Requirements

- An offered slot to be held briefly then accepted or rolled on to the next client.

## Acceptance Criteria

- [ ] An offer holds the slot for a short window, then accepts or rolls on.
- [ ] On accept: book via the create endpoint with full scope/conflict checks and mark accepted.
- [ ] On expiry: mark expired and roll the offer to the next matching entry.
- [ ] Every state (offered/accepted/expired, with timestamps) is tracked per entry.

## UI designs / screenshots

- The waitlist management list shows each entry's live offer state (offered / accepted / expired) with timestamps.
- An accepted offer creates the booking; an expired offer rolls to the next entry.
- The desk can see who was offered what and when.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(extends WAITLIST)** — WaitlistEntry.status transitions offered → accepted | expired; offered_at, expires_at tracked
  - _Accept books via the shared create endpoint with full scope/conflict checks; expiry rolls to the next matching entry._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Offer lifecycle: offered → accepted / expired**
  Behaviour: an offer holds the slot for a short window, then accepts or rolls on. Requirements: on accept, book via the create endpoint with full scope/conflict checks and mark accepted; on expiry, mark expired and roll the offer to the next matching entry; every state (offered/accepted/expired, with timestamps) is tracked per entry so the desk can see who was offered what and when.
