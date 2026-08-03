# -*- coding: utf-8 -*-
"""Sekce Vyhrazené stavby — obsah přepsaný podle návrhu (DESU_design.pdf, str. 3–9).

Odchylky od návrhu vycházejí ze zeleně schválených komentářů a jsou v maketě
označené značkou s číslem připomínky.
"""
from build import cmt
import content_vs_extra as X

C = [("Vyhrazené stavby", "vyhrazene-stavby/index.html")]

ROZCESTNIK = """
<p class="hint">Pořadí dlaždic odpovídá pořadí položek v levém submenu podstránek.""" + cmt(12, "Zajistit, aby pořadí dlaždic odpovídalo pořadí v levém submenu na navazujících stránkách.") + """</p>
<div class="grid g3" style="margin-top:18px">
  <a class="card" href="{{r}}vyhrazene-stavby/co-meni-novela.html">
    <span class="order">novinka</span>
    <h3>Co změní novela SZ""" + cmt(11, "Doplnit dlaždici „Co změní novela SZ\" jako první.") + """</h3>
    <p>Přehled všech změn na jednom místě: rozsah vyhrazených staveb, průběh řízení, rozpracovaná řízení a nové formuláře.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html">
    <h3>Co spadá pod ÚRÚ</h3>
    <p>Zjistěte, zda vaše stavba patří do kompetence ÚRÚ — včetně hraničních případů jako OZE, bateriová úložiště nebo větší bytové domy.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/jak-probiha-rizeni.html">
    <h3>Jak probíhá řízení</h3>
    <p>Krokový průvodce procesem povolování od záměru po vydání rozhodnutí. Zahrnuje změny platné od 1. 7. 2026.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html">
    <h3>Dokumenty a formuláře</h3>
    <p>Formuláře a vzory dokumentů ke stažení pro všechny typy řízení u ÚRÚ. Vždy aktuální verze.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/portal-stavebnika.html">
    <h3>Portál stavebníka</h3>
    <p>Průvodce přihlášením a podáním žádosti přes Portál stavebníka — co potřebujete mít připravené a jak postupovat.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/caste-dotazy.html">
    <h3>Odpovědi na nejčastější dotazy</h3>
    <p>Odpovědi na nejčastější otázky: co spadá pod ÚRÚ, jak probíhá řízení a co se mění od 1. 7. 2026.</p></a>
  <a class="card" href="{{r}}kontakty.html#stavebnici">
    <h3>Kontakty pro stavebníky</h3>
    <p>Kontakty na referenty podle typu stavby a věcné příslušnosti.</p></a>
</div>
"""

NOVELA = """
<div class="box gap">
  <h3>Tato obrazovka zatím není navržená</h3>
  <p>Dlaždice a položka submenu jsou v maketě doplněné podle připomínky č. 11. Samotný návrh
  stránky je v seznamu připomínek označen jako bod ke zvážení, proto je zde jen provizorní
  obsah, aby maketa nekončila slepým odkazem.</p>
</div>
<h2>Týká se mě to?</h2>
<ul>
  <li>Připravuji nový záměr → <a href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html">co se mění v příslušnosti</a></li>
  <li>Mám běžící řízení u ÚRÚ → <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">přechodná ustanovení</a></li>
  <li>Mám běžící řízení u obecného stavebního úřadu, které nově spadne pod ÚRÚ → <a href="{{r}}metodicka-podpora/prechodove-obdobi.html#delimitace">delimitace</a></li>
  <li>Jsem účastník řízení → <a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html">co se mění pro účastníky</a></li>
</ul>
<h2>Pro stavební úřady a dotčené orgány</h2>
<p>Odpovídající přehled pro úřady najdete na stránce
<a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Metodická podpora → Přechodové období</a>.</p>
"""

