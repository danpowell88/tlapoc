# CLAUDE.md — The Lounge Aesthetics POC

A self-contained static site, published to GitHub Pages at
https://danpowell88.github.io/tlapoc/ (repo: `danpowell88/tlapoc`).

## Structure
- `index.html` — landing page.
- `prototype.html` — the interactive clinic-platform prototype (single file; all data is synthetic and inlined — no data files, no network calls for data).
- `docs.html` — documentation viewer (renders `docs/*.md` via marked.js).
- `docs/` — market research, requirements & compliance, ADRs, the 11 PRDs, and UX flows.
- `.github/workflows/pages.yml` — deploys to GitHub Pages via Actions on every push to `main`.

## Working agreement
- **After each batch of work, commit and push to `main`.** The Pages Action redeploys the site automatically — keep the published site current.
- Verify changes in a local preview (`python -m http.server`) before pushing.
- All data is **synthetic**. Never add real client, staff, or business information.
- **Financials are owner-only.** Revenue, MRR, and pricing figures must stay gated behind the `.fin` capability (the `applyFin()` toggle); non-owner roles such as Reception may see memberships but no money figures.
