#!/usr/bin/env python3
"""Generátor klikatelné makety webu ÚRÚ.

    python3 build.py

Přepíše všechny .html soubory v repozitáři podle definic v modulech pages_*.py.
Pokud upravuješ texty přímo v HTML, build už nespouštěj (přepsal by je),
nebo úpravy nejdřív přenes do pages_*.py.
"""
import os, re, html

ROOT = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# hlavní navigace
# --------------------------------------------------------------------------
NAV = [
    ("vyhrazene-stavby", "Vyhrazené stavby", "vyhrazene-stavby/index.html", [
        ("Co spadá pod ÚRÚ", "vyhrazene-stavby/co-spada-pod-uru.html", "Kategorie vyhrazených staveb a hraniční případy"),
        ("Jak probíhá řízení", "vyhrazene-stavby/jak-probiha-rizeni.html", "Postup od podání po rozhodnutí, lhůty, poplatky"),
        ("Dokumenty a formuláře", "vyhrazene-stavby/dokumenty-a-formulare.html", "Formuláře podle typu stavby a typu řízení"),
        ("Portál stavebníka", "vyhrazene-stavby/portal-stavebnika.html", "Elektronické podání a evidence dokumentací"),
        ("Odpovědi na nejčastější dotazy", "vyhrazene-stavby/caste-dotazy.html", "Odpovědi na nejčastější otázky stavebníků"),
    ]),
    ("metodicka-podpora", "Metodická podpora", "metodicka-podpora/index.html", [
        ("Metodická stanoviska a výklady", "metodicka-podpora/metodicka-stanoviska.html", "Prohledávatelná databáze stanovisek"),
        ("Časté dotazy", "metodicka-podpora/caste-dotazy.html", "Podle typu úřadu a agendy"),
        ("Přechodové období", "metodicka-podpora/prechodove-obdobi.html", "Rozpracovaná řízení a delimitace"),
        ("Standardizace územního plánování", "metodicka-podpora/standardizace.html", "Jednotný standard, staré a nové znění"),
        ("Konzultační středisko", "metodicka-podpora/konzultacni-stredisko.html", "Metodické vedení úřadů územního plánování"),
        ("Tisíc otázek ke stavebnímu právu", "metodicka-podpora/tisic-otazek.html", "Databáze otázek a odpovědí"),
        ("Kontakty na metodiky", "metodicka-podpora/kontakty-na-metodiky.html", "Kontaktní karty podle věcné oblasti"),
    ]),
    ("uzemni-rozvoj", "Územní rozvoj", "uzemni-rozvoj/index.html", [
        ("Územní plánování", "uzemni-rozvoj/uzemni-planovani.html", "Strategické dokumenty a evidence"),
        ("Územně analytické podklady", "uzemni-rozvoj/uap.html", "Aktuální i ukončené ročníky"),
        ("Mezinárodní spolupráce", "uzemni-rozvoj/mezinarodni-spoluprace.html", "ESPON, V4+2, přeshraniční projekty"),
        ("Publikační činnost", "uzemni-rozvoj/publikacni-cinnost.html", "Příručky a publikace"),
        ("Časopis UaÚR", "uzemni-rozvoj/casopis.html", "Urbanismus a územní rozvoj"),
        ("Knihovna", "uzemni-rozvoj/knihovna.html", "Online katalog a služby"),
        ("Stavebně technická prevence", "uzemni-rozvoj/stavebne-technicka-prevence.html", "Systém STP a aplikace iSSTP"),
        ("Mapový portál", "uzemni-rozvoj/mapovy-portal.html", "Mapové aplikace a datové sady"),
        ("Konference a semináře", "uzemni-rozvoj/konference.html", "Akce pod záštitou ÚRÚ"),
        ("Archiv", "uzemni-rozvoj/archiv.html", "Historické projekty a výroční zprávy ÚÚR"),
    ]),
    ("kariera", "Kariéra", "kariera/index.html", []),
    ("uredni-deska", "Úřední deska", "uredni-deska.html", []),
    ("o-uradu", "O úřadu", "o-uradu/index.html", [
        ("Kdo jsme a co děláme", "o-uradu/kdo-jsme.html", "Kompetence a zákonný základ"),
        ("Organizační struktura", "o-uradu/organizacni-struktura.html", "Vedení úřadu a organizační schéma"),
        ("Pro média", "o-uradu/pro-media.html", "Tiskové zprávy a kontakt pro novináře"),
        ("Povinně zveřejňované informace", "o-uradu/povinne-informace.html", "Podle §5 zák. 106/1999 Sb."),
        ("Konference a semináře", "uzemni-rozvoj/konference.html", "Akce pod záštitou ÚRÚ"),
    ]),
    ("kontakty", "Kontakty", "kontakty.html", []),
]

