# -*- coding: utf-8 -*-
"""Doplnění obsahu podle návrhu (DESU_design.pdf, str. 28–34, 37, 40, 41)."""

# ---------------------------------------------------------------- Kariéra
KARIERA = """
<div class="btn-row"><a class="btn arrow" href="{{r}}kariera/otevrene-pozice.html">Zobrazit volné pozice</a></div>

<h2>Proč pracovat v ÚRÚ</h2>
<p>ÚRÚ je nová instituce s celostátním dopadem. Budete se podílet na povolování klíčových
staveb pro rozvoj Česka — dálnic, železnic, energetických sítí i obnovitelných zdrojů.
Přidejte se k týmu, který formuje budoucnost české infrastruktury.</p>

<div class="grid g3">
  <div class="card"><h3>XY týdnů dovolené</h3><p>Nadstandardní dovolená ve veřejné správě.</p></div>
  <div class="card"><h3>Práce z domova</h3><p>Možnost home office podle typu pozice.</p></div>
  <div class="card"><h3>Stabilní zaměstnání</h3><p>Jistota práce ve veřejné správě.</p></div>
  <div class="card"><h3>Smysluplná agenda</h3><p>Přímý dopad na rozvoj celé České republiky.</p></div>
  <div class="card"><h3>Pružná pracovní doba</h3><p>Volitelný začátek i konec pracovního dne.</p></div>
  <div class="card"><h3>Příspěvek na stravování</h3><p>Stravenky nebo příspěvek na stravné.</p></div>
</div>

<h2>Pracovněprávní vztah vs. státní služba</h2>
<p>V ÚRÚ nabízíme pozice ve dvou režimech. Hlavní rozdíl, na který se uchazeči ptají
nejčastěji:</p>
<ul>
  <li><strong>Státní služba</strong> přináší vyšší jistotu zaměstnání — služební poměr na dobu
      neurčitou, delší výpovědní doba a odměňování dle platové třídy a tarifu ze zákona.</li>
  <li><strong>Pracovněprávní vztah</strong> nabízí flexibilnější podmínky — řídí se zákoníkem
      práce, standardní výpovědní doba 2 měsíce.</li>
</ul>
<p>V obou případech: 5 týdnů dovolené a pružná pracovní doba. Typ poměru je vždy uveden
u konkrétní pozice.</p>
<table class="t">
  <tr><th style="width:24%">Parametr</th><th>Pracovněprávní vztah</th><th>Státní služba</th></tr>
  <tr><td>Zákon</td><td>Zákoník práce</td><td>Zákon o státní službě</td></tr>
  <tr><td>Jistota</td><td>Standardní</td><td>Vyšší — služební poměr na dobu neurčitou</td></tr>
  <tr><td>Výběrové řízení</td><td>Standardní pohovor</td><td>Formalizovaný postup dle zákona</td></tr>
  <tr><td>Výpovědní doba</td><td>2 měsíce</td><td>Delší dle služebního zákona</td></tr>
  <tr><td>Odměňování</td><td>Platový výměr</td><td>Platová třída + tarif dle zákona</td></tr>
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
<div class="citace">
  <p>„Přešel/a jsem z krajského úřadu, kde jsem řešil/a hlavně rodinné domy. Tady pracuju
  na dálnicích a železnicích — je to úplně jiný level. Baví mě, že vidím výsledky své práce
  na mapě."</p>
  <p class="role"><strong>Jméno</strong>, Referentka pro dopravní stavby, Praha</p>
</div>
<div class="citace">
  <p>„Nový zákoník mě lákal, ale bál jsem se byrokracie. Realita je jiná — tvoříme metodiky,
  které pomáhají tisícům úředníků po celém Česku. To mě drží."</p>
  <p class="role"><strong>Jméno</strong>, Metodik stavebního práva, Brno</p>
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
<p>Budete se podílet na povolování staveb železničních drah, metra a tramvajových tratí
celostátního a regionálního významu. Jako součást Oddělení dopravních staveb ÚRÚ povedete
řízení o povolení záměru od podání žádosti po vydání rozhodnutí v integrovaném procesu
podle stavebního zákona.</p>
<ul>
  <li>Vedení řízení o povolení záměru u drážních staveb</li>
  <li>Koordinace vyjádření dotčených orgánů v rámci integrovaného řízení</li>
  <li>Komunikace se stavebníky (Správa železnic, dopravní podniky)</li>
  <li>Příprava rozhodnutí a dalších správních aktů</li>
</ul>

<h2>Koho hledáme</h2>
<ul>
  <li>Vysokoškolské vzdělání právního, stavebního nebo technického směru</li>
  <li>Zkušenost s vedením správního řízení nebo s agendou stavebního práva výhodou</li>
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
<p>Přihlaste se prostřednictvím online formuláře, nebo si stáhněte PDF a zašlete jej datovou
schránkou, poštou nebo na kariera@uru.gov.cz. Potvrzení přijetí dostanete e-mailem, ozveme se
do deseti pracovních dnů. Součástí přihlášky je souhlas se zpracováním osobních údajů
pro účely tohoto výběrového řízení dle GDPR.</p>
<p><a href="{{r}}uredni-deska.html">Odkaz na zákonný text výběrového řízení na úřední desce</a></p>
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

<h2>Najděte správný kontakt</h2>
<p>Územní rozvoj a agenda převzatá z ÚÚR má vlastní pracoviště v Brně. Kontakty podle agendy
najdete v <a href="{{r}}kontakty.html">Kontaktech</a>.</p>

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
    ("1", "Název subjektu", "Úřad rozvoje území"),
    ("2", "Důvod a způsob založení", "Zřízen zákonem, vznik transformací Dopravního a energetického stavebního úřadu."),
    ("2.1", "Výňatek z citovaného zákona", "Doplní se."),
    ("3", "Organizační struktura", None),
    ("4", "Kontaktní údaje", None),
    ("5", "Způsob případných plateb", "Číslo účtu a variabilní symbol obdržíte ve výzvě k úhradě."),
    ("6", "IČ", "Doplní se."),
    ("7", "DIČ", "Doplní se."),
    ("8", "Dokumenty", "Rozpočet, závěrečné účty a další dokumenty ke stažení."),
    ("9", "Žádosti o informace", "Postup podání žádosti podle zák. č. 106/1999 Sb."),
    ("10", "Příjem žádostí a dalších podání", "Podatelna, datová schránka, osobní podání."),
    ("11", "Opravné prostředky", None),
    ("11.1", "Stížnost", "Postup pro podání stížnosti."),
    ("11.2", "Odvolání", "Postup pro podání odvolání proti rozhodnutí."),
    ("12", "Formuláře", None),
    ("13", "Návody na řešení životních situací", "Postupy pro nejčastější situace stavebníků a úřadů."),
    ("14", "Předpisy", "Přehled právních předpisů, podle kterých úřad postupuje."),
    ("15", "Úhrady za poskytování informací", "Sazebník úhrad."),
    ("16", "Licenční smlouvy", "Vzory licenčních smluv podle §14a zák. č. 106/1999 Sb."),
    ("17", "Výroční zprávy", None),
]

PRO_MEDIA = """
<p>Jste novinář nebo redaktor? Mediální dotazy vyřizujeme prostřednictvím dedikovaného kontaktu.
Rádi vám poskytneme informace o činnosti ÚRÚ, vyhrazených stavbách nebo územním rozvoji.</p>

