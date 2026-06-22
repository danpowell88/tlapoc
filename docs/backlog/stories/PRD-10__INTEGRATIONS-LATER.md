# Online checkout, e-prescribing, webhooks/API (placeholder)

> **Epic:** [PRD-10 — Integrations: Xero & calendar](../epics/PRD-10.md)  ·  **Key:** `PRD-10/INTEGRATIONS-LATER`  ·  **Type:** Story  ·  **Stage:** M4  ·  **Priority:** P2  ·  **Estimate:** 1 pts  ·  **Area:** integration

## Background

As a owner, I want future integrations: online checkout/deposits, e-prescribing and a public API, so that the platform extends as we scale.
Online checkout & deposits (S4 never priced/sold online), e-prescribing (eRx/ETP, 🔬), public API/webhooks (Phase 3) and Medicare/HICAPS (non-applicable to cosmetic). Placeholder (REQ-INT-2a/4/5/6/7, ADR-0035/0036).

## How it works

Placeholder (Phase 2/3) for the growth/integration roadmap shown as concept cards on Settings → Integrations: online checkout & deposits (behind the existing IPaymentProvider — and S4 is never priced or sold online, ADR-0014/0036), e-prescribing for private S4 scripts (behind IPrescribingProvider, eRx/ETP — needs feasibility validation, ADR-0035), public API / webhooks / event bus (Phase 3, ADR-0036), and Medicare/HICAPS (recorded as non-applicable to cosmetic — claimable only for therapeutic exceptions).
Each future integration sits behind an existing port so the architecture stays extension-ready with no rework: payment-class integrations on IPaymentProvider, prescribing on IPrescribingProvider, accounting on IAccountingExport, calendar on ICalendarProvider. The invariants carry forward into any future build — S4 never online, e-prescribing bound to the synchronous consult + S4 register + prescriber identity. No build in v1; design-only when scheduled.

## Requirements

- Future integrations: online checkout/deposits, e-prescribing and a public API.
- Deferred (Phase 2+): placeholder, design-only for now.

## Acceptance Criteria

- [ ] Placeholder — Phase 2/3; each future integration sits behind its existing port (IPaymentProvider, IPrescribingProvider, IAccountingExport, ICalendarProvider).
- [ ] S4 is never priced or sold online (invariant carried forward into online checkout/deposits).
- [ ] Medicare/HICAPS recorded as non-applicable to cosmetic.
- [ ] E-prescribing (eRx/ETP) flagged for feasibility validation, bound to consult + S4 register + prescriber identity when built.

## UI designs / screenshots

- Prototype: Settings → Integrations (settings-integrations.png) — concept cards, mostly disabled: 'Online checkout & deposits' (Off · roadmap), 'e-Prescribing (eRx / ETP)' (Off · research), 'Medicare / HICAPS' (Not applicable), 'Webhooks & public API' (Off · phase 3).
- Cards show the intent + status badge; Connect actions are inert until the feature is built.

![settings-integrations — prototype screen](../screens/settings-integrations.png)

## Suggested data model

- **(future)** — OnlineOrder / EPrescription / Webhook / ApiKey
  - _Behind existing ports; S4 never online; e-prescribing bound to consult + S4 register (ADR-0035/0036)._

## Technical notes (high level)

- Architecture decisions: [ADR-0035](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md), [ADR-0036](https://github.com/danpowell88/tlapoc/blob/main/docs/adr/decision-log.md)

## Other

- Source PRD: [PRD-10-integrations.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-10-integrations.md)

## Tasks (dev pickup)

- [ ] **Scope & design when pulled into a sprint**
  Deferred placeholder — no build in v1. When scheduled, confirm each still fits scope and the carried-forward invariants (S4 never priced/sold online; e-prescribing bound to the synchronous consult + S4 register + prescriber identity; Medicare/HICAPS out as non-applicable), then break down behind the existing port (IPaymentProvider / IPrescribingProvider / IAccountingExport / ICalendarProvider). E-prescribing and any inbound webhooks/public API need a feasibility spike (ADR-0035/0036) before commit.
