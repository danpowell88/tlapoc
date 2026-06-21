# The Lounge Aesthetics — Clinic Platform POC

A concept prototype for a purpose-built practice-management platform for aesthetic
injectable & cosmetic clinics — a clinical/compliance-first alternative to general
booking software.

- **[`index.html`](index.html)** — landing page.
- **[`prototype.html`](prototype.html)** — the interactive "Clinical Calm"
  prototype (dashboard, booking, client 360, charting with injection mapping &
  before/after, stock & medicines, checkout, memberships, marketing inbox,
  scheduling, reporting; with a role/persona switcher).
- **[`docs.html`](docs.html)** — documentation browser (renders the markdown in `docs/`).
- **`docs/`** — market research, requirements & compliance, ADRs, the 11 PRDs, and UX flows.

> **Sample data only.** Everything in the prototype is **synthetic** — no real client,
> staff or business information.

## Hosting

Static site, deployed to **GitHub Pages via GitHub Actions**
(`.github/workflows/pages.yml`). The prototype and docs use a few CDNs
(Tailwind, Google Fonts, marked.js), so it needs an internet connection to render.

## Running locally

```bash
python -m http.server 8000
# then open http://localhost:8000
```
