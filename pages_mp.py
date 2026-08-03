# -*- coding: utf-8 -*-
"""Sekce Metodická podpora — obsah přepsaný podle návrhu (DESU_design.pdf, str. 11–24).

Odchylky od návrhu vycházejí ze zeleně schválených komentářů a jsou označené značkou
s číslem připomínky.
"""
from build import cmt
import content_mp_extra as M

C = [("Metodická podpora", "metodicka-podpora/index.html")]

ROZCESTNIK = """
<div class="grid g3">
  <a class="card" href="{{r}}metodicka-podpora/metodicka-stanoviska.html">
    <h3>Metodická stanoviska a výklady</h3>
    <p>Databáze výkladových stanovisek k novému i starému stavebnímu zákonu.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/caste-dotazy.html">
    <h3>Často kladené otázky</h3>
    <p>Srozumitelné výklady pro každodenní praxi stavebních úřadů a dotčených orgánů.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/prechodove-obdobi.html">
    <h3>Přechodové období</h3>
    <p>Co platí pro řízení zahájená před účinností novely. Změny pro dotčené orgány.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/standardizace.html">
    <h3>Standardizace územního plánování</h3>
    <p>Standardy pro tvorbu územních plánů — odděleně pro starý zákon a nový zákon.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/konzultacni-stredisko.html">
    <h3>Konzultační středisko</h3>
    <p>Zákonná metodická podpora pro úřady územního plánování.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/tisic-otazek.html">
    <h3>Tisíc otázek</h3>
    <p>Databáze zobecněných odpovědí na opakující se dotazy ke stavebnímu právu.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/dotcene-organy.html">
    <h3>Přehled dotčených orgánů""" + cmt(61, "Přehled dotčených orgánů patří do metodické části — je to informace pro stavební úřady a orgány územního plánování.") + """</h3>
    <p>Kdo vydává jaké vyjádření a v jaké fázi řízení. Aktualizace dvakrát ročně.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">
    <h3>Kontakty na metodiky""" + cmt(31, "Doplnit dlaždici Kontakty na metodiky — kontaktní karty podle oblasti jsou v IA, v návrhu jen jako CTA v patičce stránek.") + """</h3>
    <p>Kontaktní karty metodiků podle věcné oblasti — ne obecná schránka úřadu.</p></a>
</div>
"""

