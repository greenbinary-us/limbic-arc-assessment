# CEO Briefing — Presentation Package

A non-technical, CEO-facing presentation derived from *Technical Assessment (v0.4)*.
**Scope of this deck:** pure assessment — findings, risk, roadmap, and a neutral staffing
choice. No partner/vendor positioning.

## What's here

| File | What it is |
|------|------------|
| `Limbic Arc - CEO Briefing (v0.1).pptx` | **Editable starter deck** — 17 widescreen slides, all diagrams embedded. Open and re-theme to brand. |
| `Limbic Arc - CEO Briefing Deck (v0.1).md` | **Slide-by-slide script** — per slide: on-slide text, which image to use, and speaker notes (talk track). |
| `images/*.png` | The 8 diagrams, 16:9 at 2560×1440 — drop straight onto a widescreen slide. |
| `_build/` | Sources to regenerate everything (kept for editing). |

## Slide map (17 slides)

1. Title · 2. The bottom line · 3. What we looked at · **4. How it works today** ·
5. The five things that matter · **6. #1 risk: one card, two places** ·
**7. The fix: one home for cards** · 8. You don't control your own speed ·
**9. Three websites, three logins** · 10. The missing basics ·
11. Root cause: no in-house team · **12. What "good" looks like** ·
**13. Who owns what** · **14. The recommended path** · **15. How to resource it** ·
16. What we'd need from leadership · 17. Closing
*(bold = slide carries a diagram)*

## Regenerating

Requires: Google Chrome (diagrams) and Python with `python-pptx` (deck).

```bash
# 1. Re-render one diagram after editing its HTML in _build/
bash _build/render.sh current-state 1280 720
#    (three-experiences uses 1280 760)

# 2. Rebuild the .pptx from the images
python _build/build_pptx.py
```

Diagrams are plain HTML/CSS (`_build/*.html` + `_build/style.css`) rendered to PNG with
headless Chrome. The deck is assembled by `_build/build_pptx.py`. Palette and fonts are
shared so native slides and diagrams match.

## Notes / to confirm

A few specifics are marked **[to confirm]** in the script (current card-handling & PCI
setup, the Exigo/Fluid subscription split, Fluid's API surface, and the exact Web App
boundary) — confirm with the teams/vendors before presenting as settled.
