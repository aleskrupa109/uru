# -*- coding: utf-8 -*-
"""Kariéra, O úřadu, Kontakty, úřední deska, vyhledávání a šablony."""
from build import cmt
import content_extra2 as E

KAR = [("Kariéra", "kariera/index.html")]
OU = [("O úřadu", "o-uradu/index.html")]

KARIERA = E.KARIERA

POZICE = """
<div class="filters" data-filterable>
  <div class="searchrow"><input type="search" data-q placeholder="Hledejte podle názvu pozice nebo oblasti"></div>
  <div class="row">
    <div class="field"><label for="p-pomer">Typ poměru</label>
      <select id="p-pomer" data-key="pomer"><option value="">Vše</option>
        <option value="sluzebni">Služební poměr (státní služba)</option>
        <option value="pracovni">Pracovní poměr (zákoník práce)</option></select></div>
    <div class="field"><label for="p-trida">Platová třída</label>
      <select id="p-trida" data-key="trida"><option value="">Vše</option>
        <option value="11">11</option><option value="12">12</option><option value="13">13</option></select></div>
    <div class="field"><label for="p-obor">Obor</label>
      <select id="p-obor" data-key="obor"><option value="">Vše</option>
        <option value="sr">Stavební řád</option><option value="up">Územní plánování</option>
        <option value="it">IT a digitalizace</option><option value="provoz">Provoz a podpora</option></select></div>
    <div class="field"><label for="p-lok">Lokalita</label>
      <select id="p-lok" data-key="lokalita"><option value="">Vše</option>
        <option value="praha">Praha</option><option value="brno">Brno</option></select></div>
    <div class="field"><label for="p-uvazek">Úvazek</label>
      <select id="p-uvazek" data-key="uvazek"><option value="">Vše</option>
        <option value="plny">Plný</option><option value="castecny">Částečný</option></select></div>
    <div class="field"><label>&nbsp;</label><button class="btn ghost sm" type="button" data-reset>Zrušit filtry</button></div>
  </div>
  <div class="chips" data-chips></div>
  <p class="hint">Typ poměru je uvedený jako první filtr — je to hlavní rozhodovací kritérium uchazečů
  z jiných úřadů.""" + cmt(75, "Typ poměru je podle person hlavní rozhodovací kritérium, ale ve filtrech je až mezi ostatními.") + """
  Platová třída je samostatný filtr.""" + cmt(74, "Chybí filtr podle platové třídy, který IA uvádí.") + """</p>
</div>

<div class="resultbar"><span>Nalezeno <strong data-count>0</strong> pozic</span></div>

<ul class="doclist" data-list>
  <li data-pomer="sluzebni" data-trida="12" data-obor="sr" data-lokalita="praha" data-uvazek="plny" data-date="2026-07-01">
    <div class="tags"><span class="tag neutral">Služební poměr</span><span class="tag hist">12. platová třída</span></div>
    <h3><a href="{{r}}kariera/detail-pozice.html">Referent povolování dálnic a rychlostních silnic</a></h3>
    <p>Vedení řízení o povolení záměru u dopravních a energetických staveb.</p>
    <div class="meta"><span>Praha</span><span>plný úvazek</span><span>přihlášky do 31. 8. 2026</span></div></li>
  <li data-pomer="sluzebni" data-trida="13" data-obor="up" data-lokalita="brno" data-uvazek="plny" data-date="2026-07-01">
    <div class="tags"><span class="tag neutral">Služební poměr</span><span class="tag hist">13. platová třída</span></div>
    <h3><a href="{{r}}kariera/detail-pozice.html">Referent povolování dopravních staveb — dráhy</a></h3>
    <p>Metodické vedení úřadů územního plánování a zpracování stanovisek.</p>
    <div class="meta"><span>Brno</span><span>plný úvazek</span><span>přihlášky do 31. 8. 2026</span></div></li>
  <li data-pomer="pracovni" data-trida="12" data-obor="it" data-lokalita="praha" data-uvazek="plny" data-date="2026-06-15">
    <div class="tags"><span class="tag neutral">Pracovní poměr</span><span class="tag hist">12. platová třída</span></div>
    <h3><a href="{{r}}kariera/detail-pozice.html">Specialista digitalizace agend</a></h3>
    <p>Rozvoj informačních systémů úřadu a integrace na eGovernment služby.</p>
    <div class="meta"><span>Praha</span><span>plný úvazek</span><span>přihlášky do 15. 8. 2026</span></div></li>
  <li data-pomer="pracovni" data-trida="11" data-obor="provoz" data-lokalita="praha" data-uvazek="castecny" data-date="2026-06-01">
    <div class="tags"><span class="tag neutral">Pracovní poměr</span><span class="tag hist">11. platová třída</span></div>
    <h3><a href="{{r}}kariera/detail-pozice.html">Referent spisové služby</a></h3>
    <p>Správa dokumentů a podpora agend úřadu.</p>
    <div class="meta"><span>Praha</span><span>částečný úvazek</span><span>přihlášky do 15. 8. 2026</span></div></li>
</ul>
<div class="empty" data-empty style="display:none">Zadanému filtru neodpovídá žádná pozice.</div>
"""

