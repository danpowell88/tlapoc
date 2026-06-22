# Client directory: global header search wiring

> **Epic:** [PRD-02 — Booking & scheduling (+ client/CRM basics)](../epics/PRD-02.md)  ·  **Key:** `PRD-02/CLIENT-DIR-HEADER-SEARCH`  ·  **Type:** Story  ·  **Stage:** M2  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-02/CLIENT-DIR`

## Background

As a front desk, I want the global header search to jump straight to a client from anywhere, so that I can find a client without navigating to the directory first.
Plainly: wiring the staff app shell's global header search box to the client directory so it jumps straight to a client from any screen. Where it fits: a follow-up to the client directory basic search & list (PRD-02/CLIENT-DIR) that surfaces the directory search through the global header. It reuses the basic's directory search API and deep-links to the matched Client 360. It sits in Reception (PRD-02) but is reachable across the whole staff shell.

## How it works

The basic directory provides the search API and the Clients screen; this follow-up surfaces that search through the staff app shell's global header so the desk can find a client from any screen without first navigating to the directory.
The header search reads the SAME directory search API as the Clients screen (no separate index), so results are consistent and soft-deleted clients are excluded.
A match deep-links straight to the client's Client 360 profile, making client lookup a one-step action from anywhere in the shell.

## Requirements

- The global header search to jump straight to a client from anywhere.

## Acceptance Criteria

- [ ] The global header search jumps straight to a client from anywhere in the shell.
- [ ] It reads the same directory API as the Clients screen.
- [ ] It deep-links to the matched Client 360.
- [ ] Soft-deleted clients are excluded (inherited from the basic search).

## UI designs / screenshots

- Prototype: the global header search ('Search clients, appointments, invoices…') jumps straight to a client.
- Reads the same directory API as the Clients screen; deep-links to the matched Client 360.
- Reachable from anywhere in the staff shell.

![schedule — prototype screen](../screens/schedule.png)

## Suggested data model

- **(reuses CLIENT-DIR)** — no new entities; the header search calls the directory search API
  - _Same endpoint/index as the Clients screen; deep-links to Client 360; excludes soft-deleted clients._

## Other

- Source PRD: [PRD-02-booking-scheduling.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-02-booking-scheduling.md)

## Tasks (dev pickup)

- [ ] **Global header search wiring (deep-link to Client 360)**
  Behaviour: the global header search jumps straight to a client from anywhere in the shell. Requirements: the header search reads the same directory API as the Clients screen and deep-links to the matched Client 360; soft-deleted clients are excluded (inherited from the basic search).
