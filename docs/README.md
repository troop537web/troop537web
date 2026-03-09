# Troop & Crew 537 — Static Website

Exact content/structure replica of troop537.com as plain HTML files.
Images are hotlinked from troop537.com's WordPress uploads — no images to manage.

## Files
- index.html          Home page
- about.html          About Troop 537
- crew.html           Crew 537 (Venturing)
- recent-events.html  Recent Events (blog posts)
- calendar.html       Calendar + Google Calendar embed
- photos.html         Photo gallery
- parents.html        Parents page
- resources.html      Resources & links
- contact.html        Contact form
- style.css           All styles

## Hosting (free)
Netlify: go to https://app.netlify.com/drop and drag this entire folder.
GitHub Pages: push to a repo, enable Pages in Settings.

## Contact Form
The form currently points to Formspree (free).
1. Go to https://formspree.io → sign up → New Form
2. Copy your form ID (e.g. xabcdefg)
3. In contact.html, replace REPLACE_WITH_YOUR_ID with your ID

## Updating content
All content is plain HTML. Open any .html file in a text editor.
- Add a new Recent Event: copy an <h2>...<div class="photo-gallery"> block in recent-events.html
- Add a photo: add an <img src="..."> tag inside .photo-gallery in photos.html
- Update calendar: the Google Calendar iframe auto-updates from the existing calendar