CO_SPADA = """
<div class="box change">
  <h3>Co se mění od 1. 7. 2026</h3>
  <p>Přibývají nové kategorie vyhrazených staveb. Souhrn všech změn na jednom místě najdete
  na stránce <a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co změní novela SZ</a>.""" + cmt(15, "Na stránce jsou dva různé typy zvýrazněných boxů. Po vzniku stránky o novele by měl být první z nich odkaz, ne samostatný text.") + """</p>
</div>

<div class="filters">
  <h2 style="margin-top:0">Ověření příslušnosti""" + cmt(14, "Přehled kategorií je dlouhý plochý seznam. Zvážit funkční prvek pro ověření příslušnosti — filtr podle typu stavby nebo jednoduchý průvodce.") + """</h2>
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
        <option value="plocha">Stavba v zastavitelné ploše nad 45 ha</option>
        <option value="jine">Jiná stavba</option>
      </select></div>
  </div>
  <div data-verdict="dalnice" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Dálnice, rychlostní silnice a jejich přeložky jsou vyhrazenými stavbami bez ohledu na rozsah.</p></div>
  <div data-verdict="draha" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Železniční koridory a tratě celostátního významu, metro a tramvajové dráhy ve statutárních městech.</p></div>
  <div data-verdict="letiste" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Civilní letecké stavby, dráhy ke vzletu a přistávání, letiště mezinárodního významu.</p></div>
  <div data-verdict="energetika" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Stavby přenosové soustavy a přepravní soustavy plynu.</p></div>
  <div data-verdict="oze" style="display:none" class="box edge"><h3>Záleží na instalovaném výkonu</h3><p>Fotovoltaické elektrárny nad 5 MW a ostatní obnovitelné zdroje nad 1 MW spadají pod ÚRÚ.</p></div>
  <div data-verdict="baterie" style="display:none" class="box edge"><h3>Hraniční případ</h3><p>Bateriová úložiště se posuzují podle výkonu a vazby na přenosovou soustavu. Doporučujeme ověřit u referenta.</p></div>
  <div data-verdict="bytovy" style="display:none" class="box edge"><h3>Hraniční případ</h3><p>Velké bytové projekty mohou spadat pod ÚRÚ jako stavby v zastavitelných plochách nad 45 ha.</p></div>
  <div data-verdict="plocha" style="display:none" class="box edge"><h3>Spadá pod ÚRÚ</h3><p>Stavby pro výrobu, skladování a bydlení v plochách vymezených pro tyto účely nad 45 ha.</p></div>
  <div data-verdict="jine" style="display:none" class="box edge"><h3>Pravděpodobně obecný stavební úřad</h3><p>Pokud si nejste jistí, napište nám — příslušnost ověříme bez podání žádosti.</p></div>
</div>
""" + X.KATEGORIE + """
<div class="box edge">
  <h3>Hraniční případ</h3>
  <p>Do kategorie staveb v zastavitelných plochách nad 45 ha patří i velké bytové projekty —
  mnoho stavebníků to nečeká. Než začnete připravovat dokumentaci, ověřte si příslušnost
  dotazem; vyhnete se podání na nesprávný úřad.</p>
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
<p>Řízení o povolení vyhrazené stavby probíhá podle stavebního zákona. Zde najdete přehled
kroků od záměru po vydání rozhodnutí.</p>
<p>Řízení o povolení záměru je jedno integrované řízení, které nahrazuje dřívější oddělené
územní a stavební řízení. ÚRÚ jako specializovaný úřad vede toto řízení pro vyhrazené stavby
a koordinuje vyjádření všech dotčených orgánů.</p>

<div class="box change">
  <h3>Co se mění od 1. 7. 2026</h3>
  <p>Dotčené orgány (hygienici, hasiči, ochrana přírody, správci vod a další) jsou nově
  integrováni přímo do řízení ÚRÚ. Jako stavebník komunikujete pouze s ÚRÚ — nemusíte sami
  obíhat jednotlivé orgány a shánět jejich stanoviska. Souhrn změn:
  <a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co změní novela SZ</a>.</p>
</div>

<ol class="steps">
  <li><h3>Příprava záměru</h3>
    <p>Stavebník zpracuje projektovou dokumentaci v rozsahu stanoveném vyhláškou. Dokumentace
    musí být ve formátu PDF, elektronicky podepsaná autorizovanou osobou s kvalifikovaným
    elektronickým razítkem.</p>
    <p class="updated">Délka: závisí na složitosti projektu</p></li>
  <li><h3>Podání žádosti</h3>
    <p>Žádost se podává prostřednictvím Portálu stavebníka, datovou schránkou, e-mailem,
    poštou nebo osobně. Projektová dokumentace musí být nejpozději v okamžiku podání nahrána
    v evidenci elektronických dokumentací přes Portál stavebníka.</p>
    <p>Formuláře najdete v sekci <a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html">Dokumenty a formuláře</a>.</p>
    <table class="t"><tr><th style="width:150px">Povinné</th><td>vložení projektové dokumentace přes Portál stavebníka</td></tr>
    <tr><th>Dobrovolné</th><td>ostatní komunikace včetně samotné žádosti — tu lze podat i datovou schránkou, e-mailem, poštou nebo osobně</td></tr></table></li>
  <li><h3>Kontrola úplnosti</h3>
    <p>ÚRÚ zkontroluje úplnost žádosti. Pokud žádost obsahuje vady, vyzve stavebníka
    k doplnění a stanoví lhůtu. Po dobu doplňování lhůta pro vydání rozhodnutí neběží.</p></li>
  <li><h3>Vyjádření dotčených orgánů</h3>
    <p>ÚRÚ si vyžádá vyjádření dotčených orgánů — typicky orgánů ochrany přírody, krajské
    hygieny, hasičského záchranného sboru a dalších. Vyjádření koordinuje úřad. Například ochranu
    veřejného zdraví posuzuje ÚRÚ přímo — nevydávají k ní samostatná stanoviska krajské
    hygienické stanice jako dříve.</p></li>
  <li><h3>Posouzení záměru</h3>
    <p>Úřad posoudí soulad záměru s územním rozvojovým plánem, regulačním plánem a technickými
    požadavky na výstavbu.</p></li>
  <li><h3>Rozhodnutí</h3>
    <p>Úřad vydá rozhodnutí o povolení záměru, případně žádost zamítne. Rozhodnutí vydá
    do 60 dnů od zahájení řízení, ve složitých případech do 90 dnů. Rozhodnutí se doručuje
    účastníkům řízení.</p></li>
  <li><h3>Odvolání a právní moc</h3>
    <p>Proti rozhodnutí se mohou účastníci řízení odvolat do 15 dnů. Pokud se nikdo neodvolá,
    rozhodnutí nabude právní moci. Stavebník může zahájit stavbu po nabytí právní moci
    a splnění podmínek rozhodnutí.</p></li>
</ol>

<h2>Další typy řízení</h2>
<h3>Vyvlastňovací řízení</h3>
<p>ÚRÚ vede vyvlastňovací řízení pro vyhrazené stavby. Jde o řízení, při kterém lze odejmout
nebo omezit vlastnická práva k nemovitostem za účelem veřejného zájmu. Vyžaduje předchozí pokus
o dohodu s vlastníkem a náhradu určenou znaleckým posudkem. Řízení je ústní a koncentrované —
námitky a důkazy je třeba uplatnit v jeho průběhu.</p>
<h3>Odvolací řízení</h3>
<p>ÚRÚ rozhoduje o odvoláních proti rozhodnutím krajských stavebních úřadů v případech
spadajících do jeho působnosti. Jedná se o kontrolu zákonnosti, nikoli nové projednání věci.</p>
<h3>Zkušební provoz a kolaudace</h3>
<p>ÚRÚ vydává povolení zkušebního provozu a provádí kolaudaci dokončených vyhrazených staveb.</p>

<h2>Správní poplatky</h2>
<p>Některé úkony ÚRÚ podléhají správním poplatkům dle položky č. 18 a 19 sazebníku
zákona č. 634/2004 Sb. Přehled poplatků, číslo účtu a variabilní symbol najdete na stránce
<a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html#poplatky">Dokumenty a formuláře</a>.""" + cmt(19, "Správní poplatky jsou na dvou místech. Primární umístění je Dokumenty a formuláře, zde zůstává odkaz.") + """</p>
"""

