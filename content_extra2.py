# -*- coding: utf-8 -*-
"""Doplnění obsahu podle návrhu (DESU_design.pdf, str. 28–34, 37, 40, 41)."""

# ---------------------------------------------------------------- Kariéra
KARIERA = """
<div class="btn-row"><a class="btn" href="{{r}}kariera/otevrene-pozice.html">Zobrazit volné pozice</a></div>

<h2>Proč pracovat v ÚRÚ</h2>
<p>ÚRÚ je nová instituce s celostátním dopadem. Budete se podílet na povolování klíčových
staveb pro rozvoj Česka — dálnic, železnic, energetických sítí i obnovitelných zdrojů.
Přidejte se k týmu, který formuje budoucnost české infrastruktury.</p>

<div class="grid g3">
  <div class="card"><h3>Dovolená nad rámec</h3><p>Nadstandardní dovolená ve veřejné správě.</p></div>
  <div class="card"><h3>Práce z domova</h3><p>Možnost home office podle typu pozice.</p></div>
  <div class="card"><h3>Stabilní zaměstnání</h3><p>Jistota práce ve veřejné správě.</p></div>
  <div class="card"><h3>Smysluplná agenda</h3><p>Přímý dopad na rozvoj celé České republiky.</p></div>
  <div class="card"><h3>Pružná pracovní doba</h3><p>Volitelný začátek i konec pracovního dne.</p></div>
  <div class="card"><h3>Příspěvek na stravování</h3><p>Stravenky nebo příspěvek na stravné.</p></div>
</div>

<h2>Pracovněprávní vztah vs. státní služba</h2>
<p>V ÚRÚ nabízíme pozice ve dvou režimech. Státní služba přináší vyšší jistotu zaměstnání —
služební poměr na dobu neurčitou, delší výpovědní dobu a odměňování podle platové třídy
a tarifu ze zákona. Pracovněprávní vztah nabízí flexibilnější podmínky podle zákoníku práce.
Typ poměru je vždy uveden u konkrétní pozice.</p>
<table class="t">
  <tr><th style="width:24%">Parametr</th><th>Pracovněprávní vztah</th><th>Státní služba</th></tr>
  <tr><td>Zákon</td><td>zákoník práce</td><td>zákon o státní službě</td></tr>
  <tr><td>Jistota</td><td>standardní</td><td>vyšší — služební poměr na dobu neurčitou</td></tr>
  <tr><td>Výběrové řízení</td><td>standardní pohovor</td><td>formalizovaný postup dle zákona</td></tr>
  <tr><td>Výpovědní doba</td><td>2 měsíce</td><td>delší dle služebního zákona</td></tr>
  <tr><td>Odměňování</td><td>platový výměr</td><td>platová třída a tarif dle zákona</td></tr>
</table>

<h2>Jak se přihlásit</h2>
<ol class="steps">
  <li><h3>Najděte svoji pozici</h3>
    <p>Prohlédněte si aktuální nabídky a filtrujte podle oblasti a lokality.</p></li>
  <li><h3>Připravte přihlášku</h3>
    <p>Budete potřebovat životopis a motivační dopis. Formulář najdete přímo na stránce pozice.</p></li>
  <li><h3>Odešlete a čekejte</h3>
    <p>Po odeslání dostanete potvrzení e-mailem. Ozveme se vám do 10 pracovních dnů.</p></li>
</ol>

<h2>Lidé z ÚRÚ</h2>
<div class="contactcard" style="max-width:44rem">
  <p>„Přešel jsem z krajského úřadu, kde jsem řešil hlavně rodinné domy. Tady pracuju
  na dálnicích a železnicích — je to úplně jiný level. Baví mě, že vidím výsledky své práce,
  které pomáhají tisícům úředníků po celém Česku."</p>
  <p class="role">Jméno, referentka pro dopravní stavby, Praha</p>
</div>

<div class="btn-row">
  <a class="btn" href="{{r}}kariera/otevrene-pozice.html">Otevřené pozice</a>
  <a class="btn ghost" href="{{r}}kariera/prihlaska.html">Jak podat přihlášku</a>
</div>
"""

