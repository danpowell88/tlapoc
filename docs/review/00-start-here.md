# Plain-language review — start here

> **Who this is for:** the people who actually run the clinic. You don't need a technical
> background, and you don't need to know all the rules off by heart. This section explains, in
> everyday language, **everything the system is meant to do** — what each feature is, why it's
> there, and who uses it — so you can answer one question:
>
> ### "Does this cover everything a clinic like ours needs to operate?"

The rest of the documentation (requirements, PRDs, ADRs) is written for the people building the
software. **This section is the same information, translated.** Nothing here is new — it's a
faithful, plain-English retelling of the build plan so you can sanity-check it against how a real
clinic works day to day.

---

## How to use this review

1. **Read it like a walk through the clinic**, not a spec. The chapters follow the natural shape of
   a clinic day — the front desk, the treatment room, the till, the team, and the behind-the-scenes
   safety and compliance work.
2. **For every feature, ask yourself three questions:**
   - *Would our clinic actually use this?*
   - *Is anything about how we work missing or different?*
   - *Does this match what the law / our insurer / AHPRA expects of us?*
3. **Jot down anything that feels missing, wrong, or confusing.** A gap you spot now is far cheaper
   to fix than one found after it's built. There are no silly questions — if a term isn't clear,
   that's a note worth making.
4. **Use the checklist at the end** ([Chapter 8 — Coverage & scope](08-scope-and-checklist.md)) as a
   final tick-list: "to run a clinic, you need… — is it all here?"

> **A note on "v1" vs "later".** The plan is deliberately built in stages. The first version ("v1")
> nails one treatment type — **anti-wrinkle injections** — from end to end, then widens out. Where a
> feature is planned for **later**, we say so plainly, so you can judge whether it's needed sooner.

---

## The chapters

| # | Chapter | What it covers |
|---|---------|----------------|
| — | **Start here** *(this page)* | How to review · the people · the glossary · the big picture |
| 1 | [Front desk & daily operations](01-front-desk-and-operations.md) | The diary, bookings, walk-ins, the visit journey, client records, the daily jobs list, the fridge log, rooms & equipment, the phone |
| 2 | [Treatments & clinical care](02-treatments-and-clinical.md) | Intake forms, consent, the consultation, prescribing, charting the treatment, photos, handling complications |
| 3 | [Medicines & stock](03-medicines-and-stock.md) | The product list, the prescription-medicine ledger, fridge/cold-chain, batch tracing & recalls, wastage, stocktakes |
| 4 | [Money, memberships & reporting](04-money-and-memberships.md) | Taking payment, gift cards, packages, memberships, rewards, pricing, the numbers the owner watches |
| 5 | [The team & their credentials](05-team-and-people.md) | Roles & who can do what, rosters, registration/insurance/training checks, "are we cleared to treat?" |
| 6 | [Compliance & safety](06-compliance-and-safety.md) | The safety net: adverse-event reporting, recalls, policies, waste, privacy, complaints, audit — and the 24 rules in plain English |
| 7 | [Growth, communications & the apps](07-growth-communications-and-apps.md) | Messages & reviews, reminders & re-booking, advertising rules, the public booking page, the phone apps |
| 8 | [Coverage & scope — the checklist](08-scope-and-checklist.md) | What's in now vs later, what's handled in other tools, open questions, and the master tick-list |

---

## The people (who's who)

The system gives each kind of staff member their **own view** and their **own permissions** — it only
lets people do what they're trained and legally allowed to do. Here's the cast, in plain terms.

| Role | In plain English | Can they inject / prescribe? |
|------|------------------|------------------------------|
| **Client / patient** | The person being treated. Books, fills in forms, sees their photos, history and memberships. | — |
| **Reception / front desk** | Runs the front of house: bookings, check-in, payments, messages. Sees limited clinical info. | No |
| **Dermal therapist** | Does skin treatments and facials (no prescription medicines). May also run lasers if licensed. | No — never injectables |
| **Registered Nurse (RN)** | A qualified nurse who **gives** the injection, but only against a prescription written for that specific patient. Cannot prescribe or own the medicine stock. | Administers only |
| **Lead Nurse** | A senior RN who also oversees the medicine stock and the clinical team. Same treating limits as an RN. | Administers only (+ stock oversight) |
| **Designated RN prescriber** | *(A newer role.)* An RN with extra qualifications who **may prescribe** certain medicines **in partnership with a doctor or nurse practitioner**. | Prescribes (in partnership) + administers |
| **Nurse Practitioner (NP)** | The most senior clinician. Can **assess, prescribe, hold the medicine stock, and treat**. Often the on-site prescriber. | Yes — full scope |
| **Remote prescriber (doctor/NP via video)** | A prescriber who does the consult by video from elsewhere. Can prescribe, but holds no stock on site. | Prescribes only (by video) |
| **Clinic owner (business)** | Runs the business: money, reports, settings, audit. By default **non-clinical** — they only do clinical work if they personally hold the qualification. | Only if they hold the credential |

