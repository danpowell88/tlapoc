# Cold chain: commercial-logger adapters (Testo / Dickson / LogTag)

> **Epic:** [PRD-04 — Consult, prescribing & S4 medicines governance (the moat)](../epics/PRD-04.md)  ·  **Key:** `PRD-04/COLD-CHAIN-COMMERCIAL-LOGGERS`  ·  **Type:** Story  ·  **Stage:** M3  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-04/COLD-CHAIN`

## Background

As a owner, I want to feed a commercial temperature logger's readings into the same cold-chain rule, so that I can use a validated off-the-shelf logger without changing how breaches are handled.
Plainly: this lets the clinic use an off-the-shelf temperature logger (Testo, Dickson, LogTag) instead of, or alongside, the DIY sensor — the system translates each vendor's data into one common shape and runs the same 2-8 degree rule over it. Where it fits: a follow-up to PRD-04/COLD-CHAIN that adds vendor adapters in front of the same ingest, 2-8C rule and breach/quarantine pathway the basic already owns. It converges every source onto one ingestReading() so a breach behaves identically regardless of which logger reported it.

## How it works

This follow-up adds support for validated commercial loggers on top of the basic's manual + ESP32 ingest. A per-vendor adapter normalises each payload into the canonical reading shape (their device -> our fridgeId, unit -> Celsius, timestamp -> ISO-8601), converging on the same ingestReading() / 2-8C rule / breach pathway so a breach behaves identically regardless of source.
Two integration shapes are supported: webhook-in (the vendor pushes; e.g. Testo, Disruptive) verifying the vendor signature; and poll-out (we pull on a timer; DicksonONE has no webhook and stores Fahrenheit -> convert).
Config per fridge records which source is the instrument-of-record vs early-warning (ADR-0036), so a clinic can run a DIY sensor as early-warning behind a validated logger of record.

## Requirements

- To feed a commercial temperature logger's readings into the same cold-chain rule.

## Acceptance Criteria

- [ ] A per-vendor adapter normalises each logger's payload into the canonical reading shape (their device id -> our fridge id, unit -> Celsius, timestamp -> ISO-8601).
- [ ] All sources converge on the same ingestReading() / 2-8C rule / breach-and-quarantine pathway (PRD-04/COLD-CHAIN).
- [ ] Webhook-in adapters verify the vendor signature; poll-out adapters pull on a timer for vendors without a webhook (and convert Fahrenheit where stored).
- [ ] Per fridge, config records which source is the instrument-of-record vs early-warning.

## UI designs / screenshots

- Prototype screen: Front desk / Operations — Temperature monitors (ops-monitors.png).
- A commercial logger appears as another monitor in the fleet view alongside the TM-0x ESP32 monitors, with its source kind and instrument-of-record vs early-warning role shown.
- Breaches from a commercial logger raise the same excursion/quarantine + facility job as the DIY monitor.

![stock — prototype screen](../screens/stock.png)

## Suggested data model

- **Monitor (device)** — + kind(testo|dickson|logtag), role(instrument_of_record|early_warning)
  - _Extends the basic's Monitor entity with the commercial kinds + per-fridge role; readings still land as TempLog rows via the same ingestReading() (ADR-0036)._

## Other

- Source PRD: [PRD-04-consult-prescribing-s4.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-04-consult-prescribing-s4.md)

## Tasks (dev pickup)

- [ ] **Per-vendor adapters normalising to the canonical reading**
  Behaviour: a per-vendor adapter (Testo / Dickson / LogTag) normalises each payload into the canonical reading shape (their device -> our fridgeId, unit -> Celsius, timestamp -> ISO-8601), converging on the same ingestReading() / 2-8C rule / breach pathway as the basic (PRD-04/COLD-CHAIN). Requirements: webhook-in (vendor pushes; verify the vendor signature) and poll-out (we pull on a timer; convert Fahrenheit where stored). Config per fridge: which source is the instrument-of-record vs early-warning (ADR-0036).
