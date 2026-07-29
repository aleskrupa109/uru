# -*- coding: utf-8 -*-
"""Sekce Vyhrazené stavby."""
from build import cmt

C = [("Vyhrazené stavby", "vyhrazene-stavby/index.html")]

ROZCESTNIK = """
<p class="hint" style="color:#5b6674">Pořadí dlaždic odpovídá pořadí položek v levém submenu podstránek.""" + cmt(12, "Zajistit, aby pořadí dlaždic odpovídalo pořadí v levém submenu na navazujících stránkách.") + """</p>
<div class="grid g3" style="margin-top:18px">
  <a class="card" href="{{r}}vyhrazene-stavby/co-meni-novela.html" style="border-color:#2372c4">
    <span class="order">1 / novinka</span>
    <h3>Co změní novela SZ""" + cmt(11, "Doplnit dlaždici „Co změní novela SZ\" jako první.") + """</h3>
    <p>Přehled všech změn na jednom místě: rozsah vyhrazených staveb, průběh řízení, rozpracovaná řízení a nové formuláře.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html"><span class="order">2</span>
    <h3>Co spadá pod ÚRÚ</h3>
    <p>Zjistěte, zda vaše stavba patří do kompetence ÚRÚ — včetně hraničních případů jako OZE, bateriová úložiště nebo větší bytové domy.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/jak-probiha-rizeni.html"><span class="order">3</span>
    <h3>Jak probíhá řízení</h3>
    <p>Krokový průvodce procesem povolování od záměru po vydání rozhodnutí. Zahrnuje změny platné od 1. 7. 2026.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html"><span class="order">4</span>
    <h3>Dokumenty a formuláře</h3>
    <p>Formuláře a vzory dokumentů ke stažení pro všechny typy řízení u ÚRÚ. Vždy aktuální verze.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/portal-stavebnika.html"><span class="order">5</span>
    <h3>Portál stavebníka</h3>
    <p>Průvodce přihlášením a podáním žádosti přes Portál stavebníka — co potřebujete mít připravené a jak postupovat.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/caste-dotazy.html"><span class="order">6</span>
    <h3>Odpovědi na nejčastější dotazy</h3>
    <p>Odpovědi na nejčastější otázky: co spadá pod ÚRÚ, jak probíhá řízení a co se mění od 1. 7. 2026.</p></a>
  <a class="card" href="{{r}}kontakty.html#stavebnici"><span class="order">7</span>
    <h3>Kontakty pro stavebníky</h3>
    <p>Kontaktní karty referentů podle typu vyhrazené stavby. Součást centrální stránky Kontakty.</p></a>
</div>
"""

NOVELA = """
<div class="box gap">
  <h3>Tato obrazovka zatím není navržená</h3>
  <p>Dlaždice a položka submenu jsou v maketě doplněné podle připomínky č. 11. Samotný návrh stránky
  (rozcestník změn, časová osa, blok „Týká se mě to?") je v seznamu připomínek označen jako bod ke zvážení,
  proto je zde jen provizorní obsah, aby maketa nekončila slepým odkazem.</p>
</div>
<h2>Týká se mě to?</h2>
<ul>
  <li>Připravuji nový záměr → <a href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html">co se mění v příslušnosti</a></li>
  <li>Mám běžící řízení u ÚRÚ → <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">přechodná ustanovení</a></li>
  <li>Mám běžící řízení u obecného stavebního úřadu, které nově spadne pod ÚRÚ → <a href="{{r}}metodicka-podpora/prechodove-obdobi.html#delimitace">delimitace</a></li>
  <li>Jsem účastník řízení → <a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html">co se mění pro účastníky</a></li>
</ul>
<h2>Pro stavební úřady a dotčené orgány</h2>
<p>Odpovídající přehled pro úřady najdete v sekci <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Metodická podpora → Přechodové období</a>.</p>
"""

