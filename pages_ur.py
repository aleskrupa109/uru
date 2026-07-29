# -*- coding: utf-8 -*-
"""Sekce Územní rozvoj (obsah převzatý od ÚÚR)."""
from build import cmt

C = [("Územní rozvoj", "uzemni-rozvoj/index.html")]

ROZCESTNIK = """
<div class="grid g3">
  <a class="card" href="{{r}}uzemni-rozvoj/uzemni-planovani.html"><h3>Územní plánování</h3>
    <p>Politika územního rozvoje, územní rozvojový plán, evidence územně plánovací činnosti a slovník.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/uap.html"><h3>Územně analytické podklady</h3>
    <p>Aktuální i ukončené ročníky ÚAP ČR.""" + cmt(62, "Územně analytické podklady jsou v submenu, ale nemají návrh obrazovky.") + """</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/mezinarodni-spoluprace.html"><h3>Mezinárodní spolupráce</h3>
    <p>ESPON, V4+2 a přeshraniční projekty.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/publikacni-cinnost.html"><h3>Publikační činnost</h3>
    <p>Aktualizované příručky, publikace od roku 2019 a cykly aktualizací.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/casopis.html"><h3>Časopis UaÚR</h3>
    <p>Urbanismus a územní rozvoj — čísla, ediční plán, pokyny pro autory.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/knihovna.html"><h3>Knihovna</h3>
    <p>Online katalog, služby a knihovní řád, novinky z katalogu.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/stavebne-technicka-prevence.html"><h3>Stavebně technická prevence""" + cmt(56, "Chybí Stavebně technická prevence a Konference a semináře, které IA řadí do této sekce.") + """</h3>
    <p>Systém STP a aplikace iSSTP ve spolupráci s HZS ČR.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/mapovy-portal.html"><h3>Mapový portál</h3>
    <p>Mapové aplikace a datové sady.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/konference.html"><h3>Konference a semináře</h3>
    <p>Akce pod záštitou ÚRÚ a přehled odborných setkání.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/archiv.html"><h3>Archiv</h3>
    <p>Historické projekty a výroční zprávy ÚÚR. Označeno jako archiv, ne aktivní obsah.</p></a>
</div>
"""

UP = """
<div class="grid g2">
  <a class="card" href="{{r}}uzemni-rozvoj/politika-uzemniho-rozvoje.html"><h3>Politika územního rozvoje ČR</h3>
    <p>Aktualizace, usnesení vlády, podklady a brožury.</p></a>
  <a class="card" href="#"><h3>Politika architektury a stavební kultury ČR</h3>
    <p>Implementace, pracovní skupiny a výstupy.</p></a>
  <a class="card" href="#"><h3>Územní rozvojový plán ČR</h3>
    <p>Živá dokumentace a schválené změny.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/uap.html"><h3>Územně analytické podklady ČR</h3>
    <p>Aktuální i ukončené ročníky.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/evidence-upc.html"><h3>Evidence územně plánovací činnosti</h3>
    <p>Informace k evidenci a vstup do aplikací iLAS a iKAS.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/informacni-web-up.html"><h3>Informační web územního plánování</h3>
    <p>Rozcestník odborných odkazů.</p></a>
  <a class="card" href="#"><h3>Slovník územního rozvoje</h3>
    <p>Editovatelná databáze pojmů územního rozvoje.</p></a>
</div>

<div class="box edge">
  <h3>Hledáte přehled dotčených orgánů?</h3>
  <p>Přehled je nově v sekci Metodická podpora, protože slouží především stavebním úřadům a orgánům územního plánování.
  Přejít na <a href="{{r}}metodicka-podpora/dotcene-organy.html">Přehled dotčených orgánů</a>.""" + cmt(61, "Křížový odkaz na Přehled dotčených orgánů — uživatelé ÚÚR jsou zvyklí hledat ho zde.") + """</p>
</div>
"""

PUR = """
<div class="box gap">
  <h3>Vzorová stránka dokumentu</h3>
  <p>Tato obrazovka je šablonou pro celou třídu dokumentových stránek — Politika územního rozvoje,
  Územní rozvojový plán, Územně analytické podklady, Politika architektury. Navrhuje se jednou a používá opakovaně.""" + cmt(67, "Potvrdit, že jde o vzorovou stránku pro celou třídu dokumentových stránek.") + """</p>
</div>

<h2>Přiložené dokumenty</h2>
<ul class="files">
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Úplné znění — aktualizace č. 9</span><br>
    <span class="fmeta">verze 9.0 · schváleno usnesením vlády · 12 MB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Brožura CZ / EN / DE</span><br>
    <span class="fmeta">3 jazykové verze · 4 MB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
</ul>
<p class="hint" style="color:#717171">Soubory nad limit úložiště se zpřístupňují přes řízené úložiště — způsob je předmětem technického workshopu.</p>

<h2>O dokumentu</h2>
<p>Politika územního rozvoje je celostátní nástroj územního plánování. Určuje požadavky na konkretizaci
úkolů územního plánování v republikových, přeshraničních a mezinárodních souvislostech.</p>

<h2>Historie dokumentu</h2>
<table class="t">
  <tr><th style="width:150px">Aktualizace</th><th>Rok</th><th>Stav</th></tr>
  <tr><td>Aktualizace č. 9</td><td>2026</td><td><span class="tag valid">Platná</span></td></tr>
  <tr><td>Aktualizace č. 8</td><td>2024</td><td><span class="tag hist">Historická</span></td></tr>
  <tr><td>Aktualizace č. 7</td><td>2023</td><td><span class="tag hist">Historická</span></td></tr>
</table>
"""

