# -*- coding: utf-8 -*-
"""Sekce Metodická podpora."""
from build import cmt
import content_mp_extra as M

C = [("Metodická podpora", "metodicka-podpora/index.html")]

ROZCESTNIK = """
<div class="grid g3">
  <a class="card" href="{{r}}metodicka-podpora/metodicka-stanoviska.html"><h3>Metodická stanoviska a výklady</h3>
    <p>Prohledávatelná databáze stanovisek s filtrem oblasti, zákona, platnosti a aktuálnosti.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/caste-dotazy.html"><h3>Časté dotazy</h3>
    <p>Srozumitelné výklady aktuální situace pro stavební úřady, dotčené orgány a úřady územního plánování.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/prechodove-obdobi.html"><h3>Přechodové období</h3>
    <p>Rozpracovaná řízení, delimitace agendy a vzory nových dokumentů.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/standardizace.html"><h3>Standardizace územního plánování</h3>
    <p>Jednotný standard územně plánovací dokumentace před a po změně právní úpravy.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/konzultacni-stredisko.html"><h3>Konzultační středisko</h3>
    <p>Metodické vedení úřadů územního plánování ze zákona.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/tisic-otazek.html"><h3>Tisíc otázek ke stavebnímu právu</h3>
    <p>Editovatelná databáze otázek a odpovědí s fulltextovým vyhledáváním.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/dotcene-organy.html"><h3>Přehled dotčených orgánů</h3>
    <p>Kdo vydává jaké vyjádření a v jaké fázi řízení. Aktualizace dvakrát ročně.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/kontakty-na-metodiky.html"><h3>Kontakty na metodiky""" + cmt(31, "Doplnit dlaždici Kontakty na metodiky — kontaktní karty podle oblasti jsou v IA, v návrhu jen jako CTA v patičce stránek.") + """</h3>
    <p>Kontaktní karty metodiků podle věcné oblasti — ne obecná schránka úřadu.</p></a>
</div>
"""