POZICE_FILTRY = """
  <div class="row">
    <div class="field"><label for="p-cas">Čas zveřejnění</label>
      <select id="p-cas" data-key="cas"><option value="">Nezáleží</option>
        <option value="24h">Posledních 24 hodin</option>
        <option value="tyden">Poslední týden</option>
        <option value="mesic">Poslední měsíc</option></select></div>
    <div class="field"><label for="p-vzdelani">Minimální stupeň vzdělání</label>
      <select id="p-vzdelani" data-key="vzdelani"><option value="">Vše</option>
        <option value="stredni">Středoškolské</option>
        <option value="bakalarske">Bakalářské</option>
        <option value="magisterske">Magisterské</option></select></div>
    <div class="field"><label for="p-jazyk">Požadovaná jazyková znalost</label>
      <select id="p-jazyk" data-key="jazyk"><option value="">Nezáleží</option>
        <option value="en">Angličtina</option><option value="de">Němčina</option></select></div>
    <div class="field"><label for="p-domov">Práce z domova</label>
      <select id="p-domov" data-key="domov"><option value="">Nezáleží</option>
        <option value="ano">Možnost práce z domova</option></select></div>
  </div>
"""

DETAIL_POZICE = """
<p class="updated">Oddělení dopravních staveb · aktualizováno 20. 7. 2026</p>
<div class="tags" style="display:flex;gap:8px;margin-bottom:14px">
  <span class="tag neutral">Pracovněprávní vztah</span>
  <span class="tag hist">12. platová třída</span>
  <span class="tag hist">Možnost práce z domova</span>
  <span class="tag valid">Přihlášky otevřené</span>
</div>

<table class="t">
  <tr><th style="width:230px">Lokalita</th><td>Praha</td></tr>
  <tr><th>Mzda</th><td>40 000 – 60 000 Kč měsíčně</td></tr>
  <tr><th>Typ poměru</th><td>pracovněprávní vztah na dobu neurčitou</td></tr>
  <tr><th>Úvazek</th><td>plný</td></tr>
  <tr><th>Požadované vzdělání</th><td>bakalářské</td></tr>
  <tr><th>Jazyky</th><td>angličtina (pokročilá)</td></tr>
  <tr><th>Vhodné i pro absolventy</th><td>ano</td></tr>
  <tr><th>Lhůta pro podání přihlášky</th><td>31. 8. 2026</td></tr>
  <tr><th>Oficiální text výběrového řízení</th>
      <td><a href="{{r}}uredni-deska.html">Oznámení o vyhlášení výběrového řízení (úřední deska, PDF)</a>{c78}</td></tr>
</table>

<h2>O pozici</h2>
<p>Budete vést řízení o povolení vyhrazených staveb v oblasti drah — od podání žádosti
po vydání rozhodnutí — v integrovaném procesu podle stavebního zákona.</p>
<ul>
  <li>Vedení řízení o povolení záměru u drážních staveb</li>
  <li>Koordinace vyjádření dotčených orgánů v rámci jednoho řízení</li>
  <li>Komunikace se stavebníky (Správa železnic, dopravní podniky)</li>
  <li>Příprava rozhodnutí a dalších správních aktů</li>
</ul>

<h2>Koho hledáme</h2>
<ul>
  <li>Zkušenost se správním řízením, ideálně na stavebním úřadě</li>
  <li>Znalost stavebního zákona č. 283/2021 Sb. výhodou</li>
  <li>Schopnost pracovat samostatně i v týmu</li>
  <li>Analytické myšlení a pečlivost</li>
</ul>

<h2>Co nabízíme</h2>
<ul>
  <li>Přímý dopad na rozvoj klíčové infrastruktury České republiky</li>
  <li>Pružná pracovní doba — volitelný začátek a konec pracovního dne</li>
  <li>Nadstandardní dovolená</li>
  <li>Příspěvek na stravování</li>
  <li>Benefity na míru: stravenky, příspěvek na vzdělávání, multisport karta, sick days</li>
</ul>

<h2>Jak se přihlásit</h2>
<p>Přihlaste se prostřednictvím online formuláře, nebo si stáhněte PDF a zašlete jej
datovou schránkou či poštou. Součástí přihlášky je souhlas se zpracováním osobních údajů.</p>
<div class="btn-row">
  <a class="btn" href="{{r}}kariera/prihlaska.html">Odpovědět na nabídku{c77}</a>
  <a class="btn ghost" href="{{r}}kontakty.html#hr">Zeptat se HR</a>
  <a class="btn ghost" href="#">Sdílet nabídku</a>
</div>

<div class="contactcard" style="max-width:34rem">
  <h3>Personální oddělení</h3><p class="role">Dotazy k pozici a k průběhu výběrového řízení</p>
  <dl><dt>E-mail</dt><dd>kariera@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl>
</div>

<h2>Mohlo by se vám líbit</h2>
<ul class="doclist">
  <li><div class="tags"><span class="tag neutral">Služební poměr</span></div>
    <h3><a href="{{r}}kariera/detail-pozice.html">Právník — povolování energetických staveb</a></h3>
    <p>Oddělení energetických staveb</p>
    <div class="meta"><span>Praha</span><span>plný úvazek</span></div></li>
  <li><div class="tags"><span class="tag neutral">Služební poměr</span></div>
    <h3><a href="{{r}}kariera/detail-pozice.html">Metodik územního plánování</a></h3>
    <p>Odbor územního plánování</p>
    <div class="meta"><span>Brno</span><span>plný úvazek</span></div></li>
</ul>
"""