CO_SPADA = """
<div class="box change">
  <h3>Co se mění od 1. 7. 2026</h3>
  <p>Přibývají nové kategorie vyhrazených staveb. Souhrn všech změn na jednom místě najdete na stránce
  <a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co změní novela SZ</a>.""" + cmt(15, "Na stránce jsou dva různé typy zvýrazněných boxů. Po vzniku stránky o novele by měl být první z nich odkaz, ne samostatný text.") + """</p>
</div>

<div class="filters">
  <h2 style="margin-top:0;font-size:20px">Ověření příslušnosti""" + cmt(14, "Přehled kategorií je dlouhý plochý seznam. Zvážit funkční prvek pro ověření příslušnosti — filtr podle typu stavby nebo jednoduchý průvodce.") + """</h2>
  <p class="hint" style="margin:0 0 12px">Vyberte typ záměru a zobrazí se vám odpověď, zda spadá pod ÚRÚ, nebo pod obecný stavební úřad.</p>
  <div class="row">
    <div class="field" style="min-width:280px"><label for="pruv">Typ záměru</label>
      <select id="pruv" onchange="document.querySelectorAll('[data-verdict]').forEach(function(e){e.style.display='none'});var t=document.querySelector('[data-verdict=\\''+this.value+'\\']');if(t)t.style.display='';">
        <option value="">— vyberte —</option>
        <option value="dalnice">Dálnice nebo rychlostní silnice</option>
        <option value="draha">Železniční dráha, metro, tramvajová dráha</option>
        <option value="letiste">Letiště a letecké stavby</option>
        <option value="energetika">Přenosová a přepravní energetická soustava</option>
        <option value="oze">Výrobna elektřiny z obnovitelných zdrojů</option>
        <option value="baterie">Bateriové úložiště</option>
        <option value="bytovy">Bytový dům</option>
        <option value="jine">Jiná stavba</option>
      </select></div>
  </div>
  <div data-verdict="dalnice" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Dálnice, rychlostní silnice a jejich přeložky jsou vyhrazenými stavbami bez ohledu na rozsah.</p></div>
  <div data-verdict="draha" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Železniční koridory a tratě celostátního významu, metro a tramvajové dráhy ve statutárních městech.</p></div>
  <div data-verdict="letiste" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Civilní letecké stavby, dráhy ke vzletu a přistávání, letiště mezinárodního významu.</p></div>
  <div data-verdict="energetika" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Stavby přenosové soustavy a přepravní soustavy plynu.</p></div>
  <div data-verdict="oze" style="display:none" class="box edge"><h3>Záleží na instalovaném výkonu — hraniční případ</h3><p>Rozhoduje instalovaný výkon a umístění. Doporučujeme ověřit u referenta ještě před přípravou dokumentace.</p></div>
  <div data-verdict="baterie" style="display:none" class="box edge"><h3>Hraniční případ</h3><p>Bateriová úložiště se posuzují podle výkonu a vazby na přenosovou soustavu.</p></div>
  <div data-verdict="bytovy" style="display:none" class="box edge"><h3>Hraniční případ</h3><p>Bytové domy spadají pod ÚRÚ až od stanovené hranice rozsahu. Prahovou hodnotu ověřte u referenta.</p></div>
  <div data-verdict="jine" style="display:none" class="box edge"><h3>Pravděpodobně obecný stavební úřad</h3><p>Pokud si nejste jistí, napište nám — příslušnost ověříme bez podání žádosti.</p></div>
</div>

<h2>Přehled kategorií vyhrazených staveb</h2>

<h3>Dopravní stavby — dálnice</h3>
<p>Stavby dálnic a rychlostních silnic celostátního významu.</p>
<ul><li>Dálnice a rychlostní silnice (investor: ŘSD)</li><li>Přeložky dálnic a rychlostních silnic</li></ul>

<h3>Dopravní stavby — dráhy</h3>
<p>Stavby železničních drah, metra a tramvajových tratí celostátního významu.</p>
<ul><li>Železniční koridory a tratě (investor: Správa železnic)</li>
<li>Metro ve statutárních městech</li><li>Tramvajové dráhy ve statutárních městech</li>
<li>Stavby drah dle zákona č. 266/1994 Sb.</li></ul>

<h3>Dopravní stavby — letecké</h3>
<p>Civilní letecké stavby.</p>
<ul><li>Dráhy ke vzletu a přistávání letadel</li><li>Plochy určené k pohybu a stání letadel</li>
<li>Letiště mezinárodního významu</li></ul>

<h3>Energetické stavby</h3>
<p>Stavby přenosové a přepravní soustavy a navazující infrastruktury.</p>
<ul><li>Vedení přenosové soustavy a transformovny</li><li>Přepravní soustava plynu a zásobníky</li>
<li>Výrobny elektřiny nad stanovený instalovaný výkon</li></ul>

<h3>Strategické investiční stavby</h3>
<p>Stavby vymezené zákonem o urychlení výstavby strategicky významné infrastruktury.</p>

<div class="box edge">
  <h3>Hraniční případy</h3>
  <p>U obnovitelných zdrojů, bateriových úložišť a bytových domů rozhoduje kombinace typu, rozsahu a umístění.
  Než začnete připravovat dokumentaci, ověřte si příslušnost dotazem — vyhnete se podání na nesprávný úřad.</p>
  <div class="btn-row"><a class="btn ghost" href="{{r}}kontakty.html#stavebnici">Ověřit příslušnost u referenta</a></div>
</div>
"""

