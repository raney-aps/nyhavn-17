# -*- coding: utf-8 -*-
"""Regenerate the Nyhavn 17 menu pages (DA + EN) from menu_data.py.

Rewrites only the content inside <main> on the menu pages, up to the trailing
price-note/CTA block, which is preserved verbatim. Nav, header, gallery, footer
and scripts are never touched.

Usage:  python3 build_menu.py [repo_root]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from menu_data import *  # noqa: F401,F403

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Claude Code/nyhavn-17")

# ---------------------------------------------------------------- rendering
def _pick(d, lang, key):
    return d["%s_%s" % (key, lang)] if ("%s_%s" % (key, lang)) in d else d[lang]


def render_item(it, lang):
    name = it["da"] if lang == "da" else it["en"]
    desc = it["desc_da"] if lang == "da" else it["desc_en"]
    price = it["price"]
    desc_html = ('<p class="font-sans text-cream/45 text-sm mt-1">%s</p>' % desc) if desc else ""
    price_html = ('<span class="font-sans text-gold text-sm ml-6 shrink-0">%s</span>' % price) if price else ""
    return ('<div class="menu-item py-5"><div class="flex justify-between items-start">'
            '<div><p class="item-name font-serif text-xl text-cream">%s</p>%s</div>%s</div></div>'
            % (name, desc_html, price_html))


def render_section(sec, lang, indent="      "):
    label = sec["label_da"] if lang == "da" else sec["label_en"]
    note = sec["note_da"] if lang == "da" else sec["note_en"]
    lines = [indent + '<section class="menu-sec">']
    lines.append(indent + '  <p class="section-label %s">%s</p>' % ("mb-3" if note else "mb-8", label))
    if note:
        lines.append(indent + '  <p class="font-sans text-cream/40 text-xs mb-8">%s</p>' % note)
    lines.append(indent + '  <div class="menu-cols">')
    for it in sec["items"]:
        lines.append(indent + "    " + render_item(it, lang))
    lines.append(indent + "  </div>")
    lines.append(indent + "</section>")
    return "\n".join(lines)


def render_featured(items, lang, indent="      "):
    """Grid of highlight cards (the circles on the printed menu)."""
    lines = [indent + '<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mb-16">']
    for it in items:
        name = it["da"] if lang == "da" else it["en"]
        desc = it["desc_da"] if lang == "da" else it["desc_en"]
        desc_html = ('<p class="font-sans text-cream/50 text-sm leading-relaxed mb-4">%s</p>' % desc) if desc else ""
        lines.append(indent + '  <div class="p-6 border border-gold/30 bg-navy-dark/50">'
                     '<p class="font-serif text-2xl text-cream mb-2">%s</p>%s'
                     '<span class="font-serif text-2xl text-gold">%s</span></div>'
                     % (name, desc_html, it["price"]))
    lines.append(indent + "</div>")
    return "\n".join(lines)


def render_signature(it, lang, label_da, label_en, indent="      "):
    """Wide highlight band, used for Stjerneskud."""
    name = it["da"] if lang == "da" else it["en"]
    desc = it["desc_da"] if lang == "da" else it["desc_en"]
    label = label_da if lang == "da" else label_en
    return "\n".join([
        indent + '<div class="mb-16 p-8 md:p-10 border border-gold/30 bg-navy-dark/50">',
        indent + '  <div class="flex flex-col md:flex-row md:items-start md:justify-between gap-4">',
        indent + '    <div class="flex-1">',
        indent + '      <p class="section-label mb-3">%s</p>' % label,
        indent + '      <h2 class="font-serif text-3xl md:text-4xl text-cream mb-4">%s</h2>' % name,
        indent + '      <p class="font-sans text-cream/60 text-sm leading-relaxed max-w-2xl">%s</p>' % desc,
        indent + "    </div>",
        indent + '    <span class="font-serif text-3xl text-gold md:ml-8 shrink-0">%s</span>' % it["price"],
        indent + "  </div>",
        indent + "</div>",
    ])


# ------------------------------------------------------------- page content
def breakfast_body(lang, indent="      "):
    parts = [render_featured(BREAKFAST_FEATURED, lang, indent)]
    for sec in BREAKFAST_LEFT + BREAKFAST_RIGHT:
        parts.append(render_section(sec, lang, indent))
    return "\n\n".join(parts)


def mains_body(lang, meal, indent="      "):
    """meal = 'lunch' | 'dinner' — identical apart from the opening section."""
    opener = LUNCH_HERRING if meal == "lunch" else DINNER_STARTERS
    parts = [
        render_featured(MAINS_FEATURED, lang, indent),
        render_section(opener, lang, indent),
        render_section(SMORREBROD, lang, indent),
        render_signature(STJERNESKUD, lang, "Husets specialitet", "House speciality", indent),
        render_section(HOT_KITCHEN, lang, indent),
        render_section(DANISH_CLASSICS, lang, indent),
        render_section(DESSERTS, lang, indent),
    ]
    return "\n\n".join(parts)


def drinks_body(lang, indent="      "):
    parts = [render_section(s, lang, indent) for s in
             (COCKTAILS, DRAUGHT, BOTTLED, BUBBLES, WHITE, RED, ROSE,
              NON_ALC_LEFT, NON_ALC_RIGHT)]
    return "\n\n".join(parts)


BODIES = {
    "breakfast": breakfast_body,
    "lunch": lambda lang, indent="      ": mains_body(lang, "lunch", indent),
    "dinner": lambda lang, indent="      ": mains_body(lang, "dinner", indent),
    "drinks": drinks_body,
}

# ---------------------------------------------------------------- splicing
CTA_RE = re.compile(r'(?:[ \t]*<!--[^>]*?CTA[^>]*?-->\n)?[ \t]*<div class="mt-24 pt-16 border-t')


def splice_main(html, new_body):
    """Replace everything inside <main> before the trailing CTA block."""
    m = re.search(r"<main[^>]*>", html)
    if not m:
        raise SystemExit("no <main> found")
    start = m.end()
    end = html.index("</main>", start)
    inner = html[start:end]
    cta = CTA_RE.search(inner)
    if not cta:
        raise SystemExit("no CTA block found inside <main>")
    tail = inner[cta.start():]
    return html[:start] + "\n\n" + new_body + "\n\n" + tail + html[end:]


STYLE_HOOK = ".section-label{font-family:'DM Sans',sans-serif;"
EXTRA_CSS = (
    "    .menu-sec{margin-bottom:4.5rem}.menu-sec:last-of-type{margin-bottom:0}\n"
    "    .menu-cols{column-gap:4rem}\n"
    "    @media(min-width:1024px){.menu-cols{column-count:2}}\n"
    "    .menu-cols > .menu-item{break-inside:avoid;-webkit-column-break-inside:avoid;page-break-inside:avoid}\n"
)


def ensure_css(html):
    if ".menu-cols{" in html:
        return html
    i = html.index(STYLE_HOOK)
    line_start = html.rindex("\n", 0, i) + 1
    return html[:line_start] + EXTRA_CSS + html[line_start:]


def write(path, html):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)


# --------------------------------------------------------------- sub-pages
PAGES = [
    ("menu-breakfast.html", "da", "breakfast"),
    ("menu-lunch.html", "da", "lunch"),
    ("menu-dinner.html", "da", "dinner"),
    ("menu-drinks.html", "da", "drinks"),
    ("en/menu-breakfast.html", "en", "breakfast"),
    ("en/menu-lunch.html", "en", "lunch"),
    ("en/menu-dinner.html", "en", "dinner"),
    ("en/menu-drinks.html", "en", "drinks"),
]

# header hours + <h1> + <title> + meta description, per page and language
META = {
    ("da", "breakfast"): dict(
        h1="Morgenmad i Nyhavn",
        hours='Serveres dagligt <strong class="text-cream">09:30</strong> til <strong class="text-cream">11:30</strong>',
        title="Morgenmad Menu &mdash; Nyhavn 17",
        desc="Morgenmad hos Nyhavn 17: bagværk, æggeretter, toast og morgenmadstallerken. Serveres dagligt 09:30&ndash;11:30."),
    ("da", "lunch"): dict(
        h1="Frokost i Nyhavn",
        hours='Serveres dagligt <strong class="text-cream">11:30</strong> til <strong class="text-cream">17:00</strong>',
        title="Frokost Menu &mdash; Nyhavn 17",
        desc="Frokost hos Nyhavn 17: sild, smørrebrød, stjerneskud, danske klassikere og det varme køkken. Serveres dagligt 11:30&ndash;17:00."),
    ("da", "dinner"): dict(
        h1="Aftensmad i Nyhavn",
        hours='Serveres dagligt <strong class="text-cream">17:00</strong> til <strong class="text-cream">22:00</strong>',
        title="Aftensmad Menu &mdash; Nyhavn 17",
        desc="Aftensmad hos Nyhavn 17: forretter, smørrebrød, stjerneskud, danske klassikere og det varme køkken. Serveres dagligt 17:00&ndash;22:00."),
    ("da", "drinks"): dict(
        h1="Drikkevarer",
        hours='Bar åben til <strong class="text-cream">00:00</strong> &nbsp;·&nbsp; Weekend til <strong class="text-cream">01:30</strong>',
        title="Drikkevarer Menu &mdash; Nyhavn 17",
        desc="Cocktails, fadøl, flaskeøl, vin og alkoholfrie drikkevarer hos Nyhavn 17 i hjertet af København."),
    ("en", "breakfast"): dict(
        h1="Breakfast in Nyhavn",
        hours='Served daily <strong class="text-cream">09:30</strong> &mdash; <strong class="text-cream">11:30</strong>',
        title="Breakfast Menu &mdash; Nyhavn 17",
        desc="Breakfast at Nyhavn 17: pastry, eggs, toast and our breakfast platter. Served daily 09:30&ndash;11:30."),
    ("en", "lunch"): dict(
        h1="Lunch in Nyhavn",
        hours='Served daily <strong class="text-cream">11:30</strong> &mdash; <strong class="text-cream">17:00</strong>',
        title="Lunch Menu &mdash; Nyhavn 17",
        desc="Lunch at Nyhavn 17: herring, smørrebrød, shootingstar, Danish classics and the hot kitchen. Served daily 11:30&ndash;17:00."),
    ("en", "dinner"): dict(
        h1="Dinner in Nyhavn",
        hours='Served daily <strong class="text-cream">17:00</strong> &mdash; <strong class="text-cream">22:00</strong>',
        title="Dinner Menu &mdash; Nyhavn 17",
        desc="Dinner at Nyhavn 17: starters, smørrebrød, shootingstar, Danish classics and the hot kitchen. Served daily 17:00&ndash;22:00."),
    ("en", "drinks"): dict(
        h1="Drinks",
        hours='Bar open until <strong class="text-cream">00:00</strong> &nbsp;·&nbsp; weekends until <strong class="text-cream">01:30</strong>',
        title="Drinks Menu &mdash; Nyhavn 17",
        desc="Cocktails, draught beer, bottled beer, wine and soft drinks at Nyhavn 17 in the heart of Copenhagen."),
}


def patch_header(html, meta):
    html = re.sub(r'(<h1 class="reveal reveal-delay-1 font-serif text-5xl md:text-7xl text-cream mb-4">).*?(</h1>)',
                  lambda m: m.group(1) + meta["h1"] + m.group(2), html, count=1)
    html = re.sub(r'(<p class="reveal reveal-delay-2 font-sans text-cream/55 text-sm">).*?(</p>)',
                  lambda m: m.group(1) + meta["hours"] + m.group(2), html, count=1)
    html = re.sub(r"(<title>).*?(</title>)",
                  lambda m: m.group(1) + meta["title"] + m.group(2), html, count=1)
    html = re.sub(r'(<meta name="description" content=").*?(" ?/>)',
                  lambda m: m.group(1) + meta["desc"] + m.group(2), html, count=1)
    return html


changed = []
for rel, lang, page in PAGES:
    path = os.path.join(ROOT, rel)
    with open(path, encoding="utf-8") as fh:
        html = fh.read()
    before = html
    html = ensure_css(html)
    html = splice_main(html, BODIES[page](lang))
    html = patch_header(html, META[(lang, page)])
    if html != before:
        write(path, html)
        changed.append(rel)

# ------------------------------------------------------- combined menu.html
TABS = {
    "da": [("morgenmad", "MORGENMAD", "breakfast"), ("frokost", "FROKOST", "lunch"),
           ("aftensmad", "AFTENSMAD", "dinner"), ("drikkevarer", "DRIKKEVARER", "drinks")],
    "en": [("breakfast", "BREAKFAST", "breakfast"), ("lunch", "LUNCH", "lunch"),
           ("dinner", "DINNER", "dinner"), ("drinks", "DRINKS", "drinks")],
}
TAB_HOURS = {
    "da": {"breakfast": "09:30 &ndash; 11:30", "lunch": "11:30 &ndash; 17:00",
           "dinner": "17:00 &ndash; 22:00", "drinks": "Bar åben til 00:00 &nbsp;·&nbsp; weekend til 01:30"},
    "en": {"breakfast": "09:30 &ndash; 11:30", "lunch": "11:30 &ndash; 17:00",
           "dinner": "17:00 &ndash; 22:00", "drinks": "Bar open until 00:00 &nbsp;·&nbsp; weekends until 01:30"},
}

for rel, lang in (("menu.html", "da"), ("en/menu.html", "en")):
    path = os.path.join(ROOT, rel)
    with open(path, encoding="utf-8") as fh:
        html = fh.read()
    html = ensure_css(html)
    panes = []
    for idx, (slug, comment, page) in enumerate(TABS[lang]):
        body = BODIES[page](lang, indent="      ")
        panes.append("\n".join([
            "    <!-- %s TAB -->" % comment,
            '    <div id="tab-%s" class="tab-pane%s">' % (slug, "" if idx == 0 else " hidden"),
            '      <p class="font-sans text-cream/40 text-xs mb-8">%s</p>' % TAB_HOURS[lang][page],
            "",
            body,
            "    </div>",
        ]))
    html = splice_main(html, "\n\n".join(panes))
    write(path, html)
    changed.append(rel)

# ------------------------------------------------------------- home page
FAV_GRID_RE = re.compile(
    r'(<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">\n).*?(\n      </div>\n      <div class="text-center mt-14">)',
    re.S)
MARQUEE_RE = re.compile(r'(<div class="marquee-inner">\n).*?(\n\n*    </div>)', re.S)


def render_favourites(lang):
    rows = []
    for i, it in enumerate(HOME_FAVOURITES):
        name = it["da"] if lang == "da" else it["en"]
        desc = it["desc_da"] if lang == "da" else it["desc_en"]
        rows.append(
            '        <div class="reveal reveal-delay-%d p-6 border-t border-gold/30 hover:border-gold transition-colors group cursor-default">\n'
            '          <div class="flex justify-between items-start mb-2">\n'
            '            <h3 class="font-serif text-xl text-cream group-hover:text-gold transition-colors">%s</h3>\n'
            '            <span class="font-sans text-gold text-sm ml-4">%s</span>\n'
            "          </div>\n"
            '          <p class="font-sans text-cream/50 text-sm">%s</p>\n'
            "        </div>" % (i % 3 + 1, name, it["price"], desc))
    return "\n".join(rows)


def render_marquee(lang):
    names = [d if lang == "da" else e for d, e in MARQUEE]
    span = ('      <span class="font-serif italic text-cream/30 text-xl px-8">%s</span>'
            '<span class="text-gold/30 px-2">·</span>')
    # the track is duplicated so the CSS -50% loop is seamless
    return "\n".join(span % n for n in names * 2)


for rel, lang in (("index.html", "da"), ("en/index.html", "en")):
    path = os.path.join(ROOT, rel)
    with open(path, encoding="utf-8") as fh:
        html = fh.read()
    before = html
    html, n1 = FAV_GRID_RE.subn(lambda m: m.group(1) + render_favourites(lang) + m.group(2), html, count=1)
    html, n2 = MARQUEE_RE.subn(lambda m: m.group(1) + render_marquee(lang) + m.group(2), html, count=1)
    if not (n1 and n2):
        raise SystemExit("%s: favourites=%d marquee=%d (expected 1 each)" % (rel, n1, n2))
    if html != before:
        write(path, html)
        changed.append(rel)

# ------------------------------------------- service windows across the site
# The new card sets three service windows; every page that quotes them must
# agree with the menu pages above.
SERVICE_FIXES = {
    "index.html": [
        ("Croissanter, æg, pandekager, avocado toast og vores berømte brunchtallerken. Fra kl. 09:30.",
         "Bagværk, æggeretter, toast og vores morgenmadstallerken. Serveres 09:30 til 11:30."),
        ("Smørrebrød, burgere, salater, deleretter og mere. Serveres 11:30 til 16:00.",
         "Sild, smørrebrød, stjerneskud og danske klassikere. Serveres 11:30 til 17:00."),
        ("Steak frites, pasta, schnitzel, fish &amp; chips og danske klassikere. Serveres 17:00 til 21:30.",
         "Forretter, smørrebrød, steak frites, schnitzel og danske klassikere. Serveres 17:00 til 22:00."),
    ],
    "en/index.html": [
        ("Pastries, eggs, pancakes, avocado toast and our famous brunch platter. From 09:30.",
         "Pastry, eggs, toast and our breakfast platter. Served 09:30 to 11:30."),
        ("Smørrebrød, burgers, salads, sharing plates and more. Served 11:30 to 16:00.",
         "Herring, smørrebrød, shootingstar and Danish classics. Served 11:30 to 17:00."),
        ("Steak frites, pasta, schnitzel, fish &amp; chips and Danish classics. Served 17:00 to 21:30.",
         "Starters, smørrebrød, steak frites, schnitzel and Danish classics. Served 17:00 to 22:00."),
    ],
    "menu.html": [
        ("Køkkenet åbent 11:30 — 22:00. Bar åben til midnat — weekend til 01:30.",
         "Køkkenet er åbent 09:30 til 22:00. Bar åben til midnat, weekend til 01:30."),
        ("Køkkenet er åbent 09:30\u201321:30.", "Køkkenet er åbent 09:30\u201322:00."),
    ],
    "en/menu.html": [
        ("Kitchen open 11:30 to 22:00. Bar open until midnight — weekends until 01:30.",
         "Kitchen open 09:30 to 22:00. Bar open until midnight, weekends until 01:30."),
        ("Kitchen open 09:30\u201321:30.", "Kitchen open 09:30\u201322:00."),
    ],
    "reservations.html": [
        ('<span class="font-sans text-cream/80 text-sm">Fra kl. 09:30</span>',
         '<span class="font-sans text-cream/80 text-sm">09:30 &mdash; 11:30</span>'),
        ('<span class="font-sans text-cream/80 text-sm">11:30 &mdash; 16:00</span>',
         '<span class="font-sans text-cream/80 text-sm">11:30 &mdash; 17:00</span>'),
        ('<span class="font-sans text-cream/80 text-sm">11:30 — 16:00</span>',
         '<span class="font-sans text-cream/80 text-sm">11:30 — 17:00</span>'),
        ('<span class="font-sans text-cream/80 text-sm">17:00 — 21:30</span>',
         '<span class="font-sans text-cream/80 text-sm">17:00 — 22:00</span>'),
    ],
    "en/reservations.html": [
        ('<span class="font-sans text-cream/80 text-sm">09:30 onwards</span>',
         '<span class="font-sans text-cream/80 text-sm">09:30 &mdash; 11:30</span>'),
        ('<span class="font-sans text-cream/80 text-sm">11:30 — 16:00</span>',
         '<span class="font-sans text-cream/80 text-sm">11:30 — 17:00</span>'),
        ('<span class="font-sans text-cream/80 text-sm">17:00 — 21:30</span>',
         '<span class="font-sans text-cream/80 text-sm">17:00 — 22:00</span>'),
    ],
}

for rel, subs in SERVICE_FIXES.items():
    path = os.path.join(ROOT, rel)
    with open(path, encoding="utf-8") as fh:
        html = fh.read()
    before = html
    for old, new in subs:
        html = html.replace(old, new)
    if html != before:
        write(path, html)
        if rel not in changed:
            changed.append(rel)

print("updated %d files:" % len(changed))
for c in changed:
    print("  " + c)