# ---------------------------------------------------------------- O úřadu
KDO_JSME = """
<p>Naším posláním je povolovat nejvýznamnější stavby České republiky rychle a předvídatelně,
podporovat stavební úřady po celé zemi a rozvíjet územní plánování na celostátní úrovni.</p>

<h2>Proč ÚRÚ vznikl</h2>
<p>Stavební řízení v České republice procházelo složitým systémem, kde velké infrastrukturní
stavby musely procházet desítkami úřadů a řízení trvala roky. Stavební zákon č. 283/2021 Sb.
tento systém zásadně změnil — jeden specializovaný úřad vede celé řízení od začátku do konce.
Stavebník komunikuje s jediným úřadem, který koordinuje vyjádření všech dotčených orgánů
interně. Výsledkem jsou kratší lhůty a předvídatelný proces.</p>

<h2>Naše tři agendy</h2>
<div class="grid g3">
  <a class="card" href="{{r}}vyhrazene-stavby/index.html"><h3>Vyhrazené stavby</h3>
    <p>Povolujeme stavby celostátního a nadregionálního významu — dálnice, železnice,
    energetickou infrastrukturu, obnovitelné zdroje a další vyhrazené stavby. Vedeme
    integrované řízení: jeden úřad, jedno řízení, jedno rozhodnutí.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/index.html"><h3>Metodická podpora</h3>
    <p>Jsme metodickým garantem stavebního zákona pro stavební úřady a dotčené orgány.
    Vydáváme výkladová stanoviska, provozujeme Konzultační středisko a databázi Tisíc otázek.
    Metodici, na které jsou stavební úřady zvyklé, jsou nyní u nás.</p></a>
  <a class="card" href="{{r}}uzemni-rozvoj/index.html"><h3>Územní rozvoj</h3>
    <p>Zajišťujeme celostátní územní plánování — Politiku územního rozvoje ČR, Územní
    rozvojový plán, územně analytické podklady i standardizaci. Slovník územního rozvoje,
    publikace, časopis UaÚR a knihovna pokračují pod hlavičkou ÚRÚ.</p></a>
</div>

<h2>Klíčové milníky</h2>
<ol class="steps">
  <li><h3>2024: Vznik DESÚ</h3>
    <p>Dopravní a energetický stavební úřad zahajuje činnost jako specializovaný úřad
    pro vyhrazené stavby celostátního významu.</p></li>
  <li><h3>Transformace na ÚRÚ</h3>
    <p>DESÚ se transformuje na Úřad rozvoje území a integruje agendy Ústavu územního
    rozvoje — metodickou podporu a územní rozvoj.</p></li>
  <li><h3>Od 1. 1. 2028: Rozšíření státní stavební správy</h3>
    <p>Plánovaná integrace krajských stavebních úřadů do ÚRÚ v rámci další fáze reformy.</p></li>
</ol>

<h2>ÚRÚ v číslech</h2>
<div class="grid g3">
  <div class="card"><h3>zaměstnanců</h3><p>Odborníci na stavební právo, územní plánování,
    energetiku a dopravu. Počet se doplní.</p></div>
  <div class="card"><h3>2 pracoviště</h3><p>Praha a Brno — pokrýváme celé území ČR.</p></div>
  <div class="card"><h3>řízení ročně</h3><p>Žádostí o povolení záměru, které zpracujeme.
    Počet se doplní.</p></div>
</div>

<h2>Kde sídlíme</h2>
<table class="t">
  <tr><th style="width:150px">Praha</th><td>adresa se doplní</td></tr>
  <tr><th>Brno</th><td>adresa se doplní</td></tr>
</table>

<h2>Důležité odkazy</h2>
<div class="grid g3">
  <a class="card" href="{{r}}kariera/otevrene-pozice.html"><h3>Otevřené pozice</h3>
    <p>Přidejte se k týmu.</p></a>
  <a class="card" href="{{r}}vyhrazene-stavby/index.html"><h3>Povolujete stavbu?</h3>
    <p>Postup, formuláře a kontakty pro stavebníky.</p></a>
  <a class="card" href="{{r}}kontakty.html"><h3>Kontakty</h3>
    <p>Kontakty podle agendy a oddělení.</p></a>
</div>
"""

