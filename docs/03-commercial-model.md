# Commercial Model — Pricing, QLD Market Size, Revenue & Operating Costs

> **Goal:** turn the [market research](01-market-research.md) and [locked requirements](02-requirements.md)
> into a business view — *what competitors charge*, *what we should charge*, *how many Queensland
> clinics could buy*, *what revenue/income that implies*, and *what it costs us to run the platform*.
>
> **Context:** the platform is **internal-first but SaaS-ready** (multi-tenant + RLS from day one;
> see [requirements §2](02-requirements.md) and the Phase-3 *SaaS commercialization* line). This doc
> sizes that Phase-3 opportunity **for Queensland first**, then notes the national upside.
>
> _Compiled 2026-06-20. **All figures are indicative planning estimates, not quotes or forecasts.**
> FX assumption: **1 USD ≈ A$1.55** (mid-2026). Competitor SaaS is mostly priced in USD; AUD shown
> is converted and rounded. **Prices are ex-GST.** This is a strategy document — it does not change
> the rule that the prototype's synthetic clinic revenue/MRR stays owner-gated behind `.fin`._

---

## 1. What clinics pay today — the competitor pricing landscape

Pulled from the [§2 platform deep-dives](01-market-research.md) and refreshed June 2026. Three camps,
three very different price points and billing models.

### Horizontal booking / POS (salon-grade, no AU clinical/compliance layer)

| Platform | Headline price (USD unless noted) | ≈ AUD/mo | Model | Notes |
|---|---|---|---|---|
| **Mindbody** *(incumbent we replace)* | Starter ~$129 → Ultimate $599 **per location** + $50–150/add-on | ~$200–930 +add-ons | Tiered, quote-based, marketplace commissions | "Falls short for medical/aesthetic"; opaque, climbing prices |
| **Boulevard** | Essentials $176 → **Aesthetics bundle $421** | ~$273–$653 | Tiered + EMV POS | Closest US "modern UX + charting" blend |
| **Mangomint** | $165 / $245 / $375 | ~$256 / $380 / $581 | Tiered; Forms & Charting +$50 | Best-rated UX; charting is an add-on |
| **Timely** *(ANZ)* | $11–$28 **per staff**; Independent **A$19.95** solo | ~$17–$43/staff | Per-bookable-staff, no commission | Salon-focused, not medical |
| **Fresha** | $0 subscription | $0 + fees | Takes payment % + new-client fees | No clinical charting |
| **Zenoti** | Custom / enterprise | $$$ | Quote-only | Overkill for single-site |

### Aesthetic / medical-EMR specialists (clinical depth, US/HIPAA-framed)

| Platform | Headline price (USD) | ≈ AUD | Model | Notes |
|---|---|---|---|---|
| **Pabau** *(now owns Aesthetic Record)* | from **$62/user/mo** | from ~$96/user | Per-user, full platform | Feature-complete blueprint; AU-used |
| **Aesthetic Record** | $12–$19/user/mo **+ $199–399 setup** | ~$19–$29/user +$308–618 | Per-user + setup | ⚠ reported **$1,120 (~A$1,736) fee to export your own data** after 2 yrs |
| **AestheticsPro** | $150 → $275 | ~$233–$426 | Tiered | Transparent; fewer integrations |
| **Symplast** | ~$299/provider | ~$463/provider | Per-provider | Surgery-oriented |
| **Nextech / Moxie** | Custom / bundled-services | $$$ | Quote / managed-service | MD-led / coaching-bundled |

### AU practice-management & the one direct AU competitor

| Platform | Price (AUD) | Model | Notes |
|---|---|---|---|
| **Cliniko** | **$45 / $95 / $145 / $195 / $295 / $395** by practitioner band; SMS 10¢ | Flat practitioner-band; all features included | AU-made, unbeatable value — **but no injection mapping / S4 governance / aesthetic consent** |
| **Power Diary (Zanda)** | from ~$19 | Tiered by appts/practitioners | AU allied-health PM; not aesthetic |
| **Halaxy** | Free tier + per-transaction billing fees | Freemium + transaction | Native Medicare/claiming; not aesthetic |
| **Fresh Clinics** *(closest AU rival)* | **Quote-only**, bundles **on-demand telehealth prescriber + EMR + drugbook + product supply** | Service + software | The AU compliance-aware competitor — but it sells *prescriber access as a service*, and the **QLD S4 custody clarification undercuts its remote-prescriber model** ([§4.2](01-market-research.md)) |