DETAIL_POZICE = (E.DETAIL_POZICE
                 .replace("{c78}", cmt(78, "Chybí vazba na PDF s oficiálním textem výběrového řízení na úřední desce."))
                 .replace("{c77}", cmt(77, "Chybí obrazovka formuláře přihlášky. Tlačítko Odpovědět nemá cíl.")))

PRIHLASKA = """
<p>Přihlášku lze podat online formulářem, datovou schránkou nebo poštou. Online formulář se odesílá
do spisové služby úřadu a je mu přiděleno číslo jednací.</p>

<div class="filters">
  <div class="row">
    <div class="field" style="min-width:260px"><label for="a1">Jméno a příjmení</label><input id="a1"></div>
    <div class="field" style="min-width:260px"><label for="a2">E-mail</label><input id="a2" type="email"></div>
    <div class="field" style="min-width:260px"><label for="a3">Telefon</label><input id="a3"></div>
  </div>
  <div class="row" style="margin-top:14px">
    <div class="field" style="min-width:320px"><label for="a4">Pozice, o kterou se ucházíte</label>
      <select id="a4"><option>Referent stavebního řádu — vyhrazené stavby</option>
        <option>Metodik územního plánování</option><option>Specialista digitalizace agend</option></select></div>
    <div class="field" style="min-width:320px"><label for="a5">Životopis (PDF)</label><input id="a5" type="file"></div>
  </div>
  <div class="row" style="margin-top:14px">
    <div class="field" style="flex:1;min-width:100%"><label for="a6">Motivační text</label>
      <textarea id="a6" rows="5" style="font:inherit;padding:10px;border:1px solid #D8DEE5;border-radius:6px"></textarea></div>
  </div>
  <p style="margin:14px 0 0"><label><input type="checkbox"> Souhlasím se zpracováním osobních údajů pro účely výběrového řízení.</label></p>
  <div class="btn-row"><button class="btn" type="button">Odeslat přihlášku</button>
    <a class="btn ghost" href="#">Stáhnout formulář v PDF</a></div>
</div>

<h2>Co se stane po odeslání</h2>
<ol class="steps">
  <li><h3>Potvrzení přijetí</h3><p>Obdržíte e-mail s číslem jednacím.</p></li>
  <li><h3>Posouzení přihlášek</h3><p>Po uplynutí lhůty úřad posoudí splnění podmínek.</p></li>
  <li><h3>Pozvánka k pohovoru</h3><p>Vybrané uchazeče kontaktujeme.</p></li>
</ol>
"""