POVINNE = [
    ("1", "Název", "Úřad rozvoje území"),
    ("2", "Důvod a způsob založení", "Zřízen zákonem, vznik transformací Dopravního a energetického stavebního úřadu."),
    ("2.1", "Výňatek z citovaného zákona", "Doplní se."),
    ("3", "Organizační struktura", None),
    ("4", "Kontaktní spojení", None),
    ("5", "Způsob případných plateb", "Číslo účtu a variabilní symboly obdržíte ve výzvě k úhradě."),
    ("6", "IČO", "Doplní se."),
    ("7", "Plátce daně z přidané hodnoty", "Doplní se."),
    ("8", "Dokumenty", "Rozpočet, závěrečné účty a další dokumenty ke stažení."),
    ("9", "Žádosti o informace", "Postup podání žádosti podle zák. č. 106/1999 Sb."),
    ("10", "Příjem podání a podnětů", "Podatelna, datová schránka, osobní podání."),
    ("11", "Opravné prostředky", None),
    ("11.1", "Stížnost", "Postup pro podání stížnosti."),
    ("11.2", "Odvolání", "Postup pro podání odvolání proti rozhodnutí."),
    ("12", "Formuláře", None),
    ("13", "Návody na řešení životních situací", "Postupy pro nejčastější situace stavebníků a úřadů."),
    ("14", "Předpisy", "Přehled právních předpisů, podle kterých úřad postupuje."),
    ("15", "Úhrady za poskytování informací", "Sazebník úhrad."),
    ("16", "Licenční smlouvy", "Vzory licenčních smluv podle §14a zák. č. 106/1999 Sb."),
    ("17", "Výroční zpráva podle zákona o svobodném přístupu k informacím", None),
]

