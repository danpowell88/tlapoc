# Reg-watch: 'who is cleared to inject today' compliance board

> **Epic:** [PRD-01 — Foundations & tenancy (auth, RBAC, audit, data model)](../epics/PRD-01.md)  ·  **Key:** `PRD-01/REG-WATCH-BOARD`  ·  **Type:** Story  ·  **Stage:** M1  ·  **Priority:** P2  ·  **Estimate:** 2 pts  ·  **Area:** —
>
> **Depends on:** `PRD-01/REG-WATCH`

## Background

As a manager, I want a compliance board showing who is cleared to inject today and who is blocked, so that I can see at a glance who I can book for S4 and why anyone is blocked.
Plainly: the at-a-glance Team board that shows, per practitioner, whether their registration, CPD and cosmetic indemnity all hold — and therefore whether they are bookable for S4 (Schedule 4 prescription-only medicine) today — with a red banner counting anyone flagged not-bookable. Where it fits: a follow-up to the registration/PII/CPD expiry-alerting core (PRD-01/REG-WATCH) that gives the watch a human-readable home screen. It reads the canInject derivation (PRD-01/CREDENTIALS) and the alerts the core raises; it sets no gate itself — it visualises the gate that already exists.

## How it works

Team → Compliance board (team-compliance.png) is the 'who is cleared to inject today' screen: a per-practitioner table with Registration (current·date / expired), CPD (continuing professional development, X/Yh or behind), Indemnity (covers cosmetic / EXCLUDES cosmetic) and Bookable-for-S4 (Yes / Blocked) columns, an explainer note ('an injector is bookable for S4 only when ALL of these hold: current registration, enough CPD, indemnity that covers cosmetic'), and a red banner counting injectors flagged not-bookable for S4 (Schedule 4 prescription-only medicine) — or the green all-clear when everyone holds.
The board is a read view over the canInject (the single derived cleared-to-inject gate) derivation (PRD-01/CREDENTIALS) and the alerts the watch (PRD-01/REG-WATCH) raises — it visualises the gate, it does not set it. Cells use the emerald / amber / rose states the derivation drives; non-AHPRA (Australian Health Practitioner Regulation Agency) practitioners render n/a. The surface is capability-gated to team:manage / the compliance concern.

## Requirements

- A compliance board showing who is cleared to inject today and who is blocked.

## Acceptance Criteria

- [ ] The board shows a per-practitioner table: Registration (current·date / expired), CPD (X/Yh / behind), Indemnity (covers cosmetic / EXCLUDES cosmetic), Bookable-for-S4 (Yes / Blocked).
- [ ] An explainer states an injector is bookable for S4 only when ALL of registration / CPD / cosmetic indemnity hold.
- [ ] A red banner counts injectors flagged not-bookable for S4 (or shows the green all-clear).
- [ ] Cells use emerald / amber / rose states; non-AHPRA practitioners render n/a; capability-gated to team:manage / the compliance concern.

## UI designs / screenshots

- Prototype: Team → Compliance board (team-compliance.png) — explainer note, a red 'N injector flagged not-bookable for S4' banner (or green all-clear), and the per-practitioner table with Registration / CPD / Indemnity-cosmetic / Bookable-for-S4 columns.
- Cells use emerald/amber/rose states from the canInject derivation; non-AHPRA practitioners render n/a.
- Capability-gated to team:manage / the compliance concern.

## Suggested data model

- **(read) ComplianceBoard** — per practitioner: registration state, cpd state, cosmetic-indemnity state, bookable_for_s4 (= canInject)
  - _Read view over the canInject derivation (PRD-01/CREDENTIALS) + CredentialAlerts (PRD-01/REG-WATCH); no new write model — it visualises the existing gate._

## Other

- Source PRD: [PRD-01-foundations-tenancy.md](https://github.com/danpowell88/tlapoc/blob/main/docs/prds/PRD-01-foundations-tenancy.md)

## Tasks (dev pickup)

- [ ] **Compliance board table + not-bookable banner**
  Behaviour: build Team → Compliance board (team-compliance.png) — the explainer note, the red 'N injector flagged not-bookable for S4 (Schedule 4 prescription-only medicine)' banner (or green all-clear), and the per-practitioner table with Registration / CPD (continuing professional development) / Indemnity-cosmetic / Bookable-for-S4 columns. Requirements: cells use emerald/amber/rose states read from the canInject (the derived cleared-to-inject gate) derivation (CREDENTIALS); non-AHPRA practitioners render n/a; capability-gate to team:manage / the compliance concern; the board sets no gate — it visualises the existing one.