EVIDENCE = """
<div class="grid g2">
  <a class="card" href="#" style="box-shadow:0 0 0 2px #2362A2 inset"><h3>Vstoupit do aplikace iLAS</h3>
    <p>Evidence územně plánovací činnosti obcí.</p></a>
  <a class="card" href="#" style="box-shadow:0 0 0 2px #2362A2 inset"><h3>Vstoupit do aplikace iKAS</h3>
    <p>Evidence územně plánovací činnosti krajů.</p></a>
</div>
<p class="hint" style="color:#717171">Vstupy do aplikací jsou nahoře — uživatel sem přichází primárně kvůli nim, ne kvůli textu.""" + cmt(64, "Struktura obrací prioritu: uživatel jde primárně do iLAS/iKAS, ale odkazy na aplikace jsou až pod dlouhým textem.") + """</p>

<h2>K čemu evidence slouží</h2>
<p>Evidence územně plánovací činnosti shromažďuje údaje o pořizované a vydané územně plánovací dokumentaci
obcí a krajů. Data slouží pro celostátní přehled i pro navazující analytické podklady.</p>

<h2>Kdo do evidence vkládá data</h2>
<ul><li>Úřady územního plánování obcí s rozšířenou působností</li><li>Krajské úřady</li></ul>

<h2>Související obsah</h2>
<ul>
  <li><a href="#">Metodiky a příručky k evidenci</a></li>
  <li><a href="#">Ročenky evidence</a></li>
  <li><a href="#">Seznam projektantů</a></li>
  <li><a href="#">Územní studie</a></li>
</ul>
"""

INFOWEB = """
<div class="box note">
  <h3>Obsah závisí na dosud nepřijatém rozhodnutí</h3>
  <p>O osudu informačního webu územního plánování (rozcestník s velkým množstvím odkazů) se teprve rozhodne —
  sloučení, ukončení, nebo archivace. Do rozhodnutí zůstává stránka informativní.</p>
</div>
<p>Informační web územního plánování je rozcestník odborných odkazů pro pořizovatele a zpracovatele
územně plánovací dokumentace.</p>
<div class="btn-row"><a class="btn ghost" href="#">Přejít na informační web</a></div>
"""

UAP = """
<p>Územně analytické podklady ČR jsou zveřejňovány po ročnících. Ukončené ročníky zůstávají dostupné
pro zpětné vyhodnocení vývoje.</p>
<div class="filters" data-filterable>
  <div class="row">
    <div class="field"><label for="u-stav">Stav ročníku</label>
      <select id="u-stav" data-key="stav"><option value="">Vše</option>
        <option value="zivy">Živý</option><option value="ukonceny">Ukončený</option></select></div>
    <div class="field"><label>&nbsp;</label><button class="btn ghost sm" type="button" data-reset>Zrušit filtry</button></div>
  </div>
  <div class="chips" data-chips></div>
</div>
<div class="resultbar"><span>Nalezeno <strong data-count>0</strong> ročníků</span></div>
<ul class="doclist" data-list>
  <li data-stav="zivy" data-date="2026-01-01"><div class="tags"><span class="tag valid">Živý ročník</span></div>
    <h3><a href="{{r}}uzemni-rozvoj/politika-uzemniho-rozvoje.html">ÚAP ČR 2026</a></h3>
    <p>Průběžně doplňovaný ročník, data se aktualizují v průběhu roku.</p></li>
  <li data-stav="ukonceny" data-date="2024-01-01"><div class="tags"><span class="tag hist">Ukončený ročník</span></div>
    <h3><a href="{{r}}uzemni-rozvoj/politika-uzemniho-rozvoje.html">ÚAP ČR 2024</a></h3>
    <p>Uzavřený ročník včetně tematických vrstev a rozborů.</p></li>
  <li data-stav="ukonceny" data-date="2022-01-01"><div class="tags"><span class="tag hist">Ukončený ročník</span></div>
    <h3><a href="{{r}}uzemni-rozvoj/politika-uzemniho-rozvoje.html">ÚAP ČR 2022</a></h3>
    <p>Uzavřený ročník.</p></li>
</ul>
<div class="empty" data-empty style="display:none">Zadanému filtru neodpovídá žádný ročník.</div>
"""