# levé submenu jednotlivých sekcí (může se lišit od dropdownu – vnořené položky)
SUBNAV = {
    "vyhrazene-stavby": [
        ("Co změní novela SZ", "vyhrazene-stavby/co-meni-novela.html", 0),
        ("Co spadá pod ÚRÚ", "vyhrazene-stavby/co-spada-pod-uru.html", 0),
        ("Jak probíhá řízení", "vyhrazene-stavby/jak-probiha-rizeni.html", 0),
        ("— pro účastníky řízení", "vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html", 1),
        ("Dokumenty a formuláře", "vyhrazene-stavby/dokumenty-a-formulare.html", 0),
        ("Portál stavebníka", "vyhrazene-stavby/portal-stavebnika.html", 0),
        ("Odpovědi na nejčastější dotazy", "vyhrazene-stavby/caste-dotazy.html", 0),
        ("Kontakty pro stavebníky", "kontakty.html#stavebnici", 0),
    ],
    "metodicka-podpora": [
        ("Metodická stanoviska a výklady", "metodicka-podpora/metodicka-stanoviska.html", 0),
        ("Časté dotazy", "metodicka-podpora/caste-dotazy.html", 0),
        ("Přechodové období", "metodicka-podpora/prechodove-obdobi.html", 0),
        ("Standardizace územního plánování", "metodicka-podpora/standardizace.html", 0),
        ("Konzultační středisko", "metodicka-podpora/konzultacni-stredisko.html", 0),
        ("Tisíc otázek ke stavebnímu právu", "metodicka-podpora/tisic-otazek.html", 0),
        ("Přehled dotčených orgánů", "metodicka-podpora/dotcene-organy.html", 0),
        ("Kontakty na metodiky", "metodicka-podpora/kontakty-na-metodiky.html", 0),
    ],
    "uzemni-rozvoj": [
        ("Územní plánování", "uzemni-rozvoj/uzemni-planovani.html", 0),
        ("— Politika územního rozvoje ČR", "uzemni-rozvoj/politika-uzemniho-rozvoje.html", 1),
        ("— Evidence územně plánovací činnosti", "uzemni-rozvoj/evidence-upc.html", 1),
        ("— Informační web územního plánování", "uzemni-rozvoj/informacni-web-up.html", 1),
        ("Územně analytické podklady", "uzemni-rozvoj/uap.html", 0),
        ("Mezinárodní spolupráce", "uzemni-rozvoj/mezinarodni-spoluprace.html", 0),
        ("Publikační činnost", "uzemni-rozvoj/publikacni-cinnost.html", 0),
        ("Časopis UaÚR", "uzemni-rozvoj/casopis.html", 0),
        ("Knihovna", "uzemni-rozvoj/knihovna.html", 0),
        ("Stavebně technická prevence", "uzemni-rozvoj/stavebne-technicka-prevence.html", 0),
        ("Mapový portál", "uzemni-rozvoj/mapovy-portal.html", 0),
        ("Konference a semináře", "uzemni-rozvoj/konference.html", 0),
        ("Archiv", "uzemni-rozvoj/archiv.html", 0),
    ],
    "kariera": [
        ("Proč pracovat v ÚRÚ", "kariera/index.html", 0),
        ("Otevřené pozice", "kariera/otevrene-pozice.html", 0),
        ("Jak podat přihlášku", "kariera/prihlaska.html", 0),
    ],
    "o-uradu": [
        ("Kdo jsme a co děláme", "o-uradu/kdo-jsme.html", 0),
        ("Organizační struktura", "o-uradu/organizacni-struktura.html", 0),
        ("Pro média", "o-uradu/pro-media.html", 0),
        ("Povinně zveřejňované informace", "o-uradu/povinne-informace.html", 0),
        ("Kontakty", "kontakty.html", 0),
    ],
}

BANNER = (
    "Od 1. 1. 2027 vznikl Úřad rozvoje území (ÚRÚ). Přebírá agendy zaniklého DESÚ i ÚÚR. "
    "Vyhrazené stavby vyřizujeme v sekci <a href='{r}vyhrazene-stavby/index.html'>Vyhrazené stavby</a>, "
    "obsah a metodiky ÚÚR najdete v sekci <a href='{r}uzemni-rozvoj/index.html'>Územní rozvoj</a>."
)


def rel(depth):
    return "../" * depth


# ---- ikony pro dlaždice rozcestníků ----
# Ilustrační ikony ze sady "complex" balíčku @gov-design-system-ce/icons.
# Vkládají se inline, protože používají currentColor a mají se obarvit podle tokenu.
ICON_DIR = os.path.join(ROOT, "assets", "gov", "icons")
_svg_cache = {}


def dsicon(name, kind="complex", cls="gov-tile__icon-img"):
    key = (name, kind, cls)
    if key in _svg_cache:
        return _svg_cache[key]
    path = os.path.join(ICON_DIR, kind, name + ".svg")
    if not os.path.exists(path):
        return ""
    svg = open(path, encoding="utf-8").read().strip()
    svg = re.sub(r'\s(width|height)="[^"]*"', "", svg, count=2)
    svg = svg.replace("<svg", f'<svg class="{cls}" aria-hidden="true" focusable="false"', 1)
    _svg_cache[key] = svg
    return svg