RIZENI_U = RIZENI_TABS.replace('@A1@', '').replace('@A2@', ' aria-current="page"') + """
<h2>Nahlížení do spisu</h2>
<p>Nahlížení do spisu stavebního úřadu upravuje správní řád. Nahlížet může každý, kdo je
účastníkem řízení. O nahlížení může požádat i každý, kdo prokáže právní zájem nebo jiný vážný
důvod — co je tímto důvodem, se vždy posuzuje v kontextu všech okolností daného případu.
Současně platí, že nahlédnutím do spisu takového účastníka nemůže být narušeno právo
některého z účastníků ani veřejný zájem.</p>
<p>Nahlížení do spisu musí být umožněno i osobě nevidomé — té musí být spis či jeho část
úředníkem přečtena.</p>

<h2>Postup</h2>
<ul>
  <li>projděte si záložky s informacemi, nebo</li>
  <li>vyplňte kontaktní formulář se svým dotazem a my se vám ozveme, zodpovíme váš dotaz
      a budeme vás informovat o konkrétní možnosti nahlédnutí do spisu</li>
</ul>

<h2>Jak si domluvit návštěvu</h2>
<p>Pracoviště pověřené vaším řízením zjistíte:</p>
<ul>
  <li>z úřední desky, nebo</li>
  <li>podle typu stavby v sekci <a href="{{r}}kontakty.html#stavebnici">Kontakty</a></li>
</ul>
<p>Nebo napište na: <a href="mailto:podatelna@uru.gov.cz">podatelna@uru.gov.cz</a></p>

<div class="box change">
  <h3>Co se mění od 1. 7. 2026</h3>
  <p>V přechodném období může být zajištění nahlédnutí do konkrétního spisu dočasně
  komplikovanější z důvodu předávání spisů z původních stavebních úřadů na ÚRÚ.
  Vynasnažíme se zabezpečit tuto možnost v co nejkratším čase.</p>
</div>
"""