STANOVISKA = """
<div class="filters" data-filterable>
  <div class="searchrow"><input type="search" data-q placeholder="Hledat ve stanoviscích — název, anotace i obsah PDF…"></div>
  <div class="row">
    <div class="field"><label for="f-oblast">Oblast</label>
      <select id="f-oblast" data-key="oblast"><option value="">Vše</option>
        <option value="up">Územní plánování</option><option value="sr">Stavební řád</option></select></div>
    <div class="field"><label for="f-zakon">Zákon</label>
      <select id="f-zakon" data-key="zakon"><option value="">Vše</option>
        <option value="283">283/2021 Sb.</option><option value="183">183/2006 Sb.</option></select></div>
    <div class="field"><label for="f-platnost">Platnost</label>
      <select id="f-platnost" data-key="platnost"><option value="">Vše</option>
        <option value="platna">Platná</option><option value="neplatna">Neplatná</option></select></div>
    <div class="field"><label for="f-aktualnost">Aktuálnost</label>
      <select id="f-aktualnost" data-key="aktualnost"><option value="">Vše</option>
        <option value="aktualni">Aktuální</option><option value="nahrazena">Nahrazená</option>
        <option value="historicka">Historická</option></select></div>
    <div class="field"><label for="f-rok">Rok vydání</label>
      <select id="f-rok" data-key="rok"><option value="">Vše</option>
        <option value="2026">2026</option><option value="2025">2025</option><option value="2023">2023</option></select></div>
    <div class="field"><label>&nbsp;</label><button class="btn ghost sm" type="button" data-reset>Zrušit filtry</button></div>
  </div>
  <div class="chips" data-chips></div>
  <p class="hint">Platnost je právní status dokumentu, aktuálnost říká, zda dokument nebyl nahrazen novějším.
  Jsou to dvě nezávislá metadata a u každého dokumentu se evidují zvlášť.""" + cmt(34, "Filtry Platnost a Aktuálnost jsou dvě samostatné osy — dvě povinná metadata u každého dokumentu. Potvrdit s redakcí.") + """
  Vyhledávání prochází i obsah připojených PDF.""" + cmt(98, "Chybí indikace, že se prohledává i obsah příloh (PDF).") + """</p>
</div>

<div class="resultbar">
  <span>Nalezeno <strong data-count>0</strong> stanovisek</span>
  <span class="right">
    <label>Řadit podle
      <select data-sort><option value="rel">relevance</option><option value="date">data vydání</option></select></label>""" + cmt(36, "Chybí řazení výsledků (relevance / datum) a volba počtu položek na stránku.") + """
    <label>Na stránku
      <select data-per><option>10</option><option>20</option><option>50</option></select></label>
  </span>
</div>

<ul class="doclist" data-list>
  <li data-oblast="sr" data-zakon="283" data-platnost="platna" data-aktualnost="aktualni" data-rok="2026" data-date="2026-07-10">
    <div class="tags"><span class="tag valid">Platná</span><span class="tag neutral">Aktuální</span><span class="tag hist">Stavební řád</span></div>
    <h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko ke změnám v povolovacích procesech</a></h3>
    <p>Výklad dopadů novely na průběh řízení o povolení záměru a na postavení dotčených orgánů.</p>
    <div class="meta"><span>Vydáno 10. 7. 2026</span><span>283/2021 Sb.</span><span>PDF, 412 kB</span></div></li>

  <li data-oblast="sr" data-zakon="283" data-platnost="platna" data-aktualnost="nahrazena" data-rok="2025" data-date="2025-03-02">
    <div class="tags"><span class="tag valid">Platná</span><span class="tag superseded">Nahrazená</span><span class="tag hist">Stavební řád</span></div>
    <h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k postupu při vadách žádosti</a></h3>
    <p>Postup úřadu při výzvě k doplnění a běh lhůt.</p>
    <div class="supersede">Nahrazeno novějším dokumentem: <a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko ke změnám v povolovacích procesech (2026)</a>""" + cmt(37, "Ve výpisu není navržený stav „nahrazeno novějším dokumentem\".") + """</div>
    <div class="meta"><span>Vydáno 2. 3. 2025</span><span>283/2021 Sb.</span><span>PDF, 288 kB</span></div></li>

  <li data-oblast="up" data-zakon="283" data-platnost="platna" data-aktualnost="aktualni" data-rok="2026" data-date="2026-05-20">
    <div class="tags"><span class="tag valid">Platná</span><span class="tag neutral">Aktuální</span><span class="tag hist">Územní plánování</span></div>
    <h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Metodické stanovisko k pořizování územních plánů obcí</a></h3>
    <p>Postup pořizovatele a role určeného zastupitele.</p>
    <div class="meta"><span>Vydáno 20. 5. 2026</span><span>283/2021 Sb.</span><span>PDF, 356 kB</span></div></li>

  <li data-oblast="up" data-zakon="183" data-platnost="neplatna" data-aktualnost="historicka" data-rok="2023" data-date="2023-11-08">
    <div class="tags"><span class="tag invalid">Neplatná</span><span class="tag hist">Historická</span><span class="tag hist">Územní plánování</span></div>
    <h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Stanovisko k obsahu zadání územního plánu podle zák. 183/2006 Sb.</a></h3>
    <p>Ponecháno kvůli kontinuitě a probíhajícím soudním sporům.</p>
    <div class="meta"><span>Vydáno 8. 11. 2023</span><span>183/2006 Sb.</span><span>PDF, 240 kB</span></div></li>

  <li data-oblast="sr" data-zakon="183" data-platnost="neplatna" data-aktualnost="historicka" data-rok="2023" data-date="2023-04-14">
    <div class="tags"><span class="tag invalid">Neplatná</span><span class="tag hist">Historická</span><span class="tag hist">Stavební řád</span></div>
    <h3><a href="{{r}}metodicka-podpora/stanovisko-detail.html">Stanovisko ke společnému územnímu a stavebnímu řízení</a></h3>
    <p>Historický výklad k postupu podle předchozí právní úpravy.</p>
    <div class="meta"><span>Vydáno 14. 4. 2023</span><span>183/2006 Sb.</span><span>PDF, 300 kB</span></div></li>
</ul>
<div class="empty" data-empty style="display:none">Zadanému filtru neodpovídá žádné stanovisko. Zkuste zrušit filtr platnosti nebo aktuálnosti.</div>
"""