TILE_ICON = {
    # úvodní rozcestník
    "vyhrazene-stavby/index.html": "property",
    "metodicka-podpora/index.html": "doc-personal-info",
    "uzemni-rozvoj/index.html": "doc-search",
    "kariera/index.html": "job",
    # Vyhrazené stavby
    "vyhrazene-stavby/co-meni-novela.html": "news",
    "vyhrazene-stavby/co-spada-pod-uru.html": "doc-search",
    "vyhrazene-stavby/jak-probiha-rizeni.html": "queue",
    "vyhrazene-stavby/dokumenty-a-formulare.html": "documents",
    "vyhrazene-stavby/portal-stavebnika.html": "portal",
    "vyhrazene-stavby/caste-dotazy.html": "help",
    # Metodická podpora
    "metodicka-podpora/metodicka-stanoviska.html": "doc-stamp",
    "metodicka-podpora/caste-dotazy.html": "help",
    "metodicka-podpora/prechodove-obdobi.html": "time",
    "metodicka-podpora/standardizace.html": "doc-agreement",
    "metodicka-podpora/konzultacni-stredisko.html": "chat",
    "metodicka-podpora/tisic-otazek.html": "info-list",
    "metodicka-podpora/dotcene-organy.html": "institution",
    "metodicka-podpora/kontakty-na-metodiky.html": "contact",
    # Územní rozvoj
    "uzemni-rozvoj/uzemni-planovani.html": "map",
    "uzemni-rozvoj/uap.html": "doc-registers",
    "uzemni-rozvoj/mezinarodni-spoluprace.html": "globe",
    "uzemni-rozvoj/publikacni-cinnost.html": "documents",
    "uzemni-rozvoj/casopis.html": "news",
    "uzemni-rozvoj/knihovna.html": "institute-file",
    "uzemni-rozvoj/stavebne-technicka-prevence.html": "settings",
    "uzemni-rozvoj/mapovy-portal.html": "region",
    "uzemni-rozvoj/konference.html": "communication",
    "uzemni-rozvoj/archiv.html": "history",
    "uzemni-rozvoj/politika-uzemniho-rozvoje.html": "doc-state",
    "uzemni-rozvoj/evidence-upc.html": "doc-registers",
    "uzemni-rozvoj/informacni-web-up.html": "portal",
    # Kariéra
    "kariera/otevrene-pozice.html": "job",
    "kariera/prihlaska.html": "doc-filled",
    # O úřadu
    "o-uradu/kdo-jsme.html": "institution",
    "o-uradu/organizacni-struktura.html": "city-office",
    "o-uradu/pro-media.html": "news",
    "o-uradu/povinne-informace.html": "doc-basic-info",
    "o-uradu/index.html": "institution",
    # ostatní
    "uredni-deska.html": "doc-state",
    "kontakty.html": "contact",
    "aktuality.html": "news",
    "vyhledavani.html": "doc-search",
}


def tile_icon_for(href):
    tail = href.split("{{r}}")[-1].split("#")[0]
    name = TILE_ICON.get(tail)
    return dsicon(name) if name else ""


# SVG ikony z balíčku @gov-design-system-ce/icons, vložené inline (maketa
# tak nepotřebuje běhové prostředí web komponent)
GICON = {
    "chevron-down": '<svg class="{c}" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708Z" fill="currentColor"/></svg>',
    "chevron-crumb": '<svg class="{c}" width="6" height="11" viewBox="4.5 1.5 7 13" fill="none" aria-hidden="true"><path d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708Z" fill="currentColor"/></svg>',
    "chevron-right": '<svg class="{c}" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708Z" fill="currentColor"/></svg>',
    "search": '<svg class="{c}" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.398 1.398l3.85 3.85a1 1 0 0 0 1.414-1.414l-3.85-3.85ZM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0Z" fill="currentColor"/></svg>',
    "x-lg": '<svg class="{c}" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8 2.146 2.854Z" fill="currentColor"/></svg>',
    "envelope": '<svg class="{c}" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 10.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 14h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z" fill="currentColor"/></svg>',
    "warn": '<svg class="{c}" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566ZM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5Zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2Z" fill="currentColor"/></svg>',
}


def gicon(name, cls="", slot=False):
    svg = GICON[name].format(c=cls)
    if slot:
        svg = svg.replace("<svg", '<svg slot="icon"', 1)
    return svg


def icon():
    return ('<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">'
            '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 4v5"/></svg>')


def cmt(n, text):
    """Bublina s číslem zapracované připomínky."""
    return f'<span class="cmt" title="Zapracovaná připomínka č. {n}: {html.escape(text, quote=True)}">{n}</span>'