STANOVISKA = """
<div class="filters" data-filterable>
  <div class="searchrow">
    <input type="search" data-q placeholder="Hledejte v metodických stanoviscích…">
    <button class="searchbtn" type="button" aria-label="Hledat">{SEARCH}</button>
  </div>

  <fieldset class="fgroup"><legend>Oblast</legend>
    <label for="o-sr"><input type="checkbox" id="o-sr" data-key="oblast" value="sr"> Stavební řád</label>
    <label for="o-up"><input type="checkbox" id="o-up" data-key="oblast" value="up"> Územní plánování</label>
    <label for="o-eia"><input type="checkbox" id="o-eia" data-key="oblast" value="eia"> EIA a dotčené orgány</label>
  </fieldset>

  <fieldset class="fgroup"><legend>Zákon</legend>
    <label for="z-283"><input type="checkbox" id="z-283" data-key="zakon" value="283"> 283/2021 Sb. (nový)</label>
    <label for="z-183"><input type="checkbox" id="z-183" data-key="zakon" value="183"> 183/2006 Sb. (starý)</label>
  </fieldset>

  <div class="fcols">
    <fieldset class="fgroup"><legend>Platnost</legend>
      <label for="p-platne"><input type="checkbox" id="p-platne" data-key="platnost" value="platna"> Platné</label>
      <label for="p-neplatne"><input type="checkbox" id="p-neplatne" data-key="platnost" value="neplatna"> Neplatné</label>
    </fieldset>
    <fieldset class="fgroup"><legend>Aktuálnost</legend>
      <label for="a-akt"><input type="checkbox" id="a-akt" data-key="aktualnost" value="aktualni"> Aktuální</label>
      <label for="a-hist"><input type="checkbox" id="a-hist" data-key="aktualnost" value="historicka"> Historické</label>
      <label for="a-nahr"><input type="checkbox" id="a-nahr" data-key="aktualnost" value="nahrazena"> Nahrazené</label>
    </fieldset>
  </div>

  <fieldset class="fgroup"><legend>Datum vydání</legend>
    <div class="frow">
      <span class="field"><label for="d-od">Od</label><input id="d-od" type="text" placeholder="DD.MM.RRRR"></span>
      <span class="field"><label for="d-do">Do</label><input id="d-do" type="text" placeholder="DD.MM.RRRR"></span>
    </div>
  </fieldset>

  <p class="hint">Platnost je právní status dokumentu, aktuálnost říká, zda dokument nebyl
  nahrazen novějším. Jsou to dvě nezávislá metadata a u každého dokumentu se evidují zvlášť.""" + cmt(34, "Filtry Platnost a Aktuálnost jsou dvě samostatné osy — dvě povinná metadata u každého dokumentu. Potvrdit s redakcí.") + """
  Vyhledávání prochází i obsah připojených PDF.""" + cmt(98, "Chybí indikace, že se prohledává i obsah příloh (PDF).") + """</p>
  <div class="chips" data-chips></div>
  <button class="btn ghost sm" type="button" data-reset>Zrušit filtry</button>
</div>

<div class="resultbar">
  <span>Nalezeno <strong data-count>0</strong> dokumentů</span>
  <span class="right">
    <label>Řadit podle
      <select data-sort><option value="rel">relevance</option><option value="date">data vydání</option></select></label>""" + cmt(36, "Chybí řazení výsledků (relevance / datum) a volba počtu položek na stránku.") + """
    <label>Na stránku
      <select data-per><option>10</option><option>20</option><option>50</option></select></label>
  </span>
</div>

<ul class="doclist" data-list>
<li data-oblast="sr" data-zakon="283" data-platnost="platna" data-aktualnost="aktualni" data-date="2026-11-26"><div class="tags"><span class="tag hist">Zákon č. 283/2021 Sb.</span><span class="tag hist">Stavební řád</span><span class="tag valid">Platné</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k §184a — Integrace dotčených orgánů do řízení po 1. 7. 2026</a></h3><p class="doc-date">{CAL}Aktualizováno: 26. 11. 2026</p><p>Stanovisko popisuje postup integrace dotčených orgánů do společného řízení o povolení záměru podle nového stavebního zákona, včetně lhůt a náležitostí koordinovaného závazného stanoviska.</p></li>
<li data-oblast="sr" data-zakon="283" data-platnost="platna" data-aktualnost="aktualni" data-date="2026-11-26"><div class="tags"><span class="tag hist">Zákon č. 283/2021 Sb.</span><span class="tag hist">Stavební řád</span><span class="tag valid">Platné</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k §85 — společné územní a stavební řízení</a></h3><p class="doc-date">{CAL}Aktualizováno: 26. 11. 2026</p><p>Stanovisko vyjasňuje podmínky, za nichž může stavební úřad sloučit územní a stavební řízení do společného postupu.</p></li>
<li data-oblast="sr" data-zakon="283" data-platnost="platna" data-aktualnost="nahrazena" data-date="2025-03-02"><div class="tags"><span class="tag hist">Zákon č. 283/2021 Sb.</span><span class="tag hist">Stavební řád</span><span class="tag valid">Platné</span><span class="tag superseded">Nahrazené</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k postupu při vadách žádosti</a></h3><p class="doc-date">{CAL}Aktualizováno: 2. 3. 2025</p><p>Postup úřadu při výzvě k doplnění a běh lhůt.</p><div class="supersede">Nahrazeno novějším dokumentem: <a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k §184a</a></div></li>
<li data-oblast="up" data-zakon="283" data-platnost="platna" data-aktualnost="aktualni" data-date="2026-05-20"><div class="tags"><span class="tag hist">Zákon č. 283/2021 Sb.</span><span class="tag hist">Územní plánování</span><span class="tag valid">Platné</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k pořizování územních plánů obcí</a></h3><p class="doc-date">{CAL}Aktualizováno: 20. 5. 2026</p><p>Postup pořizovatele a role určeného zastupitele.</p></li>
<li data-oblast="up" data-zakon="283" data-platnost="platna" data-aktualnost="aktualni" data-date="2026-04-14"><div class="tags"><span class="tag hist">Zákon č. 283/2021 Sb.</span><span class="tag hist">Územní plánování</span><span class="tag valid">Platné</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k vymezení zastavěného území</a></h3><p class="doc-date">{CAL}Aktualizováno: 14. 4. 2026</p><p>Postup pro obce bez územního plánu a náležitosti vymezení.</p></li>
<li data-oblast="eia" data-zakon="283" data-platnost="platna" data-aktualnost="aktualni" data-date="2026-03-05"><div class="tags"><span class="tag hist">Zákon č. 283/2021 Sb.</span><span class="tag hist">EIA a dotčené orgány</span><span class="tag valid">Platné</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k vyjádření dotčeného orgánu ve lhůtě 30 dnů</a></h3><p class="doc-date">{CAL}Aktualizováno: 5. 3. 2026</p><p>Postup dotčeného orgánu při doručení podkladů a stavění lhůty při jejich doplňování.</p></li>
<li data-oblast="eia" data-zakon="283" data-platnost="platna" data-aktualnost="aktualni" data-date="2026-02-11"><div class="tags"><span class="tag hist">Zákon č. 283/2021 Sb.</span><span class="tag hist">EIA a dotčené orgány</span><span class="tag valid">Platné</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko ke zrušení jednotného environmentálního stanoviska</a></h3><p class="doc-date">{CAL}Aktualizováno: 11. 2. 2026</p><p>Jak se obsah dosavadního JES promítá do vyjádření jednotlivých dotčených orgánů.</p></li>
<li data-oblast="sr" data-zakon="283" data-platnost="platna" data-aktualnost="historicka" data-date="2025-09-30"><div class="tags"><span class="tag hist">Zákon č. 283/2021 Sb.</span><span class="tag hist">Stavební řád</span><span class="tag valid">Platné</span><span class="tag hist">Historické</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k přechodu rozpracovaných řízení</a></h3><p class="doc-date">{CAL}Aktualizováno: 30. 9. 2025</p><p>Ponecháno kvůli řízením zahájeným před účinností novely.</p></li>
<li data-oblast="up" data-zakon="183" data-platnost="neplatna" data-aktualnost="historicka" data-date="2023-11-08"><div class="tags"><span class="tag hist">Zákon č. 183/2006 Sb.</span><span class="tag hist">Územní plánování</span><span class="tag invalid">Neplatné</span><span class="tag hist">Historické</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Stanovisko k obsahu zadání územního plánu</a></h3><p class="doc-date">{CAL}Aktualizováno: 8. 11. 2023</p><p>Ponecháno kvůli kontinuitě a probíhajícím soudním sporům.</p></li>
<li data-oblast="up" data-zakon="183" data-platnost="neplatna" data-aktualnost="historicka" data-date="2023-05-22"><div class="tags"><span class="tag hist">Zákon č. 183/2006 Sb.</span><span class="tag hist">Územní plánování</span><span class="tag invalid">Neplatné</span><span class="tag hist">Historické</span></div><h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Stanovisko k projednávání změn územního plánu zkráceným postupem</a></h3><p class="doc-date">{CAL}Aktualizováno: 22. 5. 2023</p><p>Ponecháno kvůli probíhajícím pořizovacím procesům.</p></li>
</ul>
<div class="empty" data-empty style="display:none">Zadanému filtru neodpovídá žádné stanovisko.
Zkuste zrušit filtr platnosti nebo aktuálnosti.</div>

<nav class="pager" aria-label="Stránkování">
  <a href="#" aria-current="page">1</a><a href="#">2</a><a href="#">3</a><a href="#">4</a>
  <span>…</span><a href="#">10</a><a href="#">11</a>
</nav>
"""