DETAIL = """
<div class="tags" style="display:flex;gap:8px;margin-bottom:12px">
  <span class="tag valid">Platná</span><span class="tag neutral">Aktuální</span><span class="tag hist">Stavební řád</span>
</div>
<table class="t">
  <tr><th style="width:220px">Číslo jednací</th><td>ÚRÚ-0000/2026</td></tr>
  <tr><th>Oblast</th><td>Stavební řád</td></tr>
  <tr><th>Zákon</th><td>283/2021 Sb.</td></tr>
  <tr><th>Datum vydání</th><td>10. 7. 2026</td></tr>
  <tr><th>Platnost</th><td>Platná</td></tr>
  <tr><th>Aktuálnost</th><td>Aktuální — nebylo nahrazeno novějším dokumentem</td></tr>
</table>

<h2>Anotace</h2>
<p>Stanovisko vykládá dopady novely stavebního zákona na průběh řízení o povolení záměru,
zejména na postavení dotčených orgánů a na koordinaci jejich vyjádření.</p>

<ul class="files"><li><span class="ft">PDF</span>
  <span class="grow"><span class="name">Úplné znění stanoviska</span><br>
  <span class="fmeta">verze 1.0 · 412 kB · fulltextově indexováno</span></span>
  <a class="btn ghost sm" href="#">Stáhnout</a></li></ul>

<h2>Související dokumenty""" + cmt(39, "„Související dokumenty\" nemá označení typu vztahu (nahrazuje / je nahrazeno / navazuje).") + """</h2>
<table class="t">
  <tr><th style="width:180px">Vztah</th><th>Dokument</th></tr>
  <tr><td><span class="tag superseded">Nahrazuje</span></td>
      <td><a href="#">Metodické stanovisko k postupu při vadách žádosti (2025)</a></td></tr>
  <tr><td><span class="tag neutral">Navazuje na</span></td>
      <td><a href="#">Metodické stanovisko k integraci dotčených orgánů (2026)</a></td></tr>
  <tr><td><span class="tag hist">Souvisí s</span></td>
      <td><a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a></td></tr>
</table>

<h2>Historie verzí""" + cmt(40, "Chybí historie verzí dokumentu.") + """</h2>
<table class="t">
  <tr><th style="width:140px">Verze</th><th>Datum</th><th>Změna</th></tr>
  <tr><td>1.0</td><td>10. 7. 2026</td><td>První vydání</td></tr>
  <tr><td>0.9</td><td>2. 6. 2026</td><td>Pracovní znění k připomínkám</td></tr>
</table>
"""

FAQ_TABS = """
<div class="tabs">
  <a href="{{r}}metodicka-podpora/caste-dotazy.html"@A1@>Stavební úřady</a>
  <a href="{{r}}metodicka-podpora/caste-dotazy-dotcene-organy.html"@A2@>Dotčené orgány</a>
  <a href="{{r}}metodicka-podpora/caste-dotazy-uzemni-planovani.html"@A3@>Úřady územního plánování""" + cmt(41, "Doplnit třetí záložku pro úřady územního plánování — persony ji označují jako opomíjenou podskupinu.") + """</a>
</div>
<div class="filters" style="margin-top:20px">
  <div class="searchrow"><input type="search" placeholder="Hledat v otázkách…"
    oninput="var q=this.value.toLowerCase();document.querySelectorAll('[data-faq]').forEach(function(d){d.style.display=d.textContent.toLowerCase().indexOf(q)>-1?'':'none'})"></div>
  <p class="hint" style="margin:0">Vyhledávání prochází znění otázek i odpovědí.""" + cmt(43, "Chybí vyhledávání v otázkách.") + """</p>
</div>
"""


def faq(active, items):
    a = ["", "", ""]
    a[active] = ' aria-current="page"'
    out = FAQ_TABS
    for i in (1, 2, 3):
        out = out.replace('@A%d@' % i, a[i - 1])
    for q, ans in items:
        out += f'<details class="acc" data-faq><summary>{q}</summary><div class="body"><p>{ans}</p></div></details>'
    return out


FAQ_SU = faq(0, M.FAQ_SU_EXTRA + [
    ("Kde najdu metodické stanovisko k paragrafu nového stavebního zákona?",
     'V databázi <a href="{{r}}metodicka-podpora/metodicka-stanoviska.html">Metodická stanoviska a výklady</a> s filtrem podle oblasti a zákona.'),
    ("Jak poznám, že stanovisko, které mám, je stále aktuální?",
     "U každého dokumentu je uvedena platnost i aktuálnost. Nahrazené dokumenty mají ve výpisu odkaz na novější."),
    ("Co se stane s řízeními, která jsem zahájil před účinností novely?",
     'Viz <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a>.'),
    ("Na koho se obrátit s výkladovým dotazem?",
     'Na metodika podle věcné oblasti — viz <a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">Kontakty na metodiky</a>.'),
])