RIZENI_TABS = """
<div class="tabs">
  <a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni.html"@A1@>Pro stavebníky</a>
  <a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html"@A2@>Pro účastníky řízení</a>
</div>
<p class="updated">Obě zobrazení mají vlastní adresu a vlastní položku v levém submenu.""" + cmt(17, "Záložky Pro stavebníky / Pro účastníky řízení nejsou zastoupené v levém submenu ani v drobečkové navigaci.") + """</p>
"""

RIZENI = RIZENI_TABS.replace('@A1@', ' aria-current="page"').replace('@A2@', '') + """
<p>Řízení o povolení vyhrazené stavby probíhá podle stavebního zákona. Zde najdete přehled kroků od záměru po vydání rozhodnutí.</p>
<p>Řízení o povolení záměru je jedno integrované řízení, které nahrazuje dřívější oddělené územní a stavební řízení.
ÚRÚ jako specializovaný úřad vede toto řízení pro vyhrazené stavby a koordinuje vyjádření všech dotčených orgánů.</p>

<div class="box change">
  <h3>Co se mění od 1. 7. 2026</h3>
  <p>Dotčené orgány (hygienici, hasiči, ochrana přírody, správci vod a další) jsou nově integrováni přímo do řízení ÚRÚ.
  Jako stavebník komunikujete pouze s ÚRÚ — nemusíte sami obíhat jednotlivé orgány a shánět jejich stanoviska.
  Souhrn změn: <a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co změní novela SZ</a>.</p>
</div>

<ol class="steps">
  <li><h3>Příprava záměru</h3>
    <p>Stavebník zpracuje projektovou dokumentaci v rozsahu stanoveném vyhláškou. Dokumentace musí být ve formátu PDF,
    elektronicky podepsaná autorizovanou osobou s kvalifikovaným elektronickým razítkem.</p>
    <p class="updated">Délka: závisí na složitosti projektu</p></li>
  <li><h3>Podání žádosti</h3>
    <p>Žádost se podává prostřednictvím Portálu stavebníka, datovou schránkou, poštou nebo osobně.
    Projektová dokumentace musí být nejpozději v okamžiku podání nahrána v evidenci elektronických dokumentací přes Portál stavebníka.</p>
    <p>Formuláře najdete v sekci <a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html">Dokumenty a formuláře</a>.</p></li>
  <li><h3>Kontrola úplnosti</h3>
    <p>Úřad posoudí úplnost žádosti do 5 pracovních dnů. Pokud žádost obsahuje vady, vyzve stavebníka k doplnění a stanoví lhůtu.
    Po dobu doplňování lhůta pro vydání rozhodnutí neběží.</p></li>
  <li><h3>Vyjádření dotčených orgánů</h3>
    <p>ÚRÚ si vyžádá vyjádření dotčených orgánů a koordinuje je v rámci jednoho řízení.</p></li>
  <li><h3>Rozhodnutí</h3>
    <p>Úřad vydá rozhodnutí o povolení záměru, případně žádost zamítne. Rozhodnutí se doručuje účastníkům řízení.</p></li>
  <li><h3>Odvolání a právní moc</h3>
    <p>Proti rozhodnutí lze podat odvolání. Po marném uplynutí lhůty nabývá rozhodnutí právní moci.</p></li>
</ol>

<h2 id="poplatky">Správní poplatky</h2>
<p>Některé úkony ÚRÚ podléhají správním poplatkům podle sazebníku správních poplatků.
Toto je primární místo, kde se poplatky popisují; ostatní stránky sem pouze odkazují.""" + cmt(19, "Správní poplatky jsou zde i na str. 7. Určit primární umístění a druhé místo řešit odkazem.") + """</p>
<table class="t"><tr><th>Úkon</th><th>Poplatek</th></tr>
<tr><td>Žádost o povolení záměru</td><td>dle sazebníku</td></tr>
<tr><td>Změna rozhodnutí</td><td>dle sazebníku</td></tr></table>

<h2>Další typy řízení</h2>
<ul>
  <li>Vyvlastňovací řízení</li>
  <li>Odvolací řízení</li>
  <li>Zkušební provoz a kolaudace</li>
</ul>
"""