DETAIL = """
<div class="tags" style="display:flex;gap:8px;margin-bottom:12px">
  <span class="tag hist">Stavební řád</span><span class="tag hist">Zákon č. 283/2021 Sb.</span>
  <span class="tag valid">Platné</span><span class="tag neutral">Aktuální</span>
</div>
<p class="updated">Vydáno: 26. 11. 2026 · Aktualizováno: 26. 11. 2026</p>

<p>Stanovisko vyjasňuje podmínky, za nichž může stavební úřad sloučit územní a stavební řízení
do společného postupu podle §85 nového stavebního zákona. Zaměřuje se na situace, kdy je
žadatel povinen doložit předchozí územní souhlas, a na výjimky platné pro vyhrazené stavby
ve správě ÚRÚ.</p>

<h2>Soubor ke stažení</h2>
<ul class="files"><li><span class="ft">PDF</span>
  <span class="grow"><span class="name">Metodické stanovisko k §85 — společné územní a stavební řízení</span><br>
  <span class="fmeta">296 kB · fulltextově indexováno</span></span>
  <a class="btn ghost sm" href="#">Stáhnout</a></li></ul>

<h2>Základní údaje</h2>
<table class="t">
  <tr><th style="width:220px">Číslo jednací</th><td>ÚRÚ-0000/2026</td></tr>
  <tr><th>Oblast</th><td>Stavební řád</td></tr>
  <tr><th>Zákon</th><td>č. 283/2021 Sb.</td></tr>
  <tr><th>Platnost</th><td>Platné</td></tr>
  <tr><th>Aktuálnost</th><td>Aktuální — nebylo nahrazeno novějším dokumentem</td></tr>
</table>

<h2>Související dokumenty""" + cmt(39, "„Související dokumenty\" nemá označení typu vztahu (nahrazuje / je nahrazeno / navazuje).") + """</h2>
<table class="t">
  <tr><th style="width:180px">Vztah</th><th>Dokument</th></tr>
  <tr><td><span class="tag neutral">Navazuje na</span></td>
      <td><a href="#">Metodické stanovisko k §184a — Integrace dotčených orgánů do řízení</a><br>
      <span class="fmeta">Stanovisko popisuje postup integrace dotčených orgánů do společného
      řízení o povolení záměru, včetně lhůt a náležitostí koordinovaného závazného stanoviska.</span></td></tr>
  <tr><td><span class="tag superseded">Nahrazuje</span></td>
      <td><a href="#">Metodické stanovisko k postupu při vadách žádosti (2025)</a></td></tr>
  <tr><td><span class="tag hist">Souvisí s</span></td>
      <td><a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a></td></tr>
</table>

<h2>Historie verzí""" + cmt(40, "Chybí historie verzí dokumentu.") + """</h2>
<table class="t">
  <tr><th style="width:140px">Verze</th><th>Datum</th><th>Změna</th></tr>
  <tr><td>1.0</td><td>26. 11. 2026</td><td>První vydání</td></tr>
  <tr><td>0.9</td><td>2. 6. 2026</td><td>Pracovní znění k připomínkám</td></tr>
</table>
"""