FAQ_DO = faq(1, M.FAQ_DO_EXTRA + [
    ("Co se mění v dokumentech, které vydávám?",
     "Mění se typ vydávaného dokumentu a způsob jeho zapojení do řízení vedeného ÚRÚ."),
    ("Komu vyjádření zasílám?",
     "Vyjádření se zasílá ÚRÚ jako vedoucímu řízení, nikoliv stavebníkovi."),
    ("Kde najdu vzory nových dokumentů?",
     'Ve stránce <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a>.'),
    ("Na koho se obrátit, když si nejsem jistý postupem?",
     'Na metodika podle oblasti — viz <a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">Kontakty na metodiky</a>.'),
])

FAQ_UP = faq(2, [
    ("Kdo je nyní mým metodickým garantem pro územní plánování?",
     'Metodici územního plánování přešli z MMR na ÚRÚ. Kontakt najdete v <a href="{{r}}metodicka-podpora/kontakty-na-metodiky.html">Kontaktech na metodiky</a>.'),
    ("Kde najdu metodiky vztahující se jen k územnímu plánování?",
     'V databázi stanovisek použijte filtr Oblast = Územní plánování.'),
    ("Co platí pro pořizování územního plánu zahájené dříve?",
     'Viz <a href="{{r}}metodicka-podpora/prechodove-obdobi.html">Přechodové období</a>.'),
    ("Kde najdu jednotný standard územně plánovací dokumentace?",
     'Na stránce <a href="{{r}}metodicka-podpora/standardizace.html">Standardizace územního plánování</a>.'),
])

PRECHOD = """
<div class="box change">
  <h3>Protějšek pro stavebníky</h3>
  <p>Tato stránka popisuje dopady pro úřady a dotčené orgány. Stejné téma z pohledu stavebníků najdete na stránce
  <a href="{{r}}vyhrazene-stavby/co-meni-novela.html">Co změní novela SZ</a>. Obě stránky používají stejný vzor a vzájemně se odkazují.""" + cmt(44, "Tato stránka je protějškem nové stránky „Co změní novela SZ\" pro druhé publikum. Provázat a sjednotit vzor.") + """</p>
</div>

<h2>Rozpracovaná řízení</h2>
<p>Řízení zahájená přede dnem účinnosti novely se dokončují podle dosavadních pravidel, není-li v přechodných
ustanoveních stanoveno jinak.</p>

<h2 id="delimitace">Delimitace — řízení přecházející z obecných stavebních úřadů""" + cmt(45, "Chybí část k delimitaci: co se stane s řízeními, která dnes vede obecný stavební úřad a nově spadnou pod ÚRÚ.") + """</h2>
<p>Novela rozšiřuje okruh vyhrazených staveb. Část řízení, která dnes vedou obecné stavební úřady, tím přechází na ÚRÚ.
Tato situace se řídí jinými pravidly než běžné přechodné ustanovení.</p>
<table class="t">
  <tr><th style="width:34%">Situace</th><th>Kdo řízení dokončí</th><th>Co udělat</th></tr>
  <tr><td>Řízení zahájené u obecného SÚ, stavba nově vyhrazená</td><td>ÚRÚ po předání spisu</td><td>Úřad předá spis, účastníky vyrozumí ÚRÚ</td></tr>
  <tr><td>Řízení pravomocně skončené</td><td>—</td><td>Rozhodnutí zůstává v platnosti</td></tr>
  <tr><td>Záměr dosud nepodaný</td><td>ÚRÚ</td><td>Podat rovnou u ÚRÚ</td></tr>
</table>

""" + M.PRECHOD_DETAIL + """

<h2>Změny pro dotčené orgány</h2>
<p>Mění se typ vydávaného dokumentu a způsob jeho zapojení do řízení. Podrobnosti najdete v
<a href="{{r}}metodicka-podpora/caste-dotazy-dotcene-organy.html">Častých dotazech pro dotčené orgány</a>.</p>

<h2>Vzory nových dokumentů</h2>
<p>Vzory a formuláře jsou spravovány na jednom místě v sekci
<a href="{{r}}vyhrazene-stavby/dokumenty-a-formulare.html">Dokumenty a formuláře</a>.""" + cmt(46, "„Vzory dokumentů ke stažení\" duplikují Dokumenty a formuláře. Určit jedno místo správy.") + """</p>
"""

