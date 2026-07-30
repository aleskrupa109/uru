# -*- coding: utf-8 -*-
"""Úvodní stránka a výpis aktualit."""
from build import cmt, icon

HOME = """
<section class="hero">
  <span class="disc" aria-hidden="true"></span>
  <h1>Úřad rozvoje území</h1>
  <p>Povolujeme vyhrazené stavby, podporujeme stavební úřady a rozvíjíme územní plánování České republiky.</p>
</section>

<h2 class="plain">Co hledáte?</h2>
<div class="grid g4">
  <a class="card" href="{{r}}vyhrazene-stavby/index.html">""" + icon() + """
    <h3>Stavím nebo připravuji vyhrazenou stavbu</h3>
    <p>Povolování vyhrazených staveb, kategorie a příslušnost, formuláře ke stažení a kontakty na referenty.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/index.html">""" + icon() + """
    <h3>Jsem úředník stavebního úřadu nebo dotčeného orgánu</h3>
    <p>Metodická stanoviska, výklady zákona, Tisíc otázek ke stavebnímu právu a konzultační středisko.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/index.html">""" + icon() + """
    <h3>Hledám obsah, metodiky a dokumenty ÚÚR</h3>
    <p>Územní plánování, slovník územního rozvoje, příručky a publikace, časopis UaÚR, knihovna a archiv.</p></a>
  <a class="card" href="{{r}}kariera/index.html">""" + icon() + """
    <h3>Hledám práci a kariéru v ÚRÚ</h3>
    <p>Otevřené pozice, benefity, podmínky státní služby a průvodce procesem podání přihlášky.</p></a>
</div>

<div class="section-title">
  <h2>Aktuality""" + cmt(4, "Pořadí bloků: Informace o úřadu je nad Aktualitami i nad Rychlými odkazy. Zvážit posun níž.") + """</h2>
  <a href="{{r}}aktuality.html">Zobrazit vše""" + cmt(3, "Blok Aktuality má odkaz Zobrazit vše, ale cílová stránka výpisu aktualit není navržená.") + """</a>
</div>
<div class="newsgrid">
  <a class="news" href="{{r}}clanek.html">
    <div class="ph">ilustrační foto</div>
    <div class="b"><h3>ÚRÚ vznikne k 1. červenci 2026</h3>
      <div class="date">11. 11. 2026 · Aktualita</div>
      <p>Dopravní a energetický stavební úřad se transformuje na Úřad rozvoje území s rozšířenými kompetencemi v oblasti územního plánování a metodické podpory.</p></div></a>
  <div class="newsside">
    <a class="news" href="{{r}}clanek.html"><div class="ph">foto</div>
      <div class="b"><h3>Nové metodické pokyny pro stavební úřady</h3>
        <div class="date">11. 11. 2026 · Aktualita</div>
        <p>Aktualizované metodiky k posuzování záměrů v ochranných pásmech dopravní infrastruktury.</p></div></a>
    <a class="news" href="{{r}}clanek.html"><div class="ph">foto</div>
      <div class="b"><h3>Vyhlášení výběrových řízení na 12 pozic</h3>
        <div class="date">11. 11. 2026 · Tisková zpráva</div>
        <p>ÚRÚ hledá specialisty na stavební právo, územní plánování a správní řízení.</p></div></a>
  </div>
</div>

<div class="section-title"><h2>Rychlé odkazy</h2></div>
<div class="grid g3 quicklinks">
  <a class="qlink" href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html" data-ico="business-file">
    <h3>Formuláře ke stažení</h3>
    <p>Aktuální formuláře a vzory dokumentů pro řízení o vyhrazených stavbách.</p></a>
  <a class="qlink" href="{{r}}metodicka-podpora/tisic-otazek.html" data-ico="sos">
    <h3>Tisíc otázek ke stavebnímu právu</h3>
    <p>Databáze odpovědí na nejčastější dotazy úředníků ke stavebnímu zákonu.</p></a>
  <a class="qlink" href="{{r}}metodicka-podpora/metodicka-stanoviska.html" data-ico="info">
    <h3>Metodická stanoviska</h3>
    <p>Výklady a stanoviska k zákonu č. 283/2021 Sb. a č. 183/2006 Sb.</p></a>
  <a class="qlink" href="{{r}}kontakty.html" data-ico="contact">
    <h3>Kontakty</h3>
    <p>Kontakty na oddělení a referenty podle věcné příslušnosti agendy.</p></a>
  <a class="qlink" href="{{r}}uzemni-rozvoj/uzemni-planovani.html" data-ico="doc-filled">
    <h3>Slovník územního rozvoje</h3>
    <p>Výkladový slovník 2 690 pojmů z oblasti územního plánování a rozvoje.</p></a>
</div>

<div class="section-title"><h2>Časté dotazy</h2></div>
<ul class="hp-faq gov-list--plain">
  <li><a href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html">Jaké stavby spadají pod kompetenci ÚRÚ?</a></li>
  <li><a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co se mění v řízeních po 1. 7. 2026?</a></li>
  <li><a href="{{r}}metodicka-podpora/metodicka-stanoviska.html">Kde najdu metodická stanoviska k novému stavebnímu zákonu?</a></li>
  <li><a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Jak postupovat s řízeními zahájenými před 1. 7. 2026?</a></li>
  <li><a href="{{r}}uzemni-rozvoj/index.html">Kde najdu obsah, který byl dříve na uur.cz?</a></li>
  <li><a href="{{r}}kariera/prihlaska.html">Jak podat přihlášku do výběrového řízení?</a></li>
</ul>

<div class="section-title"><h2>Informace o úřadu</h2></div>
<div class="splitblock">
  <div>
    <p>ÚRÚ je specializovaný správní úřad vzniklý k 1. 7. 2026. Povoluje vyhrazené stavby, poskytuje metodickou podporu stavebním úřadům a zajišťuje agendy územního rozvoje převzaté od ÚÚR.</p>
    <ul>
      <li>Povolování vyhrazených staveb celostátního významu.</li>
      <li>Metodická podpora stavebních úřadů a dotčených orgánů.</li>
      <li>Přístup k územně analytickým podkladům a dokumentům.</li>
    </ul>
    <div class="btn-row"><a class="btn ghost" href="{{r}}o-uradu/kdo-jsme.html">Více o úřadu</a></div>
  </div>
  <figure class="hp-photo">
    <img src="{{r}}assets/img/sidlo-uradu.jpeg" alt="Sídlo Úřadu rozvoje území" loading="lazy">
    <figcaption>Sídlo úřadu — adresa se doplní</figcaption>
  </figure>
</div>
"""