FAQ_TABS = """
<div class="tabs">
  <a href="{{r}}metodicka-podpora/caste-dotazy.html"@A1@>Stavební úřady</a>
  <a href="{{r}}metodicka-podpora/caste-dotazy-dotcene-organy.html"@A2@>Dotčené orgány</a>
  <a href="{{r}}metodicka-podpora/caste-dotazy-uzemni-planovani.html"@A3@>Úřady územního plánování""" + cmt(41, "Doplnit třetí záložku pro úřady územního plánování — persony ji označují jako opomíjenou podskupinu.") + """</a>
</div>
<div class="box change">
  <h3>Přechodné období</h3>
  <p>Řízení zahájená před účinností novely se dokončují podle dosavadní právní úpravy.
  Podrobnosti najdete v sekci
  <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a>.</p>
</div>
<div class="filters">
  <div class="searchrow"><input type="search" placeholder="Hledat v otázkách…"
    oninput="var q=this.value.toLowerCase();document.querySelectorAll('[data-faq]').forEach(function(d){d.style.display=d.textContent.toLowerCase().indexOf(q)>-1?'':'none'});document.querySelectorAll('[data-faqgroup]').forEach(function(g){g.style.display=g.querySelectorAll('[data-faq]:not([style*=none])').length?'':'none'})"></div>
  <p class="hint" style="margin:0">Vyhledávání prochází znění otázek i odpovědí.""" + cmt(43, "Chybí vyhledávání v otázkách.") + """</p>
</div>
"""


def faq(active, groups):
    a = ["", "", ""]
    a[active] = ' aria-current="page"'
    out = FAQ_TABS
    for i in (1, 2, 3):
        out = out.replace('@A%d@' % i, a[i - 1])
    for grp, qs in groups:
        out += f'<div data-faqgroup><h2>{grp}</h2>'
        for q, ans in qs:
            out += (f'<details class="acc" data-faq><summary>{q}</summary>'
                    f'<div class="body"><p>{ans}</p></div></details>')
        out += '</div>'
    return out


FAQ_SU = faq(0, [
    ("Přechodné období", [
        ("Co se stane s řízeními, která jsem zahájil před účinností novely?",
         "Dokončují se podle dosavadní právní úpravy. Rozhodující je datum doručení žádosti stavebnímu úřadu."),
        ("Jsou závazná stanoviska dotčených orgánů vydaná dříve stále platná?",
         "Ano, zůstávají platná."),
        ("Mám pravomocné územní rozhodnutí vydané dříve — je stále platné?",
         "Ano, pravomocná rozhodnutí zůstávají v platnosti."),
        ("Mohu použít projektovou dokumentaci zpracovanou podle starého stavebního zákona?",
         "Ano, dokumentace zpracovaná podle dosavadní úpravy zůstává použitelná."),
    ]),
    ("Proces řízení", [
        ("Jak probíhá integrované řízení z pohledu stavebního úřadu?",
         "Úřad vedoucí řízení si vyžádá vyjádření dotčených orgánů a koordinuje je v jednom řízení."),
        ("Musím aktivně oslovovat dotčené orgány, nebo to koordinuje Portál stavebníka?",
         "Podklady se dotčeným orgánům předávají prostřednictvím Portálu stavebníka."),
        ("Co dělat, když dotčený orgán nevydá vyjádření ve lhůtě?",
         "Postup pro nečinnost dotčeného orgánu popisuje metodické stanovisko k integraci dotčených orgánů."),
        ("Kdy aplikuji společné územní a stavební řízení a kdy ne?",
         'Podmínky vyjasňuje <a href="{{r}}metodicka-podpora/stanovisko-detail.html">metodické stanovisko k §85</a>.'),
        ("Jak postupovat při změně pravomocného rozhodnutí vydaného dříve?",
         "Změna se posuzuje podle pravidel platných v době vydání původního rozhodnutí, "
         "není-li v přechodných ustanoveních stanoveno jinak."),
    ]),
    ("Dokumentace", [
        ("V jakém formátu musí být projektová dokumentace předkládaná přes portál?",
         "V PDF, opatřená autorizačním razítkem s kvalifikovaným elektronickým podpisem a časovým razítkem."),
        ("Co je ID dokumentace a kde ho najdu?",
         "ID přiděluje evidence elektronických dokumentací po nahrání přes Portál stavebníka."),
        ("Musí být dokumentace elektronicky podepsána autorizovanou osobou?",
         "Ano. Bez autorizačního razítka nelze dokumentaci do evidence vložit."),
    ]),
    ("Metodická podpora", [
        ("Kdo je teď metodický garant pro stavební řád místo MMR?",
         'Metodické vedení převzal ÚRÚ. Kontakt najdete v <a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">Kontaktech na metodiky</a>.'),
        ("Kde najdu výklad konkrétního paragrafu nového stavebního zákona?",
         'V databázi <a href="{{r}}metodicka-podpora/metodicka-stanoviska.html">Metodická stanoviska a výklady</a>.'),
        ("Na koho se obrátit, když metodické stanovisko neřeší můj konkrétní případ?",
         'Na metodika podle věcné oblasti, u územního plánování na '
         '<a href="{{r}}metodicka-podpora/konzultacni-stredisko.html">Konzultační středisko</a>.'),
    ]),
])