> **Why this matters:** in cosmetic injecting, "who is allowed to do what" is not just clinic
> policy — it's the law. The system enforces these limits automatically so a mistake can't happen by
> accident. You'll see this theme — *the safe path is the only path* — throughout.

---

## The glossary (every term, explained once)

Keep this open as you read. If a word in a later chapter is unfamiliar, it's almost certainly here.

### The medicines & the rules

- **Injectable / cosmetic injectable** — a treatment given by needle, e.g. anti-wrinkle injections
  or dermal fillers.
- **S4 / Schedule 4 / "prescription-only medicine"** — a class of medicine that, by law, can only be
  given on a prescription (anti-wrinkle injections are S4). Most of the clinic's strict rules exist
  *because* these are S4 medicines. **Non-S4** simply means everything that isn't — skincare, facials,
  retail products.
- **AHPRA** — the national body that registers health practitioners (nurses, doctors) and sets the
  rules they must follow. Losing or lapsing AHPRA registration means you can't legally practise.
- **TGA** — the government agency that regulates medicines and medical devices in Australia (approvals,
  safety, advertising). The advertising rules you'll see come from the TGA and AHPRA.
- **ARTG** — the official register of medicines/devices the TGA has approved for use in Australia. A
  product being "on the ARTG" means it's legally approved; the system records this for every medicine.
- **Off-label** — using an approved medicine for a purpose it wasn't officially approved for (common
  and legal in cosmetics, but it must be flagged and consented to).
- **Batch / lot** — a manufacturing batch of a medicine, identified by a number on the box/vial. If a
  batch is ever recalled, you must be able to find exactly which patients received it.
- **Vial** — the small bottle a medicine comes in. One vial may treat several patients, so the system
  tracks how many units were drawn from each vial (**vial reconciliation**) to make sure stock,
  billing and the medicine register all agree.
- **Cold-chain / cool-chain** — keeping a medicine within its required temperature range (anti-wrinkle
  toxin must stay at **2–8°C**) from delivery to use. A temperature breach can ruin the medicine.
- **Custody** — being the legally-responsible holder of the medicine stock. In our first version,
  only an on-site prescriber may hold S4 stock.
- **Recall** *(of a medicine)* — when a manufacturer/authority flags a batch as unsafe and it must be
  traced and pulled. *(Not to be confused with patient "recall" below.)*

### The clinical journey

- **Consult / consultation (synchronous)** — a real-time assessment of the patient (in person or by
  video) *before* any prescription. "Synchronous" just means live/real-time — not a form or a text.
- **Prescription (individual)** — an authorisation, written for **one named patient after their
  consult**, for a specific medicine and dose. The law forbids "batch" or "standing-order"
  prescriptions (one script covering many patients) for these treatments.
- **Intake** — the pre-visit questionnaire: medical history, medications, allergies, things that would
  make a treatment unsafe.
- **Consent** — the patient's informed, signed agreement to a treatment after being told the risks,
  benefits, alternatives, costs and who's treating them.
- **BDD screen** — a short questionnaire that screens for **Body Dysmorphic Disorder**, a mental-health
  condition where someone is preoccupied with perceived flaws. Cosmetic guidelines require screening
  for it, because treatment can do harm rather than good for these patients.
- **Cooling-off period** — a required wait between consent and treatment so the patient isn't rushed.
  Mandatory (7 days) for **under-18s**; for adults it's an optional clinic policy, not a legal rule.
- **Charting** — the clinical record of what was done: for injectables, a **map** of where each
  injection went, how much, how deep, and from which batch.
- **Modality** — the *type* of treatment (anti-wrinkle toxin, filler, skin, laser, weight-loss). Each
  type has its own rules, so the system adapts the record to match.