DOKUMENTY = """
<h2>Přílohy a vzory</h2>
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

<ul class="files rich" data-list>
  <li data-stavba="vse" data-rizeni="povoleni" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Žádost o povolení záměru</span><br>
    <span class="fmeta">verze 3.0 · platné od 1. 7. 2026 · 296 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="vse" data-rizeni="povoleni" data-format="DOCX"><span class="ft">DOCX</span>
    <span class="grow"><span class="name">Příloha — identifikace záměru</span><br>
    <span class="fmeta">verze 3.0 · platné od 1. 7. 2026 · 296 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="doprava" data-rizeni="povoleni" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Vzor průvodní zprávy — dopravní stavby</span><br>
    <span class="fmeta">verze 2.1 · platné od 1. 7. 2026 · 296 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="energetika" data-rizeni="povoleni" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Vzor průvodní zprávy — energetické stavby</span><br>
    <span class="fmeta">verze 2.1 · platné od 1. 7. 2026 · 296 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="vse" data-rizeni="zmena" data-format="DOCX"><span class="ft">DOCX</span>
    <span class="grow"><span class="name">Žádost o změnu rozhodnutí</span><br>
    <span class="fmeta">verze 1.4 · platné od 1. 7. 2026 · 296 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="vse" data-rizeni="kolaudace" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Žádost o kolaudační rozhodnutí</span><br>
    <span class="fmeta">verze 1.2 · platné od 1. 7. 2026 · 296 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li data-stavba="vse" data-rizeni="vyvlastneni" data-format="PDF"><span class="ft">PDF</span>
    <span class="grow"><span class="name">Návrh na zahájení vyvlastňovacího řízení</span><br>
    <span class="fmeta">verze 1.0 · platné od 1. 7. 2026 · 296 kB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
</ul>
<div class="empty" data-empty style="display:none">Zadanému filtru neodpovídá žádný soubor.</div>

<h2>Projektová dokumentace</h2>
<p>Veškerá projektová dokumentace musí být podána v elektronické podobě (PDF), opatřena
elektronickým autorizačním razítkem s kvalifikovaným elektronickým podpisem a kvalifikovaným
časovým razítkem. Dokumentace se vkládá prostřednictvím Portálu stavebníka do evidence
elektronických dokumentací.</p>

<h2 id="poplatky">Správní poplatky</h2>
<p>Některé úkony ÚRÚ podléhají správním poplatkům ve smyslu položky č. 18 a 19 sazebníku
správních poplatků (příloha zákona č. 634/2004 Sb.).</p>
<table class="t">
  <tr><th style="width:220px">Číslo účtu</th><td>3711-1426011/0710</td></tr>
  <tr><th>Variabilní symbol</th><td>obdržíte od ÚRÚ ve výzvě k úhradě</td></tr>
</table>

<h2>Podat žádost elektronicky</h2>
<p>Žádosti můžete podat online prostřednictvím Portálu stavebníka, datovou schránkou,
e-mailem, poštou nebo osobně. Projektovou dokumentaci je nutné vždy vložit přes Portál
stavebníka.</p>
<div class="btn-row"><a class="btn" href="{{r}}vyhrazene-stavby/portal-stavebnika.html">Přejít na Portál stavebníka</a></div>
"""