def render_nav(active, r):
    out = ['<nav class="mainnav" aria-label="Hlavní navigace"><div class="wrap">'
           '<ul class="gov-list--plain">']
    for key, label, href, items in NAV:
        cls = []
        if items:
            cls.append("has-drop")
        if key == active:
            cls.append("active")
        out.append(f'<li class="{" ".join(cls)}">')
        caret = gicon("chevron-down", "caret") if items else ""
        out.append(f'<a href="{r}{href}">{label}{caret}</a>')
        if items:
            wide = " wide" if len(items) >= 9 else ""
            out.append(f'<div class="dropdown{wide}"><div class="wrap"><div class="cols">')
            for t, h, d in items:
                out.append(f'<a href="{r}{h}" title="{d}">{t}</a>')
            out.append('</div></div></div>')
        out.append('</li>')
    out.append('</ul></div></nav>')
    return "".join(out)


def render_subnav(section, current, r):
    items = SUBNAV.get(section)
    if not items:
        return ""
    label = next((t for k, t, _h, _i in NAV if k == section), "V této sekci")
    out = [f'<nav class="subnav" aria-label="Obsah sekce"><h2>{label}</h2>']
    for label, href, level in items:
        cur = ' aria-current="page"' if href == current else ""
        pad = ' style="padding-left:26px;font-size:13.5px"' if level else ""
        out.append(f'<a href="{r}{href}"{cur}{pad}>{label}</a>')
    out.append('</nav>')
    return "".join(out)


def render_crumbs(crumbs, r):
    """Návrh: první položka „Domů", mezi položkami šipka, odstup 12 px na každou stranu."""
    if not crumbs:
        return ""
    sep = f'<span class="sep">{gicon("chevron-crumb")}</span>'
    items = [f'<li><a href="{r}index.html">Domů</a></li>']
    for label, href in crumbs:
        inner = f'<a href="{r}{href}">{label}</a>' if href else f'<span aria-current="page">{label}</span>'
        items.append(f'<li>{sep}{inner}</li>')
    return ('<div class="wrap"><nav class="gov-breadcrumbs crumbs" aria-label="Drobečková navigace">'
            f'<ul class="gov-list--plain">{"".join(items)}</ul></nav></div>')


MOCKBAR = """<div class="mockbar"><div class="wrap">
<strong>Maketa webu ÚRÚ</strong>
<span>pracovní prototyp — obsah je návrh k dopracování</span>
<span class="sep"></span>
<span data-edit-status style="opacity:.7"></span>
<button data-edit-toggle type="button">Upravit texty</button>
<button data-export type="button">Stáhnout texty</button>
<label class="btn-import" style="cursor:pointer;border:1px solid #4b5563;padding:4px 12px;border-radius:999px">Načíst texty<input data-import type="file" accept="application/json" hidden></label>
<button data-clear type="button">Zahodit úpravy</button>
<button data-cmt-toggle type="button">Skrýt poznámky</button>
</div></div>"""


# ---- opakující se blok „Potřebujete pomoct?" ----
# Návrh ho má na konci obsahových stránek; liší se jen nadpisem kontaktu a adresou.
HELP = {
    "stavebnici": ("Potřebujete pomoct?", "Kontakt pro stavebníky",
                   "Máte otázky? Napište nám — rádi poradíme.", "obecny-dotaz@uru.gov.cz"),
    "metodiky":   ("Máte dotaz k metodickým stanoviskům?", "Kontakt na metodiky",
                   "Napište nám — rádi poradíme.", "obecny-dotaz@uru.gov.cz"),
    "hr":         ("Potřebujete pomoct?", "Personální oddělení",
                   "Máte otázky? Napište nám — rádi poradíme.", "kariera@uru.gov.cz"),
    "media":      (None, "Kontakt pro média",
                   "Máte otázky? Napište nám — rádi poradíme.", "media@uru.gov.cz"),
}


def help_block(kind, r):
    """Blok „Potřebujete pomoct?" podle návrhu: šedý panel, ikona obálky 48 px,
    modrý nadpis kontaktu, popisný text a e-mail jako odkaz — vše pod sebou."""
    head, title, text, mail = HELP[kind]
    h = f"<h2>{head}</h2>" if head else ""
    return (f'{h}<div class="helpbox">{dsicon("simple-envelope", cls="helpbox__icon")}'
            f'<h3>{title}</h3><p>{text}</p>'
            f'<p class="mail">{gicon("envelope")}'
            f'<a href="mailto:{mail}">{mail}</a></p></div>')