OURAD = """
<div class="grid g3 hub">
  <a class="card" href="{{r}}o-uradu/kdo-jsme.html"><h3>Kdo jsme a co děláme</h3>
    <p>Kompetence, zákonný základ, vznik z DESÚ</p></a>
  <a class="card" href="{{r}}o-uradu/organizacni-struktura.html"><h3>Organizační struktura</h3>
    <p>Vedení úřadu a organizační schéma</p></a>
  <a class="card" href="{{r}}o-uradu/pro-media.html"><h3>Pro média</h3>
    <p>Dedikovaný kontakt pro novináře a tiskové zprávy</p></a>
  <a class="card" href="{{r}}o-uradu/povinne-informace.html"><h3>Povinné informace</h3>
    <p>Zákonně zveřejňované dokumenty ke stažení</p></a>
  <a class="card" href="#"><span class="order">Externí odkaz</span><h3>Veřejné zakázky</h3>
    <p>Odkaz na profil zadavatele v NEN</p></a>
  <a class="card" href="{{r}}o-uradu/povinne-informace.html#o17"><h3>Výroční zprávy</h3>
    <p>Výroční zprávy podle zákona o svobodném přístupu k informacím</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/konference.html"><h3>Konference a semináře</h3>
    <p>Akce pod záštitou ÚRÚ</p></a>
  <a class="card" href="{{r}}kontakty.html"><h3>Kontakty""" + cmt(83, "Doplnit dlaždici Kontakty — z rozcestníku O úřadu na ně nevede cesta.") + """</h3>
    <p>Adresa, datová schránka a kontakty podle agendy</p></a>
</div>
"""

KDO_JSME = E.KDO_JSME

ORG = """
<div class="box note">
  <p>Granularita schématu (vedení / odbory / oddělení / jmenovití pracovníci) se upřesní podle výsledné
  organizační struktury úřadu. Do té doby je zobrazena úroveň odborů.</p>
</div>
<h2>Vedení úřadu</h2>
<table class="t">
  <tr><th style="width:280px">Ředitel úřadu</th><td>jméno se doplní</td></tr>
  <tr><th>Zástupce ředitele</th><td>jméno se doplní</td></tr>
</table>
<h2>Odbory</h2>
<table class="t">
  <tr><th style="width:36%">Odbor</th><th>Agenda</th><th>Kontakt</th></tr>
  <tr><td>Odbor stavebního řádu</td><td>Povolování vyhrazených staveb</td><td><a href="{{r}}kontakty.html#stavebnici">kontakt</a></td></tr>
  <tr><td>Odbor územního plánování</td><td>Metodika a strategické dokumenty</td><td><a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">kontakt</a></td></tr>
  <tr><td>Odbor metodiky</td><td>Metodická stanoviska a konzultační středisko</td><td><a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">kontakt</a></td></tr>
  <tr><td>Odbor provozu a digitalizace</td><td>Informační systémy a spisová služba</td><td><a href="{{r}}kontakty.html">kontakt</a></td></tr>
</table>
<p class="hint" style="color:#717171">Kontaktní údaje se zobrazují z centrální stránky Kontakty, která je jediným zdrojem dat.""" + cmt(92, "Určit jeden zdroj kontaktních dat a pravidlo, co se kde zobrazuje.") + """</p>
"""

MEDIA = E.PRO_MEDIA + """
<h2>Tiskové zprávy</h2>
<p>Tiskové zprávy jsou součástí společného výpisu aktualit a odlišují se typem.""" + cmt(87, "Tiskové zprávy a Aktuality jsou dva obsahové typy bez společného výpisu.") + """</p>
<div class="btn-row"><a class="btn ghost" href="{{r}}aktuality.html">Zobrazit všechny tiskové zprávy</a></div>
<ul class="doclist">
  <li><h3><a href="{{r}}clanek.html">ÚRÚ přebírá rozhodování o nových kategoriích vyhrazených staveb</a></h3>
    <p>Mezi vyhrazené stavby nově patří i stavby v zastavitelných plochách nad 45 ha.
    Stavebníci těchto projektů podávají žádosti o povolení u ÚRÚ.</p>
    <div class="meta"><span>18. 9. 2026</span></div></li>
  <li><h3><a href="{{r}}clanek.html">Vyhlášení výběrových řízení na 12 pozic</a></h3>
    <div class="meta"><span>18. 9. 2026</span></div></li>
</ul>
"""

# Povinně zveřejňované informace: číslovaná struktura podle §5 zák. 106/1999 Sb.
POVINNE = ('<div class="toc"><h2>Obsah stránky</h2><ol>'
           + "".join(f'<li><a href="#o{n.replace(".", "-")}">{n} {t}</a></li>'
                     for n, t, _d in E.POVINNE)
           + '</ol></div>'
           + '<p class="hint">Položky, které mají vlastní podstránku, jsou označené odkazem.'
           + cmt(89, "Doplnit, které z položek mají vlastní podstránku a které jsou jen odstavcem.")
           + '</p>')