PORTAL = """
<h2>Co je Portál stavebníka</h2>
<p>Portál stavebníka je centrální online systém státní stavební správy. Slouží k podání
žádostí, vložení projektové dokumentace do evidence a sledování stavu řízení. Provozuje ho
Digitální a informační agentura (DIA).</p>

<h2>Co musíte udělat před podáním žádosti</h2>
<ol class="steps">
  <li><h3>Připravte projektovou dokumentaci</h3>
    <p>Ve formátu PDF, elektronicky podepsanou autorizovanou osobou s kvalifikovaným
    elektronickým razítkem.</p></li>
  <li><h3>Vložte dokumentaci do evidence</h3>
    <p>Do evidence elektronických dokumentací přes Portál stavebníka — jako příjemce
    zvolte ÚRÚ.</p></li>
  <li><h3>Zaznamenejte si ID dokumentace</h3>
    <p>Budete ho potřebovat při vyplňování žádosti.</p></li>
</ol>

<h2>Jak podat žádost</h2>
<p>Žádost podáváte přímo v Portálu stavebníka, datovou schránkou, e-mailem, poštou nebo
osobně. Vložení projektové dokumentace přes portál je povinné vždy — bez ohledu na způsob
podání žádosti.</p>

<div class="btn-row"><a class="btn" href="#">Přejít na Portál stavebníka</a></div>
"""