def footer(r):
    """Patička podle návrhu: čtyři sloupce zrcadlící hlavní navigaci (x 144 / 432 / 720
    / 1008 při rámu 1440), pod nimi související loga a spodní lišta s povinnými odkazy."""
    cols = [
        ("Vyhrazené stavby", "vyhrazene-stavby/index.html", [
            ("Co spadá pod ÚRÚ", "vyhrazene-stavby/co-spada-pod-uru.html"),
            ("Jak probíhá řízení", "vyhrazene-stavby/jak-probiha-rizeni.html"),
            ("Dokumenty a formuláře", "vyhrazene-stavby/dokumenty-a-formulare.html"),
            ("Portál stavebníka", "vyhrazene-stavby/portal-stavebnika.html"),
            ("Odpovědi na nejčastější otázky", "vyhrazene-stavby/caste-dotazy.html"),
        ]),
        ("Metodická podpora", "metodicka-podpora/index.html", [
            ("Metodická stanoviska a výklady", "metodicka-podpora/metodicka-stanoviska.html"),
            ("Často kladené otázky", "metodicka-podpora/caste-dotazy.html"),
            ("Přechodové období", "metodicka-podpora/prechodove-obdobi.html"),
            ("Standardizace územního plánování", "metodicka-podpora/standardizace.html"),
            ("Konzultační středisko", "metodicka-podpora/konzultacni-stredisko.html"),
            ("Tisíc otázek", "metodicka-podpora/tisic-otazek.html"),
        ]),
        ("Územní rozvoj", "uzemni-rozvoj/index.html", [
            ("Územní plánování", "uzemni-rozvoj/uzemni-planovani.html"),
            ("Mezinárodní spolupráce", "uzemni-rozvoj/mezinarodni-spoluprace.html"),
            ("Publikační činnost", "uzemni-rozvoj/publikacni-cinnost.html"),
            ("Časopis UaÚR", "uzemni-rozvoj/casopis.html"),
            ("Knihovna", "uzemni-rozvoj/knihovna.html"),
            ("Mapový portál", "uzemni-rozvoj/mapovy-portal.html"),
            ("Archiv", "uzemni-rozvoj/archiv.html"),
        ]),
    ]
    out = ['<footer class="site-footer"><div class="wrap"><div class="cols">']
    for title, href, items in cols:
        out.append(f'<div><h3><a href="{r}{href}">{title}</a></h3><ul class="gov-list--plain">')
        for t, h in items:
            out.append(f'<li><a href="{r}{h}">{t}</a></li>')
        out.append('</ul></div>')
    out.append(
        '<div><h3>Kontakt</h3><ul class="gov-list--plain">'
        '<li>Úřad rozvoje území</li>'
        '<li>adresa se doplní</li>'
        '<li>telefon se doplní</li>'
        f'<li><a href="{r}kontakty.html">Všechny kontakty</a></li></ul>'
        '<div class="footer-social" aria-label="Sociální sítě">'
        + "".join(f'<span title="{n}">{n[0]}</span>' for n in
                  ("Facebook", "Instagram", "YouTube", "LinkedIn"))
        + '</div></div>')
    out.append('</div>')

    out.append('<a class="footer-top" href="#" aria-label="Zpět nahoru">'
               + gicon("chevron-down", "up") + '</a>')
    out.append('<div class="footer-logos"><h3>Související loga</h3><div class="logos">'
               '<span>Národní plán obnovy</span><span>Financováno Evropskou unií</span></div></div>')

    out.append('<div class="bottom"><ul class="gov-list--plain legal">'
               '<li><a href="#">Prohlášení o přístupnosti</a></li>'
               '<li><a href="#">Ochrana osobních údajů a cookies</a></li>'
               f'<li><a href="{r}o-uradu/povinne-informace.html">Povinně zveřejňované informace</a></li>'
               '<li><a href="#">Oznámení protiprávního jednání</a></li></ul>'
               '<div class="bottom-row">'
               '<span>© 2026 Úřad rozvoje území • Informace jsou poskytovány v souladu '
               'se zákonem č. 106/1999 Sb.</span>'
               f'<span><a href="{r}mapa-webu.html">Mapa webu</a></span>'
               '<span class="ver">Maketa — design systém gov.cz 4.6.5</span>'
               '</div></div>')
    out.append('</div></footer>')
    return "".join(out)


MODE_SCRIPT = """<script>
/* Pracovní režim makety (lišta s nástroji, značky připomínek, editace textů) se
   zapíná parametrem ?edit=1 a vypíná ?edit=0; volba se pamatuje v prohlížeči.
   Bez něj se maketa chová jako běžný web — to je stav, ve kterém ji lze poslat
   třetí straně. Není to ochrana dat: úpravy textů se ukládají jen v prohlížeči
   editora a nikam se neodesílají. */
(function () {
  var q = location.search, K = "uru-maketa-editor";
  try {
    if (/[?&]edit=0(&|$)/.test(q)) localStorage.removeItem(K);
    else if (/[?&]edit(=1)?(&|$)/.test(q)) localStorage.setItem(K, "1");
    if (localStorage.getItem(K) === "1") document.documentElement.setAttribute("data-mode", "edit");
  } catch (e) {}
})();
</script>"""