<div class="contactcard" style="max-width:34rem">
  <h3>Kontakt pro média</h3><p class="role">Tiskové dotazy a vyjádření úřadu</p>
  <p class="agenda">Odpovídáme do 2 pracovních dnů. Pro urgentní záležitosti volejte
  na uvedené telefonní číslo.</p>
  <dl><dt>E-mail</dt><dd>media@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl>
</div>

<h2>O úřadu pro média</h2>
<p>Úřad rozvoje území (ÚRÚ) je ústřední správní úřad zřízený zákonem. Vznikl transformací
Dopravního a energetického stavebního úřadu (DESÚ) a integrací agend Ústavu územního rozvoje (ÚÚR).</p>

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
<p>Evidence územně plánovací činnosti je prováděna na základě § 162 zákona č. 183/2006 Sb.,
o územním plánování a stavebním řádu. Postup orgánů územního plánování při evidenci je dále
upraven <a href="#">Metodikou OÚP MMR pro postup orgánů územního plánování při evidenci územně
plánovací činnosti</a>.</p>

<h2>Dvě části evidence</h2>
<p>Evidence územně plánovací činnosti má dvě relativně samostatné části:</p>
<ul>
  <li>evidenci územně plánovací činnosti obcí,</li>
  <li>evidenci územně plánovací činnosti krajů.</li>