FAQ_GROUPS = [
    ("Příslušnost ÚRÚ", [
        ("Co je to vyhrazená stavba?",
         "Vyhrazené stavby jsou stavby celostátního a nadregionálního významu vyjmenované v příloze stavebního zákona."),
        ("Spadá moje stavba pod ÚRÚ, nebo pod obecný stavební úřad?",
         'Použijte ověření příslušnosti na stránce <a href="{{r}}vyhrazene-stavby/co-spada-pod-uru.html">Co spadá pod ÚRÚ</a>.'),
        ("Jaký je rozdíl mezi ÚRÚ a běžným stavebním úřadem?",
         "ÚRÚ je specializovaný správní úřad s celostátní působností pro vyjmenované typy staveb."),
        ("Moje solární elektrárna má instalovaný výkon 3 MW — spadá pod ÚRÚ?",
         "Fotovoltaické elektrárny spadají pod ÚRÚ od instalovaného výkonu 5 MW."),
        ("Bytový dům nad jakou hranicí spadá pod ÚRÚ?",
         "Velké bytové projekty mohou spadat pod ÚRÚ jako stavby v zastavitelných plochách nad 45 ha."),
        ("Co se stalo s DESÚ? Je ÚRÚ jeho nástupcem?",
         "ÚRÚ přebírá agendy zaniklého DESÚ i Ústavu územního rozvoje."),
    ]),
    ("Přechodové období", [
        ("Mám zahájené řízení na DESÚ — co se s ním stane?",
         'Viz <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a>.'),
        ("Mám pravomocné územní rozhodnutí vydané před účinností novely — je stále platné?",
         "Ano, pravomocná rozhodnutí zůstávají v platnosti."),
        ("Mohu použít projektovou dokumentaci zpracovanou podle dosavadní úpravy?",
         "Ano, dokumentace zpracovaná podle dosavadní úpravy zůstává použitelná."),
        ("Jsou závazná stanoviska dotčených orgánů vydaná dříve stále platná?",
         "Ano, zůstávají platná; podrobnosti popisují přechodná ustanovení novely."),
    ]),
    ("Proces řízení", [
        ("Jak probíhá integrované řízení a co to znamená pro moji stavbu?",
         'Viz <a href="{{r}}vyhrazene-stavby/jak-probiha-rizeni.html">Jak probíhá řízení</a>.'),
        ("Musím sám obstarat závazná stanoviska od dotčených orgánů?",
         "Nemusíte. Vyjádření dotčených orgánů zajišťuje ÚRÚ v rámci řízení."),
        ("Jak dlouho trvá řízení o povolení záměru?",
         "Lhůty jsou uvedené u jednotlivých kroků řízení."),
        ("Jak podat žádost o povolení vyhrazené stavby?",
         'Viz <a href="{{r}}vyhrazene-stavby/portal-stavebnika.html">Portál stavebníka</a>.'),
        ("Mohu podat žádost e-mailem nebo poštou?",
         "Ano. Projektovou dokumentaci je však nutné vždy vložit přes Portál stavebníka."),
        ("Co dělat, když ÚRÚ vyzve k doplnění žádosti?",
         "Doplňte podklady ve stanovené lhůtě. Po dobu doplňování lhůta pro vydání rozhodnutí neběží."),
        ("Mám pravomocné rozhodnutí a potřebuji ho změnit — jak postupovat?",
         "Podejte žádost o změnu rozhodnutí; formulář najdete v Dokumentech a formulářích."),
    ]),
    ("Dokumentace a technické požadavky", [
        ("V jakém formátu musí být projektová dokumentace?",
         "PDF s autorizačním razítkem a kvalifikovaným časovým razítkem."),
        ("Co je to ID dokumentace a kde ho najdu?",
         "ID přiděluje evidence elektronických dokumentací po nahrání přes Portál stavebníka."),
        ("Musí být dokumentace elektronicky podepsaná autorizovanou osobou?",
         "Ano. Bez autorizačního razítka nelze dokumentaci do evidence vložit."),
    ]),
    ("Správní poplatky", [
        ("Jaké správní poplatky se platí a za co?",
         'Podle položek č. 18 a 19 sazebníku správních poplatků — viz '
         '<a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html#poplatky">Dokumenty a formuláře</a>.'),
        ("Jak a kam uhradit správní poplatek?",
         "Na účet 3711-1426011/0710. Variabilní symbol obdržíte ve výzvě k úhradě."),
    ]),
    ("Vyvlastnění", [
        ("Kdy může ÚRÚ zahájit vyvlastňovací řízení?",
         "Za podmínek stanovených zákonem o vyvlastnění, pokud nebylo možné získat práva k pozemku dohodou."),
        ("Přebírá ÚRÚ vyvlastňovací řízení zahájená před účinností novely?",
         "Řízení se dokončují podle pravidel platných v době jejich zahájení."),
    ]),
    ("Kontakty", [
        ("Na koho se obrátit s dotazem k mému konkrétnímu řízení?",
         "Na oddělení, které vaše řízení vede — kontakt najdete v oznámení o zahájení řízení."),
        ("Kde najdu kontakt na příslušné oddělení podle typu stavby?",
         'V sekci <a href="{{r}}kontakty.html#stavebnici">Kontakty</a> jsou kontaktní karty '
         'rozdělené podle typu vyhrazené stavby.'),
    ]),
]

FAQ_VS = ('<div class="filters">'
          '<div class="searchrow"><input type="search" placeholder="Hledat v otázkách…" '
          'oninput="var q=this.value.toLowerCase();document.querySelectorAll(\'[data-faq]\')'
          '.forEach(function(d){d.style.display=d.textContent.toLowerCase().indexOf(q)>-1?\'\':\'none\'})">'
          '</div><p class="hint" style="margin:0">Vyhledávání prochází znění otázek i odpovědí.'
          + cmt(26, "FAQ je členěné do skupin bez vyhledávání. Doplnit vyhledávání v otázkách.")
          + '</p></div>')