PRO_MEDIA = """
<div class="contactcard" style="max-width:34rem">
  <h3>Kontakt pro média</h3><p class="role">Tiskové dotazy a vyjádření úřadu</p>
  <p class="agenda">Odpovídáme do 2 pracovních dnů. Pro urgentní záležitosti volejte
  na uvedené telefonní číslo.</p>
  <dl><dt>E-mail</dt><dd>media@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl>
</div>

<h2>Základní údaje o úřadu</h2>
<table class="t">
  <tr><th style="width:220px">Adresa</th><td>doplní se</td></tr>
  <tr><th>IČO</th><td>doplní se</td></tr>
  <tr><th>Datová schránka</th><td>doplní se</td></tr>
  <tr><th>Ředitel</th><td>doplní se</td></tr>
</table>
"""

# ---------------------------------------------------------------- Kontakty
KONTAKTY_POBOCKY = """
<h2>Pracoviště</h2>
<p>ÚRÚ působí na dvou pracovištích a pokrývá celé území České republiky.</p>
<div class="contactcards">
  <div class="contactcard"><h3>Praha</h3><p class="role">Hlavní pracoviště</p>
    <dl><dt>Adresa</dt><dd>doplní se</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
  <div class="contactcard"><h3>Brno</h3><p class="role">Pracoviště územního rozvoje (dříve ÚÚR)</p>
    <dl><dt>Adresa</dt><dd>doplní se</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
</div>
"""

KONTAKTY_ODDELENI = """
<h2>Kontakty na oddělení</h2>
<p>Kontakty na oddělení úřadu podle jejich zaměření a odpovědnosti.</p>
<div class="contactcards">
  <div class="contactcard"><h3>Komunikace a média</h3>
    <p class="role">Tiskové a mediální dotazy</p>
    <p class="agenda">Zajišťuje komunikaci s médii a veřejností a správu tiskových materiálů.</p>
    <dl><dt>E-mail</dt><dd>media@uru.gov.cz</dd></dl></div>
  <div class="contactcard"><h3>Podpora elektronických služeb</h3>
    <p class="role">Portál stavebníka a online podání</p>
    <p class="agenda">Pomáhá s využíváním online služeb a řeší technické problémy spojené
    s elektronickým podáním.</p>
    <dl><dt>E-mail</dt><dd>podpora@uru.gov.cz</dd></dl></div>
</div>
"""

# ---------------------------------------------------------------- Územní rozvoj
EVIDENCE = """
<h2>K čemu evidence slouží</h2>
<p>Evidence územně plánovací činnosti shromažďuje údaje o pořizované a vydané územně
plánovací dokumentaci obcí a krajů. Data slouží pro celostátní přehled i pro navazující
analytické podklady.</p>

<h2>Jak evidence probíhá</h2>
<ul>
  <li>Evidence dokumentace obcí probíhá průběžně na základě registračních listů,
      které krajským úřadům zasílají úřady územního plánování.</li>
  <li>Krajské úřady pořizují zápis do centrální databáze.</li>
  <li>Evidence dokumentace velkých územních celků probíhá průběžně prostřednictvím aplikace.</li>
</ul>

<h2>Výstupy evidence</h2>
<ul>
  <li>Průběžně aktualizovaná data zveřejňovaná na webu úřadu</li>
  <li>Statistiky (struktura pořizovatelů, průměrná doba procesu pořizování a další)</li>
  <li>Články v odborných časopisech</li>
</ul>

<h2>Vývoj systému evidence</h2>
<p>Rozvoj evidence územně plánovací činnosti pokračuje. Systém umožňuje přístup obcím
s rozšířenou působností i krajům a připojení k mapovému podkladu.</p>

<h2>Související obsah</h2>
<ul>
  <li><a href="#">Metodiky a příručky k evidenci</a></li>
  <li><a href="#">Ročenky evidence</a></li>
  <li><a href="#">Seznam projektantů</a></li>
  <li><a href="#">Územní studie</a></li>
  <li><a href="#">Historie evidence</a></li>
</ul>
"""

