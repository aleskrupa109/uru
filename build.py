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
        ("Časté dotazy", "vyhrazene-stavby/caste-dotazy.html", "Odpovědi na nejčastější otázky stavebníků"),
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
        ("Časté dotazy", "vyhrazene-stavby/caste-dotazy.html", 0),
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
    "Od 1. 7. 2026 vznikl Úřad rozvoje území (ÚRÚ). Přebírá agendy zaniklého DESÚ i ÚÚR. "
    "Vyhrazené stavby vyřizujeme v sekci <a href='{r}vyhrazene-stavby/index.html'>Vyhrazené stavby</a>, "
    "obsah a metodiky ÚÚR najdete v sekci <a href='{r}uzemni-rozvoj/index.html'>Územní rozvoj</a>."
)
BANNER_META = "Přechodové sdělení — zobrazuje se do konce přechodného období, poté se vypíná v CMS. Zavření platí do konce relace."


def rel(depth):
    return "../" * depth


def icon():
    return ('<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">'
            '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 4v5"/></svg>')


def cmt(n, text):
    """Bublina s číslem zapracované připomínky."""
    return f'<span class="cmt" title="Zapracovaná připomínka č. {n}: {html.escape(text, quote=True)}">{n}</span>'


def render_nav(active, r):
    out = ['<nav class="mainnav" aria-label="Hlavní navigace"><div class="wrap"><ul>']
    for key, label, href, items in NAV:
        cls = []
        if items:
            cls.append("has-drop")
        if key == active:
            cls.append("active")
        out.append(f'<li class="{" ".join(cls)}">')
        caret = '<span class="caret"></span>' if items else ""
        out.append(f'<a href="{r}{href}">{label}{caret}</a>')
        if items:
            out.append('<div class="dropdown"><div class="wrap"><div class="cols">')
            for t, h, d in items:
                out.append(f'<a href="{r}{h}"><strong>{t}</strong><small>{d}</small></a>')
            out.append('</div></div></div>')
        out.append('</li>')
    out.append('</ul></div></nav>')
    return "".join(out)


def render_subnav(section, current, r):
    items = SUBNAV.get(section)
    if not items:
        return ""
    out = [f'<nav class="subnav" aria-label="Obsah sekce"><h2>V této sekci</h2>']
    for label, href, level in items:
        cur = ' aria-current="page"' if href == current else ""
        pad = ' style="padding-left:26px;font-size:13.5px"' if level else ""
        out.append(f'<a href="{r}{href}"{cur}{pad}>{label}</a>')
    out.append('</nav>')
    return "".join(out)


def render_crumbs(crumbs, r):
    if not crumbs:
        return ""
    parts = [f'<span><a href="{r}index.html">Úvod</a></span>']
    for label, href in crumbs:
        if href:
            parts.append(f'<span><a href="{r}{href}">{label}</a></span>')
        else:
            parts.append(f'<span>{label}</span>')
    return f'<div class="wrap"><div class="crumbs">{"".join(parts)}</div></div>'


MOCKBAR = """<div class="mockbar"><div class="wrap">
<strong>Maketa webu ÚRÚ</strong>
<span>pracovní prototyp — obsah je návrh k dopracování</span>
<span class="sep"></span>
<span data-edit-status style="opacity:.7"></span>
<button data-edit-toggle type="button">Upravit texty</button>
<button data-export type="button">Stáhnout texty</button>
<label class="btn-import" style="cursor:pointer;border:1px solid #4b5563;padding:4px 12px;border-radius:999px">Načíst texty<input data-import type="file" accept="application/json" hidden></label>
<button data-clear type="button">Zahodit úpravy</button>
<button data-cmt-toggle type="button">Skrýt značky</button>
</div></div>"""