RIZENI_U = RIZENI_TABS.replace('@A1@', '').replace('@A2@', ' aria-current="page"') + """
<h2>Nahlížení do spisu</h2>
<p>Účastníci řízení a osoby, které prokáží právní zájem, mohou nahlížet do spisu vedeného ÚRÚ.
Nahlížení se sjednává předem, spis je veden v elektronické podobě.</p>
<ol class="steps">
  <li><h3>Zjistěte spisovou značku</h3><p>Najdete ji v oznámení o zahájení řízení nebo na úřední desce.</p></li>
  <li><h3>Požádejte o nahlédnutí</h3><p>Písemně, datovou schránkou nebo osobně. Uveďte, v jakém postavení do spisu nahlížíte.</p></li>
  <li><h3>Nahlédnutí do spisu</h3><p>Úřad sjedná termín. Z dokumentů lze pořizovat kopie a výpisy.</p></li>
</ol>
<h2>Co se mění pro účastníky řízení</h2>
<p>Podrobnosti k dopadům novely najdete na stránce <a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co změní novela SZ</a>.</p>
"""

DOKUMENTY = """
<div class="filters" data-filterable>
  <p class="hint" style="margin:0 0 12px">Formuláře jsou členěné podle typu stavby a typu řízení.""" + cmt(22, "Plochý seznam příloh neobstojí při reálném počtu formulářů. Doplnit členění podle typu stavby / typu řízení a filtr.") + """
  U každého souboru je uvedena platnost a verze.""" + cmt(23, "Chybí metadata u souborů (platnost od, verze).") + """</p>
  <div class="searchrow"><input type="search" data-q placeholder="Hledat ve formulářích a vzorech…"></div>
  <div class="row">
    <div class="field"><label for="f-stavba">Typ stavby</label>
      <select id="f-stavba" data-key="stavba"><option value="">Vše</option>
        <option value="doprava">Dopravní stavby</option><option value="energetika">Energetické stavby</option>
        <option value="strategicka">Strategické investiční stavby</option><option value="vse">Společné pro všechny</option></select></div>
    <div class="field"><label for="f-rizeni">Typ řízení</label>
      <select id="f-rizeni" data-key="rizeni"><option value="">Vše</option>
        <option value="povoleni">Povolení záměru</option><option value="zmena">Změna rozhodnutí</option>
        <option value="kolaudace">Kolaudace a zkušební provoz</option><option value="vyvlastneni">Vyvlastnění</option></select></div>
    <div class="field"><label for="f-format">Formát</label>
      <select id="f-format" data-key="format"><option value="">Vše</option>
        <option value="PDF">PDF</option><option value="DOCX">DOCX</option></select></div>
    <div class="field"><label>&nbsp;</label><button class="btn ghost sm" type="button" data-reset>Zrušit filtry</button></div>
  </div>
  <div class="chips" data-chips></div>
</div>

<div class="resultbar"><span>Nalezeno <strong data-count>0</strong> souborů</span></div>

<ul class="files" data-list>
  <li data-stavba="vse" data-rizeni="povoleni" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Žádost o povolení záměru</span><br>
    <span class="fmeta">verze 3.0 · platné od 1. 7. 2026 · 296 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="vse" data-rizeni="povoleni" data-format="DOCX"><span class="ft">DOCX</span>
    <span class="grow"><span class="name">Příloha — identifikace záměru</span><br>
    <span class="fmeta">verze 3.0 · platné od 1. 7. 2026 · 128 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="doprava" data-rizeni="povoleni" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Vzor průvodní zprávy — dopravní stavby</span><br>
    <span class="fmeta">verze 2.1 · platné od 1. 7. 2026 · 402 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="energetika" data-rizeni="povoleni" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Vzor průvodní zprávy — energetické stavby</span><br>
    <span class="fmeta">verze 2.1 · platné od 1. 7. 2026 · 388 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="vse" data-rizeni="zmena" data-format="DOCX"><span class="ft">DOCX</span>
    <span class="grow"><span class="name">Žádost o změnu rozhodnutí</span><br>
    <span class="fmeta">verze 1.4 · platné od 1. 7. 2026 · 176 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="vse" data-rizeni="kolaudace" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Žádost o kolaudační rozhodnutí</span><br>
    <span class="fmeta">verze 1.2 · platné od 1. 7. 2026 · 210 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="vse" data-rizeni="vyvlastneni" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Návrh na zahájení vyvlastňovacího řízení</span><br>
    <span class="fmeta">verze 1.0 · platné od 1. 7. 2026 · 264 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
</ul>
<div class="empty" data-empty style="display:none">Zadanému filtru neodpovídá žádný soubor.</div>

<h2>Projektová dokumentace</h2>
<p>Veškerá projektová dokumentace musí být podána v elektronické podobě (PDF), opatřena elektronickým autorizačním razítkem
s kvalifikovaným elektronickým podpisem a kvalifikovaným časovým razítkem. Dokumentace se vkládá prostřednictvím
Portálu stavebníka do evidence elektronických dokumentací.</p>

<h2>Správní poplatky</h2>
<p>Přehled poplatků, čísla účtu a variabilních symbolů najdete na stránce
<a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni.html#poplatky">Jak probíhá řízení</a>.""" + cmt(19, "Správní poplatky jsou na dvou místech. Zde ponechán pouze odkaz na primární umístění.") + """</p>

<div class="box note">
  <h3>Potřebujete pomoct?</h3>
  <p>Máte otázky? Napište nám — rádi poradíme. Kontakty podle typu stavby najdete na stránce
  <a href="{{r}}kontakty.html#stavebnici">Kontakty</a>.</p>
</div>
"""