_ODKAZY = {"3": '{{r}}o-uradu/organizacni-struktura.html',
           "4": '{{r}}kontakty.html', "12": '{{r}}vyhrazene-stavby/dokumenty-a-formulare.html'}
for _n, _t, _d in E.POVINNE:
    POVINNE += f'<h2 id="o{_n.replace(".", "-")}">{_n} {_t}</h2>'
    if _n in _ODKAZY:
        POVINNE += f'<p>Viz <a href="{_ODKAZY[_n]}">{_t}</a> — vlastní podstránka.</p>'
    elif _n == "17":
        POVINNE += ('<ul class="files"><li><span class="ft">PDF</span>'
                    '<span class="grow"><span class="name">Výroční zpráva za rok 2026</span><br>'
                    '<span class="fmeta">dle §18 zák. č. 106/1999 Sb.</span></span>'
                    '<a class="btn ghost sm" href="#">Stáhnout</a></li></ul>')
    else:
        POVINNE += f'<p>{_d}</p>'
POVINNE += ('<h2>Veřejné zakázky</h2><p>Profil zadavatele je veden v NEN.</p>'
            '<div class="btn-row"><a class="btn ghost" href="#">Přejít na profil zadavatele</a></div>')

KONTAKTY = """
<div class="box note">
  <p>Tato stránka je jediným zdrojem kontaktních dat. Kontakty zobrazené v sekcích Vyhrazené stavby,
  Metodická podpora a v organizační struktuře se načítají odsud.""" + cmt(92, "Kontakty jsou na třech místech. Určit jeden zdroj dat a pravidlo, co se kde zobrazuje.") + """</p>
</div>

<h2>Centrální kontakt</h2>
<table class="t">
  <tr><th style="width:220px">Adresa</th><td>doplní se</td></tr>
  <tr><th>Datová schránka</th><td>doplní se</td></tr>
  <tr><th>Podatelna</th><td>posta@uru.gov.cz</td></tr>
  <tr><th>Telefonní ústředna</th><td>+420 000 000 000</td></tr>
  <tr><th>IČO</th><td>doplní se</td></tr>
</table>

""" + E.KONTAKTY_POBOCKY + """
<h2>Kontakty podle agendy""" + cmt(91, "Chybí členění podle agendy a oddělení, což je napříč personami nejsilnější opakovaná potřeba.") + """</h2>
<div class="contactcards">
  <div class="contactcard" id="stavebnici"><h3>Vyhrazené stavby — dopravní</h3>
    <p class="role">Odbor stavebního řádu, oddělení dopravních staveb</p>
    <p class="agenda">Dálnice, dráhy, letecké stavby — povolení záměru, změny, kolaudace</p>
    <dl><dt>E-mail</dt><dd>doprava@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
  <div class="contactcard"><h3>Vyhrazené stavby — energetické</h3>
    <p class="role">Odbor stavebního řádu, oddělení energetických staveb</p>
    <p class="agenda">Přenosová soustava, přepravní soustava plynu, výrobny elektřiny</p>
    <dl><dt>E-mail</dt><dd>energetika@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
  <div class="contactcard"><h3>Ověření příslušnosti</h3>
    <p class="role">Odbor stavebního řádu</p>
    <p class="agenda">Obecný úvodní dotaz — spadá moje stavba pod ÚRÚ?</p>
    <dl><dt>E-mail</dt><dd>prislusnost@uru.gov.cz</dd></dl></div>
  <div class="contactcard"><h3>Metodická podpora</h3>
    <p class="role">Odbor metodiky</p>
    <p class="agenda">Výkladové dotazy stavebních úřadů a dotčených orgánů</p>
    <dl><dt>Karty</dt><dd><a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">Kontakty na metodiky</a></dd></dl></div>
  <div class="contactcard" id="hr"><h3>Personální oddělení (HR)</h3>
    <p class="role">Výběrová řízení a podmínky zaměstnání</p>
    <p class="agenda">Dotazy k pozicím, přihláškám a služebnímu poměru</p>
    <dl><dt>E-mail</dt><dd>kariera@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
  <div class="contactcard" id="media"><h3>Kontakt pro média</h3>
    <p class="role">Tiskové dotazy</p>
    <p class="agenda">Vyjádření úřadu, podklady pro novináře</p>
    <dl><dt>E-mail</dt><dd>media@uru.gov.cz</dd></dl></div>
</div>
""" + E.KONTAKTY_ODDELENI