AKTUALITY = """
<div class="filters" data-filterable>
  <div class="searchrow"><input type="search" data-q placeholder="Hledat v aktualitách…"></div>
  <div class="row">
    <div class="field"><label for="f-typ">Typ</label>
      <select id="f-typ" data-key="typ"><option value="">Vše</option>
        <option value="aktualita">Aktualita</option>
        <option value="tiskova">Tisková zpráva</option>
        <option value="metodika">Metodické sdělení</option></select></div>
    <div class="field"><label for="f-rok">Rok</label>
      <select id="f-rok" data-key="rok"><option value="">Vše</option>
        <option value="2026">2026</option><option value="2025">2025</option></select></div>
    <div class="field"><label for="f-tag">Štítek</label>
      <select id="f-tag" data-key="tag"><option value="">Vše</option>
        <option value="novela">novela</option><option value="kariera">kariéra</option>
        <option value="metodika">metodika</option><option value="uzemni-planovani">územní plánování</option></select></div>
    <div class="field"><label>&nbsp;</label><button class="btn ghost sm" type="button" data-reset>Zrušit filtry</button></div>
  </div>
  <div class="chips" data-chips></div>
  <p class="hint">Tiskové zprávy jsou zde součástí jednoho výpisu a odlišují se typem.""" + cmt(87, "Tiskové zprávy a Aktuality jsou dva obsahové typy bez společného výpisu. Rozhodnout, zda jsou tiskové zprávy podmnožinou aktualit.") + """
  Štítky ve výpisu i v článku vedou na tento výpis s předvyplněným filtrem.""" + cmt(94, "Tagy nemají cílovou stránku (výpis podle tagu).") + """</p>
</div>

<div class="resultbar"><span>Nalezeno <strong data-count>0</strong> záznamů</span></div>

<ul class="doclist" data-list>
  <li data-typ="aktualita" data-rok="2026" data-tag="novela" data-date="2026-11-11">
    <div class="tags"><span class="tag neutral">Aktualita</span><span class="tag hist">novela</span></div>
    <h3><a href="{{r}}clanek.html">ÚRÚ vznikne k 1. červenci 2026</a></h3>
    <p>Dopravní a energetický stavební úřad se transformuje na Úřad rozvoje území s rozšířenými kompetencemi.</p>
    <div class="meta"><span>11. 11. 2026</span></div></li>
  <li data-typ="aktualita" data-rok="2026" data-tag="metodika" data-date="2026-10-02">
    <div class="tags"><span class="tag neutral">Aktualita</span><span class="tag hist">metodika</span></div>
    <h3><a href="{{r}}clanek.html">Nové metodické pokyny pro stavební úřady</a></h3>
    <p>Aktualizované metodiky k posuzování záměrů v ochranných pásmech dopravní infrastruktury.</p>
    <div class="meta"><span>2. 10. 2026</span></div></li>
  <li data-typ="tiskova" data-rok="2026" data-tag="kariera" data-date="2026-09-18">
    <div class="tags"><span class="tag neutral">Tisková zpráva</span><span class="tag hist">kariéra</span></div>
    <h3><a href="{{r}}clanek.html">Vyhlášení výběrových řízení na 12 pozic</a></h3>
    <p>ÚRÚ hledá specialisty na stavební právo, územní plánování a správní řízení.</p>
    <div class="meta"><span>18. 9. 2026</span></div></li>
  <li data-typ="metodika" data-rok="2026" data-tag="uzemni-planovani" data-date="2026-08-05">
    <div class="tags"><span class="tag neutral">Metodické sdělení</span><span class="tag hist">územní plánování</span></div>
    <h3><a href="{{r}}clanek.html">Změna gesce metodické podpory územního plánování</a></h3>
    <p>Metodici územního plánování přecházejí z MMR na ÚRÚ. Kontakty najdete v sekci Metodická podpora.</p>
    <div class="meta"><span>5. 8. 2026</span></div></li>
  <li data-typ="tiskova" data-rok="2025" data-tag="novela" data-date="2025-12-11">
    <div class="tags"><span class="tag neutral">Tisková zpráva</span><span class="tag hist">novela</span></div>
    <h3><a href="{{r}}clanek.html">Novela stavebního zákona prošla Poslaneckou sněmovnou</a></h3>
    <p>Sněmovní tisk č. 67 mění rozsah vyhrazených staveb a postavení dotčených orgánů v řízení.</p>
    <div class="meta"><span>11. 12. 2025</span></div></li>
</ul>
<div class="empty" data-empty style="display:none">Zadanému filtru neodpovídá žádný záznam. Zkuste zrušit některý z filtrů.</div>
"""

PAGES = [
    dict(path="index.html", title="Úvod", section="", crumbs=None, body=HOME, sidebar=False),
    dict(path="aktuality.html", title="Aktuality", section="", sidebar=False,
         crumbs=[("Aktuality", None)],
         h1="Aktuality a tiskové zprávy",
         perex="Sdělení úřadu k legislativním změnám, metodické podpoře a výběrovým řízením.",
         body=AKTUALITY),
]