PORTAL = """
<p>Žádosti o povolení vyhrazené stavby se podávají prostřednictvím Portálu stavebníka — státního online systému
pro komunikaci se stavebními úřady. Před přechodem na portál si přečtěte, co budete potřebovat.</p>

<h2>Co potřebujete mít připravené</h2>
<ul>
  <li>Prostředek pro elektronickou identifikaci (bankovní identita, eObčanka, NIA ID)</li>
  <li>Projektovou dokumentaci v PDF s autorizačním razítkem</li>
  <li>Vyplněný formulář žádosti — viz <a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html">Dokumenty a formuláře</a></li>
</ul>

<ol class="steps">
  <li><h3>Přihlášení do portálu</h3><p>Přihlaste se pomocí elektronické identity.</p></li>
  <li><h3>Vložení dokumentace</h3><p>Dokumentaci nahrajte do evidence elektronických dokumentací. Systém přidělí ID dokumentace.</p></li>
  <li><h3>Podání žádosti</h3><p>Vyplňte žádost, uveďte ID dokumentace a jako příjemce zvolte Úřad rozvoje území.</p></li>
</ol>

<div class="btn-row"><a class="btn" href="#">Přejít na Portál stavebníka</a></div>
"""

FAQ_VS = """
<div class="filters">
  <div class="searchrow"><input type="search" id="faqq" placeholder="Hledat v otázkách…"
    oninput="var q=this.value.toLowerCase();document.querySelectorAll('[data-faq]').forEach(function(d){d.style.display=d.textContent.toLowerCase().indexOf(q)>-1?'':'none'});document.querySelectorAll('[data-faqgroup]').forEach(function(g){g.style.display=g.querySelectorAll('[data-faq]:not([style*=none])').length?'':'none'})"></div>
  <p class="hint" style="margin:0">Vyhledávání prochází znění otázek i odpovědí.""" + cmt(26, "FAQ je členěné do šesti skupin bez vyhledávání. Doplnit vyhledávání v otázkách.") + """</p>
</div>

<div data-faqgroup><h2>Příslušnost ÚRÚ</h2>
<details class="acc" data-faq><summary>Co je to vyhrazená stavba?</summary><div class="body"><p>Vyhrazené stavby jsou stavby celostátního a nadregionálního významu vyjmenované v příloze stavebního zákona.</p></div></details>
<details class="acc" data-faq><summary>Spadá moje stavba pod ÚRÚ, nebo pod obecný stavební úřad?</summary><div class="body"><p>Použijte ověření příslušnosti na stránce <a href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html">Co spadá pod ÚRÚ</a>.</p></div></details>
<details class="acc" data-faq><summary>Jaký je rozdíl mezi ÚRÚ a běžným stavebním úřadem?</summary><div class="body"><p>ÚRÚ je specializovaný správní úřad s celostátní působností pro vyjmenované typy staveb.</p></div></details>
<details class="acc" data-faq><summary>Moje solární elektrárna má instalovaný výkon 3 MW — spadá pod ÚRÚ?</summary><div class="body"><p>Rozhoduje instalovaný výkon a umístění. Jde o hraniční případ, doporučujeme ověřit u referenta.</p></div></details>
<details class="acc" data-faq><summary>Bytový dům nad jakou hranicí spadá pod ÚRÚ?</summary><div class="body"><p>Prahovou hodnotu ověřte u referenta, hranice se s novelou mění.</p></div></details>
</div>

<div data-faqgroup><h2>Přechodové období</h2>
<details class="acc" data-faq><summary>Co se stalo s DESÚ? Je ÚRÚ jeho nástupcem?</summary><div class="body"><p>ÚRÚ přebírá agendy zaniklého DESÚ i ÚÚR.</p></div></details>
<details class="acc" data-faq><summary>Mám zahájené řízení na DESÚ — co se s ním stane?</summary><div class="body"><p>Viz <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a>.</p></div></details>
<details class="acc" data-faq><summary>Mám pravomocné rozhodnutí vydané dříve — je stále platné?</summary><div class="body"><p>Pravomocná rozhodnutí zůstávají v platnosti.</p></div></details>
<details class="acc" data-faq><summary>Jsou závazná stanoviska dotčených orgánů vydaná dříve stále platná?</summary><div class="body"><p>Viz přechodná ustanovení novely.</p></div></details>
</div>

<div data-faqgroup><h2>Proces řízení</h2>
<details class="acc" data-faq><summary>Jak probíhá integrované řízení a co to znamená pro moji stavbu?</summary><div class="body"><p>Viz <a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni.html">Jak probíhá řízení</a>.</p></div></details>
<details class="acc" data-faq><summary>Musím sám obstarat závazná stanoviska od dotčených orgánů?</summary><div class="body"><p>Nemusíte. Vyjádření dotčených orgánů zajišťuje ÚRÚ v rámci řízení.</p></div></details>
<details class="acc" data-faq><summary>Jak dlouho trvá řízení o povolení záměru?</summary><div class="body"><p>Lhůty jsou uvedené u jednotlivých kroků řízení.</p></div></details>
<details class="acc" data-faq><summary>Co dělat, když ÚRÚ vyzve k doplnění žádosti?</summary><div class="body"><p>Doplňte podklady ve stanovené lhůtě. Po dobu doplňování lhůta pro vydání rozhodnutí neběží.</p></div></details>
</div>

<div data-faqgroup><h2>Dokumentace a technické požadavky</h2>
<details class="acc" data-faq><summary>V jakém formátu musí být projektová dokumentace?</summary><div class="body"><p>PDF s autorizačním razítkem a kvalifikovaným časovým razítkem.</p></div></details>
<details class="acc" data-faq><summary>Co je to ID dokumentace a kde ho najdu?</summary><div class="body"><p>ID přiděluje evidence elektronických dokumentací po nahrání přes Portál stavebníka.</p></div></details>
</div>

<div data-faqgroup><h2>Správní poplatky</h2>
<details class="acc" data-faq><summary>Jaké správní poplatky se platí a za co?</summary><div class="body"><p>Viz <a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni.html#poplatky">Správní poplatky</a>.</p></div></details>
<details class="acc" data-faq><summary>Jak a kam uhradit správní poplatek?</summary><div class="body"><p>Údaje k platbě obdržíte spolu s výzvou k úhradě.</p></div></details>
</div>
"""