DESKA = """
<div class="box gap">
  <h3>Tato obrazovka zatím není navržená</h3>
  <p>O způsobu řešení úřední desky se teprve rozhodne — buď stránka dodaná dodavatelem elektronické spisové služby,
  nebo vlastní stránka napojená přes API. Maketa obsahuje pouze provizorní výpis, aby položka hlavní navigace
  nekončila slepým odkazem.</p>
</div>
<ul class="doclist">
  <li><h3><a href="#">Oznámení o zahájení řízení — modernizace železničního koridoru</a></h3>
    <div class="meta"><span>Vyvěšeno 20. 7. 2026</span><span>Sejmuto 4. 8. 2026</span></div></li>
  <li><h3><a href="#">Oznámení o vyhlášení výběrového řízení — referent stavebního řádu</a></h3>
    <div class="meta"><span>Vyvěšeno 15. 7. 2026</span><span>Sejmuto 31. 8. 2026</span></div></li>
  <li><h3><a href="#">Veřejná vyhláška — doručení rozhodnutí</a></h3>
    <div class="meta"><span>Vyvěšeno 8. 7. 2026</span><span>Sejmuto 23. 7. 2026</span></div></li>
</ul>
"""

VYHLEDAVANI = """
<div class="filters" data-filterable>
  <div class="searchrow"><input type="search" data-q placeholder="Zadejte hledaný výraz…" value=""></div>
  <div class="row">
    <div class="field"><label for="v-typ">Typ obsahu</label>
      <select id="v-typ" data-key="typ"><option value="">Vše</option>
        <option value="stranka">Stránka</option><option value="stanovisko">Metodické stanovisko</option>
        <option value="formular">Formulář</option><option value="otazka">Otázka a odpověď</option>
        <option value="pozice">Pracovní pozice</option><option value="deska">Úřední deska</option></select></div>
    <div class="field"><label for="v-sekce">Sekce</label>
      <select id="v-sekce" data-key="sekce"><option value="">Vše</option>
        <option value="vs">Vyhrazené stavby</option><option value="mp">Metodická podpora</option>
        <option value="ur">Územní rozvoj</option><option value="kar">Kariéra</option>
        <option value="ou">O úřadu</option></select></div>
    <div class="field"><label for="v-zakon">Zákon</label>
      <select id="v-zakon" data-key="zakon"><option value="">Vše</option>
        <option value="283">283/2021 Sb.</option><option value="183">183/2006 Sb.</option></select></div>
    <div class="field"><label for="v-platnost">Platnost</label>
      <select id="v-platnost" data-key="platnost"><option value="">Vše</option>
        <option value="platna">Platná</option><option value="neplatna">Neplatná</option></select></div>
    <div class="field"><label>&nbsp;</label><button class="btn ghost sm" type="button" data-reset>Zrušit filtry</button></div>
  </div>
  <div class="chips" data-chips></div>
  <p class="hint">Fasety jsou upravené pro obsah ÚRÚ — původní šablona design systému pro služby
  (Občan / Podnikatel / Czech POINT) se sem nehodí.""" + cmt(96, "Šablona je převzatá z design systému pro služby. Pro ÚRÚ je potřeba jiná sada faset.") + """
  Vyhledávání prochází i obsah připojených PDF.""" + cmt(98, "Chybí indikace, že se prohledává i obsah příloh (PDF).") + """</p>
</div>

<div class="resultbar">
  <span>Nalezeno <strong data-count>0</strong> výsledků</span>
  <span class="right"><label>Řadit podle
    <select data-sort><option value="rel">relevance</option><option value="date">data</option></select></label></span>
</div>

<ul class="doclist" data-list>
  <li data-typ="stranka" data-sekce="vs" data-zakon="" data-platnost="" data-date="2026-06-12">
    <div class="tags"><span class="tag neutral">Stránka</span><span class="tag hist">Vyhrazené stavby</span></div>
    <h3><a href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html">Co spadá pod ÚRÚ</a></h3>
    <p>Přehled kategorií vyhrazených staveb a hraničních případů.</p></li>
  <li data-typ="stanovisko" data-sekce="mp" data-zakon="283" data-platnost="platna" data-date="2026-07-10">
    <div class="tags"><span class="tag neutral">Metodické stanovisko</span><span class="tag valid">Platná</span></div>
    <h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko ke změnám v povolovacích procesech</a></h3>
    <p>Shoda nalezena i v textu připojeného PDF (str. 4).</p></li>
  <li data-typ="formular" data-sekce="vs" data-zakon="" data-platnost="platna" data-date="2026-07-01">
    <div class="tags"><span class="tag neutral">Formulář</span></div>
    <h3><a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html">Žádost o povolení záměru (PDF)</a></h3>
    <p>verze 3.0 · platné od 1. 7. 2026</p></li>
  <li data-typ="otazka" data-sekce="mp" data-zakon="283" data-platnost="" data-date="2026-06-03">
    <div class="tags"><span class="tag neutral">Otázka a odpověď</span></div>
    <h3><a href="{{r}}metodicka-podpora/tisic-otazek-heslo.html">Kdo je dotčeným orgánem v řízení?</a></h3>
    <p>Heslo Dotčené orgány, Tisíc otázek ke stavebnímu právu.</p></li>
  <li data-typ="pozice" data-sekce="kar" data-zakon="" data-platnost="" data-date="2026-07-01">
    <div class="tags"><span class="tag neutral">Pracovní pozice</span></div>
    <h3><a href="{{r}}kariera/detail-pozice.html">Referent stavebního řádu — vyhrazené stavby</a></h3>
    <p>Praha · služební poměr · přihlášky do 31. 8. 2026</p></li>
  <li data-typ="stanovisko" data-sekce="mp" data-zakon="183" data-platnost="neplatna" data-date="2023-04-14">
    <div class="tags"><span class="tag neutral">Metodické stanovisko</span><span class="tag invalid">Neplatná</span></div>
    <h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Stanovisko ke společnému územnímu a stavebnímu řízení</a></h3>
    <p>Historický dokument ponechaný kvůli kontinuitě.</p></li>
</ul>
<div class="empty" data-empty style="display:none">
  Zadanému dotazu neodpovídá žádný výsledek.<br>
  Zkuste zrušit filtry, nebo pokračujte na <a href="{{r}}vyhrazene-stavby/index.html">Vyhrazené stavby</a>,
  <a href="{{r}}metodicka-podpora/index.html">Metodickou podporu</a> nebo
  <a href="{{r}}uzemni-rozvoj/index.html">Územní rozvoj</a>.
</div>
"""

