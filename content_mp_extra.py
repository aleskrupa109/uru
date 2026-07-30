# -*- coding: utf-8 -*-
"""Doplnění obsahu sekce Metodická podpora podle návrhu (DESU_design.pdf, str. 16–24)."""

PRECHOD_DETAIL = """
<h2>Jak poznat datum zahájení řízení</h2>
<p>Rozhodující je datum doručení žádosti stavebnímu úřadu, nikoli datum jejího podání
ani datum vydání prvního úkonu v řízení.</p>
<div class="box edge">
  <h3>Na co dát pozor</h3>
  <ul>
    <li>Integraci dotčených orgánů podle nové úpravy nelze aplikovat zpětně na již zahájená řízení.</li>
    <li>Projektová dokumentace zpracovaná podle dosavadní úpravy zůstává použitelná.</li>
    <li>Závazná stanoviska vydaná před účinností novely zůstávají platná.</li>
  </ul>
</div>

<h2>Jak postupovat při přijetí podkladů od stavebního úřadu</h2>
<p>Podklady k řízení přicházejí prostřednictvím Portálu stavebníka, nikoli e-mailem.
Lhůta pro vydání vyjádření je 30 dnů od doručení podkladů. Dotčený orgán vydává vyjádření
samostatně v rámci koordinovaného stanoviska.</p>
"""

STANDARDIZACE_DETAIL = """
<h2>Jednotný standard územně plánovací dokumentace</h2>
<p>Standard sjednocuje strukturu, značení a datový model územně plánovací dokumentace.
Je závazný pro pořizovatele i zpracovatele.</p>

<h3>Krajská úroveň — pořizuje kraj</h3>
<p>Zásady územního rozvoje a jejich aktualizace.</p>

<h3>Obecní úroveň — pořizuje obec s rozšířenou působností</h3>
<p>Územní plány a jejich změny.</p>

<h3>Podrobná regulace využití území — pořizuje obec nebo kraj</h3>
<p>Regulační plány a územní studie.</p>

<h3>Vymezení zastavěného území</h3>
<p>Postup pro obce bez územního plánu.</p>
"""

KONZULTACNI_DETAIL = """
<p>Konzultační středisko poskytuje metodickou podporu ve věcech územního plánování
a reaguje formou písemných odborných názorů.</p>

<div class="grid g2">
  <div class="card"><h3>Komu středisko slouží</h3>
    <ul>
      <li>Krajské úřady</li>
      <li>Obecní a městské úřady</li>
      <li>Další orgány státní správy a samosprávy</li>
    </ul></div>
  <div class="card"><h3>Komu středisko neslouží</h3>
    <ul>
      <li>Fyzické a právnické osoby</li>
      <li>Stavebníci a investoři</li>
      <li>Projektanti a architekti</li>
    </ul></div>
</div>
<p>Odpovědi na obecné otázky ke stavebnímu právu najdete v databázi
<a href="{{r}}metodicka-podpora/tisic-otazek.html">Tisíc otázek ke stavebnímu právu</a>.</p>

<h2>Co dostanete</h2>
<p>Písemný odborný názor k položené otázce. ÚRÚ není ve věcech upravovaných stavebním zákonem
orgánem veřejné správy ani dotčeným orgánem — odborný názor proto není závazným výkladem
ani rozhodnutím.</p>

<h2>Co musí dotaz obsahovat</h2>
<ul>
  <li>přesně formulovanou otázku</li>
  <li>odkaz na konkrétní paragraf nebo zákon</li>
  <li>popis situace a dosavadního postupu</li>
</ul>
<div class="box note">
  <h3>Na co středisko neodpovídá</h3>
  <p>Na dotazy, jejichž zodpovězení vyžaduje znalost konkrétních podmínek, které jsou
  předmětem konkrétního správního řízení.</p>
</div>
"""

TISIC_ROZCESTNIK = """
<p>Databáze otázek a odpovědí ke stavebnímu právu. Slouží ke sjednocování postupů státní
správy. Obsah je členěný podle právní úpravy, ke které se vztahuje.</p>
<div class="grid g2">
  <a class="card" href="{{r}}metodicka-podpora/tisic-otazek-seznam.html">
    <h3>Stavební zákon platný od 1. 7. 2024</h3>
    <p>Otázky jsou zařazované tak, jak vyplývají ze zavádění nového stavebního zákona do praxe.</p></a>
  <a class="card" href="{{r}}metodicka-podpora/tisic-otazek-seznam.html">
    <h3>Stavební zákon platný do 30. 6. 2024</h3>
    <p>Odpovědi k ukončeným činnostem a k dokončení postupů podle dosavadních právních předpisů.</p></a>
</div>
"""

HESLA = [("Adresář", 2), ("Autorizace", 6), ("Bioplynové stanice", 1),
         ("České technické normy (ČSN)", 1), ("Dělení pozemků", 12), ("Dotčené orgány", 28),
         ("Kolaudace", 19), ("Odstraňování staveb", 14), ("Územní plán obce", 41)]

FAQ_SU_EXTRA = [
    ("Mám pravomocné územní rozhodnutí vydané před účinností novely — je stále platné?",
     "Ano. Pravomocná rozhodnutí zůstávají v platnosti."),
    ("Jak postupovat při změně pravomocného rozhodnutí vydaného před účinností novely?",
     "Změna se posuzuje podle pravidel platných v době vydání původního rozhodnutí, "
     "není-li v přechodných ustanoveních stanoveno jinak."),
    ("Co dělat, když dotčený orgán nevydá vyjádření ve lhůtě?",
     "Postup pro nečinnost dotčeného orgánu popisuje metodické stanovisko k integraci dotčených orgánů."),
    ("Kdo je teď metodický garant pro stavební řád místo MMR?",
     "Metodické vedení převzal ÚRÚ. Kontakt najdete v Kontaktech na metodiky."),
]

FAQ_DO_EXTRA = [
    ("Co nahrazuje závazné stanovisko od účinnosti novely?",
     "Dotčený orgán vydává vyjádření, které se zapojuje do koordinovaného stanoviska."),
    ("Co se stalo s jednotným environmentálním stanoviskem (JES)?",
     "Jednotné environmentální stanovisko se ruší; jeho obsah přechází do vyjádření dotčených orgánů."),
    ("Vydáváme vyjádření samostatně, nebo společně s ostatními dotčenými orgány?",
     "Samostatně, v rámci koordinovaného stanoviska, které sestavuje úřad vedoucí řízení."),
    ("Platí pro nás jiné lhůty než dosud?",
     "Lhůta pro vydání vyjádření je 30 dnů od doručení podkladů."),
    ("Kde najdeme podklady k řízení, ke kterým máme vydat vyjádření?",
     "Podklady přicházejí prostřednictvím Portálu stavebníka, nikoli e-mailem."),
    ("Jak postupovat, pokud je věc mimo naši věcnou příslušnost?",
     "Neprodleně to sdělte úřadu vedoucímu řízení, aby mohl vyžádat vyjádření správného orgánu."),
    ("Co dělat, když nestíháme vydat vyjádření ve lhůtě?",
     "Obraťte se na úřad vedoucí řízení; postup pro tento případ popisuje metodické stanovisko."),
    ("Kdo je teď metodický garant pro naši oblast místo MMR?",
     "Metodické vedení převzal ÚRÚ. Kontakt najdete v Kontaktech na metodiky."),
]