STANDARDIZACE = """
<div class="tabs">
  <a href="{{r}}metodicka-podpora/standardizace.html" aria-current="page">Nová právní úprava</a>
  <a href="{{r}}metodicka-podpora/standardizace.html#stara">Předchozí právní úprava</a>
</div>
""" + M.STANDARDIZACE_DETAIL + """
<ul class="files">
  <li><span class="ft">PDF</span><span class="grow"><span class="name">Jednotný standard — metodika</span><br>
    <span class="fmeta">verze 2.0 · platné od 1. 7. 2024</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
  <li><span class="ft">ZIP</span><span class="grow"><span class="name">Datový model a vzorové soubory</span><br>
    <span class="fmeta">verze 2.0 · platné od 1. 7. 2024</span></span><a class="btn ghost sm" href="#">Stáhnout</a></li>
</ul>
<h2 id="stara">Předchozí právní úprava</h2>
<p>Materiály k dokumentaci pořizované podle dřívější právní úpravy zůstávají dostupné kvůli kontinuitě a probíhajícím řízením.</p>
"""

KONZULTACNI = """
""" + M.KONZULTACNI_DETAIL + """
<h2>Položit dotaz""" + cmt(50, "Chybí strukturovaný formulář dotazu. Stránka sama vyjmenovává, co musí dotaz obsahovat.") + """</h2>
<div class="filters">
  <div class="row">
    <div class="field" style="min-width:260px"><label for="k1">Úřad</label><input id="k1" placeholder="Název úřadu"></div>
    <div class="field" style="min-width:260px"><label for="k2">Kontaktní osoba a e-mail</label><input id="k2" placeholder="Jméno, e-mail"></div>
    <div class="field" style="min-width:220px"><label for="k3">Oblast dotazu</label>
      <select id="k3"><option>Územní plánování</option><option>Stavební řád</option><option>Standardizace</option></select></div>
  </div>
  <div class="row" style="margin-top:14px">
    <div class="field" style="flex:1;min-width:100%"><label for="k4">Popis situace, dotčené ustanovení a dosavadní postup</label>
      <textarea id="k4" rows="5" style="font:inherit;padding:10px;border:1px solid #D8DEE5;border-radius:6px"></textarea></div>
  </div>
  <div class="btn-row"><button class="btn" type="button">Odeslat dotaz</button></div>
  <p class="hint">Formulář se odesílá do spisové služby úřadu a je mu přiděleno číslo jednací.</p>
</div>
"""

TISIC = M.TISIC_ROZCESTNIK

TISIC_SEZNAM = """
<div class="filters">
  <div class="searchrow">
    <input type="search" id="tq" placeholder="Hledat…"
      oninput="var q=this.value.toLowerCase();document.querySelectorAll('[data-h]').forEach(function(d){d.style.display=d.textContent.toLowerCase().indexOf(q)>-1?'':'none'})">
    <select id="tscope" style="font:inherit;padding:9px;border:1px solid #D8DEE5;border-radius:6px">
      <option>Hledat v názvech hesel</option>
      <option>Hledat v hesle i v odpovědích</option>
    </select>
  </div>
  <p class="hint" style="margin:0">Přepínač určuje, zda se hledá jen v názvu hesla, nebo i v textu odpovědí.""" + cmt(53, "Není zřejmé, zda vyhledávací pole hledá v názvech hesel, nebo i v textu odpovědí.") + """</p>
</div>
<ul class="doclist" style="margin-top:16px">""" + "".join(
  f'<li data-h><h3><a href="{{{{r}}}}metodicka-podpora/tisic-otazek-heslo.html">{t}</a></h3>'
  f'<p>{n} otázek</p></li>' for t, n in M.HESLA) + """</ul>
"""