CLANEK = """
<p class="updated">11. 11. 2026 · Aktualita ·
  <a href="{{r}}aktuality.html">novela</a>, <a href="{{r}}aktuality.html">transformace</a>""" + cmt(94, "Tagy nemají cílovou stránku (výpis podle tagu).") + """</p>
<p>Perex článku shrnuje sdělení v jednom odstavci. Šablona se používá pro aktuality, tiskové zprávy
i obecné textové stránky.</p>
<h2>Mezititulek</h2>
<p>Tělo článku. Text je pracovní a nahradí se finálním zněním.</p>
<ul><li>Odrážka</li><li>Odrážka</li></ul>
<h2>Přílohy</h2>
<ul class="files"><li><span class="ft">PDF</span>
  <span class="grow"><span class="name">Příloha k článku</span><br><span class="fmeta">296 kB</span></span>
  <a class="btn ghost sm" href="#">Stáhnout</a></li></ul>
"""

MAPA = """
<div class="grid g3">
  <div class="card"><h3><a href="{{r}}vyhrazene-stavby/index.html">Vyhrazené stavby</a></h3>
    <ul><li><a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co změní novela SZ</a></li>
    <li><a href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html">Co spadá pod ÚRÚ</a></li>
    <li><a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni.html">Jak probíhá řízení</a>
      <ul><li><a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html">Pro účastníky řízení</a></li></ul></li>
    <li><a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html">Dokumenty a formuláře</a></li>
    <li><a href="{{r}}vyhrazene-stavby/portal-stavebnika.html">Portál stavebníka</a></li>
    <li><a href="{{r}}vyhrazene-stavby/caste-dotazy.html">Odpovědi na nejčastější otázky</a></li></ul></div>

  <div class="card"><h3><a href="{{r}}metodicka-podpora/index.html">Metodická podpora</a></h3>
    <ul><li><a href="{{r}}metodicka-podpora/metodicka-stanoviska.html">Metodická stanoviska a výklady</a>
      <ul><li><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Detail stanoviska</a></li></ul></li>
    <li><a href="{{r}}metodicka-podpora/caste-dotazy.html">Časté dotazy</a></li>
    <li><a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a></li>
    <li><a href="{{r}}metodicka-podpora/standardizace.html">Standardizace ÚP</a></li>
    <li><a href="{{r}}metodicka-podpora/konzultacni-stredisko.html">Konzultační středisko</a></li>
    <li><a href="{{r}}metodicka-podpora/tisic-otazek.html">Tisíc otázek</a>
      <ul><li><a href="{{r}}metodicka-podpora/tisic-otazek-seznam.html">Seznam hesel</a>
        <ul><li><a href="{{r}}metodicka-podpora/tisic-otazek-heslo.html">Heslo</a></li></ul></li></ul></li>
    <li><a href="{{r}}metodicka-podpora/dotcene-organy.html">Přehled dotčených orgánů</a></li>
    <li><a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">Kontakty na metodiky</a></li></ul></div>

  <div class="card"><h3><a href="{{r}}uzemni-rozvoj/index.html">Územní rozvoj</a></h3>
    <ul><li><a href="{{r}}uzemni-rozvoj/uzemni-planovani.html">Územní plánování</a>
      <ul><li><a href="{{r}}uzemni-rozvoj/politika-uzemniho-rozvoje.html">Politika územního rozvoje ČR</a></li>
      <li><a href="{{r}}uzemni-rozvoj/evidence-upc.html">Evidence ÚP činnosti</a></li>
      <li><a href="{{r}}uzemni-rozvoj/informacni-web-up.html">Informační web ÚP</a></li></ul></li>
    <li><a href="{{r}}uzemni-rozvoj/uap.html">Územně analytické podklady</a></li>
    <li><a href="{{r}}uzemni-rozvoj/mezinarodni-spoluprace.html">Mezinárodní spolupráce</a></li>
    <li><a href="{{r}}uzemni-rozvoj/publikacni-cinnost.html">Publikační činnost</a></li>
    <li><a href="{{r}}uzemni-rozvoj/casopis.html">Časopis UaÚR</a></li>
    <li><a href="{{r}}uzemni-rozvoj/knihovna.html">Knihovna</a></li>
    <li><a href="{{r}}uzemni-rozvoj/stavebne-technicka-prevence.html">Stavebně technická prevence</a></li>
    <li><a href="{{r}}uzemni-rozvoj/mapovy-portal.html">Mapový portál</a></li>
    <li><a href="{{r}}uzemni-rozvoj/konference.html">Konference a semináře</a></li>
    <li><a href="{{r}}uzemni-rozvoj/archiv.html">Archiv</a></li></ul></div>

  <div class="card"><h3><a href="{{r}}kariera/index.html">Kariéra</a></h3>
    <ul><li><a href="{{r}}kariera/otevrene-pozice.html">Otevřené pozice</a>
      <ul><li><a href="{{r}}kariera/detail-pozice.html">Detail pozice</a></li></ul></li>
    <li><a href="{{r}}kariera/prihlaska.html">Jak podat přihlášku</a></li></ul></div>

  <div class="card"><h3><a href="{{r}}o-uradu/index.html">O úřadu</a></h3>
    <ul><li><a href="{{r}}o-uradu/kdo-jsme.html">Kdo jsme a co děláme</a></li>
    <li><a href="{{r}}o-uradu/organizacni-struktura.html">Organizační struktura</a></li>
    <li><a href="{{r}}o-uradu/pro-media.html">Pro média</a></li>
    <li><a href="{{r}}o-uradu/povinne-informace.html">Povinně zveřejňované informace</a></li></ul></div>

  <div class="card"><h3>Ostatní</h3>
    <ul><li><a href="{{r}}aktuality.html">Aktuality</a></li>
    <li><a href="{{r}}uredni-deska.html">Úřední deska</a></li>
    <li><a href="{{r}}kontakty.html">Kontakty</a></li>
    <li><a href="{{r}}vyhledavani.html">Vyhledávání</a></li>
    <li><a href="{{r}}clanek.html">Šablona článku</a></li></ul></div>
</div>
"""

