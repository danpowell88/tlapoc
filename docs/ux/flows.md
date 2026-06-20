# UX Flows — End-to-End Journeys

The core journeys across all three surfaces, with compliance gates called out (`→ C#`). Pairs with
[README.md](README.md) (IA, screens, principles) and the [PRDs](../prds/). Diagrams are Mermaid.

---

## Flow 1 — Client: first booking → intake → consent (with under-18 branch)
*(PRD-02, PRD-03)*

```mermaid
flowchart TD
  A[Public booking site] --> B[Pick service (generic name)<br/>→ practitioner (RN/NP) → slot]
  B --> C[Create account<br/>social / email+pw / OTP]
  C --> D[Confirm booking<br/>+ cancellation policy]
  D --> E[Receive intake + consent links]
  E --> F[Complete intake<br/>history · meds · allergies · BDD screen]
  F --> G[Read + e-sign consent<br/>(risks/benefits/alts · qualifications · costs)]
  G --> H[Image-use consent? (separate, optional)]
  H --> I{Under 18?}
  I -- yes --> J[7-day cooling-off starts<br/>payment blocked · 2nd consult offered]
  I -- no --> K[Ready for visit]
  J --> K
```
**Walkthrough & gates**
1. Service names are **generic** publicly; no S4 brand/price shown (**→ C9**).
2. Only RN/NP appear for injectables (**→ C4**).
3. Intake includes the **BDD/psychological screen**; a flag is routed to the prescriber (**→ C3**).
4. Consent is plain-language, versioned, e-signed, with mandated content + complaint/AHPRA info (**→ C5**).
5. **Image-use consent is separate** and withdrawable later (**→ C14**).
6. Under-18 → **cooling-off timer + payment block**, second-consult offered (**→ C6**).

**Edge:** incomplete intake/consent ⇒ visit can't proceed to charting; blocked-action banner explains what's missing.

---

## Flow 2 — Client: recall → rebook → pre-care
*(PRD-07, PRD-02)*

```mermaid
flowchart LR
  A[~12 weeks since toxin] --> B{Future booking?}
  B -- no --> C[Recall nudge<br/>(SMS/app, opt-in respected)]
  C --> D[Tap to rebook<br/>(pre-filled service/practitioner)]
  D --> E[Pre-care instructions]
  E --> F[Reminders + confirm/decline]
```
Recall/marketing respects **opt-in + unsubscribe** (**→ C23**) and the **advertising linter** (**→ C9**); transactional reminders/pre-care always send.

---

## Flow 3 — Client: membership join + autopay + non-S4 rewards
*(PRD-06)*

```mermaid
flowchart TD
  A[Choose plan] --> B[Add card-on-file<br/>(in-app/online OR at desk)]
  B --> C[Automatic recurring charge<br/>+ dunning on failure]
  A --> D[Earn visit-based rewards]
  D --> E{Redeem against item}
  E -- S4 (toxin/filler) --> F[Blocked<br/>reward controls disabled (→C9/MEMB-7)]
  E -- non-S4 (skincare/add-on/credit) --> G[Reward applied<br/>(within margin cap)]
```
Autopay is **automatic** (card-not-present recurring); the card can be added by the client online/in-app. Rewards **only ever** apply to **non-S4** items — enforced by the catalog `schedule` flag, not staff discipline (**→ C9, REQ-MEMB-7**).

---

## Flow 4 — Front desk: check-in → POS → membership → closeout
*(PRD-02, PRD-06)*

```mermaid
flowchart TD
  A[Today board: client arrives] --> B[Check-in]
  B --> C{Injectable visit?}
  C -- yes --> D[Verify consult + consent + cooling-off]
  D --> E[Provider treats (Flow 5)]
  C -- no --> E
  E --> F[Checkout: line items<br/>(item schedule tagged)]
  F --> G[Tender: Square card / record cash / gift card]
  G --> H[Redeem package/series · apply non-S4 rewards]
  H --> I[Receipt + balance]
  I --> J[Post to Xero]
  J --> K[End of day: closeout<br/>(card + cash reconcile)]
```
Payments are **in-person** in v1 (card-present or recorded cash) (**PRD-06**); membership card-on-file may already be on file for autopay. S4 line items show no reward/discount controls (**→ C9**).

---

## Flow 5 — Provider: treatment-room (map + photos + finalise) with offline
*(PRD-05, PRD-04, PRD-09)*