TISIC_HESLO = """
<p class="updated">Heslo aktualizováno 3. 6. 2026 · 28 otázek</p>
<details class="acc" open id="q-1024"><summary>Kdo je dotčeným orgánem v řízení o povolení vyhrazené stavby?</summary>
  <div class="body"><p>Dotčenými orgány jsou správní orgány chránící veřejné zájmy podle zvláštních právních předpisů.</p>
  <p class="source">Zdroj: metodické stanovisko ÚRÚ · <a href="#q-1024">trvalý odkaz na otázku</a>
  <button class="btn ghost sm" type="button" onclick="navigator.clipboard&&navigator.clipboard.writeText(location.origin+location.pathname+'#q-1024');this.textContent='Zkopírováno'">Kopírovat odkaz</button>""" + cmt(54, "Chybí trvalý odkaz na jednotlivou otázku — odpovědi se používají v korespondenci.") + """</p></div></details>
<details class="acc" id="q-1025"><summary>Jak se vyjádření dotčeného orgánu zapojuje do řízení?</summary>
  <div class="body"><p>Vyjádření si vyžádá úřad vedoucí řízení a koordinuje je v rámci jednoho řízení.</p>
  <p class="source"><a href="#q-1025">trvalý odkaz na otázku</a></p></div></details>
<details class="acc" id="q-1026"><summary>Co dělat, když se vyjádření dotčených orgánů rozcházejí?</summary>
  <div class="body"><p>Rozpor se řeší postupem podle správního řádu.</p>
  <p class="source"><a href="#q-1026">trvalý odkaz na otázku</a></p></div></details>
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
  <div class="contactcard"><h3>Metodika — standardizace</h3><p class="role">Oddělení standardizace</p>
    <p class="agenda">Jednotný standard, datový model, výměnné formáty</p>
    <dl><dt>E-mail</dt><dd>standard@uru.gov.cz</dd><dt>Telefon</dt><dd>+420 000 000 000</dd></dl></div>
  <div class="contactcard"><h3>Konzultační středisko</h3><p class="role">Metodické vedení úřadů územního plánování</p>
    <p class="agenda">Dotazy úřadů územního plánování ze zákona</p>
    <dl><dt>Formulář</dt><dd><a href="{{r}}metodicka-podpora/konzultacni-stredisko.html">Položit dotaz</a></dd></dl></div>
</div>
"""

DOTCENE = """
<div class="box gap">
  <h3>Přesunuto z Územního rozvoje</h3>
  <p>Přehled dotčených orgánů je primárně informace pro stavební úřady a orgány územního plánování,
  proto je zařazen do Metodické podpory. Ze sekce Územní rozvoj sem vede křížový odkaz, protože uživatelé
  ÚÚR jsou zvyklí hledat obsah tam.""" + cmt(61, "Chybí Přehled dotčených orgánů. I po přesunu do Metodické podpory doplnit křížový odkaz z Územního plánování.") + """</p>
</div>
<p class="updated">Přehled se aktualizuje dvakrát ročně. Poslední aktualizace 30. 6. 2026.</p>
<table class="t">
  <tr><th>Chráněný veřejný zájem</th><th>Dotčený orgán</th><th>Typ dokumentu</th></tr>
  <tr><td>Ochrana veřejného zdraví</td><td>Krajská hygienická stanice</td><td>vyjádření</td></tr>
  <tr><td>Požární ochrana</td><td>Hasičský záchranný sbor kraje</td><td>vyjádření</td></tr>
  <tr><td>Ochrana přírody a krajiny</td><td>Orgán ochrany přírody</td><td>vyjádření</td></tr>
  <tr><td>Vodní hospodářství</td><td>Vodoprávní úřad</td><td>vyjádření</td></tr>
  <tr><td>Památková péče</td><td>Orgán státní památkové péče</td><td>vyjádření</td></tr>
</table>
"""