</ul>
<p>Evidence ÚPD a ÚPP obcí nyní probíhá průběžně, a to na základě registračních listů, které
krajským úřadům zasílají jejich pořizovatelé (obecní úřady). Pracovníci krajských úřadů pak
prostřednictvím aplikace iLAS pořizují zápis do centrální databáze.</p>
<p>Evidence ÚPD a ÚPP velkých územních celků probíhá taktéž průběžně, a to prostřednictvím
aplikace iKAS. Zápis do centrální databáze pořizují pověření pracovníci krajských úřadů.</p>
<p>Bližší podrobnosti o postupu orgánů územního plánování při evidenci viz výše uvedená
Metodika OÚP MMR pro postup orgánu územního plánování při evidenci územně plánovací činnosti
(dále jen Metodika OÚP MMR).</p>

<h2>Zveřejňování získaných údajů</h2>
<p>Zveřejňování získaných údajů o územně plánovací činnosti v ČR je prováděno prostřednictvím:</p>
<ul>
  <li>průběžně aktualizovaných dat na www stránce ÚÚR a MMR;</li>
  <li>ročních přehledů (internetových prezentací), které obsahují vedle přehledů o stavu územně
      plánovací připravenosti obcí a krajů rovněž některé strukturně vývojové analýzy — schválené
      ÚPD podle velikostních kategorií obcí, počty obcí bez ÚPD podle velikostních kategorií obcí,
      struktury pořizovatelů ÚPD, průměrné doby procesu pořizování a další;</li>
  <li>článků v časopisech, například Urbanismus a územní rozvoj nebo Moderní obec.</li>
</ul>

<h2>Vývoj systému evidence</h2>
<p>Rozvoj evidence územně plánovací činnosti neustále pokračuje. Byl vyřešen problém aktualizace
databáze zodpovědných projektantů — autorizovaných architektů. Rovněž je průběžně čištěna databáze
zhotovitelů tak, aby byla v souladu s celostátními registry podnikatelských subjektů, právnických
i fyzických osob. Jedná se zejména o Obchodní rejstřík a Registr ekonomických subjektů.
Zde je nutno zdůraznit význam správného vyplňování registračních listů pořizovateli ÚPD a ÚPP,
a to nejlépe na základě smlouvy o dílo.</p>
<p>Evidence územně plánovací činnosti má vazbu na registr územní identifikace, adres a nemovitostí
(RÚIAN). Dovoluje tak přiřazovat data k příslušným katastrálním územím, obcím, obcím s rozšířenou
působností a krajům. Dále pak dovoluje připojení k mapovému podkladu.</p>