def footer(r):
    return f"""<footer class="site-footer"><div class="wrap">
<div class="cols">
<div><h3>Úřad rozvoje území</h3><ul>
<li><a href="{r}o-uradu/kdo-jsme.html">Kdo jsme a co děláme</a></li>
<li><a href="{r}o-uradu/organizacni-struktura.html">Organizační struktura</a></li>
<li><a href="{r}kariera/index.html">Kariéra</a></li>
<li><a href="{r}o-uradu/pro-media.html">Pro média</a></li></ul></div>
<div><h3>Agendy</h3><ul>
<li><a href="{r}vyhrazene-stavby/index.html">Vyhrazené stavby</a></li>
<li><a href="{r}metodicka-podpora/index.html">Metodická podpora</a></li>
<li><a href="{r}uzemni-rozvoj/index.html">Územní rozvoj</a></li>
<li><a href="{r}uredni-deska.html">Úřední deska</a></li></ul></div>
<div><h3>Kontakt</h3><ul>
<li><a href="{r}kontakty.html">Všechny kontakty</a></li>
<li>Datová schránka: <strong>xxxxxxx</strong></li>
<li>posta@uru.gov.cz</li>
<li>+420 000 000 000</li></ul></div>
<div><h3>Povinné informace</h3><ul>
<li><a href="{r}o-uradu/povinne-informace.html">Povinně zveřejňované informace</a></li>
<li><a href="#">Prohlášení o přístupnosti</a></li>
<li><a href="#">Ochrana osobních údajů a cookies</a></li>
<li><a href="#">Oznámení protiprávního jednání</a></li></ul></div>
</div>
<div class="bottom"><span>© 2026 Úřad rozvoje území</span>
<span><a href="{r}mapa-webu.html">Mapa webu</a></span>
<span>Národní plán obnovy · Financováno Evropskou unií</span>
<span style="opacity:.6">Maketa — design systém gov se doplní po vydání nové verze</span></div>
</div></footer>"""


TPL = """<!doctype html>
<html lang="cs">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Úřad rozvoje území</title>
<link rel="stylesheet" href="{r}assets/uru.css">
</head>
<body>
{mockbar}
<header class="site-header"><div class="wrap">
<a class="brand" href="{r}index.html">
<svg width="30" height="34" viewBox="0 0 30 34" fill="#12365f"><path d="M15 1l13 6v10c0 8-5.5 13.5-13 16C7.5 30.5 2 25 2 17V7z"/></svg>
<span>Úřad rozvoje území</span></a>
<form class="header-search" role="search" action="{r}vyhledavani.html">
<input type="search" name="q" placeholder="Hledejte v názvu, obsahu i v přílohách (PDF)…" aria-label="Vyhledávání">
<button type="submit" aria-label="Hledat">&#128269;</button>
</form>
<span class="header-note">Prohledáváme i obsah PDF{c98}</span>
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


def build_page(p):
    depth = p["path"].count("/")
    r = rel(depth)
    banner = ""
    if p.get("banner", True):
        banner = ('<div class="infobanner"><div class="wrap"><span>&#9888;</span>'
                  f'<p>{BANNER.format(r=r)}<span class="meta">{BANNER_META}</span></p>'
                  '<button class="close" type="button" aria-label="Zavřít">&times;</button></div></div>')
    body = p["body"]
    if p.get("section") in SUBNAV and p.get("sidebar", True):
        body = (f'<div class="cols-side">{render_subnav(p["section"], p["path"], r)}'
                f'<div class="content">{body}</div></div>')
    head = ""
    if p.get("h1"):
        head = f'<div class="page-head"><h1>{p["h1"]}</h1>'
        if p.get("perex"):
            head += f'<p class="perex">{p["perex"]}</p>'
        if p.get("updated"):
            head += f'<p class="updated">{p["updated"]}</p>'
        head += '</div>'
    html_out = TPL.format(
        title=p["title"], r=r, mockbar=MOCKBAR,
        nav=render_nav(p.get("section", ""), r),
        banner=banner,
        crumbs=render_crumbs(p.get("crumbs"), r),
        body=head + body,
        footer=footer(r),
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
