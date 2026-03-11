// ============================================================
//  site.js — Shared header, navigation, and footer
//  Edit this file to update those elements across all pages.
// ============================================================

(function () {

  // ── HEADER ──────────────────────────────────────────────
  var HEADER = `
<header id="page-header">
  <div id="fleurdelis">
    <img src="images/Boy-Scout-Logo.png" alt="Scouting America">
  </div>
  <div id="brand">
    <p id="site-tagline">Scouting America<sup>&reg;</sup></p>
    <h1 id="site-name"><a href="index.html">Troop and Crew 537</a></h1>
  </div>
  <div id="charter-box">
    Lakewood, CO<br><a href="https://www.scouting.org/">Scouting America</a>
  </div>
</header>`;

  // ── NAVIGATION ──────────────────────────────────────────
  //  To add or rename a nav item, edit this list.
  //  Format: ['filename.html', 'Label']
  var NAV_ITEMS = [
    ['index.html',        'Home'],
    ['about.html',        'About Troop 537'],
    ['crew.html',         'Crew 537'],
    ['recent-events.html','Recent Events'],
    ['calendar.html',     'Calendar'],
    ['photos.html',       'Photos'],
    ['parents.html',      'Parents'],
    ['resources.html',    'Resources'],
    ['contact.html',      'Contact'],
  ];

  // ── FOOTER ──────────────────────────────────────────────
  var FOOTER = `
<div id="footer">
  <div id="footer-inner">
    <p>&copy; 2026 Troop and Crew 537 - Greater Colorado Council - Lakewood, CO - Scouting America</p>
  </div>
</div>`;

  // ── INJECT HEADER ───────────────────────────────────────
  var headerEl = document.getElementById('page-header-placeholder');
  if (headerEl) headerEl.outerHTML = HEADER;

  // ── INJECT NAV (auto-highlights current page) ───────────
  var navEl = document.getElementById('main-navigation-placeholder');
  if (navEl) {
    var currentPage = window.location.pathname.split('/').pop() || 'index.html';
    var items = NAV_ITEMS.map(function(item) {
      var href = item[0], label = item[1];
      var isCurrent = (currentPage === href) ? ' class="current"' : '';
      return '      <li' + isCurrent + '><a href="' + href + '">' + label + '</a></li>';
    }).join('\n');
    navEl.outerHTML =
      '<div id="main-navigation">\n  <nav>\n    <ul class="flexnav">\n' +
      items +
      '\n    </ul>\n  </nav>\n</div>';
  }

  // ── INJECT FOOTER ───────────────────────────────────────
  var footerEl = document.getElementById('footer-placeholder');
  if (footerEl) footerEl.outerHTML = FOOTER;

})();