for _g, _qs in FAQ_GROUPS:
    FAQ_VS += f'<div data-faqgroup><h2>{_g}</h2>'
    for _q, _a in _qs:
        FAQ_VS += (f'<details class="acc" data-faq><summary>{_q}</summary>'
                   f'<div class="body"><p>{_a}</p></div></details>')
    FAQ_VS += '</div>'

PAGES = [
    dict(path="vyhrazene-stavby/index.html", title="Vyhrazené stavby", section="vyhrazene-stavby",
         crumbs=[("Vyhrazené stavby", None)], sidebar=False,
         h1="Vyhrazené stavby",
         perex="Úřad rozvoje území povoluje vyhrazené stavby celostátního významu. Zjistěte, zda vaše stavba spadá pod ÚRÚ, jak probíhá řízení a kde najdete potřebné dokumenty.",
         body=ROZCESTNIK),
    dict(path="vyhrazene-stavby/co-meni-novela.html", title="Co změní novela SZ", section="vyhrazene-stavby",
         crumbs=C + [("Co změní novela SZ", None)], help="stavebnici",
         h1="Co změní novela stavebního zákona",
         perex="Přehled změn pro stavebníky a projektanty vyhrazených staveb.", body=NOVELA),
    dict(path="vyhrazene-stavby/co-spada-pod-uru.html", title="Co spadá pod ÚRÚ", section="vyhrazene-stavby",
         crumbs=C + [("Co spadá pod ÚRÚ", None)], help="stavebnici",
         h1="Co spadá pod ÚRÚ",
         perex="Úřad rozvoje území je stavebním úřadem pro vyhrazené stavby — stavby celostátního a nadregionálního významu vyjmenované v příloze stavebního zákona. Níže najdete přehled kategorií i konkrétních příkladů.",
         updated="Přehled kategorií naposledy aktualizován 12. 6. 2026." + cmt(16, "Chybí datum poslední aktualizace přehledu — u obsahu vázaného na legislativu je to funkční prvek."),
         body=CO_SPADA),
    dict(path="vyhrazene-stavby/jak-probiha-rizeni.html", title="Jak probíhá řízení", section="vyhrazene-stavby",
         crumbs=C + [("Jak probíhá řízení", None)], help="stavebnici",
         h1="Jak probíhá řízení", body=RIZENI),
    dict(path="vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html", title="Jak probíhá řízení — pro účastníky",
         section="vyhrazene-stavby", help="stavebnici",
         crumbs=C + [("Jak probíhá řízení", "vyhrazene-stavby/jak-probiha-rizeni.html"), ("Nahlížení do spisu", None)],
         h1="Jak probíhá řízení", body=RIZENI_U),
    dict(path="vyhrazene-stavby/dokumenty-a-formulare.html", title="Dokumenty a formuláře",
         section="vyhrazene-stavby", crumbs=C + [("Dokumenty a formuláře", None)], help="stavebnici",
         h1="Dokumenty a formuláře",
         perex="Zde najdete požadavky na projektovou dokumentaci, informace o správních poplatcích a odkaz na Portál stavebníka, kde žádosti podáváte online.",
         body=DOKUMENTY),
    dict(path="vyhrazene-stavby/portal-stavebnika.html", title="Portál stavebníka", section="vyhrazene-stavby",
         crumbs=C + [("Portál stavebníka", None)], help="stavebnici",
         h1="Portál stavebníka",
         perex="Žádosti o povolení vyhrazené stavby se podávají prostřednictvím Portálu stavebníka — státního online systému pro komunikaci se stavebními úřady. Před přechodem na portál si přečtěte, co budete potřebovat.",
         body=PORTAL),
    dict(path="vyhrazene-stavby/caste-dotazy.html", title="Odpovědi na nejčastější otázky",
         section="vyhrazene-stavby", crumbs=C + [("Odpovědi na nejčastější otázky", None)],
         help="stavebnici", h1="Odpovědi na nejčastější otázky",
         perex="Odpovědi na nejčastější otázky stavebníků a projektantů vyhrazených staveb.",
         body=FAQ_VS),
]