PAGES = [
    dict(path="metodicka-podpora/index.html", title="Metodická podpora", section="metodicka-podpora",
         crumbs=[("Metodická podpora", None)], sidebar=False, h1="Metodická podpora",
         perex="Metodická stanoviska, výklady a praktické návody pro stavební úřady, dotčené orgány a úřady územního plánování.",
         body=ROZCESTNIK),
    dict(help="metodiky", path="metodicka-podpora/metodicka-stanoviska.html", title="Metodická stanoviska a výklady",
         section="metodicka-podpora", crumbs=C + [("Metodická stanoviska a výklady", None)],
         h1="Metodická stanoviska a výklady",
         perex="Autoritativní výklady, na které se lze v řízení odvolat. Databáze zahrnuje i historické dokumenty.",
         body=STANOVISKA),
    dict(help="metodiky", path="metodicka-podpora/stanovisko-detail.html", title="Detail metodického stanoviska",
         section="metodicka-podpora",
         crumbs=C + [("Metodická stanoviska a výklady", "metodicka-podpora/metodicka-stanoviska.html"), ("Detail stanoviska", None)],
         h1="Metodické stanovisko ke změnám v povolovacích procesech",
         perex="Detail stanoviska zůstává v kontextu sekce — levé submenu je stejné jako u ostatních podstránek." + cmt(38, "Chybí levé submenu a kontext sekce. Ostatní detailní stránky submenu mají."),
         body=DETAIL),
    dict(help="metodiky", path="metodicka-podpora/caste-dotazy.html", title="Časté dotazy — stavební úřady",
         section="metodicka-podpora", crumbs=C + [("Časté dotazy", None)], h1="Časté dotazy", body=FAQ_SU),
    dict(help="metodiky", path="metodicka-podpora/caste-dotazy-dotcene-organy.html", title="Časté dotazy — dotčené orgány",
         section="metodicka-podpora", crumbs=C + [("Časté dotazy", "metodicka-podpora/caste-dotazy.html"), ("Dotčené orgány", None)],
         h1="Časté dotazy", body=FAQ_DO),
    dict(help="metodiky", path="metodicka-podpora/caste-dotazy-uzemni-planovani.html", title="Časté dotazy — úřady územního plánování",
         section="metodicka-podpora", crumbs=C + [("Časté dotazy", "metodicka-podpora/caste-dotazy.html"), ("Úřady územního plánování", None)],
         h1="Časté dotazy", body=FAQ_UP),
    dict(help="metodiky", path="metodicka-podpora/prechodove-obdobi.html", title="Přechodové období", section="metodicka-podpora",
         crumbs=C + [("Přechodové období", None)], h1="Přechodové období",
         perex="Co se děje s rozpracovanými řízeními, jak probíhá delimitace a co se mění pro dotčené orgány.",
         body=PRECHOD),
    dict(help="metodiky", path="metodicka-podpora/standardizace.html", title="Standardizace územního plánování",
         section="metodicka-podpora", crumbs=C + [("Standardizace územního plánování", None)],
         h1="Standardizace územního plánování", body=STANDARDIZACE),
    dict(help="metodiky", path="metodicka-podpora/konzultacni-stredisko.html", title="Konzultační středisko",
         section="metodicka-podpora", crumbs=C + [("Konzultační středisko", None)],
         h1="Konzultační středisko",
         perex="Metodické vedení úřadů územního plánování ze zákona.", body=KONZULTACNI),
    dict(help="metodiky", path="metodicka-podpora/tisic-otazek.html", title="Tisíc otázek ke stavebnímu právu",
         section="metodicka-podpora", crumbs=C + [("Tisíc otázek ke stavebnímu právu", None)],
         h1="Tisíc otázek ke stavebnímu právu", body=TISIC),
    dict(help="metodiky", path="metodicka-podpora/tisic-otazek-seznam.html", title="Tisíc otázek — seznam hesel",
         section="metodicka-podpora",
         crumbs=C + [("Tisíc otázek", "metodicka-podpora/tisic-otazek.html"), ("Seznam hesel", None)],
         h1="Seznam hesel", body=TISIC_SEZNAM),
    dict(help="metodiky", path="metodicka-podpora/tisic-otazek-heslo.html", title="Tisíc otázek — heslo",
         section="metodicka-podpora",
         crumbs=C + [("Tisíc otázek", "metodicka-podpora/tisic-otazek.html"),
                     ("Seznam hesel", "metodicka-podpora/tisic-otazek-seznam.html"), ("Dotčené orgány", None)],
         h1="Dotčené orgány", body=TISIC_HESLO),
    dict(path="metodicka-podpora/kontakty-na-metodiky.html", title="Kontakty na metodiky",
         section="metodicka-podpora", crumbs=C + [("Kontakty na metodiky", None)],
         h1="Kontakty na metodiky",
         perex="Kontakt na věcně příslušného metodika, ne na obecnou schránku úřadu.", body=KONTAKTY_METODIKY),
    dict(path="metodicka-podpora/dotcene-organy.html", title="Přehled dotčených orgánů",
         section="metodicka-podpora", crumbs=C + [("Přehled dotčených orgánů", None)],
         h1="Přehled dotčených orgánů", body=DOTCENE),
]
