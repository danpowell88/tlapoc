# Chapter 8 — Coverage & scope: the checklist

> *New here? Read [Start here](00-start-here.md) first — it has the glossary and the cast of people.*

This final chapter is your **assessment tool**. It lays out plainly what's being built now, what's
deliberately left for later, what's handled in other software, and what's still an open question — then
gives you a **master tick-list** to judge whether everything a clinic needs is covered.

---

## 1. What's in the first version (v1)

The first version deliberately nails **one treatment type — anti-wrinkle injections — from end to
end**, plus everything needed to run the clinic around it:

- ✅ Booking & scheduling (with reminders, waitlist, walk-ins, the visit journey)
- ✅ Client records (the "client 360"), the daily jobs list, the phone log
- ✅ Pre-visit intake, the BDD screen, consent (incl. separate photo consent), cooling-off
- ✅ The consult → individual prescription → treatment chain, with all the safety gates
- ✅ Injection mapping, before/after photos, locked records, complication handling
- ✅ The S4 medicine ledger: receiving, custody, secure & cold storage, batch tracing, recall lookup,
  wastage/reconciliation, disposal, stocktake
- ✅ In-person payments (card + cash), gift cards, packages, **memberships with autopay**, non-S4
  rewards
- ✅ Pricing & what-if, plus the core reporting dashboards and the owner's "needs attention" digest
- ✅ The team & credentials system, the "cleared to treat" board, rosters
- ✅ The compliance/governance hub and the 24 rules (advertising tooling is **out of scope** — handled in your own marketing tools)
- ✅ Reminders & recall, the unified inbox (SMS/email), reviews, the public booking page
- ✅ Both phone apps (client + provider), Xero & calendar integration, Australian data hosting

---

## 2. What's deliberately for later (and why)

These are **known, intentional** deferrals — not gaps. The question for you is whether any are needed
**sooner** than planned.

| Planned for later | Why it's deferred |
|-------------------|-------------------|
| Other treatments (filler, laser, skin, weight-loss) in full depth | v1 proves the model on anti-wrinkle first; the design already anticipates the others |
| Customer-facing **online checkout** for one-off purchases | In-person payment first (membership card-on-file is the one online exception) |
| **Booking deposits / card holds** | Not required to book in v1 |
| **Pharmacy-dispensing model** ("Mode B") | No pharmacy partner yet; on-site stock model used first |
| Advanced **loyalty campaigns & deep referrals** | Core mechanics first |
| Full **retail inventory & supplier ordering** | The S4 ledger is the priority |
| **AI features** (e.g. note dictation, auto-detecting injection points) | Explicitly out for now — everything is manual and human-controlled |
| Two-way calendar sync, electronic prescribing, social-DM messaging | Flagged as needing technical validation first |
| Public API / webhooks, multi-location switching, SaaS sign-up | Much later (scale phase) |

---

## 3. What's handled in other software (not rebuilt here)

| Handled elsewhere | Where |
|-------------------|-------|
| Accounting books, payroll, super, supplier bills, BAS/GST, reconciliation | **Xero** |
| Email newsletters / campaigns | **Mailchimp** (or similar) |
| Social-media posting | **Meta Business Suite** (or similar) |
| The telehealth **video call** itself | Your **existing telehealth app** (this system records the consult details) |

The system **passes data across** to these tools (e.g. sales to Xero) so you don't double-enter.

---

## 4. Open questions to confirm

A short list of things the build team has explicitly flagged for **your** decision:

1. **Membership plans & reward rules** — the exact tiers, prices, perks and caps need to be defined by
   you.
2. **Adult cooling-off** — do you want an *optional* adult cooling-off as clinic policy (not legally
   required)?
3. **Public booking-page naming** — confirm injectable services are listed generically with prices
   withheld (the safe default).
4. **Your prescriber arrangement** — does the consult/prescription model match how prescribing actually
   works in your clinic (on-site NP, remote doctor, designated RN prescriber)?
5. **Deposits & online payments** — are you comfortable these come later, or are they needed sooner?
6. **Retail & supplier ordering** — needed in v1, or can it wait?
7. A **product name** hasn't been chosen — it's referred to generically for now.

---

## 5. The master coverage checklist

Go through each line and tick it, question it, or note what's missing. *"To run our clinic, we need…"*

### Getting clients in
- [ ] Take bookings (online, by phone, walk-in)
- [ ] Reminders, reschedule/cancel, waitlist, no-show handling
- [ ] A clear view of the day and the visit journey
- [ ] Keep a complete client record and history

### Treating safely & legally
- [ ] Collect medical history and screen (incl. BDD) before treating
- [ ] Capture informed, signed consent (and separate photo consent)
- [ ] Enforce cooling-off for under-18s
- [ ] Require a real consult and an individual prescription before any S4 treatment
- [ ] Only let qualified, registered, insured staff treat
- [ ] Chart the treatment precisely (injection map, units, depth, batch)
- [ ] Take and compare before/after photos securely
- [ ] Have an emergency/complication workflow

### Medicines
- [ ] Only buy/use approved medicine from lawful suppliers
- [ ] Hold stock under correct custody, locked and temperature-controlled
- [ ] Trace every dose to a patient and batch; run a recall instantly
- [ ] Record wastage, disposal and stocktakes

### Money
- [ ] Take payment (card, cash, gift card, packages)
- [ ] Run memberships with automatic billing
- [ ] Offer rewards/loyalty (within margin and advertising rules)
- [ ] See the numbers needed to run the business; books reconcile to Xero

### People
- [ ] Manage rosters and leave
- [ ] Track registration, training (CPD) and insurance
- [ ] Know at a glance who's cleared to treat

### Compliance & safety
- [ ] Report adverse events; run recalls
- [ ] Keep policies signed, infection-control and waste logged
- [ ] Handle privacy requests and data breaches
- [ ] Record complaints and surface the right pathways
- [ ] Stay inside the advertising rules everywhere
- [ ] Produce evidence for an inspection quickly

### Communications & growth
- [ ] One inbox for client messages
- [ ] Reminders and re-booking nudges (opt-in respected)
- [ ] Manage reviews and reputation
- [ ] A compliant public booking page
- [ ] Apps for clients and clinicians

> **Anything you couldn't tick, or anything not on this list that your clinic needs, is exactly the
> feedback this review is for.** Note it down — that's the most valuable outcome of reading this
> section.

---

## Where to dig deeper

If you want the detailed, technical version behind any of this:

- The full requirements list: [Requirements & compliance](../02-requirements.md)
- Per-area function tours (with workflow diagrams): [Area overviews](../overviews/00-overviews-index.md)
- The per-feature build documents: [the PRDs](../00-index.md#the-prd-set)

> Back to the start: **[Start here](00-start-here.md)**.
