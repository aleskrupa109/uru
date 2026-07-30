# -*- coding: utf-8 -*-
"""Doplnění obsahu sekce Vyhrazené stavby podle návrhu (DESU_design.pdf, str. 4–9)."""

KATEGORIE = """
<h2>Přehled kategorií vyhrazených staveb</h2>

<h3>Dopravní stavby — dálnice a silnice</h3>
<ul>
  <li>Dálnice a rychlostní silnice včetně přeložek (investor ŘSD)</li>
  <li>Stavby na dálnicích a jejich součásti</li>
</ul>

<h3>Dopravní stavby — dráhy</h3>
<ul>
  <li>Železniční koridory a tratě celostátního významu (Správa železnic)</li>
  <li>Metro ve statutárních městech</li>
  <li>Tramvajové dráhy ve statutárních městech</li>
  <li>Stavby drah podle zákona č. 266/1994 Sb.</li>
</ul>

<h3>Dopravní stavby — letecké</h3>
<ul>
  <li>Dráhy ke vzletu a přistávání letadel</li>
  <li>Plochy určené k pohybu a stání letadel</li>
  <li>Letiště mezinárodního významu</li>
</ul>

<h3>Energetické stavby — elektroenergetika</h3>
<ul>
  <li>Vedení přenosové soustavy a transformovny</li>
  <li>Fotovoltaické elektrárny nad 5 MW</li>
  <li>Obnovitelné zdroje energie nad 1 MW (větrné parky, bioplynové stanice a další)</li>
  <li>Zařízení na energetické využívání odpadů</li>
  <li>Jaderné elektrárny a stavby jaderných zařízení</li>
</ul>

<h3>Energetické stavby — plynárenství a produktovody</h3>
<ul>
  <li>Přepravní soustava plynu a podzemní zásobníky</li>
  <li>Plynovody a produktovody kategorie VVTL</li>
</ul>

<h3>Tepelná infrastruktura a zachytávání CO₂</h3>
<ul>
  <li>Rozvodné tepelné soustavy a tepelná zařízení o dimenzi potrubí DN 300 a více</li>
  <li>Stavby pro zachytávání a ukládání oxidu uhličitého do přírodních horninových struktur</li>
  <li>Přepravní sítě k úložištím CO₂</li>
</ul>

<h3>Těžební stavby a stavby pro nakládání s výbušninami</h3>
<ul>
  <li>Stavby pro přípravu a dobývání ložisek, úpravu a zušlechťování nerostů</li>
  <li>Úložná místa pro těžební odpad</li>
  <li>Úložiště radioaktivních odpadů obsahujících přírodní radionuklidy</li>
  <li>Stavby určené k nakládání s výbušninami</li>
</ul>

<h3>Strategické investiční stavby</h3>
<p>Stavby vymezené zákonem o urychlení výstavby strategicky významné infrastruktury.</p>

<h3>Stavby v zastavitelných plochách nad 45 ha</h3>
<p>Stavby pro výrobu, skladování a bydlení umisťované v plochách vymezených pro tyto účely.
Do této kategorie spadají i průmyslové areály, které dříve pod ÚRÚ nespadaly:</p>
<ul>
  <li>Gigafaktory a velké výrobní závody</li>
  <li>Logistické parky a centra</li>
  <li>Výrobní areály (například automobilky)</li>
  <li>Podnikatelská centra v průmyslových zónách</li>
</ul>
"""