FAQ_DO = faq(1, [
    ("Co se mění", [
        ("Co nahrazuje závazné stanovisko?",
         "Dotčený orgán vydává vyjádření, které se zapojuje do koordinovaného stanoviska."),
        ("Co se stalo s jednotným environmentálním stanoviskem (JES)?",
         "Jednotné environmentální stanovisko se ruší; jeho obsah přechází do vyjádření dotčených orgánů."),
        ("Vydáváme vyjádření samostatně, nebo společně s ostatními dotčenými orgány?",
         "Samostatně, v rámci koordinovaného stanoviska, které sestavuje úřad vedoucí řízení."),
        ("Jak se mění forma dokumentu, který vydáváme?",
         "Mění se typ dokumentu i způsob jeho zapojení do řízení. Vzory najdete v Přechodovém období."),
        ("Platí pro nás jiné lhůty než dosud?",
         "Lhůta pro vydání vyjádření je 30 dnů od doručení podkladů."),
    ]),
    ("Přechodové období", [
        ("Jak postupovat u řízení zahájených dříve, kde jsme vydali závazné stanovisko?",
         "Řízení se dokončuje podle dosavadní úpravy; vydané závazné stanovisko zůstává platné."),
        ("Je naše závazné stanovisko vydané dříve stále platné pro probíhající řízení?",
         "Ano, zůstává platné."),
    ]),
    ("Komunikace a technické otázky", [
        ("Jak nás stavební úřad osloví — přes Portál stavebníka, nebo e-mailem?",
         "Podklady přicházejí prostřednictvím Portálu stavebníka, nikoli e-mailem."),
        ("Kde najdeme podklady k řízení, ke kterým máme vydat vyjádření?",
         "V Portálu stavebníka, v evidenci elektronických dokumentací."),
        ("Co dělat, když potřebujeme k vydání vyjádření více podkladů, než jsme dostali?",
         "Vyžádejte doplnění u úřadu vedoucího řízení; po dobu doplňování lhůta neběží."),
        ("Jak postupovat, pokud je věc mimo naši věcnou příslušnost?",
         "Neprodleně to sdělte úřadu vedoucímu řízení, aby mohl vyžádat vyjádření správného orgánu."),
        ("Co dělat, když nestíháme vydat vyjádření ve lhůtě?",
         "Obraťte se na úřad vedoucí řízení; postup pro tento případ popisuje metodické stanovisko."),
    ]),
    ("Metodická podpora", [
        ("Kdo je teď metodický garant pro naši oblast místo MMR?",
         'Metodické vedení převzal ÚRÚ. Kontakt najdete v <a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">Kontaktech na metodiky</a>.'),
        ("Kde najdeme instrukce k novému formátu vyjádření?",
         'V sekci <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a>.'),
        ("Na koho se obrátit s dotazem k přechodnému období?",
         "Na metodika podle věcné oblasti."),
    ]),
])

FAQ_UP = faq(2, [
    ("Metodické vedení", [
        ("Kdo je nyní mým metodickým garantem pro územní plánování?",
         'Metodici územního plánování přešli z MMR na ÚRÚ. Kontakt najdete v '
         '<a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">Kontaktech na metodiky</a>.'),
        ("Kde najdu metodiky vztahující se jen k územnímu plánování?",
         "V databázi stanovisek použijte filtr Oblast = Územní plánování."),
        ("Kam se obrátit s dotazem, který stanoviska neřeší?",
         'Na <a href="{{r}}metodicka-podpora/konzultacni-stredisko.html">Konzultační středisko</a>.'),
    ]),
    ("Pořizování dokumentace", [
        ("Co platí pro pořizování územního plánu zahájené dříve?",
         'Viz <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a>.'),
        ("Kde najdu jednotný standard územně plánovací dokumentace?",
         'Na stránce <a href="{{r}}metodicka-podpora/standardizace.html">Standardizace územního plánování</a>.'),
    ]),
])

PRECHOD = """
<div class="box change">
  <h3>Protějšek pro stavebníky</h3>
  <p>Tato stránka popisuje dopady pro úřady a dotčené orgány. Stejné téma z pohledu stavebníků
  najdete na stránce <a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co změní novela SZ</a>.
  Obě stránky používají stejný vzor a vzájemně se odkazují.""" + cmt(44, "Tato stránka je protějškem stránky „Co změní novela SZ\" pro druhé publikum. Provázat a sjednotit vzor.") + """</p>
</div>

<h2>Rozpracovaná řízení</h2>
<p>Řízení zahájená přede dnem účinnosti novely se dokončují podle dosavadních pravidel,
není-li v přechodných ustanoveních stanoveno jinak.</p>
""" + M.PRECHOD_DETAIL + """

<h2 id="delimitace">Delimitace — řízení přecházející z obecných stavebních úřadů""" + cmt(45, "Chybí část k delimitaci: co se stane s řízeními, která dnes vede obecný stavební úřad a nově spadnou pod ÚRÚ.") + """</h2>
<p>Novela rozšiřuje okruh vyhrazených staveb. Část řízení, která dnes vedou obecné stavební
úřady, tím přechází na ÚRÚ. Tato situace se řídí jinými pravidly než běžné přechodné ustanovení.</p>
<table class="t">
  <tr><th style="width:34%">Situace</th><th>Kdo řízení dokončí</th><th>Co udělat</th></tr>
  <tr><td>Řízení zahájené u obecného SÚ, stavba nově vyhrazená</td><td>ÚRÚ po předání spisu</td><td>Úřad předá spis, účastníky vyrozumí ÚRÚ</td></tr>
  <tr><td>Řízení pravomocně skončené</td><td>—</td><td>Rozhodnutí zůstává v platnosti</td></tr>
  <tr><td>Záměr dosud nepodaný</td><td>ÚRÚ</td><td>Podat rovnou u ÚRÚ</td></tr>
</table>

<h2>Změny pro dotčené orgány</h2>
<p>Mění se typ vydávaného dokumentu i způsob jeho zapojení do řízení. Podrobnosti najdete
v <a href="{{r}}metodicka-podpora/caste-dotazy-dotcene-organy.html">Často kladených otázkách
pro dotčené orgány</a>.</p>

<h2>Vzory dokumentů ke stažení</h2>
<p>Vzory a formuláře jsou spravovány na jednom místě v sekci
<a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html">Dokumenty a formuláře</a>.""" + cmt(46, "„Vzory dokumentů ke stažení\" duplikují Dokumenty a formuláře. Určit jedno místo správy.") + """</p>
"""