<h2>Proč je evidence důležitá</h2>
<p>Závěrem nutno zdůraznit, že schválený územní plán s jasnými, obecně závaznými pravidly pro
využití území významně ovlivňuje rozhodování soukromého sektoru o tom, kam vloží své prostředky
a jak se bude podílet na rozvoji obce nebo kraje. Územně plánovací dokumentace je dále jedním
z rozhodujících podkladů pro získávání veřejných prostředků a pro posouzení jejich hospodárného
vynaložení. Přehled o tom, které obce nebo kraje v České republice mají schválenou nebo
rozpracovanou územně plánovací dokumentaci, je velmi cennou informací, která se zveřejňováním
formou publikací (ročenek) a zejména prostřednictvím internetu zpřístupňuje široké veřejnosti.
Monitorování a zveřejňování výsledků evidence chápou ÚÚR a MMR jako službu veřejnosti, pomoc
prosadit a urychlit investice do území.</p>

<details class="acc" open data-faq>
  <summary>On-line evidence</summary>
  <div class="body"><ul>
      <li><a href="#">Evidence územně plánovací činnosti obcí – Lokální aktualizační systém - iLAS</a></li>
      <li><a href="#">Evidence územně plánovací činnosti krajů – Krajský aktualizační systém - iKAS</a></li>
    </ul></div>
</details>
<details class="acc" data-faq>
  <summary>Metodiky a příručky</summary>
  <div class="body"><p>Metodika OÚP MMR pro postup orgánů územního plánování při evidenci územně plánovací
    činnosti a navazující příručky.</p></div>
</details>
<details class="acc" data-faq>
  <summary>Ročenky</summary>
  <div class="body"><p>Roční přehledy o stavu územně plánovací připravenosti obcí a krajů.</p></div>
</details>
<details class="acc" data-faq>
  <summary>Seznam projektantů</summary>
  <div class="body"><p>Databáze zodpovědných projektantů — autorizovaných architektů.</p></div>
</details>
<details class="acc" data-faq>
  <summary>Územní studie</summary>
  <div class="body"><p>Evidence územních studií pořízených obcemi a kraji.</p></div>
</details>
<details class="acc" data-faq>
  <summary>Historie</summary>
  <div class="body"><p>Vývoj evidence územně plánovací činnosti a starší ročníky přehledů.</p></div>
</details>
"""

INFOWEB = """
<div class="btn-row"><a class="btn ghost lg" href="#">Vstup do portálu</a></div>

<h2>Základní informace</h2>
<ul>
  <li>Informační web územního plánování je oficiální portál (rozcestník odkazů) z oblasti
      územního plánování.</li>
  <li>Do 31. 12. 2021 fungoval pod názvem Portál územního plánování.</li>
  <li>Od 1. 1. 2022 došlo ke změně názvu Portálu územního plánování na Informační web územního
      plánování (zkratka IWÚP). Nový název více odpovídá zaměření webu — soustředění informací
      v oblasti územního plánování a souvisejících oborů do jednoho místa pro odbornou i laickou
      veřejnost, rozcestník odkazů a prezentace výstupů z činnosti ÚÚR a MMR. Současně je třeba
      předejít případné záměně s Národním geoportálem územního plánování, který nově připravuje
      MMR dle § 11 odst. 1 písm. d) stavebního zákona.</li>
  <li>Portál územního plánování byl uveden do provozu Ústavem územního rozvoje ve spolupráci
      s Odborem územního plánování Ministerstva pro místní rozvoj ČR v roce 2004.</li>
</ul>

<h2>Cíle portálu</h2>
<ul>
  <li>Cílem portálu je směřovat k vytváření otevřeného a průběžně aktualizovaného systému odkazů
      na relevantní informace v oblasti územního plánování a územního rozvoje, jež vyplývají
      zejména z činností ÚÚR, MMR a ostatních orgánů veřejné správy a odborných institucí.</li>
  <li>Je určen pro veřejnou správu, odbornou i laickou veřejnost.</li>
</ul>

<h2>Základní vize portálu</h2>
<ul>
  <li>Prioritně udržovat aktuálnost a kvalitu informací.</li>
  <li>Sledovat nová témata v územním rozvoji.</li>
  <li>Propagovat portál tak, aby byl cenným zdrojem informací nejen pro odbornou veřejnost.</li>