**Read-across:**
- **Spread is enormous** — A$0 (Fresha) to A$650+/clinic/mo (Boulevard Aesthetics), or A$460+/provider (Symplast).
- **AU tools are cheap but clinically empty;** US aesthetic tools are deep but US-framed and pricier; **nobody bundles QLD S4 + AHPRA-2025 compliance.** That gap is the pricing power.
- **Switching-cost traps** (AR's data-export fee, Mindbody's opaque add-ons) are a wedge: *free migration + free data export* is a cheap, high-impact promise.

---

## 2. Where we price — positioning

The wedge from [market research §5](01-market-research.md) is **modern UX + aesthetic clinical depth +
native AU/QLD compliance**, which no incumbent combines. So we price:

- **Above** commodity AU PM (Cliniko's $45–$395) — we do far more than scheduling.
- **At or just below** US aesthetic specialists (Boulevard Aesthetics ≈ A$650, Mangomint top ≈ A$580,
  Pabau ≈ A$96/user) — close enough to look premium, cheap enough to win on TCO.
- **On value, not seats-tax** — Cliniko's "all features included, banded by practitioner" model is
  loved in AU; we mirror it and refuse to gate *compliance* behind a higher tier (compliance **is**
  the product).

**Willingness-to-pay is unusually high right now in QLD:** the April-2025 S4 custody clarification put
~560 nurse-led clinics into compliance crisis ([§4.2](01-market-research.md)). A tool that makes the
compliant path the default is a painkiller, not a vitamin.

---

## 3. Recommended pricing structure

**Model:** per-location **base** + **practitioner bands** (familiar from Cliniko), full platform included,
**usage costs passed through** (SMS/email), **card processing stays on the clinic's own Square account**
(we never take a payment margin — avoids becoming a money-services business and keeps us cheaper than
Fresha/Mindbody on effective rate).

| Tier | Who | Practitioners | **AUD/mo (monthly)** | **AUD/mo (annual, ~2 mths free)** |
|---|---|---|---|---|
| **Solo Injector** | Single nurse-led / solo clinic | 1 | **$149** | **$125** |
| **Clinic** *(most common)* | Standard nurse-led clinic | 2–5 | **$329** | **$275** |
| **Group** | Larger / busy multi-injector | 6–15 | **$599** | **$499** |
| **Multi-location / Enterprise** | Clinic groups | 16+ | from **$599 + $99/extra location** | custom |

**Included in every tier (no upsell on compliance):** S4 medicines governance & custody ledger,
AHPRA-2025 consult-gating, injection mapping + before/after, consent versioning, client + provider
Flutter apps, memberships/autopay, recall, Xero + calendar integration, compliance dashboards & audit
exports, **free onboarding + free data export** (the anti-AR promise).

**Pass-through / add-ons:**
- **SMS** sold in bundles at ~**8¢/msg** (cost ≈ 5–8¢ — see §6) or clinic brings its own provider.
- **Optional white-glove migration** from Mindbody/AR — *free* as an acquisition lever.
- Future (Phase 2+): retail-inventory module, advanced campaigns/referrals, online checkout.

**Blended ARPU target ≈ A$300–350/clinic/mo** (most clinics land in the 2–5 band). This sits **below**
Boulevard Aesthetics and Mangomint-top, **above** Cliniko's mid bands — defensible because we carry the
compliance + clinical load they don't.

---

## 4. Queensland market size (TAM / SAM / SOM)

**Clinic universe.** Hard counts are scarce, so triangulate:
- **~560 nurse-led cosmetic clinics in QLD** (May 2025), employing **800–900 cosmetic nurses** — the
  figure cited throughout the S4 debate.
- One wholesaler/telehealth prescriber alone services **≥100 QLD clinics** (subset of its ~450 AU clients).
- Add doctor/NP-led clinics, dermatology, plastic-surgery, GP-cosmetic and medspa sites that also inject.
- → **Estimated QLD injectable-clinic universe ≈ 700–900.** Use **~800** as the planning anchor.

> ⚠ **Regulatory consolidation is a two-way sensitivity.** The S4 clarification may *shrink* clinic
> count (some nurse-led closures/mergers) — but it *sharpens* the pain for survivors, lifting
> willingness-to-pay for a compliance-native tool. Net effect on our ARR is plausibly positive.

| Layer | Definition | Clinics | × ARPU (A$325/mo) | **Annual value** |
|---|---|---:|---:|---:|
| **TAM** | All QLD clinics doing injectables | ~800 | × $3,900/yr | **≈ A$3.1M ARR** |
| **SAM** | Compliance-native fit — nurse-led + multi-injector who feel the S4 pain; exclude dormant/tiny & locked-in enterprise | ~480 (≈60%) | × $3,900/yr | **≈ A$1.9M ARR** |
| **SOM (3-yr)** | Realistic capture by a lean solo build via word-of-mouth in a tight nurse community | see §5 | | **≈ A$0.45M ARR by Yr3** |

**National upside (later phases):** ~**2,500 cosmetic/aesthetic clinics across AU/NZ** → roughly **10×**
the QLD TAM. QLD is the beachhead precisely because its regulation is the strictest and our
compliance moat is sharpest there.

---

## 5. Revenue & income projection (QLD, 3-year base case)

Assumes the §3 pricing, blended **ARPU A$325/mo (~A$3,900/yr)**, and steady SOM capture of the ~480-clinic SAM.

| | **Yr 1** | **Yr 2** | **Yr 3** |
|---|---:|---:|---:|
| Paying clinics (end of year) | ~25 (3% of SAM) | ~65 (8%) | ~115 (14%) |
| Avg active clinics in year | ~15 | ~45 | ~90 |
| **Revenue (ARR run-rate, EOY)** | **~A$98k** | **~A$254k** | **~A$449k** |
| Recognised revenue (in-year) | ~A$59k | ~A$176k | ~A$351k |
| COGS — infra + comms (§6, ~10%) | ~A$6k | ~A$18k | ~A$35k |
| **Gross profit** | **~A$53k** | **~A$158k** | **~A$316k** |
| Gross margin | ~90% | ~90% | ~90% |
| Cash opex (tools, fees, light support) | ~A$10–20k | ~A$20–35k | ~A$40–70k |
| **Operating income** *(excl. founder salary)* | **~A$35–43k** | **~A$120–138k** | **~A$245–275k** |

**Scenario range (Yr-3 ARR run-rate):**

| Scenario | Yr-3 clinics | Yr-3 ARR | Driver |
|---|---:|---:|---|
| Conservative | ~70 (8% SAM) | ~A$270k | slower trust-building; some consolidation churn |
| **Base** | **~115 (14%)** | **~A$449k** | word-of-mouth in nurse community |
| Upside | ~180 (incl. early interstate) | ~A$700k+ | QLD reference clinics pull NSW/VIC enquiries |

> **"Income" framing:** software gross margins are ~90% because marginal cost per tenant is tiny (§6).
> The real cost is **founder time**, not cash. If a market salary for the owner is imputed, Yr-1 is
> ~break-even-to-modest; the model turns strongly positive in Yr 2–3 as fixed effort amortises across
> tenants. CAC is low (no paid sales team; community + referral led), which is what makes a lean solo
> build viable here.

---

## 6. Operating costs — what it costs to run ("the site")

Three cost layers, lowest to highest.

### (a) The POC / demo site today
The current static site is **GitHub Pages + GitHub Actions** → **A$0/mo** hosting; only a custom domain
(~**A$20/yr**) is optional. Nothing below applies until the real platform ships.

### (b) Single-clinic production (The Lounge, internal use)
Azure-native stack from [requirements §7](02-requirements.md), sized for one busy clinic. Monthly, AUD,
Australia East:

| Component | Service / SKU | ≈ AUD/mo |
|---|---|---:|
| Database | PostgreSQL Flexible **Burstable B1ms** (1 vCore/2 GiB) + ~32 GB storage | ~$28 |
| API / jobs | **Container Apps** (consumption, scale-to-zero; mostly within free grant) + Functions | ~$15–30 |
| Web | **Static Web Apps** (Free tier ok; Standard if custom auth) | $0–14 |
| Media | **Blob storage** (photos; ~50 GB hot + egress) | ~$2–5 |
| Identity | **Entra External ID** — first **50,000 MAU free** | $0 |
| Secrets / monitoring | **Key Vault** + **App Insights** (free tiers) | ~$0–5 |
| Email | **SES** (~A$0.15/1k) or SendGrid Essentials | ~$2–31 |
| Domain / TLS | domain (~A$20/yr) + managed certs (free) | ~$2 |
| **Subtotal (fixed)** | | **≈ A$60–115/mo** |
| SMS (pass-through) | Twilio ~A$0.08/msg / MessageMedia 5.7–8¢ | usage |

→ **≈ A$90–180/mo all-in** for one clinic (with headroom). **Square card-processing fees
(~1.6% card-present, ~2.2% online) are borne by the clinic**, not the platform.

### (c) Multi-tenant SaaS at scale (~100 QLD tenants)
RLS multi-tenancy means tenants **share** infrastructure — cost grows far slower than tenant count:

| Component | At ~100 tenants | ≈ AUD/mo |
|---|---|---:|
| PostgreSQL | scale Burstable → **General Purpose** (2–4 vCore) + storage/backups | ~$250–500 |
| Container Apps / Functions | autoscaled API across tenants | ~$150–350 |
| Blob (photos, all tenants) | ~1–2 TB hot + egress | ~$60–180 |
| Email / monitoring / Key Vault | higher volume | ~$60–120 |
| Entra External ID | likely still <50k MAU; SMS-MFA $0.03/attempt | ~$0–50 |
| **Platform fixed total** | | **≈ A$500–1,200/mo** |

→ **Marginal infra ≈ A$5–12/tenant/mo;** add comms + light support tooling → **~A$15–40/tenant/mo
all-in**, i.e. **~85–92% gross margin** at the §3 pricing. This is why COGS is held at ~10% in §5.

**One-off build cost:** a **lean solo + Claude Code** build ([requirements §2](02-requirements.md)) means
near-zero external cash for development — the investment is **founder time**, plus modest spend on dev
tooling, an Apple/Google developer account (~A$150/yr for the Flutter apps), and a pre-launch
**compliance/legal review** (budget a few A$k — the highest-value external spend, given the moat is
regulatory).

---

## 7. Internal-first ROI — the bet is cheap even with zero customers

Before a single external sale, the build **pays for itself by replacing Mindbody** at The Lounge:

- **Mindbody medspa** runs ~A$200–930/location + add-ons; realistic all-in ≈ **A$250–900+/mo**.
- Our **run-cost ≈ A$90–180/mo** (§6b) → **net saving ~A$100–700+/mo**, *plus* a compliance posture
  Mindbody can't give a QLD injectable clinic.

So even if QLD SaaS capture lands at the conservative end, the project is **self-funding** through
internal use — the external revenue in §5 is upside on an already-positive internal ROI. That asymmetry
(low downside, 10×-national upside) is the core commercial argument.

---

## 8. Key assumptions, risks & sensitivities

| Factor | Assumption | Risk / sensitivity |
|---|---|---|
| **FX** | 1 USD ≈ A$1.55 | competitor AUD-equivalents move with the rate; our costs are mostly AUD |
| **Clinic universe** | ~800 QLD injectable clinics | regulatory consolidation could cut count — but raises per-clinic willingness-to-pay |
| **ARPU** | A$325/mo blended | downward pressure from Cliniko-anchored expectations; protected by the compliance moat |
| **Capture** | 3% → 14% of SAM over 3 yrs | trust-led; a few flagship reference clinics are the unlock |
| **Churn** | low (compliance lock-in + data gravity) | a clinic closure ≠ a switch; closures hit revenue regardless |
| **Competition** | Fresh Clinics is the AU incumbent | but its remote-prescriber model is the very thing QLD S4 undercut — our on-site/designated-RN model is better-aligned |
| **CAC** | community + referral, ~A$0 paid | scaling interstate later needs real go-to-market spend (modelled only as upside) |
| **Regulatory drift** | AHPRA/TGA/QLD settling 2025→late-2026 | both a risk (rework) and the moat's source — keep the medicines module configurable |

---

## Sources

**QLD clinic counts & regulatory impact**
- [Australian College of Nursing — Cosmetic nurse injectors in Queensland](https://www.acn.edu.au/nurseclick/cosmetic-nurse-injectors-in-queensland)
- [Change.org — Protect Nurse-Led Cosmetic Clinics in Queensland (clinic/nurse counts)](https://www.change.org/p/protect-nurse-led-cosmetic-clinics-in-queensland)
- [Medical Republic — Patients or consumers? Queensland's cosmetic injectables industry trials](https://www.medicalrepublic.com.au/patients-or-consumers-queenslands-cosmetic-injectables-industry-trials/116621)
- [Aesthetic Medical Practitioner — S4 cosmetic injectables confusion (buying & storage)](https://aestheticmedicalpractitioner.com.au/features/cosmetic-practice/s4-cosmetic-injectables-confusion-re-buying-and-storage/)
- [Queensland Health — Medicines in beauty treatment/cosmetic businesses (fact sheet PDF)](https://www.health.qld.gov.au/__data/assets/pdf_file/0038/1393994/fs-cosmetic-injectables.pdf)

**AU market size**
- [IMARC — Australia Medical Aesthetics Market (USD 396.4M in 2025 → 784.8M by 2034)](https://www.imarcgroup.com/australia-medical-aesthetics-market)
- [Grand View Research — Australia Facial Injectables Market](https://www.grandviewresearch.com/industry-analysis/australia-facial-injectables-market-report)
- [Mordor Intelligence — Australia Aesthetic Devices Market](https://www.mordorintelligence.com/industry-reports/australia-aesthetic-devices-market)

**Competitor pricing**
- [Cliniko pricing](https://www.cliniko.com/pricing/) · [Capterra AU — Cliniko cost](https://www.capterra.com.au/software/180878/cliniko)
- [Zanda Health (formerly Power Diary)](https://www.zandahealth.com/) · [Halaxy](https://www.halaxy.com/)
- [Pabau pricing](https://pabau.com/pricing/) · [Pabau — Aesthetic Record pricing](https://pabau.com/blog/aesthetic-record-pricing) · [Capterra — Aesthetic Record pricing](https://www.capterra.com/p/162938/Aesthetic-Record/pricing/)
- [Pabau — Mindbody pricing breakdown](https://pabau.com/blog/mindbody-pricing/) · [The Salon Business — Mindbody review](https://thesalonbusiness.com/mindbody-software-review/)
- [Capterra — Timely pricing](https://www.capterra.com/p/142756/Timely/)
- [Fresh Clinics — cosmetic clinic management (AU)](https://www.freshclinics.com/en-au/cosmetic-clinic-management)

**Operating-cost inputs**
- [Azure Database for PostgreSQL Flexible Server — pricing](https://azure.microsoft.com/en-us/pricing/details/postgresql/flexible-server/) · [compute SKUs (B1ms/B2s)](https://learn.microsoft.com/en-AU/azure/postgresql/flexible-server/concepts-compute-storage)
- [Azure Container Apps — pricing (AU)](https://azure.microsoft.com/en-au/pricing/details/container-apps/) · [billing model](https://learn.microsoft.com/en-us/azure/container-apps/billing)
- [Microsoft Entra External ID — pricing (first 50k MAU free)](https://learn.microsoft.com/en-us/entra/external-id/external-identities-pricing)
- [Twilio — SMS pricing Australia](https://www.twilio.com/en-us/sms/pricing/au) · [Sinch MessageMedia — pricing (AU)](https://messagemedia.com/au/pricing/)
- [Twilio SendGrid — Email API pricing](https://www.twilio.com/en-us/products/email-api/pricing)