TPL = """<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Úřad rozvoje území</title>
<link rel="stylesheet" href="{r}assets/gov/styles/tokens.css">
<link rel="stylesheet" href="{r}assets/uru-tokens.css">
<link rel="stylesheet" href="{r}assets/gov/fonts/roboto.css">
<link rel="stylesheet" href="{r}assets/gov/styles/styles.css">
<link rel="stylesheet" href="{r}assets/gov/styles/layout.css">
<link rel="stylesheet" href="{r}assets/gov/styles/content.css">
<link rel="stylesheet" href="{r}assets/gov/styles/animations.css">
<link rel="stylesheet" href="{r}assets/gov/styles/components.css">
<link rel="stylesheet" href="{r}assets/uru.css">
{mode_script}
</head>
<body>
{mockbar}
<header class="site-header"><div class="wrap">
<a class="brand" href="{r}index.html">
{logo}
<span>Úřad rozvoje území</span></a>
<form class="header-search" role="search" action="{r}vyhledavani.html">
<input type="search" name="q" placeholder="Hledejte v názvu, obsahu i v přílohách (PDF)…" aria-label="Vyhledávání">
<button type="submit" aria-label="Hledat">{search_icon}</button>
</form>
<span class="cmt" title="Zapracovaná připomínka č. 98: vyhledávací pole uvádí, že se prohledává i obsah příloh (PDF).">98</span>
<span class="header-toggle" aria-hidden="true"></span>
</div></header>
{nav}
{banner}
{crumbs}
<main class="page"><div class="wrap">
{body}
</div></main>
{footer}
<script src="{r}assets/uru.js"></script>
</body>
</html>
"""



# --------------------------------------------------------------------------
# převod vlastního značkování na komponenty design systému gov
# --------------------------------------------------------------------------
TAG_COLOR = {"valid": ("success", "subtle"), "invalid": ("error", "subtle"),
             "superseded": ("warning", "subtle"), "neutral": ("primary", "subtle"),
             "hist": ("neutral", "subtle")}