STANDARDIZACE = """
<div class="tabs">
  <a href="{{r}}metodicka-podpora/standardizace.html" aria-current="page">Nový zákon (od 1. 7. 2024)</a>
  <a href="{{r}}metodicka-podpora/standardizace.html#stara">Starý zákon (do 30. 6. 2024)</a>
</div>
""" + M.STANDARDIZACE_DETAIL + """
<h2 id="stara">Starý zákon</h2>
<p>Materiály k dokumentaci pořizované podle dřívější právní úpravy zůstávají dostupné kvůli
kontinuitě a probíhajícím řízením.</p>
"""

KONZULTACNI = M.KONZULTACNI_DETAIL + """
<h2>Jak podat dotaz</h2>
<p>Zašlete e-mail na adresu konzultačního střediska. Aby bylo možné dotaz rychle zpracovat,
uveďte prosím:</p>
<ul>
  <li>název orgánu a obec / kraj</li>
  <li>stručný popis situace, kterou řešíte</li>
  <li>odkaz na konkrétní paragraf nebo zákon</li>
  <li>přesně formulovanou otázku</li>
</ul>

<h2>Formulář dotazu""" + cmt(50, "Chybí strukturovaný formulář dotazu. Stránka sama vyjmenovává, co musí dotaz obsahovat.") + """</h2>
<div class="filters">
  <div class="row">
    <div class="field" style="min-width:260px"><label for="k1">Název orgánu</label><input id="k1" placeholder="Např. Úřad územního plánování…"></div>
    <div class="field" style="min-width:220px"><label for="k1b">Obec / kraj</label><input id="k1b"></div>
    <div class="field" style="min-width:260px"><label for="k2">Kontaktní osoba a e-mail</label><input id="k2"></div>
    <div class="field" style="min-width:220px"><label for="k3">Odkaz na paragraf nebo zákon</label><input id="k3" placeholder="Např. §85 zák. č. 283/2021 Sb."></div>
  </div>
  <div class="row" style="margin-top:14px">
    <div class="field" style="flex:1;min-width:100%"><label for="k4">Stručný popis situace a přesně formulovaná otázka</label>
      <textarea id="k4" rows="5"></textarea></div>
  </div>
  <div class="btn-row"><button class="btn" type="button">Odeslat dotaz</button></div>
  <p class="hint">Formulář se odesílá do spisové služby úřadu a je mu přiděleno číslo jednací.</p>
</div>
"""

TISIC = M.TISIC_ROZCESTNIK

TISIC_SEZNAM = """
<div class="filters">
  <div class="searchrow">
    <input type="search" id="tq" placeholder="Hledat v otázkách…"
      oninput="var q=this.value.toLowerCase();document.querySelectorAll('[data-h]').forEach(function(d){d.style.display=d.textContent.toLowerCase().indexOf(q)>-1?'':'none'})">
    <select id="tscope">
      <option>Hledat v názvech hesel</option>
      <option>Hledat v hesle i v odpovědích</option>
    </select>
  </div>
  <p class="hint" style="margin:0">Přepínač určuje, zda se hledá jen v názvu hesla, nebo i v textu odpovědí.""" + cmt(53, "Není zřejmé, zda vyhledávací pole hledá v názvech hesel, nebo i v textu odpovědí.") + """</p>
</div>
<h2>Seznam hesel</h2>
<ul class="doclist">""" + "".join(
    f'<li data-h><h3><a href="{{{{r}}}}metodicka-podpora/tisic-otazek-heslo.html">{t}</a></h3>'
    f'<p>{n} otázek</p></li>' for t, n in M.HESLA) + """</ul>
"""

TISIC_HESLO = """
<div class="filters">
  <div class="searchrow"><input type="search" placeholder="Hledat v otázkách…"
    oninput="var q=this.value.toLowerCase();document.querySelectorAll('[data-faq]').forEach(function(d){d.style.display=d.textContent.toLowerCase().indexOf(q)>-1?'':'none'})"></div>
</div>
<h2>Seznam otázek</h2>
<details class="acc" data-faq open id="q-01">
  <summary>01. Kde najdu adresy krajských úřadů a jejich odborů s kompetencí pro územní plánování a stavební řád?</summary>
  <div class="body">
    <p>Adresář krajských úřadů naleznete na stránkách Konzultačního střediska.</p>
    <p class="source">Aktualizace 7/2024 · <a href="#q-01">trvalý odkaz na otázku</a>
    <button class="btn ghost sm" type="button" onclick="navigator.clipboard&&navigator.clipboard.writeText(location.origin+location.pathname+'#q-01');this.textContent='Zkopírováno'">Kopírovat odkaz</button>""" + cmt(54, "Chybí trvalý odkaz na jednotlivou otázku — odpovědi se používají v korespondenci.") + """</p>
  </div>
</details>
<details class="acc" data-faq id="q-02">
  <summary>02. Kde najdu adresy úřadů územního plánování?</summary>
  <div class="body">
    <p>Seznam najdete ve vyhlášce č. 553/2020 Sb., o seznamu obecních úřadů a úřadů městských
    částí nebo městských obvodů, které jsou kontaktními místy veřejné správy, ve znění
    pozdějších předpisů. Adresář úřadů územního plánování naleznete na stránkách úřadu.</p>
    <p class="source">Aktualizace 7/2024 · <a href="#q-02">trvalý odkaz na otázku</a></p>
  </div>
</details>
"""

