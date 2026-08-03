# -*- coding: utf-8 -*-
"""Šablona článku podle návrhu (DESU_design.pdf, str. 42).

Návrh je obecná šablona s výplňovým textem. Maketa přebírá její stavbu — hlavičku
s metadaty a štítky, perex, hero fotografii, dvousloupcové rozvržení s bočním
obsahem článku, citační blok, obrázek s popiskem, číslované kroky, akordeon
a galerii — a naplňuje ji českým pracovním textem.
"""

TELO = """
<h2 id="c1">Co se mění</h2>
<p>Text článku je pracovní a nahradí se finálním zněním. Šablona se používá pro
aktuality, tiskové zprávy i obecné textové stránky. Odstavec je zde v základní
podobě, bez zvýraznění.</p>
<p>Druhý odstavec ukazuje, jak vypadá delší souvislý text. Řádkování a šířka
sloupce vycházejí z návrhu, aby byl text čitelný i při delších pasážích.</p>

<h3 id="c1a">Podnadpis třetí úrovně</h3>
<p>Text pod podnadpisem. Struktura nadpisů je součástí šablony, aby redakce viděla,
jak se článek člení a jak se to promítá do bočního obsahu vpravo.</p>

<blockquote class="quote">
  <p>Citace ve vlastním bloku. Používá se pro vyjádření vedení úřadu nebo pro
  zvýraznění klíčové věty z dokumentu.</p>
  <footer><span class="avatar" aria-hidden="true"></span>Jméno Příjmení, funkce</footer>
</blockquote>

<p>Text navazující na citaci. Blok citace text nepřerušuje, jen jej opticky odděluje.</p>

<h2 id="c2">Podrobnosti</h2>
<p>Další oddíl článku. Nadpisy druhé úrovně tvoří hlavní kostru a v bočním obsahu
se zobrazují bez odsazení.</p>

<h3 id="c2a">Číslovaný seznam</h3>
<ol>
  <li>První položka seznamu</li>
  <li>Druhá položka seznamu</li>
  <li>Třetí položka seznamu</li>
  <li>Čtvrtá položka seznamu</li>
  <li>Pátá položka seznamu</li>
</ol>

<h2 id="c3">Obrazová příloha</h2>
<p>Obrázek uvnitř článku má popisek a zabírá celou šířku hlavního sloupce.</p>
<figure class="article-figure">
  <img src="{{r}}assets/img/aktualita-vyberova-rizeni.jpg" alt="" loading="lazy">
  <figcaption>Popisek obrázku. Uvádí se pod obrázkem menším písmem.</figcaption>
</figure>

<h2 id="c4">Postup krok za krokem</h2>
<ol class="steps">
  <li><h3>Krok návodu</h3><p>Popis prvního kroku.</p></li>
  <li><h3>Krok návodu</h3><p>Popis druhého kroku.</p></li>
  <li><h3>Krok návodu</h3><p>Popis třetího kroku.</p></li>
  <li><h3>Krok návodu</h3><p>Popis čtvrtého kroku.</p></li>
  <li><h3>Krok návodu</h3><p>Popis pátého kroku.</p></li>
</ol>

<h3 id="c4a">Rozbalovací otázky</h3>
<details class="acc"><summary>Nadpis rozbalovací části</summary>
  <div class="body"><p>Obsah rozbalovací části. Používá se pro doplňující informace,
  které nemusí být vidět hned.</p></div></details>
<details class="acc"><summary>Nadpis rozbalovací části</summary>
  <div class="body"><p>Obsah rozbalovací části.</p></div></details>
<details class="acc"><summary>Nadpis rozbalovací části</summary>
  <div class="body"><p>Obsah rozbalovací části.</p></div></details>

<h2 id="c5">Galerie</h2>
<p>Poslední oddíl článku uzavírá galerie s náhledy.</p>
<div class="gallery">
  <img src="{{r}}assets/img/aktualita-metodiky.jpg" alt="" loading="lazy">
  <img src="{{r}}assets/img/sidlo-uradu.jpeg" alt="" loading="lazy">
  <img src="{{r}}assets/img/aktualita-vyberova-rizeni.jpg" alt="" loading="lazy">
  <a class="gallery-more" href="#">59 dalších</a>
</div>

<h2>Přílohy</h2>
<ul class="files"><li><span class="ft">PDF</span>
  <span class="grow"><span class="name">Příloha k článku</span>
  <span class="fmeta">PDF, 296 kB</span></span></li></ul>
"""

TOC = """
<nav class="article-toc" aria-label="Obsah článku">
  <h2>Obsah článku</h2>
  <ul class="gov-list--plain">
    <li><a href="#c1">Co se mění</a></li>
    <li class="lvl3"><a href="#c1a">Podnadpis třetí úrovně</a></li>
    <li><a href="#c2">Podrobnosti</a></li>
    <li class="lvl3"><a href="#c2a">Číslovaný seznam</a></li>
    <li><a href="#c3">Obrazová příloha</a></li>
    <li><a href="#c4">Postup krok za krokem</a></li>
    <li class="lvl3"><a href="#c4a">Rozbalovací otázky</a></li>
    <li><a href="#c5">Galerie</a></li>
  </ul>
</nav>
"""