PAGES = [
    dict(help="hr", path="kariera/index.html", title="Kariéra", section="kariera", crumbs=[("Kariéra", None)],
         h1="Kariéra v ÚRÚ", perex="Hledáme odborníky na stavební právo, územní plánování a digitalizaci agend.",
         body=KARIERA),
    dict(help="hr", path="kariera/otevrene-pozice.html", title="Otevřené pozice", section="kariera",
         crumbs=KAR + [("Otevřené pozice", None)], h1="Otevřené pozice", body=POZICE),
    dict(help="hr", path="kariera/detail-pozice.html", title="Detail pozice", section="kariera",
         crumbs=KAR + [("Otevřené pozice", "kariera/otevrene-pozice.html"), ("Detail pozice", None)],
         h1="Referent stavebního řádu — vyhrazené stavby", body=DETAIL_POZICE),
    dict(help="hr", path="kariera/prihlaska.html", title="Jak podat přihlášku", section="kariera",
         crumbs=KAR + [("Jak podat přihlášku", None)], h1="Jak podat přihlášku", body=PRIHLASKA),

    dict(path="o-uradu/index.html", title="O úřadu", section="o-uradu", crumbs=[("O úřadu", None)],
         sidebar=False, h1="O úřadu", perex="Úřad rozvoje území vznikl transformací Dopravního a energetického stavebního úřadu (DESÚ). Přebírá agendy DESÚ a Ústavu územního rozvoje (ÚÚR).",
         body=OURAD),
    dict(path="o-uradu/kdo-jsme.html", title="Kdo jsme a co děláme", section="o-uradu",
         crumbs=OU + [("Kdo jsme a co děláme", None)], h1="Kdo jsme a co děláme",
         perex="Úřad rozvoje území (ÚRÚ) vznikl transformací Dopravního a energetického stavebního úřadu (DESÚ). Přebíráme agendy DESÚ a Ústavu územního rozvoje (ÚÚR) a stáváme se klíčovou institucí reformované státní stavební správy.",
         body=KDO_JSME),
    dict(path="o-uradu/organizacni-struktura.html", title="Organizační struktura", section="o-uradu",
         crumbs=OU + [("Organizační struktura", None)], h1="Organizační struktura", body=ORG),
    dict(help="media", path="o-uradu/pro-media.html", title="Pro média", section="o-uradu",
         crumbs=OU + [("Pro média", None)], h1="Pro média", body=MEDIA),
    dict(path="o-uradu/povinne-informace.html", title="Povinně zveřejňované informace", section="o-uradu",
         crumbs=OU + [("Povinně zveřejňované informace", None)], h1="Povinně zveřejňované informace",
         body=POVINNE),

    dict(path="kontakty.html", title="Kontakty", section="kontakty", sidebar=False,
         crumbs=[("Kontakty", None)], h1="Kontakty", body=KONTAKTY),
    dict(path="uredni-deska.html", title="Úřední deska", section="uredni-deska", sidebar=False,
         crumbs=[("Úřední deska", None)], h1="Úřední deska", body=DESKA),
    dict(path="vyhledavani.html", title="Vyhledávání", section="", sidebar=False,
         crumbs=[("Vyhledávání", None)], h1="Výsledky vyhledávání", body=VYHLEDAVANI),
    dict(path="clanek.html", title="Šablona článku", section="", sidebar=False,
         crumbs=[("Aktuality", "aktuality.html"), ("Nadpis článku", None)], h1="Nadpis článku", body=CLANEK),
    dict(path="mapa-webu.html", title="Mapa webu", section="", sidebar=False,
         crumbs=[("Mapa webu", None)], h1="Mapa webu", body=MAPA),
]
