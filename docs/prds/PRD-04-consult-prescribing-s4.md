# PRD-04 — Consult, Prescribing & S4 Medicines Governance  *(the moat)*

> **Phase:** 1 · **Status:** Draft
> **Requirements:** REQ-RX-1…5, REQ-MED-1…10 · **Compliance:** C1, C2, C7, C8, C11, C13, C15, C16, C17
> **ADRs:** 0008 (compliance-by-construction), 0011 (telehealth external), 0010 (immutability)
> **Depends on:** PRD-01, PRD-03

## 1. Summary
The defensible core: every S4 administration is provably tied to a **synchronous consult**, an
**individual prescription**, valid **consent**, and a **batch/lot** drawn from lawfully-supplied,
ARTG-approved stock held under correct custody. Implements the QLD S4 + TGA medicines rules as
**enforced invariants**, not checklists, and produces an audit-ready medicine register.

## 2. Goals & non-goals
**Goals:** record consults (in-person or external-telehealth); individual scripts (no batch/async);
administration gated on script+consent+consent+lot; Mode-A on-site stock ledger with secure storage,
cold-chain, vial reconciliation, disposal/destruction, stocktake, ARTG/supply provenance; lot→clients
recall lookup.
**Non-goals (v1):** Mode-B pharmacy dispensing; e-prescribing via ETP networks (structured script +
PDF only); built-in telehealth video (ADR-0011).

## 3. Users
NP/on-site prescriber, remote prescriber, RN (administers), owner (medicines custody/audit).

## 4. User stories
- As a **prescriber**, after a **synchronous consult** (in person or recorded from our external telehealth app) I write an **individual prescription** for this patient — never batch/standing-order.
- As an **RN**, I can only administer S4 against a **valid, unconsumed prescription for this patient**, and I must record the **product, units, depth, site and batch-lot/expiry**.
- As a **prescriber/owner**, I receive S4 stock from a **TGA-approved wholesaler**, confirm **ARTG** status, and hold it in **secure, temperature-logged** storage.
- As an **owner**, I run a **stocktake**, log **wastage/destruction** (incl. partial vials), and can instantly list **which clients received a given lot** for a recall.

## 5. Key flow
```mermaid
flowchart TD
  A[Consult recorded\nin-person / telehealth-ext] --> B[Individual prescription\nfor this client]
  B --> C{Admin attempt}
  C --> D{Valid unconsumed Rx\n+ current consent\n+ this client?}
  D -- no --> E[BLOCK + reason + audit]
  D -- yes --> F[Select stock lot\nARTG + in-date + custody OK]
  F --> G[Record units/site/depth\n+ batch-lot/expiry]
  G --> H[Decrement stock\n+ vial reconciliation]
  H --> I[Append to medicine register\n(immutable)]
  I --> J[Lot ↔ client link\nfor recall]
```

## 6. Functional scope
**Consult & prescribing**
- REQ-RX-1 (C1): `Consult` records modality (in-person/telehealth-external), prescriber, timestamp, external reference, notes — required before any script.
- REQ-RX-2 (C2): individual prescription per client per consult; **no batch/bulk/standing-order**, **no async** (text/email/online-only).
- REQ-RX-3: administration must reference a valid, unexpired, **unconsumed** script for the **same** client.
- REQ-RX-4: remote-prescriber path links the externally-conducted consult + resulting script.
- REQ-RX-5: **off-label** flag on the script; linked consent must cover it.

**Medicines governance (Mode A)**
- REQ-MED-1 (C7): tenant mode switch (A on-site / B pharmacy); **v1 = Mode A only**.
- REQ-MED-2: stock ledger — receipt, custodian, storage, administration (decrement), wastage, disposal, expiry alerts; custody limited to NP/prescriber.
- REQ-MED-4 (C8): each administration writes batch-lot, qty, prescriber, administrator, client, datetime → **audit-ready register** + **lot→clients** recall lookup.
- REQ-MED-5: **vial/unit reconciliation** (units drawn vs vial size + wastage).
- REQ-MED-6 (C11): record **ARTG status, brand, sponsor, lawful supply source**; warn on non-ARTG/unverified-source.
- REQ-MED-7 (C13): **temperature logging** (2–8°C) with excursion alerts.
- REQ-MED-8 (C15): **secure storage** (locked cabinet/room; restricted + logged access).
- REQ-MED-9 (C16): **disposal/destruction & wastage** records (incl. partial vials), licensed/RUM pathway, certificates.
- REQ-MED-10 (C17): **stocktake & discrepancy**; loss/theft reporting.

## 7. Data & entities
`Consult`, `Prescription` (+off-label), `Administration` (immutable), `Product` (medicine; ARTG#, sponsor, supply-source),
`StockItem`/`StockLedger` (lot, expiry, storage-temp, custodian, location), `Stocktake`, `StockDestruction`,
`TempLog`/`Excursion`, `MedicineMode`. (`DispensedItem` reserved for Mode B — deferred.)

## 8. Acceptance criteria
- **AC1 (C1):** A prescription cannot be saved without a linked synchronous `Consult` at/just-before script time.
- **AC2 (C2):** The system rejects any attempt to apply one script to multiple clients or to create a standing-order/batch script.
- **AC3 (C8):** An `Administration` cannot persist without a valid script (same client), current consent, and a selected **in-date lot**; it is **immutable** once saved and appears in the register.
- **AC4 (recall):** Given a lot number, the system lists every client/administration for that lot.
- **AC5 (C7/C15):** Only NP/prescriber roles can take custody of stock; stock is bound to a secure location; access is logged.
- **AC6 (C13):** A temperature excursion raises an alert and flags affected stock.
- **AC7 (C11):** Receiving non-ARTG or unverified-source stock is warned/blocked per config; ARTG + supply source are recorded.
- **AC8 (C5/RX-5):** An off-label script requires consent that covers off-label use.
- **AC9 (C16/C17):** Destruction (incl. partial vials) and stocktake discrepancies are recorded; a discrepancy can trigger a loss/theft report.

## 9. Dependencies & sequencing
After PRD-01 (audit/roles) and PRD-03 (consent). Highest-risk module → **build right after PRD-01**, with a compliance/legal review of `02-requirements.md` first.

## 10. Out of scope
Mode-B pharmacy dispensing; ETP e-prescribing; telehealth video.

## 11. Open questions
- Remote-prescriber + on-site-stock custody interpretation (QLD nuance, §10.5) — confirm with legal.
- ARTG validation: manual entry vs lookup against an ARTG dataset.