def to_ds(html_body):
    """Nahradí vlastní značkování komponentami design systému gov.

    CSS design systému cílí zároveň na element i na třídu a varianty čte
    z atributů data-*, takže komponenty jde použít v čistém HTML bez
    běhového prostředí web komponent.
    """

    # ---- Button ----
    def btn(m):
        cls, attrs, label = m.group("cls"), m.group("attrs"), m.group("label")
        typ = "outlined" if "ghost" in cls else "solid"
        size = "s" if " sm" in " " + cls else "m"
        arrow = " arrow" if "arrow" in cls.split() else ""
        href = re.search(r'href="([^"]*)"', attrs)
        if href:
            inner = f'<a class="element{arrow}" href="{href.group(1)}">{label}</a>'
        else:
            inner = f'<button class="element{arrow}" type="button">{label}</button>'
        return (f'<span class="gov-button" data-color="primary" data-type="{typ}" '
                f'data-size="{size}">{inner}</span>')

    html_body = re.sub(r'<a class="(?P<cls>btn[^"]*)"(?P<attrs>[^>]*)>(?P<label>.*?)</a>',
                       btn, html_body, flags=re.S)
    html_body = re.sub(r'<button class="(?P<cls>btn[^"]*)"(?P<attrs>[^>]*)>(?P<label>.*?)</button>',
                       btn, html_body, flags=re.S)

    # ---- Tag ----
    def tag(m):
        color, typ = TAG_COLOR.get(m.group(1).strip(), ("neutral", "subtle"))
        return (f'<span class="gov-tag" data-color="{color}" data-type="{typ}" data-size="s">'
                f'<span class="element">{m.group(2)}</span></span>')

    html_body = re.sub(r'<span class="tag ([a-z]+)">(.*?)</span>', tag, html_body, flags=re.S)

    # ---- Chip (aktivní filtry) ----
    html_body = html_body.replace(
        '<div class="chips" data-chips></div>',
        '<div class="chips gov-chips" data-chips></div>')

    # ---- Message (zvýrazněné boxy) ----
    BOX = {"change": ("warning", "bold"), "edge": ("primary", "subtle"),
           "note": ("neutral", "subtle"), "gap": ("success", "subtle")}

    def box(m):
        color, typ = BOX.get(m.group(1), ("neutral", "subtle"))
        return (f'<div class="gov-message" data-color="{color}" data-type="{typ}" role="status">'
                f'<span>{gicon("warn", "gov-message__icon")}</span>'
                f'<div class="gov-message__content">{m.group(2)}</div></div>')

    html_body = re.sub(r'<div class="box ([a-z]+)">(.*?)</div>\s*(?=<|$)', box, html_body, flags=re.S)

    def box_attrs(m):
        pre, kind, inner = m.group(1), m.group(2), m.group(3)
        color, typ = BOX.get(kind, ("neutral", "subtle"))
        return (f'<div{pre} class="gov-message" data-color="{color}" data-type="{typ}" role="status">'
                f'<span>{gicon("warn", "gov-message__icon")}</span>'
                f'<div class="gov-message__content">{inner}</div></div>')

    html_body = re.sub(r'<div((?:\s+[a-z-]+="[^"]*")+) class="box ([a-z]+)">(.*?)</div>\s*(?=<|$)',
                       box_attrs, html_body, flags=re.S)

    # ---- Accordion ----
    def acc(m):
        attrs, label, body = m.group(1), m.group(2), m.group(3)
        ident = re.search(r'id="([^"]*)"', attrs)
        i = f' id="{ident.group(1)}"' if ident else ""
        op = " open" if re.search(r'\sopen(?=[\s>])', attrs) else ""
        extra = " data-faq" if "data-faq" in attrs else ""
        return (f'<div class="gov-accordion-item" data-size="m" role="listitem"{extra}>'
                f'<details class="gov-accordion-item__details"{i}{op}>'
                f'<summary class="gov-accordion-item__summary">'
                f'<span class="gov-accordion-item__title"><span slot="label">{label}</span></span>'
                f'<span class="gov-accordion-item__right"><span class="gov-accordion-item__arrow">'
                f'{gicon("chevron-down")}</span></span></summary>'
                f'<div class="gov-accordion-item__content">{body}</div></details></div>')

    html_body = re.sub(
        r'<details class="acc"([^>]*)>\s*<summary>(.*?)</summary>\s*<div class="body">(.*?)</div>\s*</details>',
        acc, html_body, flags=re.S)
    html_body = re.sub(r'(\s*)((?:<div class="gov-accordion-item".*?</details></div>\s*){1,})',
                       lambda m: m.group(1) + '<div class="gov-accordion" role="list">'
                                 + m.group(2).strip() + '</div>',
                       html_body, flags=re.S)

    # ---- Tile (rozcestníky) ----
    def tile(m):
        href, inner = m.group(1), m.group(2)
        order = re.search(r'<span class="order">(.*?)</span>', inner, re.S)
        h3 = re.search(r'<h3>(.*?)</h3>', inner, re.S)
        p = re.search(r'<p>(.*?)</p>', inner, re.S)
        if not h3:
            return m.group(0)
        head = f'<span class="tile-order">{order.group(1)}</span>' if order else ""
        desc = p.group(1) if p else ""
        ico = tile_icon_for(href)
        ico = f'<span slot="icon">{ico}</span>' if ico else ""
        # návrh v dlaždicích rozcestníku šipku nemá
        return (f'<div class="gov-tile uru-card" data-size="m" data-orientation="vertical" data-clickable="1">'
                f'{ico}<div class="gov-tile__content"><div class="gov-tile__text">{head}'
                f'<div class="gov-tile__title"><a class="gov-tile__link" href="{href}">{h3.group(1)}</a></div>'
                f'<div class="gov-tile__annotation">{desc}</div>'
                f'</div></div></div>')

    def qlink(m):
        attrs, href, inner = m.group(1), m.group(2), m.group(3)
        h3 = re.search(r'<h3>(.*?)</h3>', inner, re.S)
        p = re.search(r'<p>(.*?)</p>', inner, re.S)
        if not h3:
            return m.group(0)
        name = re.search(r'data-ico="([a-z0-9-]+)"', attrs)
        ico = dsicon(name.group(1), cls="gov-tile__icon-img") if name else tile_icon_for(href)
        ico = f'<span slot="icon">{ico}</span>' if ico else ""
        desc = p.group(1) if p else ""
        return (f'<div class="gov-tile uru-qlink" data-size="s" data-orientation="vertical" data-clickable="1">'
                f'{ico}<div class="gov-tile__content"><div class="gov-tile__text">'
                f'<div class="gov-tile__title"><a class="gov-tile__link" href="{href}">{h3.group(1)}</a>'
                f'<span class="gov-tile__icon">{gicon("chevron-right")}</span></div>'
                f'<div class="gov-tile__annotation gov-tile__annotation--padding">{desc}</div>'
                f'</div></div></div>')

    html_body = re.sub(r'<a class="qlink"([^>]*?)href="([^"]*)"([^>]*)>(.*?)</a>',
                       lambda m: qlink(type("M", (), {"group": lambda self, i: [None, m.group(1) + m.group(3), m.group(2), m.group(4)][i]})()),
                       html_body, flags=re.S)
    html_body = re.sub(r'<a class="card" href="([^"]*)"[^>]*>(.*?)</a>', tile, html_body, flags=re.S)

    def tile_static(m):
        inner = m.group(1)
        h3 = re.search(r'<h3>(.*?)</h3>', inner, re.S)
        p = re.search(r'<p>(.*?)</p>', inner, re.S)
        if not h3 or "<ul>" in inner:
            return m.group(0)
        desc = p.group(1) if p else ""
        return (f'<div class="gov-tile" data-size="m" data-orientation="vertical">'
                f'<div class="gov-tile__content"><div class="gov-tile__text">'
                f'<div class="gov-tile__title">{h3.group(1)}</div>'
                f'<div class="gov-tile__annotation">{desc}</div></div></div></div>')

    html_body = re.sub(r'<div class="card">(.*?)</div>', tile_static, html_body, flags=re.S)
    html_body = html_body.replace('<div class="card">', '<div class="sitemap-card">')

    # ---- Empty (prázdné stavy výpisů) ----
    html_body = re.sub(
        r'<div class="empty"([^>]*)>(.*?)</div>',
        lambda m: (f'<div class="gov-empty" data-size="m" data-direction="column" '
                   f'data-align="center"{m.group(1)}>'
                   f'<div class="gov-empty__content"><p>{m.group(2)}</p></div></div>'),
        html_body, flags=re.S)


    # ---- poznámky makety ----
    # Vysvětlující poznámky (odstavce se značkou připomínky a zelené boxy) dostanou
    # třídu mock-note. Zobrazují se jen v pracovním režimu a jde je vypnout jedním
    # tlačítkem spolu se značkami.
    def mark_note(m):
        tag, attrs, inner = m.group(1), m.group(2), m.group(3)
        if 'class="cmt"' not in inner:
            return m.group(0)
        if 'class="' in attrs:
            attrs = re.sub(r'class="([^"]*)"', lambda k: f'class="{k.group(1)} mock-note"', attrs, count=1)
        else:
            attrs += ' class="mock-note"'
        return f'<{tag}{attrs}>{inner}</{tag}>'

    html_body = re.sub(r'<(p)((?:\s+[a-z-]+="[^"]*")*)>((?:(?!</p>).)*?)</p>',
                       mark_note, html_body, flags=re.S)
    html_body = html_body.replace('<div class="gov-message" data-color="success"',
                                  '<div class="gov-message mock-note" data-color="success"')

    return html_body