- **Adverse event / complication** — an unwanted reaction or harm. Two serious ones you'll see named:
  **vascular occlusion (VO)** — a blocked blood vessel, a filler emergency — and **anaphylaxis** — a
  severe allergic reaction. **Hyaluronidase** is the emergency medicine used to reverse filler.
- **DAEN** — the TGA's database for reporting adverse events. The system helps fill in and lodge these.

### Money & growth

- **POS (point of sale)** — the checkout / till.
- **Card-on-file** — securely storing a patient's card so recurring charges (e.g. a membership) can
  run automatically. **Autopay** is the automatic recurring charge itself.
- **Dunning** — the polite retry-and-remind process when an automatic payment fails.
- **Package / series** — pre-paid bundle of visits ("buy a course of 3"), redeemed over time.
- **Membership** — a recurring paid plan (monthly/annual) that gives members perks.
- **MRR** — *Monthly Recurring Revenue*: the predictable income from memberships each month.
- **Churn** — the rate at which members/clients leave or stop coming back.
- **Recall / recare** *(of a patient)* — a friendly nudge to re-book when a treatment is due again
  (anti-wrinkle ~every 12 weeks). *(Different from a medicine recall above.)*
- **No-show** — a booked patient who doesn't turn up. **Waitlist** — clients who want an earlier slot
  if one frees up.
- **Lead / prospect** — an enquiry who hasn't booked yet; tracking them is "lead CRM".

### The team & the back office

- **Scope of practice** — the set of things a given role is trained and legally allowed to do.
- **CPD** — *Continuing Professional Development*: the ongoing training hours practitioners must log
  each year to keep their registration.
- **Indemnity / PII** — *Professional Indemnity Insurance*, the cover a practitioner must hold; for
  cosmetic work it must specifically **cover cosmetic procedures**.
- **Xero** — the popular accounting software. The clinic's "books" (payroll, tax, supplier bills) live
  there; this system sends sales/payment data across rather than rebuilding accounting.
- **GST / BAS** — the goods-and-services tax and the business activity statement lodged for it.

### Privacy, safety & "the plumbing"

- **Privacy Act / APPs** — Australia's privacy law and its *Australian Privacy Principles*. They give
  patients rights over their data (to see it, correct it) and limit what the clinic can do with it.
- **DSAR** — a *Data Subject Access Request*: when someone formally asks to see or correct the
  personal information you hold about them. There's a legal clock (≤30 days) to respond.
- **Data breach / NDB / OAIC** — if personal data is exposed, the **Notifiable Data Breaches** scheme
  may require telling the affected people and the regulator (**OAIC**).
- **Spam Act** — the law requiring marketing messages to be opt-in, identify the sender, and include a
  working unsubscribe.
- **Audit log / audit trail** — an automatic, tamper-resistant record of *who did or saw what, and
  when*. Essential if AHPRA or QLD Health ever inspect the clinic.
- **Data residency** — *where* the data is physically stored. Patient data here stays on Australian
  servers (Sydney).
- **Immutable** — "can't be secretly edited". Once a clinical note is finalised it's locked; any change
  is added as a visible, dated amendment — never a silent overwrite.
- **Sign-in terms** — **SSO** (sign in with your existing Microsoft 365 work account),
  **MFA** (a second check, e.g. a code on your phone), **OTP** (a one-time code sent by SMS/email).

---

## The big picture in one paragraph

A patient **books** (Chapter 1), fills in **intake & consent** ahead of time (Chapter 2), has a
**consult** with a prescriber who writes an **individual prescription** (Chapter 2), is **treated and
charted** by a nurse who draws from a specific, in-date, properly-stored **batch of medicine**
(Chapters 2–3), **pays** at the desk and maybe **joins a membership** (Chapter 4) — all performed only
by staff the system has confirmed are **cleared to treat** (Chapter 5), with every step quietly
building the **safety, privacy and compliance record** the clinic would need in an inspection
(Chapter 6), while **reminders, reviews and re-booking** keep clients coming back within the
**advertising rules** (Chapter 7). The promise running through all of it: **the compliant, safe way of
doing something is the easy, default way — and the unsafe way is simply blocked.**

> Ready? Start with **[Chapter 1 — Front desk & daily operations](01-front-desk-and-operations.md)**.