</ul>

<h2>Kontaktní osoby</h2>
<ul>
  <li>Kontakty na správce portálu najdete v <a href="{{r}}kontakty.html">Kontaktech</a>.</li>
</ul>
"""

PUR_DOKUMENTY = """
<div class="dokumenty">
<h3>Přiložené dokumenty</h3>
<ul class="files">
  <li><span class="ft">PDF</span><span class="grow"><span class="name">POLITIKA ÚZEMNÍHO ROZVOJE České republiky od 1.10. 2025</span><br>
    <span class="fmeta">296 KB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">PDF</span><span class="grow"><span class="name">POLITIKA ÚZEMNÍHO ROZVOJE České republiky od 1.10.2025</span><br>
    <span class="fmeta">296 KB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">PDF</span><span class="grow"><span class="name">SPATIAL DEVELOPMENT POLICY OF THE CZECH REPUBLIC</span><br>
    <span class="fmeta">296 KB</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
</ul>
</div>

<h2>O dokumentu</h2>
<p>Politika územního rozvoje ČR (dále také PÚR ČR) je celostátní nástroj územního plánování,
který slouží zejména pro koordinaci územního rozvoje na celostátní úrovni a pro koordinaci
územně plánovací činnosti krajů a současně jako zdroj důležitých argumentů při prosazování
zájmů ČR v rámci územního rozvoje Evropské unie.</p>
<p class="zvyrazneno">Aktuální a závazná od 1. 10. 2025 je Politika územního rozvoje České
republiky po Změně č. 8 Politiky územního rozvoje České republiky.</p>
<p class="zvyrazneno">Politika územního rozvoje České republiky (Úplné znění závazné
od 1. 10. 2025) a brožury v české, anglické a německé verzi jsou v části Přiložené dokumenty.</p>

<h2>Evidence podkladů pro Politiku územního rozvoje ČR</h2>
<p>Politika územního rozvoje – Evidence podkladů je součástí úkolu A.1.08/ÚP – Politika územního
rozvoje ČR a potřebné územně plánovací podklady. Úkol zpracovává Ústav územního rozvoje (ÚÚR)
z pověření odboru územního plánování Ministerstva pro místní rozvoj (OÚP MMR).</p>
<p>Cílem evidence je shromažďování vstupních podkladů a vedení databáze relevantních podkladů
pro pořizování aktualizací nebo nového návrhu PÚR ČR.</p>
<p>Zveřejněný seznam relevantních podkladů PÚR ČR (ve formátu PDF a XLSX):</p>
<ul class="files">
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Seznam relevantních podkladů PÚR ČR k 1. 7. 2023</span><br>
    <span class="fmeta">296 KB</span><span class="fpath">(Seznam-relevantnich-podkladu-PUR-CR-2023-07-01.pdf, 425 kB)</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">XLS</span><span class="grow"><span class="name">Seznam relevantních podkladů PÚR ČR k 1. 7. 2023</span><br>
    <span class="fmeta">296 KB</span><span class="fpath">(Seznam-relevantnich-podkladu-PUR-CR-2023-07-01.xlsx, 138 kB)</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
</ul>

<h2>Historie dokumentu</h2>
<ul>
  <li>Politika územního rozvoje České republiky 2008 (2009)</li>
  <li>Politika územního rozvoje České republiky – Aktualizace č. 1 (2015)</li>
  <li>Politika územního rozvoje České republiky – Aktualizace č. 2, 3 (2019)</li>
  <li>Politika územního rozvoje České republiky – Aktualizace č. 5 (2020)</li>
  <li>Politika územního rozvoje České republiky – Aktualizace č. 4 (2021)</li>
  <li>Politika územního rozvoje České republiky – Aktualizace č. 6 (2023)</li>
  <li>Politika územního rozvoje České republiky – Aktualizace č. 7 (2024)</li>
  <li>Politika územního rozvoje České republiky – Změna č. 9 (2025)</li>
  <li>Politika územního rozvoje České republiky – Změna č. 8 (2025)</li>