def build_page(p):
    depth = p["path"].count("/")
    r = rel(depth)
    banner = ""
    if p.get("banner", True):
        # Struktura podle design systému: .gov-infobar drží barevný pruh přes celou
        # šířku okna, .gov-infobar__section je zároveň flex řádek a centrovaný
        # kontejner — vlastní obal by rozvržení rozbil.
        banner = ('<div class="gov-infobar infobanner" data-hydrated data-color="primary" data-type="bold">'
                  '<section class="gov-infobar__section">'
                  f'<span>{gicon("warn", cls="", slot=True)}</span>'
                  f'<div class="gov-infobar__content"><p>{BANNER.format(r=r)}</p></div>'
                  '<span class="gov-button gov-infobar__close" data-color="primary" data-type="base" data-size="s">'
                  f'<button class="element close" type="button" aria-label="Zavřít">{gicon("x-lg")}</button></span>'
                  '</section></div>')
    body = to_ds(p["body"])
    if p.get("help"):
        body += help_block(p["help"], r)
    head = ""
    if p.get("h1"):
        head = f'<div class="page-head"><h1>{p["h1"]}</h1>'
        if p.get("perex"):
            cls = "perex mock-note" if 'class="cmt"' in p["perex"] else "perex"
            head += f'<p class="{cls}">{p["perex"]}</p>'
        if p.get("updated"):
            cls = "updated mock-note" if 'class="cmt"' in p["updated"] else "updated"
            head += f'<p class="{cls}">{p["updated"]}</p>'
        head += '</div>'
    # v návrhu je nadpis podstránky i perex součástí pravého bílého panelu
    if p.get("section") in SUBNAV and p.get("sidebar", True):
        body = (f'<div class="cols-side">{render_subnav(p["section"], p["path"], r)}'
                f'<div class="content">{head}{body}</div></div>')
        head = ""
    html_out = TPL.format(
        title=p["title"], r=r, mockbar=MOCKBAR, mode_script=MODE_SCRIPT,
        nav=render_nav(p.get("section", ""), r),
        banner=banner,
        crumbs=render_crumbs(p.get("crumbs"), r),
        body=head + body,
        footer=footer(r),
        search_icon=gicon("search"),
        logo=open(os.path.join(ROOT, "assets", "img", "logo.svg"), encoding="utf-8").read().strip(),
        c98=cmt(98, "Chybí indikace, že se prohledává i obsah příloh (PDF)."),
    )
    # relativní odkazy uvnitř těla stránek
    html_out = html_out.replace("{{r}}", r)
    out = os.path.join(ROOT, p["path"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html_out)
    return p["path"]


def main():
    import pages_home, pages_vs, pages_mp, pages_ur, pages_ostatni
    pages = (pages_home.PAGES + pages_vs.PAGES + pages_mp.PAGES
             + pages_ur.PAGES + pages_ostatni.PAGES)
    seen = set()
    for p in pages:
        if p["path"] in seen:
            raise SystemExit("Duplicitní cesta: " + p["path"])
        seen.add(p["path"])
        build_page(p)
    print(f"Vygenerováno {len(pages)} stránek.")


if __name__ == "__main__":
    main()