INFOWEB = """
<div class="btn-row"><a class="btn" href="#">Vstup do portálu</a></div>

<h2>Cíle portálu</h2>
<p>Informační portál územního plánování je rozcestník odborných informací podle
§ 11 odst. 1 písm. d) stavebního zákona. Je určen pro veřejnou správu, odbornou
i laickou veřejnost.</p>

<h2>Základní vize portálu</h2>
<ul>
  <li>Prioritně udržovat aktuálnost a kvalitu informací</li>
  <li>Sledovat nová témata v územním rozvoji</li>
  <li>Zpřístupňovat obsah přehledně pro odbornou i laickou veřejnost</li>
</ul>

<h2>Kontaktní osoby</h2>
<p>Kontakty na správce portálu najdete v <a href="{{r}}kontakty.html">Kontaktech</a>.</p>
"""

PUR_DOKUMENTY = """
<h2>Přiložené dokumenty</h2>
<ul class="files">
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Politika územního rozvoje ČR — úplné znění</span><br>
    <span class="fmeta">aktuální znění po poslední aktualizaci</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Spatial Development Policy of the Czech Republic</span><br>
    <span class="fmeta">anglická verze</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Raumentwicklungspolitik der Tschechischen Republik</span><br>
    <span class="fmeta">německá verze</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">XLSX</span><span class="grow"><span class="name">Seznam relevantních podkladů PÚR ČR</span><br>
    <span class="fmeta">podklady pro pořizování aktualizací</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
</ul>
<p class="hint">Verze v anglickém a německém jazyce jsou součástí přiložených dokumentů.</p>

<h2>O dokumentu</h2>
<p>Politika územního rozvoje je celostátní nástroj územního plánování. Určuje požadavky
na konkretizaci úkolů územního plánování v republikových, přeshraničních a mezinárodních
souvislostech, zejména s ohledem na udržitelný rozvoj území, a koordinuje územně plánovací
činnost krajů. Navazuje na dokumenty územního rozvoje Evropské unie.</p>

<h2>Historie dokumentu</h2>
<table class="t">
  <tr><th style="width:200px">Aktualizace</th><th>Rok</th><th>Stav</th></tr>
  <tr><td>Změna č. 9</td><td>2025</td><td><span class="tag valid">Platná</span></td></tr>
  <tr><td>Aktualizace č. 1–8</td><td>2015–2024</td><td><span class="tag hist">Historická</span></td></tr>
  <tr><td>První vydání PÚR ČR</td><td>2009</td><td><span class="tag hist">Historická</span></td></tr>
</table>
<p>Z důvodu naléhavého veřejného zájmu byla pořízena mimořádná změna PÚR ČR — Změna č. 9.</p>

<h2>Pracovní výbor pro zpracování</h2>
<p>Podkladové materiály pro jednotlivá jednání jsou k dispozici členům výboru
v neveřejné části webu.</p>
"""

MEZINARODNI = """
<h2>ESPON</h2>
<p>ÚRÚ zajišťuje funkci národního kontaktního místa programu ESPON — Evropské pozorovací
sítě pro územní rozvoj a soudržnost. Agenda programu je průběžně aktualizovaná
a naplňuje mezinárodní závazky ČR.</p>
<div class="btn-row"><a class="btn ghost" href="#">Přejít na ESPON</a></div>

<h2>V4+2</h2>
<p>ÚRÚ zabezpečuje spolupráci států Visegrádské skupiny a přidružených států v oblasti
územního rozvoje. Agenda má uzavřený pracovní intranet a je vedená na samostatné doméně.</p>
<div class="box note"><p>Odkaz vede mimo web ÚRÚ na samostatnou doménu projektu.
Zpět se dostanete tlačítkem prohlížeče.</p></div>
<div class="btn-row"><a class="btn ghost" href="#">Přejít na web V4+2</a></div>

<h2>Přeshraniční spolupráce</h2>
<p>Česko-polská a další přeshraniční spolupráce v územním plánování.</p>
"""
