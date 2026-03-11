# Troop & Crew 537 — Website Editor Guide

This is the source code for the Troop 537 website, hosted on GitHub Pages at
**https://troop537web.github.io/troop537web/** (or your custom domain).

All pages are plain HTML files. You do not need any special software — a basic text editor works.
The sections below walk through the most common editing tasks.

---

## File Overview

```
docs/
├── index.html          Home page
├── about.html          About Troop 537
├── crew.html           Crew 537 (Venturing)
├── recent-events.html  Recent Events (most frequently updated)
├── calendar.html       Calendar (Google Calendar embed — auto-updates)
├── photos.html         Photo gallery
├── parents.html        Parents page
├── resources.html      Resources & links
├── contact.html        Contact form (see Formspree section below)
├── style.css           All visual styles
├── includes/
│   └── site.js         Shared header, navigation bar, and footer
└── images/
    ├── Events/         Photos used on the Recent Events page
    ├── Photos/         Photos used on the Photos page
    └── (shared images used across multiple pages)
```

---

## Adding a New Event (most common task)

1. Copy the new event photo(s) into `docs/images/Events/`.
2. Open `docs/recent-events.html` in a text editor.
3. Find the comment block near the top of the file that reads:
   ```
   <!-- TO ADD A NEW EVENT: Copy one block below, paste it at the top ... -->
   ```
4. Copy an existing event block (from `<h2>` down to the closing `</div>` of the photo gallery).
5. Paste it **above** all other events (just below that comment).
6. Update the title, date, description, and image filename(s).

**Example event block:**
```html
<h2><a href="#">Your Event Title</a></h2>
<p class="post-meta">Posted on Month DD, YYYY by Webmaster</p>
<p>Description of the event goes here.</p>
<div class="photo-gallery">
  <img src="images/Events/your-photo-filename.jpg" alt="">
</div>
```

To show **multiple photos** for one event, add more `<img>` lines inside the same `<div class="photo-gallery">`.

---

## Adding Photos to the Photo Gallery

1. Copy the photo into `docs/images/Photos/`.
2. Open `docs/photos.html`.
3. Find the `<div class="photo-gallery">` section.
4. Add a new `<img>` line:
   ```html
   <img src="images/Photos/your-photo-filename.jpg" alt="Brief description">
   ```

---

## Updating Page Content

Each page contains only its own unique content. Open the relevant `.html` file and look for
text between `<p>` and `</p>` tags (paragraphs), `<h1>` / `<h2>` (headings), or `<li>` (list items).
Edit the text directly.

**Do not edit** these lines near the top/bottom of every page — they load the shared elements:
```html
<div id="page-header-placeholder"></div>
<div id="main-navigation-placeholder"></div>
...
<div id="footer-placeholder"></div>
<script src="includes/site.js"></script>
```

---

## Editing the Header, Navigation, or Footer

The site header (logo + troop name), navigation bar, and footer are **shared across all pages**.
They are defined in one place: **`docs/includes/site.js`**.

### To rename a navigation item or change its link:
Find the `NAV_ITEMS` list in `site.js` and edit the relevant line:
```javascript
var NAV_ITEMS = [
  ['index.html',        'Home'],
  ['about.html',        'About Troop 537'],
  // ... etc.
];
```
Format: `['filename.html', 'Label shown in nav']`

### To add a new page to the nav:
1. Create the new `.html` file (copy any existing page as a starting template).
2. Add a new line to `NAV_ITEMS` in `site.js`:
   ```javascript
   ['new-page.html', 'New Page Label'],
   ```

### To update the footer text (e.g., the copyright year):
Find the `FOOTER` variable in `site.js` and edit the `<p>` line:
```javascript
var FOOTER = `
<div id="footer">
  <div id="footer-inner">
    <p>&copy; 2026 Troop and Crew 537 - Greater Colorado Council - ...</p>
  </div>
</div>`;
```

---

## Contact Form (Formspree)

The contact form on `contact.html` uses **Formspree** to receive form submissions by email
without exposing any email address publicly.

**To view or change where submissions are sent:**
1. Go to [https://formspree.io](https://formspree.io) and log in with the troop's Formspree account credentials.
   *(Credentials are held by the site developer / troop leadership — do not store them here.)*
2. Select the form named for this site.
3. From there you can: change the recipient email address, view submission history, and adjust
   spam-filtering settings.

**To edit the form fields** (labels, add/remove fields):
Open `docs/contact.html` and edit inside the `<form>` block. Each field follows this pattern:
```html
<div class="field-row">
  <label>Field Label *</label>
  <input type="text" name="field_name" required>
</div>
```
The `name="..."` attribute determines what label appears in the emailed submission.
If you add a new field, give it a clear `name` value (e.g., `name="phone_number"`).

**Do not change** the `action="https://formspree.io/f/xyknkqdd"` attribute on the `<form>` tag
unless you are intentionally switching to a different form endpoint in Formspree.

---

## Adding or Replacing Images

1. Place the image file in the appropriate folder under `docs/images/`:
   - `images/Events/` — for images that appear on the Recent Events page
   - `images/Photos/` — for images that appear on the Photos page
   - `images/` — for images used anywhere else (home page, About page, etc.)
2. Reference it in the HTML as: `src="images/Events/filename.jpg"` (adjust subfolder as needed).

Recommended image sizes:
- Event/gallery photos: resize to ~1024px wide before uploading to keep the site fast.
- Sidebar/widget images: 300px wide is sufficient.

---

## Publishing Changes (GitHub)

The site is hosted on GitHub Pages. Changes go live automatically after they are pushed to the
`main` branch of the repository. Typically this is done with Git:

```bash
git add .
git commit -m "Brief description of what changed"
git push
```

After pushing, the live site updates within about a minute.

---

## Getting Help

If you're unsure about an edit, the safest approach is to:
1. Make a copy of the file before editing it.
2. Make your change.
3. Open the file in a web browser (File → Open) to preview it before publishing.
