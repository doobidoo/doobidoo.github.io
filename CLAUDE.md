# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static HTML/CSS/JS portfolio website for Henry Krupp, deployed via GitHub Pages at `doobidoo.github.io`. No build system, no bundler, no SSG — just a single `index.html` served directly.

## Tech Stack

- **HTML5** single-page application (`index.html`, ~960 lines)
- **Tailwind CSS** via CDN (`cdn.tailwindcss.com`) — not installed locally
- **Font Awesome 6.4.0** via CDN
- **Google Fonts** (Poppins) via CSS `@import`
- **Vanilla JavaScript** — no frameworks, no transpilation
- **Formspree** for contact form submission (`https://formspree.io/f/mrebnwpj`)

## Development

There is no build step. To develop locally:

```bash
# Any static file server works
python3 -m http.server 8000
# Then open http://localhost:8000
```

## Deployment

Push to `main` branch — GitHub Pages serves from root automatically. No CI/CD pipeline.

## Architecture

Everything lives in `index.html`:

- **Lines 1-100**: `<head>`, CDN imports, `<style>` block with custom CSS (gradient-text, card-hover, nav animations, skill-bar, timeline)
- **Lines ~100-200**: Navigation (fixed header, mobile hamburger menu)
- **Lines ~200-350**: Hero section with CTA buttons and profile image (loaded from GitHub avatar)
- **Lines ~350-500**: About section, Skills section (categorized: Cloud/DevOps, Mobile, AI/Memory, Enterprise, Programming)
- **Lines ~500-750**: Projects section (featured cards), Experience section (timeline layout)
- **Lines ~750-900**: Contact form (Formspree integration with async fetch, status messages, form reset)
- **Lines ~900-960**: Footer, JavaScript (scroll behavior, mobile menu toggle, form submission handler, scroll-to-top, intersection observer animations)

### Key CSS Classes

| Class | Purpose |
|-------|---------|
| `.gradient-text` | Blue-to-purple gradient text (brand color) |
| `.card-hover` | Lift + blue shadow on hover for project cards |
| `.nav-link::after` | Animated underline on nav hover |
| `.skill-bar` | Animated progress bars in skills section |
| `.timeline-item` | Left-bordered experience entries |

### Color Scheme

- Background: `#0f172a` (slate-900)
- Text: `#f8fafc` (slate-50)
- Primary gradient: `#3b82f6` (blue-500) → `#8b5cf6` (violet-500)
- Card backgrounds: `bg-slate-800/50` with `border-slate-700`

## Supporting Files

- `Github Profile Updates/` — Architecture Decision Records (ADR-001 through ADR-004) documenting enterprise solutions
- `github-profile-README-optimized.md` — Optimized GitHub profile README
- `index.bak` — Backup of previous site version

## Conventions

- Commit messages use conventional format: `feat:`, `fix:`, `docs:`, etc.
- All styling uses Tailwind utility classes inline; custom CSS only for effects not available in Tailwind CDN
- No external JS dependencies — keep it vanilla
- Profile image sourced from GitHub avatar URL, not a local file
