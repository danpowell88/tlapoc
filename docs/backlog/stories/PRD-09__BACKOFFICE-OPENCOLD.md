# Back-office tablet: open/close + cold-chain panels

> **Epic:** [PRD-09 — Apps (Flutter): client & provider](../epics/PRD-09.md)  ·  **Key:** `PRD-09/BACKOFFICE-OPENCOLD`  ·  **Type:** Story  ·  **Stage:** M5  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-09/BACKOFFICE-TABLET`, `PRD-11/OPENCLOSE`

## Background

As a clinic staff, I want open/close checklist and cold-chain log panels on the bench tablet, so that I can run the open/close routine and log fridge temps at the bench.
Plainly: the back-office tablet panels for the day's open/close checklist and the cold-chain (the unbroken temperature-controlled storage required for medicines) fridge log. Where it fits: a follow-up to the back-office tablet basic (PRD-09/BACKOFFICE-TABLET) that adds the open/close + cold-chain panels; both reuse the operations modules (PRD-11/OPENCLOSE + TEMP-MONITORS) rather than re-implementing them, and the cold-chain breach pathway stays intact.

## How it works

The Open & close panel renders today's checklist (tick items, each recording who/when, with the responsible role) and the Cold chain panel logs AM/PM fridge temperatures with in-range / breach states. Both reuse PRD-11/OPENCLOSE + TEMP-MONITORS — no parallel data store; audited.
An out-of-2–8°C reading raises the breach pathway: quarantine the affected lot (the manufacturer's batch of a medicine vial) + raise a job — the cold-chain breach pathway stays intact at the bench exactly as it does on the operations web view. Completion state feeds the hub's morning attention items (BACKOFFICE-TABLET).

## Requirements

- Open/close checklist and cold-chain log panels on the bench tablet.

## Acceptance Criteria

- [ ] The Open & close panel renders today's checklist (tick items, each recording who/when, with the responsible role).
- [ ] The Cold chain panel logs AM/PM fridge temperatures with in-range / breach states.
- [ ] An out-of-2–8°C reading raises the breach pathway (quarantine the affected lot + a job).
- [ ] Reuses PRD-11/OPENCLOSE + TEMP-MONITORS — no parallel data store; audited.

## UI designs / screenshots

- Prototype: backroom — tabs Open & close, Cold chain.
- Checklist tick with role + who/when; AM/PM fridge temps with in-range / breach; breach → quarantine lot + job.

![client-app — prototype screen](../screens/client-app.png)

## Suggested data model

- **(reuses) OpenCloseChecklist/FridgeLog** — PRD-11 — open/close + cold-chain panels
  - _Extends BACKOFFICE-TABLET; reuses PRD-11/OPENCLOSE + TEMP-MONITORS; breach pathway intact._

## Other

- Source PRD: [PRD-09-apps-client-provider.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-09-apps-client-provider.md)

## Tasks (dev pickup)

- [ ] **Open/close checklist + cold-chain (fridge) log panels (PRD-11)**
  Behaviour: the Open & close panel renders today's checklist (tick items, each recording who/when, with the responsible role) and the Cold chain panel logs AM/PM fridge temperatures with in-range / breach states. Requirements: reuses PRD-11/OPENCLOSE + TEMP-MONITORS — an out-of-2–8°C reading raises the breach pathway (quarantine the affected lot (the manufacturer's batch of a medicine vial) + a job); no parallel data store; audited.