MEZINARODNI = """
<h2>ESPON</h2>
<p>Evropská pozorovací síť pro územní rozvoj a soudržnost. Průběžně aktualizovaný obsah a mezinárodní závazky ČR.</p>
<h2>V4+2</h2>
<p>Spolupráce zemí Visegrádské skupiny a přidružených států v oblasti územního rozvoje.
Obsah je vedený na samostatné doméně.</p>
<div class="box note"><p>Odkaz vede mimo web ÚRÚ na samostatnou doménu projektu. Zpět se dostanete tlačítkem prohlížeče.</p></div>
<div class="btn-row"><a class="btn ghost" href="#">Přejít na web V4+2</a></div>
<h2>Přeshraniční projekty</h2>
<p>Česko-polská a další přeshraniční spolupráce v územním plánování.</p>
"""

PUBLIKACE = """
<div class="filters" data-filterable>
  <div class="searchrow"><input type="search" data-q placeholder="Hledat v publikacích…"></div>
  <div class="row">
    <div class="field"><label for="p-typ">Typ</label>
      <select id="p-typ" data-key="typ"><option value="">Vše</option>
        <option value="prirucka">Aktualizovaná příručka</option><option value="publikace">Publikace</option></select></div>
    <div class="field"><label>&nbsp;</label><button class="btn ghost sm" type="button" data-reset>Zrušit filtry</button></div>
  </div>
  <div class="chips" data-chips></div>
</div>
<div class="resultbar"><span>Nalezeno <strong data-count>0</strong> položek</span></div>
<ul class="doclist" data-list>
  <li data-typ="prirucka" data-date="2026-04-01"><h3><a href="#">Principy a pravidla územního plánování</a></h3>
    <p>Klíčová publikace, aktualizované kapitoly.</p><div class="meta"><span>Aktualizace 2×ročně</span></div></li>
  <li data-typ="prirucka" data-date="2026-03-01"><h3><a href="#">Limity využití území</a></h3>
    <p>Přehled limitů podle jednotlivých agend.</p><div class="meta"><span>Aktualizace 2×ročně</span></div></li>
  <li data-typ="publikace" data-date="2025-06-01"><h3><a href="#">Ceny dopravní a technické infrastruktury</a></h3>
    <p>Podklad pro odhad nákladů.</p><div class="meta"><span>Aktualizace 1× za 2 roky</span></div></li>
</ul>
<div class="empty" data-empty style="display:none">Zadanému filtru neodpovídá žádná publikace.</div>
"""

CASOPIS = """
<div class="grid g3">
  <a class="card" href="#"><h3>O časopise / About Journal</h3><p>Zaměření a bibliografické údaje.</p></a>
  <a class="card" href="#"><h3>Čísla časopisu / Journal Issues</h3><p>Archiv vydaných čísel.</p></a>
  <a class="card" href="#"><h3>Pro autory / For Authors</h3><p>Pokyny pro autory a šablony.</p></a>
  <a class="card" href="#"><h3>Výzva k zasílání článků</h3><p>Call for Papers.</p></a>
  <a class="card" href="#"><h3>Ediční plán</h3><p>Plán vydání na aktuální rok.</p></a>
  <a class="card" href="#"><h3>Publikační etika</h3><p>Pravidla recenzního řízení.</p></a>
  <a class="card" href="#"><h3>Redakční rada</h3><p>Složení redakční rady.</p></a>
  <a class="card" href="#"><h3>Redakce</h3><p>Kontakty redakce.</p></a>
  <a class="card" href="#"><h3>Předplatné / Subscription</h3><p>Podmínky odběru.</p></a>
</div>
"""

KNIHOVNA = """
<div class="grid g2">
  <a class="card" href="#" style="box-shadow:0 0 0 2px #2362A2 inset"><h3>Online katalog</h3><p>Vyhledávání ve fondu knihovny.</p></a>
  <a class="card" href="#"><h3>Služby a knihovní řád</h3><p>Podmínky využívání fondu.</p></a>
</div>
<h2>Novinky v katalogu</h2>
<p>Automatický výpis přírůstků za poslední rok.</p>
<ul class="doclist">
  <li><h3><a href="#">Přírůstky — 2. čtvrtletí 2026</a></h3><p>Nové tituly zařazené do fondu.</p></li>
  <li><h3><a href="#">Přírůstky — 1. čtvrtletí 2026</a></h3><p>Nové tituly zařazené do fondu.</p></li>
</ul>
"""