KONTAKTY_METODIKY = """
<p>Kontaktní karty metodiků podle věcné oblasti. Údaje jsou převzaté z centrální stránky
<a href="{{r}}kontakty.html">Kontakty</a>, která je jediným zdrojem kontaktních dat.""" + cmt(92, "Kontakty jsou na třech místech. Určit jeden zdroj dat a pravidlo, co se kde zobrazuje.") + """</p>
<div class="contactcards">
  <div class="contactcard"><h3>Metodika — stavební řád</h3><p class="role">Oddělení metodiky stavebního řádu</p>
    <p class="agenda">Výklad povolovacích procesů, vady žádosti, lhůty, odvolání</p>
    <dl><dt>E-mail</dt><dd>metodika-sr@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
  <div class="contactcard"><h3>Metodika — územní plánování</h3><p class="role">Oddělení metodiky územního plánování</p>
    <p class="agenda">Pořizování ÚPD, zadání a změny územních plánů, zásady územního rozvoje</p>
    <dl><dt>E-mail</dt><dd>metodika-up@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
  <div class="contactcard"><h3>Metodika — EIA a dotčené orgány</h3><p class="role">Oddělení metodiky</p>
    <p class="agenda">Integrace dotčených orgánů, vyjádření, koordinované stanovisko</p>
    <dl><dt>E-mail</dt><dd>metodika-do@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
  <div class="contactcard"><h3>Konzultační středisko</h3><p class="role">Metodické vedení úřadů územního plánování</p>
    <p class="agenda">Dotazy úřadů územního plánování ze zákona</p>
    <dl><dt>Formulář</dt><dd><a href="{{r}}metodicka-podpora/konzultacni-stredisko.html">Položit dotaz</a></dd></dl></div>
</div>
"""

DOTCENE = """
<div class="box gap">
  <h3>Přesunuto z Územního rozvoje</h3>
  <p>Přehled dotčených orgánů je primárně informace pro stavební úřady a orgány územního
  plánování, proto je zařazen do Metodické podpory. Ze sekce Územní rozvoj sem vede křížový
  odkaz, protože uživatelé ÚÚR jsou zvyklí hledat obsah tam.""" + cmt(61, "Chybí Přehled dotčených orgánů. I po přesunu do Metodické podpory doplnit křížový odkaz z Územního plánování.") + """</p>
</div>
<p class="updated">Přehled se aktualizuje dvakrát ročně. Poslední aktualizace 30. 6. 2026.</p>
<table class="t">
  <tr><th>Chráněný veřejný zájem</th><th>Dotčený orgán</th><th>Typ dokumentu</th></tr>
  <tr><td>Ochrana veřejného zdraví</td><td>Krajská hygienická stanice</td><td>vyjádření</td></tr>
  <tr><td>Požární ochrana</td><td>Hasičský záchranný sbor kraje</td><td>vyjádření</td></tr>
  <tr><td>Ochrana přírody a krajiny</td><td>Orgán ochrany přírody</td><td>vyjádření</td></tr>
  <tr><td>Vodní hospodářství</td><td>Vodoprávní úřad</td><td>vyjádření</td></tr>
  <tr><td>Památková péče</td><td>Orgán státní památkové péče</td><td>vyjádření</td></tr>
  <tr><td>Ochrana zemědělského půdního fondu</td><td>Orgán ochrany ZPF</td><td>vyjádření</td></tr>
</table>
"""