PAGES = [
    dict(path="vyhrazene-stavby/index.html", title="Vyhrazené stavby", section="vyhrazene-stavby",
         crumbs=[("Vyhrazené stavby", None)], sidebar=False,
         h1="Vyhrazené stavby",
         perex="Úřad rozvoje území povoluje vyhrazené stavby celostátního významu. Zjistěte, zda vaše stavba spadá pod ÚRÚ, jak probíhá řízení a kde najdete potřebné dokumenty.",
         body=ROZCESTNIK),
    dict(path="vyhrazene-stavby/co-meni-novela.html", title="Co změní novela SZ", section="vyhrazene-stavby",
         crumbs=C + [("Co změní novela SZ", None)],
         h1="Co změní novela stavebního zákona", perex="Přehled změn pro stavebníky a projektanty vyhrazených staveb.",
         body=NOVELA),
    dict(path="vyhrazene-stavby/co-spada-pod-uru.html", title="Co spadá pod ÚRÚ", section="vyhrazene-stavby",
         crumbs=C + [("Co spadá pod ÚRÚ", None)],
         h1="Co spadá pod ÚRÚ",
         perex="Úřad rozvoje území je stavebním úřadem pro vyhrazené stavby — stavby celostátního a nadregionálního významu vyjmenované v příloze stavebního zákona.",
         updated="Přehled kategorií naposledy aktualizován 12. 6. 2026." + cmt(16, "Chybí datum poslední aktualizace přehledu — u obsahu vázaného na legislativu je to funkční prvek."),
         body=CO_SPADA),
    dict(path="vyhrazene-stavby/jak-probiha-rizeni.html", title="Jak probíhá řízení", section="vyhrazene-stavby",
         crumbs=C + [("Jak probíhá řízení", None)], h1="Jak probíhá řízení", body=RIZENI),
    dict(path="vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html", title="Jak probíhá řízení — pro účastníky",
         section="vyhrazene-stavby", crumbs=C + [("Jak probíhá řízení", "vyhrazene-stavby/jak-probiha-rizeni.html"), ("Pro účastníky řízení", None)],
         h1="Jak probíhá řízení", body=RIZENI_U),
    dict(path="vyhrazene-stavby/dokumenty-a-formulare.html", title="Dokumenty a formuláře", section="vyhrazene-stavby",
         crumbs=C + [("Dokumenty a formuláře", None)], h1="Dokumenty a formuláře",
         perex="Formuláře, vzory a požadavky na projektovou dokumentaci pro všechny typy řízení u ÚRÚ.",
         body=DOKUMENTY),
    dict(path="vyhrazene-stavby/portal-stavebnika.html", title="Portál stavebníka", section="vyhrazene-stavby",
         crumbs=C + [("Portál stavebníka", None)], h1="Portál stavebníka", body=PORTAL),
    dict(path="vyhrazene-stavby/caste-dotazy.html", title="Odpovědi na nejčastější otázky", section="vyhrazene-stavby",
         crumbs=C + [("Odpovědi na nejčastější otázky", None)], h1="Odpovědi na nejčastější otázky",
         body=FAQ_VS),
]