STP = """
<p>Systém stavebně technické prevence shromažďuje poznatky o poruchách a haváriích staveb.
Provozuje se ve spolupráci s Hasičským záchranným sborem ČR.</p>
<div class="grid g2">
  <a class="card" href="#" style="box-shadow:0 0 0 2px #2362A2 inset"><h3>Vstoupit do aplikace iSSTP</h3>
    <p>Evidence poruch a havárií staveb.</p></a>
  <a class="card" href="#"><h3>Metodika hlášení</h3><p>Kdo, co a v jaké lhůtě hlásí.</p></a>
</div>
"""

MAPY = """
<p>Mapový portál zpřístupňuje mapové aplikace a datové sady k územnímu rozvoji.</p>
<div class="btn-row"><a class="btn ghost" href="#">Přejít na mapový portál</a></div>
<div class="box note"><p>Část vrstev je neveřejná a vyžaduje přihlášení. Rozsah a způsob přihlášení se teprve rozhodne.</p></div>
"""

KONFERENCE = """
<p>Přehled konferencí a seminářů pořádaných ÚRÚ nebo konaných pod jeho záštitou.</p>
<ul class="doclist">
  <li><h3><a href="{{r}}clanek.html">Konference o územním rozvoji 2026</a></h3>
    <p>Program, prezentace a sborník.</p><div class="meta"><span>říjen 2026</span></div></li>
  <li><h3><a href="{{r}}clanek.html">Seminář k jednotnému standardu ÚPD</a></h3>
    <p>Pro pořizovatele a zpracovatele.</p><div class="meta"><span>září 2026</span></div></li>
</ul>
"""

ARCHIV = """
<div class="box note"><h3>Archiv</h3>
  <p>Obsah v této části je archivní. Nejde o aktivní agendu úřadu a materiály se neaktualizují.</p></div>
<h2>Výroční zprávy ÚÚR</h2>
<ul class="files">
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Výroční zpráva ÚÚR 2025</span><br>
    <span class="fmeta">historický kontext · 2 MB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Výroční zpráva ÚÚR 2024</span><br>
    <span class="fmeta">historický kontext · 2 MB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
</ul>
<h2>Historické projekty</h2>
<ul><li>CORCAP</li><li>INKA</li><li>MAS</li><li>Památka roku</li><li>SSTP 2009</li><li>UAP Karvinsko</li><li>Cestovní ruch</li></ul>
"""


def p(path, title, crumb, h1, body, perex=None):
    return dict(path="uzemni-rozvoj/" + path, title=title, section="uzemni-rozvoj",
                crumbs=C + [(crumb, None)], h1=h1, perex=perex, body=body)


PAGES = [
    dict(path="uzemni-rozvoj/index.html", title="Územní rozvoj", section="uzemni-rozvoj",
         crumbs=[("Územní rozvoj", None)], sidebar=False, h1="Územní rozvoj",
         perex="Agendy, dokumenty a aplikace převzaté od Ústavu územního rozvoje. Obsah pokračuje beze změny rozsahu.",
         body=ROZCESTNIK),
    p("uzemni-planovani.html", "Územní plánování", "Územní plánování", "Územní plánování", UP,
      "Strategické dokumenty územního plánování, evidence činnosti a navazující aplikace."),
    p("politika-uzemniho-rozvoje.html", "Politika územního rozvoje ČR", "Politika územního rozvoje ČR",
      "Politika územního rozvoje ČR", PUR),
    p("evidence-upc.html", "Evidence územně plánovací činnosti", "Evidence územně plánovací činnosti",
      "Evidence územně plánovací činnosti", EVIDENCE),
    p("informacni-web-up.html", "Informační web územního plánování", "Informační web územního plánování",
      "Informační web územního plánování", INFOWEB),
    p("uap.html", "Územně analytické podklady", "Územně analytické podklady",
      "Územně analytické podklady ČR", UAP),
    p("mezinarodni-spoluprace.html", "Mezinárodní spolupráce", "Mezinárodní spolupráce",
      "Mezinárodní spolupráce", MEZINARODNI),
    p("publikacni-cinnost.html", "Publikační činnost", "Publikační činnost", "Publikační činnost", PUBLIKACE),
    p("casopis.html", "Časopis UaÚR", "Časopis UaÚR", "Urbanismus a územní rozvoj", CASOPIS,
      "Odborný časopis vydávaný dvakrát ročně, bilingvní."),
    p("knihovna.html", "Knihovna", "Knihovna", "Knihovna", KNIHOVNA),
    p("stavebne-technicka-prevence.html", "Stavebně technická prevence", "Stavebně technická prevence",
      "Stavebně technická prevence", STP),
    p("mapovy-portal.html", "Mapový portál", "Mapový portál", "Mapový portál", MAPY),
    p("konference.html", "Konference a semináře", "Konference a semináře", "Konference a semináře", KONFERENCE),
    p("archiv.html", "Archiv", "Archiv", "Archiv", ARCHIV),
]