```mermaid
flowchart TD
  A[Open patient on provider app] --> B{Consult + consent + (cooling-off) OK?}
  B -- no --> X[Blocked banner: what's missing + who resolves]
  B -- yes --> C[Injection-mapping canvas]
  C --> D[Drop points: product·units·depth·site·LOT]
  D --> E[Capture before/after photos<br/>(signed-URL upload; consent-gated)]
  E --> F{Connectivity?}
  F -- offline --> G[Encrypted local queue<br/>+ sync indicator]
  G --> H[Auto-sync on reconnect]
  F -- online --> I[Save draft]
  H --> I
  I --> J[Finalise → server-side, immutable]
  J --> K{Adverse event?}
  K -- yes --> L[Log → DAEN pathway (→C12)]
```
**Gates:** can't open charting without a linked **consult** + current **consent** (**→ C1/C5**); each point captures **batch-lot** (**→ C8**); photos never persist on device (**→ C14, ADR-0009**); finalised notes are **immutable** (**ADR-0010**); nothing is lost offline (**ADR-0015**).

---

## Flow 6 — Prescriber: consult → individual script (in-person & remote)
*(PRD-04)*

```mermaid
flowchart TD
  A{Consult modality} --> B[In-person consult]
  A --> C[Telehealth in external app<br/>→ record metadata + reference]
  B --> D[Record Consult<br/>(prescriber, time, notes)]
  C --> D
  D --> E[Write INDIVIDUAL prescription<br/>for this client]
  E --> F[(No batch / standing-order / async — blocked)]
  E --> G[Script available to RN<br/>for administration (Flow 5/7)]
```
Every script is **gated on a synchronous consult** and is **individual** (**→ C1, C2**); telehealth video happens in the external app — we record the consult only (**ADR-0011**).

---

## Flow 7 — Medicines: receive → store → administer → wastage → stocktake → recall
*(PRD-04)*

```mermaid
flowchart TD
  A[Receive stock from<br/>TGA-approved wholesaler] --> B[Record ARTG + brand + supply source<br/>(warn if non-ARTG) (→C11)]
  B --> C[Store: secure locked location<br/>+ temperature log 2–8°C (→C13,C15)]
  C --> D[Administer (Flow 5):<br/>select in-date lot · decrement · vial reconcile (→C8)]
  D --> E[Wastage / partial-vial &<br/>destruction records (→C16)]
  C --> F[Periodic stocktake<br/>→ discrepancy → loss/theft report (→C17)]
  D --> G[Lot → clients recall lookup (→C8)]
```
Custody is limited to **NP/prescriber** (Mode A) (**→ C7**); the medicine register is **append-only** (**ADR-0010**).

---

## Flow 8 — Owner/compliance: business + compliance evidence
*(PRD-08)*

```mermaid
flowchart LR
  A[Dashboards] --> B[Business: revenue · retention ·<br/>no-shows · MRR/churn · per-practitioner]
  A --> C[Compliance]
  C --> C1[Consent coverage · consult-before-script (→C1)]
  C --> C2[S4 register export · lot recall (→C8)]
  C --> C3[Registration-expiry watch (→C19)]
  C --> C4[Retention/destruction due (→C18)]
  C --> C5[Breach (→C22) · Complaints (→C24) registers]
  C --> C6[DAEN adverse-event prefilled export (→C12)]
```
Dashboards read from **materialized read models** (**ADR-0013**); compliance views double as audit evidence for QLD Health / AHPRA.

---

## Compliance-gate cheat-sheet (where each surfaces in the UX)
| Gate | Where the user feels it | Criterion |
|---|---|---|
| Consult before script | Provider/prescriber can't script/administer without a recorded consult | C1 |
| Individual script only | Batch/standing-order option doesn't exist | C2 |
| Assessment + BDD | Intake screen; prescriber sees the flag | C3 |
| Scope / registration | Booking & clinical actions hidden/blocked off-scope or lapsed | C4, C19 |
| Consent completeness | Treatment blocked until current consent signed | C5 |
| Cooling-off (U18) | Timer + payment block on the booking/checkout | C6 |
| Lot/recall | Mandatory lot per injection point | C8 |
| Advertising-safe | Generic public names; linter on comms; S4 reward controls disabled | C9 |
| Image-use consent | Separate toggle; withdraw any time | C14 |
| Secure/cold-chain stock | Storage + temp screens in Medicines | C13, C15 |
| Privacy rights | Client "Your data & privacy" | C21 |