PAGES = [
    dict(path="metodicka-podpora/index.html", title="Metodická podpora", section="metodicka-podpora",
         crumbs=[("Metodická podpora", None)], sidebar=False, h1="Metodická podpora",
         perex="Metodická podpora stavebních úřadů a dotčených orgánů je zákonnou agendou ÚRÚ. Najdete zde výkladová stanoviska, návody k novému stavebnímu zákonu, databázi Tisíc otázek a přímý kontakt na metodiky.",
         body=ROZCESTNIK),
    dict(help="metodiky", path="metodicka-podpora/metodicka-stanoviska.html",
         title="Metodická stanoviska a výklady", section="metodicka-podpora",
         crumbs=C + [("Metodická stanoviska a výklady", None)],
         h1="Metodická stanoviska a výklady",
         perex="Přehled metodických stanovisek, výkladů a pokynů. Dokumenty slouží jako závazný výklad právních předpisů v oblasti územního plánování, stavebního řádu a souvisejících agend. Pomocí filtrů níže můžete vyhledávat podle oblasti, zákona, platnosti nebo data vydání.",
         body=STANOVISKA),
    dict(help="metodiky", path="metodicka-podpora/stanovisko-detail.html",
         title="Detail metodického stanoviska", section="metodicka-podpora",
         crumbs=C + [("Metodická stanoviska a výklady", "metodicka-podpora/metodicka-stanoviska.html"),
                     ("Metodické stanovisko k §85", None)],
         h1="Metodické stanovisko k §85 — společné územní a stavební řízení",
         perex="Detail stanoviska zůstává v kontextu sekce — levé submenu je stejné jako u ostatních podstránek." + cmt(38, "Chybí levé submenu a kontext sekce. Ostatní detailní stránky submenu mají."),
         body=DETAIL),
    dict(help="metodiky", path="metodicka-podpora/caste-dotazy.html",
         title="Často kladené otázky — stavební úřady", section="metodicka-podpora",
         crumbs=C + [("Často kladené otázky", None)], h1="Často kladené otázky", body=FAQ_SU),
    dict(help="metodiky", path="metodicka-podpora/caste-dotazy-dotcene-organy.html",
         title="Často kladené otázky — dotčené orgány", section="metodicka-podpora",
         crumbs=C + [("Často kladené otázky", "metodicka-podpora/caste-dotazy.html"), ("Dotčené orgány", None)],
         h1="Často kladené otázky", body=FAQ_DO),
    dict(help="metodiky", path="metodicka-podpora/caste-dotazy-uzemni-planovani.html",
         title="Často kladené otázky — úřady územního plánování", section="metodicka-podpora",
         crumbs=C + [("Často kladené otázky", "metodicka-podpora/caste-dotazy.html"), ("Úřady územního plánování", None)],
         h1="Často kladené otázky", body=FAQ_UP),
    dict(help="metodiky", path="metodicka-podpora/prechodove-obdobi.html", title="Přechodové období",
         section="metodicka-podpora", crumbs=C + [("Přechodové období", None)],
         h1="Přechodové období",
         perex="Co platí pro řízení zahájená před účinností novely, jak probíhá delimitace a co se mění pro dotčené orgány.",
         body=PRECHOD),
    dict(help="metodiky", path="metodicka-podpora/standardizace.html",
         title="Standardizace územního plánování", section="metodicka-podpora",
         crumbs=C + [("Standardizace územního plánování", None)],
         h1="Standardizace územního plánování",
         perex="Standardizační dokumenty pro zpracování územně plánovací dokumentace — metodické pokyny, vzorové struktury, databáze a grafické styly. Obsah je rozdělen podle platné legislativy.",
         body=STANDARDIZACE),
    dict(help="metodiky", path="metodicka-podpora/konzultacni-stredisko.html", title="Konzultační středisko",
         section="metodicka-podpora", crumbs=C + [("Konzultační středisko", None)],
         h1="Konzultační středisko",
         perex="Konzultační středisko poskytuje konzultační a metodickou pomoc orgánům veřejné správy při plnění úkolů ze stavebního zákona na úseku územního plánování. Dotazy zasílejte e-mailem — středisko na ně reaguje formou písemných odborných názorů.",
         body=KONZULTACNI),
    dict(help="metodiky", path="metodicka-podpora/tisic-otazek.html",
         title="Tisíc otázek ke stavebnímu právu", section="metodicka-podpora",
         crumbs=C + [("Tisíc otázek ke stavebnímu právu", None)],
         h1="Tisíc otázek ke stavebnímu právu", body=TISIC),
    dict(help="metodiky", path="metodicka-podpora/tisic-otazek-seznam.html",
         title="Tisíc otázek — seznam hesel", section="metodicka-podpora",
         crumbs=C + [("Tisíc otázek", "metodicka-podpora/tisic-otazek.html"), ("Seznam hesel", None)],
         h1="1000 otázek ke stavebnímu právu k zákonu č. 283/2021 Sb.", body=TISIC_SEZNAM),
    dict(help="metodiky", path="metodicka-podpora/tisic-otazek-heslo.html", title="Tisíc otázek — heslo",
         section="metodicka-podpora",
         crumbs=C + [("Tisíc otázek", "metodicka-podpora/tisic-otazek.html"),
                     ("Seznam hesel", "metodicka-podpora/tisic-otazek-seznam.html"), ("Adresář", None)],
         h1="Heslo: Adresář",
         perex="1000 otázek ke stavebnímu právu k zákonu č. 283/2021 Sb.", body=TISIC_HESLO),
    dict(help="metodiky", path="metodicka-podpora/kontakty-na-metodiky.html", title="Kontakty na metodiky",
         section="metodicka-podpora", crumbs=C + [("Kontakty na metodiky", None)],
         h1="Kontakty na metodiky",
         perex="Kontakt na věcně příslušného metodika, ne na obecnou schránku úřadu.",
         body=KONTAKTY_METODIKY),
    dict(help="metodiky", path="metodicka-podpora/dotcene-organy.html", title="Přehled dotčených orgánů",
         section="metodicka-podpora", crumbs=C + [("Přehled dotčených orgánů", None)],
         h1="Přehled dotčených orgánů", body=DOTCENE),
]