RIZENI_DETAIL = """
<h2 id="poplatky">Správní poplatky</h2>
<p>Některé úkony podléhají správnímu poplatku podle sazebníku správních poplatků.
Toto je primární místo, kde se poplatky popisují; ostatní stránky sem odkazují.</p>
<table class="t">
  <tr><th>Úkon</th><th>Poplatek</th></tr>
  <tr><td>Žádost o povolení záměru</td><td>dle položek sazebníku správních poplatků</td></tr>
  <tr><td>Změna rozhodnutí</td><td>dle sazebníku</td></tr>
  <tr><td>Vydání kolaudačního rozhodnutí</td><td>dle sazebníku</td></tr>
</table>
<table class="t">
  <tr><th style="width:220px">Číslo účtu</th><td>3711-1426011/0710</td></tr>
  <tr><th>Variabilní symbol</th><td>obdržíte od ÚRÚ ve výzvě k úhradě</td></tr>
</table>

<h2>Další typy řízení</h2>

<h3>Vyvlastňovací řízení</h3>
<p>ÚRÚ vede vyvlastňovací řízení pro vyhrazené stavby. Řízení je ústní a koncentrované —
námitky a důkazy je třeba uplatnit v jeho průběhu.</p>

<h3>Odvolací řízení</h3>
<p>ÚRÚ rozhoduje o odvoláních proti rozhodnutím krajských stavebních úřadů v případech
stanovených zákonem.</p>

<h3>Zkušební provoz a kolaudace</h3>
<p>Po dokončení stavby následuje zkušební provoz a kolaudační řízení.</p>
"""

UCASTNICI_DETAIL = """
<h2>Kdy je nahlédnutí možné</h2>
<p>Do spisu mohou nahlížet účastníci řízení a jejich zástupci. Jiné osoby, pokud prokáží
právní zájem, a to za podmínky, že nahlédnutím nebude narušeno právo některého z účastníků
ani veřejný zájem.</p>

<h2>Jak si domluvit návštěvu</h2>
<ol class="steps">
  <li><h3>Zjistěte spisovou značku</h3>
    <p>Najdete ji v oznámení o zahájení řízení nebo na úřední desce.</p></li>
  <li><h3>Napište nám</h3>
    <p>Na adresu podatelny uveďte spisovou značku, své postavení v řízení a navrhované termíny.</p></li>
  <li><h3>Potvrdíme termín</h3>
    <p>Ozve se vám oddělení pověřené vaším řízením a potvrdí konkrétní možnost nahlédnutí do spisu.</p></li>
</ol>
<p>Spis je veden v elektronické podobě. Z dokumentů lze pořizovat kopie a výpisy.</p>
"""

PORTAL_DETAIL = """
<h2>Co je Portál stavebníka</h2>
<p>Portál stavebníka je státní online systém pro komunikaci se stavebními úřady.
Provozuje jej Digitální a informační agentura (DIA).</p>

<h2>Co musíte udělat před podáním žádosti</h2>
<ul>
  <li>Mít prostředek pro elektronickou identifikaci (bankovní identita, eObčanka, NIA ID)</li>
  <li>Mít projektovou dokumentaci v PDF opatřenou autorizačním razítkem
      s kvalifikovaným elektronickým podpisem a časovým razítkem</li>
  <li>Mít vyplněný formulář žádosti podle typu řízení</li>
</ul>
"""

FAQ_EXTRA = [
    ("Dokumentace a technické požadavky", [
        ("V jakém formátu musí být projektová dokumentace předkládaná přes portál?",
         "V PDF, opatřená autorizačním razítkem s kvalifikovaným elektronickým podpisem a časovým razítkem."),
        ("Musí být dokumentace elektronicky podepsána autorizovanou osobou?",
         "Ano. Bez autorizačního razítka nelze dokumentaci do evidence vložit."),
    ]),
    ("Podání a komunikace", [
        ("Mohu podat žádost e-mailem nebo poštou?",
         "Žádost lze podat datovou schránkou, poštou i osobně. Projektová dokumentace však musí být "
         "vždy vložena do evidence elektronických dokumentací přes Portál stavebníka."),
        ("Na koho se obrátit s dotazem k mému konkrétnímu řízení?",
         "Na oddělení, které vaše řízení vede — kontakt najdete v oznámení o zahájení řízení."),
        ("Kde najdu kontakt na příslušné oddělení podle typu stavby?",
         "V sekci Kontakty jsou kontaktní karty rozdělené podle typu vyhrazené stavby."),
    ]),
    ("Vyvlastnění", [
        ("Kdy může ÚRÚ zahájit vyvlastňovací řízení?",
         "Za podmínek stanovených zákonem o vyvlastnění, pokud nebylo možné získat práva k pozemku dohodou."),
        ("Co s vyvlastňovacími řízeními zahájenými před účinností novely?",
         "Dokončují se podle pravidel platných v době jejich zahájení."),
    ]),
]