</ul>
<p>Ministerstvo pro místní rozvoj ČR pořídilo první dokument Politiky územního rozvoje České
republiky (PÚR ČR) v roce 2009.</p>
<p>Na základě Zprávy o uplatňování PÚR ČR 2008 Ministerstvo pro místní rozvoj pořídilo řádnou
Aktualizaci č. 1 PÚR ČR, na základě Zprávy o uplatňování Politiky územního rozvoje ČR, ve znění
Aktualizace č. 1 Ministerstvo pro místní rozvoj pořídilo řádnou Aktualizaci č. 4 PÚR ČR a na
základě Zprávy o uplatňování Politiky územního rozvoje ČR, po Aktualizaci č. 4 Ministerstvo pro
místní rozvoj nyní pořizuje řádnou aktualizaci PÚR ČR – návrh Změny č. 8 PÚR ČR (s termínem pro
předložení vládě ČR do 30. 6. 2025). Na základě požadavku MMR byl termín pro předložení návrhu
Změny č. 8 PÚR ČR vládě ČR prodloužen do 31. 8. 2025.</p>
<p>Z důvodu naléhavého veřejného zájmu byly pořízeny z podnětů různých ministerstev mimořádné
aktualizace PÚR ČR – Aktualizace č. 2, 3, 5, 6 a 7.</p>
<p>Z důvodu naléhavého veřejného zájmu byla pořízena z podnětu Ministerstva průmyslu a obchodu
mimořádná změna PÚR ČR – Změna č. 9 PÚR ČR.</p>

<h2>Konzultační výbor pro zpracování Politiky územního rozvoje ČR</h2>
<p>Náplní práce Konzultačního výboru pro zpracování Politiky územního rozvoje ČR je zejména
zajišťování součinnosti ministerstev a jiných ústředních správních úřadů a krajů při pořizování
Politiky územního rozvoje ČR, resp. její aktualizace a při poskytování relevantních podkladů.</p>
<ul>
  <li><a href="#">Konzultační výbor pro zpracování Politiky územního rozvoje ČR</a> – přístup
      s heslem, určeno pro členy Konzultačního výboru PÚR ČR. Jsou zde k dispozici podkladové
      materiály pro jednotlivá jednání.</li>
  <li><a href="#">Konzultační výbor pro zpracování Politiky územního rozvoje ČR</a> – webové
      stránky MMR ČR.</li>
</ul>

<details class="acc" open data-faq>
  <summary>PÚR ČR – Aktualizace č. 1</summary>
  <div class="body"><p>Lorem</p></div>
</details>
<details class="acc" data-faq>
  <summary>Lorem ipsum</summary>
  <div class="body"><p>Lorem ipsum</p></div>
</details>
<details class="acc" data-faq>
  <summary>Lorem ipsum</summary>
  <div class="body"><p>Lorem ipsum</p></div>
</details>
<details class="acc" data-faq>
  <summary>Lorem ipsum</summary>
  <div class="body"><p>Lorem ipsum</p></div>
</details>
"""

MEZINARODNI = """
<div class="grid hub prejit">
  <a class="card" href="#" id="espon" data-more="Přejít" data-ico="zadna"><h3>ESPON</h3>
    <p>Monitorovací síť pro evropské územní plánování. ÚRÚ působí jako národní kontaktní místo
    programu, průběžně aktualizovaná agenda.</p></a>
  <a class="card" href="#" id="v42" data-more="Přejít" data-ico="zadna"><h3>V4+2</h3>
    <p>Spolupráce v oblasti územního rozvoje Visegrádských zemí, Rakouska a Německa. Oživující se
    agenda s uzavřeným pracovním intranetem.</p></a>
</div>
"""
