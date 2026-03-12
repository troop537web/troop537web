# CLAUDE.md — AI Assistant Guide for Troop 537 Website

## What this project is

A static HTML/CSS website for Boy Scout Troop and Crew 537 in Lakewood, CO.
It is hosted on **GitHub Pages** from the `docs/` folder of this repository.
There is no build step, no framework, no server — just HTML files served directly by GitHub.

Pushing to the `main` branch publishes changes to the live site within ~1 minute.

## File structure

```
docs/                   ← GitHub Pages serves this folder
├── index.html          Home page
├── about.html
├── crew.html
├── recent-events.html  Most frequently updated — new events added here
├── calendar.html       Google Calendar embed (auto-updates, no edits needed)
├── photos.html
├── parents.html
├── resources.html
├── contact.html        Contact form via Formspree (see below)
├── style.css           All styles — single stylesheet for the whole site
├── includes/
│   └── site.js         Shared header, navigation bar, and footer (see below)
└── images/
    ├── Events/         Images used only on recent-events.html
    ├── Photos/         Images used only on photos.html
    └── (other images shared across pages)
```

## The most important architectural decision: `includes/site.js`

Every page's header, navigation bar, and footer are defined **once** in `docs/includes/site.js`
and injected into placeholder divs at page load. This means:

- To add a nav item, edit `NAV_ITEMS` in `site.js` — not all 9 HTML files
- To change the footer text, edit `FOOTER` in `site.js`
- To change the site title or logo, edit `HEADER` in `site.js`

Every HTML page has these three placeholder divs and a script tag — do not remove them:

```html
<div id="page-header-placeholder"></div>
<div id="main-navigation-placeholder"></div>
<!-- ... page content ... -->
<div id="footer-placeholder"></div>
<script src="includes/site.js"></script>
```

`site.js` also auto-highlights the current page in the nav by comparing
`window.location.pathname` to each nav item's filename — no manual `class="current"` needed.

## Layout system

The site uses a float-based 2-column layout:
- `#content` — 66% wide, float left
- `#sidebar` — 28% wide, float right

The homepage (`index.html`) overrides this with a 3-column hero layout using CSS sibling selectors
(`#front-pic + #content` and `#front-pic ~ #sidebar`).

Mobile breakpoint is `max-width: 640px` — at that width everything stacks to a single column
and the sidebar is hidden.

## Design tokens

| Purpose       | Value     |
|---------------|-----------|
| Blue          | `#005A9C` |
| Red           | `#CE1126` |
| Text          | `#252525` |
| Max page width | `990px`  |
| Mobile breakpoint | `640px` |

## Contact form — Formspree

`contact.html` submits to `https://formspree.io/f/xyknkqdd` (the troop's Formspree account).
Formspree emails submissions to the configured recipient without exposing any email address.

To change the recipient email or view submissions, log in at https://formspree.io with the
troop's account credentials (held by site developer / troop leadership).

**Do not change the `action` URL** in `contact.html` unless switching to a new Formspree form.

## Conventions — keep these in mind

- **No build tools.** No npm, no webpack, no preprocessors. Editors update raw HTML files.
- **No inline styles** except where unavoidable. Use `style.css` classes instead.
- **All images must be local.** Place them in `docs/images/` (or the appropriate subfolder)
  and reference them with a relative path. Do not hotlink external images.
- **Adding a new page:** copy an existing page as a template, add it to `NAV_ITEMS` in `site.js`.
- **Adding a new event:** copy an event block in `recent-events.html`, paste at the top,
  update title/date/description/image. Add the image to `docs/images/Events/`.
- **Image sizing:** resize event/gallery photos to ~1024px wide before adding.
- **Publishing:** `git add`, `git commit`, `git push` — GitHub Pages deploys automatically.

## What not to do

- Do not introduce a build step or package manager.
- Do not add JavaScript frameworks or libraries.
- Do not hardcode the header, nav, or footer into individual HTML files — use `site.js`.
- Do not reference images from external URLs.
