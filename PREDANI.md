# Předání práce — maketa webu ÚRÚ

Tento soubor slouží k navázání v novém chatu. Popisuje, kde práce stojí, jak
probíhá a na co si dát pozor.

## Než se začne

Do nového chatu je potřeba nahrát **dva soubory**:

1. `uru-maketa.zip` — celý repozitář makety
2. `DESU_design.pdf` — návrh designu od dodavatele Cognito (48 stran)

Bez návrhu nelze nic porovnávat. Prostředí nového chatu je prázdné.

## Co maketa je

Klikatelná maketa webu Úřadu rozvoje území — 52 statických HTML stránek
generovaných Pythonem, postavená na design systému gov.cz 4.6.5. Slouží
k připomínkování návrhu od Cognita a jako podklad pro dodavatele.

Nasazená na `aleskrupa109.github.io/uru`. Aleš pracuje na macOS, klonuje přes
GitHub Desktop.

**Kontrola, že prohlížeč čte nové soubory.** V patičce je razítko
`sestaveno DD. MM. RRRR HH:MM`. Musí být stejné lokálně i na nasazeném webu.
Když se liší, není to chyba makety: v srpnu 2026 padala na GitHubu nasazení
(„pages build and deployment“ končilo po ~10 min timeoutem) a web tiše servíroval
poslední úspěšnou verzi starou několik dávek. Když nasazená stránka vypadá starě,
podívej se nejdřív do záložky Actions, jestli je poslední běh zelený.

Při přetažení souborů přes Cmd+A Finder **nevybere skryté soubory** — `.nojekyll`
a `.gitignore` se tím nepřenášejí. V repozitáři už jsou, ale kdyby někdy zmizely,
Jekyll začne zpracovávat celý vendorovaný design systém a nasazení spadne.

## Struktura repozitáře

```
build.py              generátor — layout, navigace, patička, to_ds(), ikony
pages_home.py         úvodní stránka
pages_vs.py           Vyhrazené stavby
pages_mp.py           Metodická podpora
pages_ur.py           Územní rozvoj
pages_ostatni.py      Kariéra, O úřadu, Kontakty, článek, mapa webu, ostatní
content_*.py          delší obsahové bloky vytažené z pages_*
assets/gov/           design systém (CSS, Roboto, ikony) — vendorováno
assets/uru-tokens.css přemapování primární palety na barvy ÚRÚ
assets/uru.css        projektová vrstva (hlavička, navigace, patička, layout)
assets/uru.js         navigace, filtry, režim úprav
assets/img/           fotografie a znak úřadu
tools/                porovnávací nástroje + seznam schválených odchylek
```

**Nikdy neupravovat vygenerované HTML** — `python3 build.py` přepíše všech
52 souborů. Změny patří do `pages_*.py`, `content_*.py`, `build.py` nebo CSS.

## Jak práce probíhá

Smyčka, která se osvědčila:

1. Aleš pustí `node tools/visual_diff.js --page N`
2. Pošle `_maketa.png` (návrh mám z PDF, ten posílat netřeba)
3. Já snímek porovnám s návrhem, **odchylky odměřím v PDF** a opravím
4. Pošlu balíček, Aleš rozbalí do naklonované složky a pustí znovu

**Zásada: neodhadovat, měřit.** Barvy, rozměry i rozestupy se dají z PDF
odečíst rasterizací (`pdftoppm -r 72`) a analýzou pixelů. Každá oprava, která
vznikla odhadem, se dříve nebo později ukázala jako špatná.

**Pixelové procento je hrubé vodítko, ne měřítko pokroku.** Zúžení sloupce
přelomí text jinde a číslo může i vzrůst, přestože je rozvržení nově správné.
Rozhoduje snímek.

Nástroje a jejich zvláštnosti popisuje `tools/README.md`.

## Pravidlo věrnosti

Maketa má odpovídat návrhu obsahem i vzhledem **s výjimkou** míst, kde návrh
mění zeleně schválené připomínky (Aleš roztřídil 111 připomínek barevně:
46 zelených k zapracování, 46 červených, 29 oranžových ke zvážení).

Odchylky se označují značkou `cmt(číslo, "vysvětlení")` — zelené kolečko
s číslem připomínky. Zobrazuje se jen v pracovním režimu.

Schválené odchylky jsou v `tools/odchylky.yaml` (17 položek), aby je textové
porovnání nehlásilo jako chybu.

## Stav k předání

**Hotovo je šest typů stránek** — z každého vzešly systémové opravy, které se
propsaly do celého webu:

| Typ | Vzorová stránka | Odlišnost |
|---|---|---|
| obsahová podstránka | str. 8 Portál stavebníka | 9,4 % |
| výpis s filtry | str. 12 Metodická stanoviska | 7,9 % |
| detailová stránka | str. 15 Detail stanoviska | viz níže |
| rozcestník sekce | str. 11 Metodická podpora | — |
| článek | str. 42 Šablona článku | 41,6 % |
| úvodní stránka | str. 1 | zčásti |

U detailu stanoviska pixelové porovnání neposlouzí — maketa je delší než návrh
kvůli zapracovaným připomínkám, takže se od poloviny překrývá obsah s návrhovou
patičkou.

U článku je rozdíl výšky inherentní: návrh opakuje tentýž odstavec Lorem ipsum
dvanáctkrát (6907 px proti 4877).

**Rozpracováno:** str. 4 Co spadá pod ÚRÚ (naposledy měřeno 11,4 %, od té doby
zapracovány ikony a rozestupy — potřebuje přeměřit). Ikony z Figmy dorazily
a jsou nasazené, viz níže.

**Textové pokrytí návrhu:** 73,8 % (`python3 tools/text_diff.py`). Číslo vyskončilo ze 67,5 %
poté, co porovnání umí párovat bloky podle písmen bez mezer; obsah makety se tím
nezměnil, jen se přestaly hlásit bloky rozsekané exportem z Figmy.

## Ikony z návrhu (srpen 2026)

Aleš vyexportoval z Figmy deset ikon. Devět je ke kategoriím na str. 4, desátá
je obálka bloku „Potřebujete pomoct?". Pořadí exportu odpovídalo pořadí kategorií
v návrhu; ověřeno porovnáním s rasterizovanou str. 4.

| Soubor | Kategorie |
|---|---|
| `vs-dalnice` | Dopravní stavby — dálnice |
| `vs-drahy` | Dopravní stavby — dráhy |
| `vs-letecke` | Dopravní stavby — letecké |
| `vs-strategicke` | Strategické investiční stavby |
| `vs-oze` | Energetické stavby — OZE |
| `vs-energetika` | Energetické stavby a ostatní |
| `vs-tezba` | Těžební stavby a výbušniny |
| `vs-teplo-co2` | Tepelná infrastruktura a CO₂ |
| `vs-plochy-45ha` | Stavby v plochách nad 45 ha |
| `obalka` | blok „Potřebujete pomoct?" (25 stránek) |

Modrá v exportech je `rgb(35, 98, 162)`, tedy přesně `--color-primary-600`
z `uru-tokens.css` — nic se nepřebarvuje. Ikony č. 4 a 6 jsou dvoubarevné
(ozubené kolo a obrys baterie tmavě šedé); ověřeno při 600 dpi, že to není
chyba exportu.

Rám 18 × 24 px odpovídá tokenům design systému: `--icon-size-l` je 18 px
a `--height-line-m` 24 px, což je přesně to, s čím počítá
`.gov-message span:has([slot=icon])`. Ikony jsou proto oříznuté na 18 × 18
a vkládají se jako `<img slot="icon">` — rozměr i svislé zarovnání řeší
design systém sám.

Box dostane vlastní ikonu atributem `data-ico`:

```html
<div class="box edge" data-ico="vs-dalnice"> … </div>
```

Bez atributu platí původní pravidlo (výčtový box informační ikonu, ostatní
varovnou). Obálka nahradila `simple-envelope` z design systému — návrh má
silnější obrys a zaoblené rohy, s ikonou ze sady se nekryla.

**Exporty jsou 1×.** Na maketu a na `visual_diff` (rám 1440 px, měřítko 1)
sedí přesně, na ostrém webu budou na retina displeji měkké. Až se bude
sahat do Figmy, hodí se export 3× — výměna souborů je pak triviální.

## Str. 7 — proč je odlišnost vysoká a je to v pořádku

Maketa je o 723 px vyšší než návrh. Návrh má v „Přílohách a vzorech" tři výplňové
řádky „Lorem ipsum"; maketa má filtr (typ stavby / typ řízení / formát), počítadlo
nálezů a sedm konkrétních formulářů s verzí a platností. To jsou zelené připomínky
22 a 23 a je to největší schválená odchylka na webu. Pixelové číslo té stránky
proto zůstane vysoké — posuzuje se snímek.

Doplněno do `tools/odchylky.yaml`, aby to textové porovnání nehlásilo jako chybu.
Str. 7 je textově na 100 %.

Tabulka s číslem účtu nahrazena dvěma prostými odstavci, jak to má návrh. Řádek
s variabilním symbolem návrh nemá, ale str. 5 na něj podle připomínky 19 odkazuje,
proto zůstává — je zapsaný mezi odchylkami.

## Řádek souboru (`ul.files`) podle návrhu

Návrh nemá u souboru štítek formátu ani tlačítko Stáhnout: je tam ikona dokumentu
(list se zahnutým rohem, u PDF s popiskem „PDF“), název souboru je modrý podtržený
odkaz, kterým se stahuje, a za ním formát a velikost v závorce. Maketa měla barevný
štítek PDF/DOCX, název černý a vpravo tlačítko Stáhnout.

Převod je v `to_ds()`, ne v obsahu — `<span class="ft">PDF</span>` se mění na ikonu
a `<span class="name">` na odkaz. Propsalo se to do 31 řádků na všech stránkách
se seznamem souborů.

Ikony jsou vytažené přímo z PDF návrhu: vykresleny při 600 dpi, průhlednost dopočítána
z prolnění mezi bílou a `#2362A2`, uloženy jako `soubor.png` a `soubor-pdf.png`
na plátně 72 × 72 (4× proti zobrazovaným 18 px). Stejný postup půjde použít i jinde,
kde návrh má ikonu, kterou design systém nemá.

Tlačítko „Přejít na Portál stavebníka“ na str. 7 dostalo šipku (třída `btn arrow`),
stejnou, jakou má též tlačítko na str. 8.

## Ze str. 31: stránka je v návrhu mnohem kratší

Návrh má jen perex a dvě dlaždice — ESPON a V4+2 — s krátkým popisem a odkazem
„Přejít“. Maketa měla delší odstavce, dvě velká tlačítka, varovný box o odchodu
mimo web a navíc oddíl „Přeshraniční spolupráce“, který návrh nemá. Zkráceno
podle návrhu; použity též dlaždice s `data-more="Přejít"` jako na str. 27.

**Postranní nabídka se v návrhu mění podle otevřené sekce.** Na str. 31 jsou pod
„Mezinárodní spoluprácí“ zanořené položky ESPON a V4+2. Doplněno jako kotvy.
Návrh má v nabídce překlep **„EPSON“** — maketa píše správně ESPON.

## Ze str. 30: tabulka místo historie dokumentu

**Dva odstavce jsou v návrhu červené** — ty o tom, co je aktuálně závazné.
Barva je `rgb(179 34 34)`, což **není žádný token design systému**; nejbližší
`color-error-700` je 181 8 23. Prohledal jsem další vykreslené strany návrhu
(4–7, 16, 18, 19, 21, 22, 24, 26–36) a tahle červená se nikde jinde nevyskytuje.

Zapracováno třídou `zvyrazneno`, ale **stálo by za otázku na Cognito**, jestli jde
o záměr, nebo o poznámku návrháře. Červený běžný text je na úředním webu
neobvyklý a barva mimo paletu tomu nasvědčuje.

**Přiložené dokumenty jsou v modrém panelu.** Návrh je sází do světle modrého
pruhu přes celou šířku obsahu (452–1203) s nadpisem 20 px a odkazy na soubory
**18 px** — tedy výrazně většími než v prostém seznamu souborů na str. 19, kde mají
12 px. Jsou to dvě různé podoby téhož prvku, ne nejednotnost — třída `.dokumenty`.

**Druhý seznam má dvouřádkové položky:** odkaz s formátem a velikostí v závorce
a pod ním samostatný řádek s názvem souboru, také v závorce. Řešeno třídou `fpath`.

Maketa měla oddíl „Aktualizace a změny“ s tabulkou Dokument / Rok / Stav.
Návrh má místo toho **Historie dokumentu** — devět odrážek s ročníky — a za nimi
čtyři odstavce o tom, kdo a proč jednotlivé aktualizace pořídil. Maketa je měla
shrnuté do jedné věty.

Oddíl „Pracovní výbor pro zpracování“ se v návrhu jmenuje **Konzultační výbor pro
zpracování Politiky územního rozvoje ČR** a má jiný text plus dva odkazy.
Na konci stránky je akordeon, jehož první položka „PÚR ČR – Aktualizace č. 1“
je rozbalená; zbytek je výplňový Lorem ipsum.

## Ze str. 29: odrážky místo odstavců

Návrh má „Základní informace“, „Cíle portálu“ i „Kontaktní osoby“ jako odrážkové
seznamy, maketa je měla jako odstavce. Tlačítko „Vstup do portálu“ je obtahované
(bílé s modrým okrajem), ne plné, a má 48 px, tedy velikost `l`. Do generátoru
proto přibyla třída `btn lg` — do té doby uměl jen `sm` a výchozí `m`.

V oddílu Kontaktní osoby má návrh jen otazník jako výplň; maketa tam odkazuje
na stránku Kontakty — zapsáno mezi odchylky.

## Ze str. 28: chyběl závěr a rozbalovací obsah

Celá spodní část je akordeon o šesti položkách, včetně **On-line evidence**, která
je v návrhu **rozbalená** a obsahuje dva odkazy. Zbylých pět je zavřených.

V prvním odstavci je část „Metodikou OÚP MMR pro postup orgánů územního plánování
při evidenci územně plánovací činnosti“ odkazem — v návrhu podtržená.

Poznámka k zápisu akordeonu: generátor čeká tvar
`<details class="acc" open data-faq><summary>…</summary><div class="body">…</div></details>`.
Atribut `open` **nesmí být poslední** — přepíše se jen tehdy, když za ním je
ještě mezera, ne rovnou `>`.

Maketa měla místo závěrečného oddílu tabulku „Aplikace a související obsah“
s třemi řádky a seznam čtyř odkazů. Návrh má místo toho oddíl **On-line evidence**
se dvěma odkazy (iLAS, iKAS) a pod ním **pět rozbalovacích položek** — Metodiky
a příručky, Ročenky, Seznam projektantů, Územní studie, Historie. Územní studie
maketa neměla vůbec.

Odstavec „Proč je evidence důležitá“ byl v maketě zkrácený zhruba na třetinu —
chyběla část o ročenkách, zpřístupnění veřejnosti a o tom, že ÚÚR a MMR chápou
monitorování jako službu veřejnosti. Doplněno podle návrhu.

## Ze str. 27: dlaždice pod sebou, ne ve dvou sloupcích

Dlaždice nemají v návrhu stín, ale **tenký šedý okraj** — 1 px, `rgb(209 209 209)`,
tedy `color-neutral-200`. Odečteno při 600 dpi z hrany karty, kde je barva čistá;
při 100 dpi vychází 225, což je jen prolínaní s bílou. Při najetí myší se mění
barva okraje, ne stín.

Poznámka: stín mají dál karty aktualit (`.news`) a karta mapy webu (`.sitemap-card`).
U těch jsem podobu z návrhu neřešil, takže to nechávám — stojí za ověření,
až přijdou na řadu příslušné stránky.

Návrh má sedm dlaždic **na celou šířku pod sebou**, bez ikon, s odkazem „Přejít“.
Maketa je měla ve dvou sloupcích, s ikonami a s popiskem „Zjistit více“. Lišilo se
i pořadí a všechny popisy — maketa měla vlastní, kratší znění. Přepsáno podle návrhu.

Kvůli tomu přibyly dva atributy dlaždice: `data-more` přepíše popisek odkazu
a `data-ico="zadna"` ikonu vypne. Obojí se hodí i jinde — popisek byl do té doby
natvrdo „Zjistit více“.

**Pozor na číslo u téhle stránky:** porovnání hlásilo 0 % pokrytí, protože návrh má
nadpis a popis dlaždice ve dvou řádcích pod sebou a extraktor je sloučí do jednoho
bloku, kdežto maketa je má jako `h3` a `p` zvlášť. Stejná třída problému jako
slévání sloupců na str. 26.

## Ze str. 26: porovnání slévá sloupce

**Pozor na výsledek porovnání u vícesloupcových stránek.** Rozcestník Územního rozvoje
má dlaždice ve třech sloupcích a `pdftotext -layout` je slévá do jednoho bloku
(„Mezinárodní spolupráce Publikační činnost ESPON — průběžně aktualizováno,
Aktualizované příručky…“). Takový blok se nemůže spárovat s žádným blokem makety
a stránka vychází na 33 %, i když je obsah v pořádku. Bez `-layout` se sloupce
rozdělí správně, ale režim se nedal přepnout globálně, aniž by se překopalo
oddělování postranní nabídky. **U takových stránek se musí číst
`pdftotext -f N -l N` bez přepínače a porovnat ručně.**

Při tom se našlo, že maketa měla u dvou dlaždic prohozený popis: „Publikační činnost“
měla text Archivu a „Časopis UaÚŘ“ větu navíc. Opraveno podle návrhu.

Oddíl „Užitečné odkazy“ není tabulka, ale šest karet ve dvou sloupcích. Karta má
125 px, rozteč 150 px, vnitřní okraj 16 px, mezi štítkem a názvem 12 px a mezi
názvem a popisem 8 px. Štítky nejsou stejné: „Aplikace“ má 231 231 231
(`color-neutral-100`), „Web“ 254 240 208 (`color-secondary-200`) a jantarový text.
Každý nese ikonu — zařízení u aplikace, řetěz u webu; vytaženo z PDF jako maska,
takže si ikona bere barvu textu štítku.

**K vyjasnění:** maketa má o dvě dlaždice víc — Stavebně technická prevence
a Konference a semináře. Návrh je nemá ani v rozbalené nabídce na str. 25; iSSTP
tam figuruje jen jako aplikace v užitečných odkazech. Ponecháno — odstraněním
by osiřely dvě existující stránky a položky v nabídce.

## Ze str. 24: stránka bez postranní nabídky

Heslo v katalogu otázek nemá v návrhu postranní nabídku ani bílý panel — obsah leží
přímo na šedém pozadí a karty otázek jsou široké 1000 px (144–1143). Maketa měla
běžné rozvržení s nabídkou. Řešeno příznakem `sidebar=False`, který už generátor uměl.

Otázky nejsou akordeony, ale rozbalené bílé karty se štítkem data aktualizace,
modrým číslovaným nadpisem a odpovědí. Štítek má barvu 254 240 208, což je
`color-secondary-200` — do mapování `TAG_COLOR` přibyl klíč `akt`.

Nadpis a perex si prohodily role: v návrhu je `h1` „1000 otázek ke stavebnímu právu
k zákonu č. 283/2021 Sb.“ a „Heslo: Adresář“ je modrý `h2` pod vyhledávacím polem.
Maketa to měla naopak. Blok „Máte dotaz k metodickým stanoviskům?“ návrh nemá.

Odpovědi byly v maketě zkrácené. Návrh končí obojí odkazem na adresář —
„… na adrese: krajské úřady“ a „… na stránkách ÚÚR na adrese: úřady územního
plánování“. Doplněno včetně odkazů. Drobečková navigace má v návrhu čtyři články
a poslední je celý název stránky, ne „Seznam hesel / Adresář“. Vyhledávací řádek
má 715 px (146–861), tlačítko 48 px, výška 40 px.

**Zástupný text pole porovnání nevidí.** „Hledat v otázkách“ je v maketě atribut
`placeholder`, ne textový uzel, takže ho `text_diff.py` hlásí jako chybějící.
Zapsáno mezi odchylky s poznámkou, že jde o omezení nástroje.

## Ze str. 22: dlaždice katalogu

Návrh má dvě bílé karty s tenkým okrajem, štítkem („Nový zákon“ / „Starý zákon“),
modrým nadpisem, řádkem platnosti s ikonou kalendáře a tlačítkem „Přejít na otázky“
přes celou šířku karty. Maketa měla prosté dlaždice-odkazy bez štítku, data i tlačítka
a jiný perex. Přepsáno; nová třída `.katalog` a pomocná funkce `_katalog()`
v `pages_mp.py`, aby šlo použít `gicon("calendar")`.

Rozměry odměřené na návrhu a zapsané do makety: karta 302 px široká, mezera mezi
kartami 150 px (karty leží na 451–752 a 903–1205 v obsahovém sloupci 452–1203),
štítek 24 px vysoký, tlačítko 32 px vysoké přes celou vnitřní šířku karty.
Design systém dává malému štítku 32 px, proto přepisuje `min-height`.

Barvy štítků sedí na tokeny přesně: zelená 226 246 227 je `color-success-100`
(třída `tag valid`), šedá 231 231 231 je `color-neutral-100` (`tag hist`).
Maketa měla původně `tag neutral`, což je v mapování modrá.

Blok „Máte dotaz k metodickým stanoviskům?“ na téhle stránce návrh nemá — odstraněn.

## Ze str. 19 a 21: řádek souboru a konzultační středisko

**Řádek souboru.** Návrh má rozteč řádků 56 px (odměřeno na pěti řádcích str. 19),
obsah řádku je vysoký 18 px, tedy 19 px okraje nahoru i dolů. Odkaz je 12 px
(`body-xs`, výška verzálky 8,6 px), ne 14. Do závorky patří i formát: „(PDF, 296 KB)“.
Formát se doplňuje v `to_ds()` jen u prostých řádků — bohatší varianta s verzí
a platností ho nemá, tam formát nese ikona.

**Str. 21 byla přestavěná.** Maketa měla „Komu slouží / neslouží“ ve dvou dlaždicích
vedle sebe, navíc oddíl „Co musí dotaz obsahovat“, který duplikoval odrážky z „Jak
podat dotaz“. Návrh má obojí jako prosté seznamy pod sebou. Doplněna chybějící
odrážka „Laická veřejnost“ a tři odstavce, které maketa vůbec neměla.

Kontaktní panel na konci má na téhle stránce **světle modré pozadí** (229 238 249)
proti šedému (246 246 246) na ostatních stránkách, jiný nadpis i jinou adresu —
je to kontakt střediska, ne obecné „Potřebujete pomoct?“. Řešeno třídou
`helpbox--modry` a blokem přímo v obsahu, aby za ním mohl stát závěrečný odstavec.

**Nadpisy oddílů na str. 21 mají 20 px, ale odstup nad sebou 48 px.** To je jiná
kombinace než na str. 4, 6 a 18, kde 20px nadpis má nad sebou 24 px. Maketa je sází
jako `h3` se standardními 24 px — velikost tedy sedí a odstup ne. Vypadá to na
nejednotnost v návrhu; stálo by za dotaz na Cognito, než se kvůli tomu zavádí
čtvrtá úroveň nadpisu.

## Ze str. 18: členění přechodného období

**Text v boxu bral barvu z obsahového sloupce.** Pravidlo `.content p` míří přímo
na `<p>`, takže přebíjelo dědění z `.gov-message` — na plném modrém boxu tak vyšel
tmavý text na tmavém pozadí. Uvnitř boxu teď barvu určuje box (`color: inherit`).

**Výrazný box není jen žlutý.** Návrh má dvě varianty: žlutou (str. 4, 5, 6, 16)
a plnou modrou s bílým textem (str. 18). Maketa znala jen žlutou. Přibyl druh boxu
`box hl` = `primary` + `bold`. Žárovka se teď kreslí maskou přes `currentColor`,
takže na žlutém boxu vyjde černá a na modrém bílá z jednoho souboru.

**Text str. 18 srovnán s návrhem včetně dat.** Dřív jsem se domíval, že maketa data
záměrně obchází formulací „přede dnem účinnosti novely“. Není to pravda: „1. 7. 2026“
je ve zdrojích 19× a opisná formulace 17×, obojí i v týchž souborech. Je to nedůslednost
v psaní, ne záměr. Datum účinnosti novely (1. 7. 2026) tedy nemá s otevřeným
rozhodnutím č. 1 nic společného — to se týká data vzniku úřadu v infobanneru.

**Rozestup odrážek v obsahu byl o 8 px větší.** Design systém dává každé položce
`margin-bottom: 8px`, návrh má rozestup rovný výšce řádku, tedy 24 px. Odměřeno
na str. 18: v návrhu 23–25 px mezi odrážkami, v maketě 31–33. Od nadpisu k první
odrážce má návrh 24 px, maketa měla 16. Týká se to jedenácti stránek. Je to táž
chyba, kterou jsem dřív opravil uvnitř zvýrazněných boxů — jen tam pochází
z projektové vrstvy, tady přímo z design systému.

**Box bez ikony.** Na str. 18 má návrh modrý box s levým pruhem, ale bez ikony —
jen text odsazený o 16 px. Maketa tam dávala výstražný trojúhelník. Řešeno
atributem `data-ico="zadna"`, který ikonu vypne. Ostatní rozměry boxu jsou shodné
(pruh 452–456, pozadí od 456,5, text od 468,6).

Maketa slila tři oddíly návrhu do jednoho modrého boxu „Na co dát pozor“ se sedmi
odrážkami. Návrh má tři podnadpisy s vlastními seznamy: „Jak poznat datum zahájení
řízení“, „Co platí pro tato řízení“ a „Pravomocná územní rozhodnutí“. Přeskládáno
podle návrhu; při tom se našly dvě odrážky, které v maketě úplně chyběly (řízení
z moci úřední, odvolací řízení podle úpravy platné v době prvního stupně).

Oddíl „Změny pro dotčené orgány“ byl na stránce dvakrát — jednou jako výklad, jednou
jako odkaz na časté dotazy. Sloučeno do jednoho, obsah převeden do boxů podle návrhu.
Nadpisy sníženy na `h3` tam, kde má návrh 20 px (výška verzálky 14,4 px).

**Data zůstávají nedotčená.** Návrh píše všude „od 1. 7. 2026“, maketa důsledně
„přede dnem účinnosti novely“. To vypadá jako záměr, ne opomenutí — souvisí
s otevřeným rozhodnutím č. 1 o znění infobanneru. Nepřepisoval jsem to ani jedním
směrem. Jediný zbývající chybějící blok na str. 18 je perex, který datum obsahuje.

## Ze str. 16: žárovka a dvě opravy nástroje

**Box za záložkami se o ně opíral.** V návrhu má zvýrazněný box nad sebou 24 px.
Za odstavcem to vycházelo samo z okraje odstavce, ale záložky spodní okraj nemají,
takže box na nich seděl natvrdo. Odměřeno na str. 16 (linka záložek 424, box 448)
a ověřeno na str. 6 (řádek nad boxem končí 1042, box začíná 1066). Řešeno okrajem
na `.content > .gov-message`, týká se pěti stránek se záložkami.

**Žlutý box má v návrhu žárovku,** ne výstražný trojúhelník. Ověřeno na str. 4, 6
i 16 — všude táž vyplněná žárovka 13,7 × 18 px. Vytažena z PDF stejně jako ikony
souborů, uložena jako `zarovka.png`. Nasazuje se automaticky na každý `box change`,
což je sedm stránek.

**Odpovědi v zavřeném akordeonu se hlásily jako přebývající text.** Návrh je nemůže
ukázat, když je akordeon zavřený. `text_diff.py` teď obsah zavřeného `<details>`
z přebývajících vynechává (`summary` z toho vyjmut, ten vidět je). Ze strany návrhu
se spárovat pořád může — na stránkách, kde návrh akordeon otevřený ukazuje. Ubralo
to 23 falešných hlášení.

**pdftotext na tomhle PDF občas selže** a stránka pak vrátí nula bloků. Celkové číslo
tiše klesne — zachytil jsem běh, kde vyšlo 368 z 522 místo 382 z 542. Skript na to
teď upozorní na chybový výstup. Když se číslo mezi běhy změní bez zásahu do obsahu,
je to tohle a stačí spustit znovu.

## Vědomá odchylka: sedm kroků řízení na str. 5

Návrh má šest kroků a slučuje „Posouzení a rozhodnutí" do jednoho. Maketa je má
zvlášť jako „Posouzení záměru" a „Rozhodnutí". **Aleš rozhodl, že sedm bodů
zůstane** — není to tedy chyba k opravě.

Důsledek: str. 5 zůstane proti návrhu zhruba o 90 px vyšší a všechno pod
seznamem kroků bude o tolik posunuté. Pixelová odlišnost té stránky proto
nespadne pod několik procent a nemá smysl ji tam honit; rozhoduje snímek.

Lhůty u kroků jsou doplněné podle návrhu: 5 pracovních dnů, 30 dnů od vyžádání,
60–90 dnů a odvolací 15 dnů. Návrh je má u kroků 1, 3, 4, 5 a 6; maketa u 1, 3,
4, 6 a 7 (krok „Posouzení záměru" žádnou lhůtu nemá).

## Systémové opravy ze str. 5 a 6

**Seznam kroků (`ol.steps`).** Maketa měla kolečko s tmavě modrou výplní a bílým
číslem, černý nadpis kroku a text 16 px. Návrh má kolečko Ø 32 px se světlým
pozadím (`primary-100`) a modrým číslem, nadpis kroku modrý 16 px, text kroku
14 px a řádek lhůty 12 px polotučně v `neutral-700`. Velikosti odečteny z výšek
verzálek na str. 5: 11,5 px u nadpisu (16), 10,1 px u textu (14), 8,6 px
u lhůty (12). Text kroku začíná 29 px za spojnicí — spojnice je na 468 px,
text na 497 px. Rozestup odstavců uvnitř kroku je 8 px (měření dává 10, což
není hodnota ze škály).

Používá se i na str. 32, 36 a v šabloně článku, takže se změna propíše dál.

**Záložky.** V návrhu vyplňují celou šířku obsahu a mají stejnou šířku, popisek
je uprostřed a menší (14 px, `body-s`). Maketa je měla široké podle obsahu,
zarovnané doleva a 16 px. Odměřeno na str. 5: řada 452–1203 px, popisky široké
94 a 127 px se středy v 637 a 1018 — to sedí na stejně široké záložky, nikoli na
šířku podle obsahu ani na stejné vnitřní okraje. Svisle je návrh sevřenější:
mezi spodkem řádku popisku a podtržením jsou 4 px, maketa měla 12.

**Nadpis bez obsahu.** Odstavec se značkou připomínky se v prezentačním režimu
skrývá jako poznámka makety. Když je ale takový odstavec jediným obsahem oddílu,
zůstane na stránce nadpis a pod ním nic — na str. 5 takhle visel prázdný oddíl
„Správní poplatky", na str. 18 totéž. Výjimka pro odstavce uvnitř zvýrazněných
boxů teď platí i pro odstavec, který stojí mezi dvěma nadpisy nebo na konci
stránky. Týkalo se to dvou stránek.

**Úrovně nadpisů se musí ověřovat po stránkách.** Návrh používá obě velikosti:
24 px (`h2`) i 20 px (`h3`). Na str. 4 byly kategorie 24 px, ale na str. 6 jsou
„Postup" a „Jak si domluvit návštěvu" 20 px — maketa je měla jako `h2`, což při
okrajích 48 / 24 přidávalo 46 px na každý nadpis. Velikost se pozná z výšky
verzálek: 17,3 px odpovídá 24 px, 14,2 px odpovídá 20 px.

## Systémové opravy ze str. 4

**Rozestupy nadpisů a odstavců.** Odměřeno na str. 4 a ověřeno na str. 8:
nadpis sekce má nad sebou 48 px (`spacing-3xl`) a pod sebou 24 px (`spacing-l`),
odstavec má 24 px pod sebou — do dalšího textu i do modrého boxu. Maketa měla
40 / 12 a u odstavce výchozích 16 px prohlížeče.

Opora měření: hrany modrých boxů jsou v rastru ostré, takže blok „nadpis +
jednořádkový odstavec" mezi dvěma boxy jde změřit přesně — v návrhu je 157 px
u všech osmi přechodů na str. 4 (a 181 px tam, kde je odstavec dvouřádkový).
Z toho 36 px je řádek nadpisu a 24 px řádek odstavce, na okraje zbývá 97 px,
tedy 48 + 24 + 24. Na str. 8 vychází mezera nadpis → text stejně (79 px při
rasterizaci na 100 dpi u obou stránek).

**Názvy kategorií jsou v návrhu nadpis sekce, ne podnadpis.** Výška verzálek je
17,3 px, což při poměru 0,711 dává písmo 24 px — stejné jako nadpisy „Co musíte
udělat před podáním žádosti" na str. 8, které maketa sází jako `h2`. Maketa je
měla jako `h3` (20 px). Změněno na `h2`.

**Úvodní nadpis „Přehled kategorií vyhrazených staveb" návrh nemá** — jde rovnou
od žlutého boxu k první kategorii. Odstraněn. Textové porovnání ho nehlásilo,
protože se slovním překryvem spároval s perexem, kde je „přehled kategorií
i konkrétních příkladů".

**Rozestupy v seznamech uvnitř boxů.** Maketa dávala každé položce 4 px nahoru
i dolů. Návrh je nemá — rozestup je čistá výška řádku 24 px. Odměřeno na výškách
boxů: dvě položky 80 px (2 × 24 + 2 × 16 vnitřního okraje), sedm položek 200 px,
tři 104 px — všechny devět boxů na str. 4 vychází na pixel. Odstavec za seznamem
odsazuje 8 px. Kromě str. 4 má box se seznamem jen str. 18 (Přechodové období).

**Hraniční případy patří dovnitř boxu.** Návrh drží větu „Hraniční případ: …"
jako odstavec uvnitř téhož modrého boxu se seznamem (u OZE a u ploch nad 45 ha).
Maketa z toho dělala dva boxy pod sebou, tedy dva rámečky navíc. Věta je běžným
řezem, ne tučně.

## Pasti, na které jsem opakovaně narazil

**`slot="icon"`** — komponenty design systému (Message, Infobar, Tile) očekávají
tento atribut na SVG ikoně. Bez něj se nepoužijí pravidla pro velikost, barvu
a svislé zarovnání a ikona se láme nad text. Chytlo mě to třikrát.

**`to_ds()` mění třídy** — `.btn` → `.gov-button`, `.tag` → `.gov-tag`,
`.card` → `.gov-tile`, `.box` → `.gov-message`. CSS psané proti původním
třídám tiše přestane platit. Selektory musí mířit na výsledné třídy.

**Náhradní pravidla design systému** — CSS obsahuje `:not([data-hydrated])`
varianty pro stav před inicializací web komponent. Maketa běhové prostředí
nemá, takže je potřeba atribut `data-hydrated` doplnit ručně (infobar, chip).

**Skrývání poznámek** — odstavec se značkou připomínky se označuje jako
poznámka makety a v prezentačním režimu se skryje. Odstavce uvnitř
zvýrazněných boxů jsou z toho vyňaté, jinak by zůstal prázdný barevný box.

**Cache prohlížeče a stará složka** — po výměně souborů je někdy potřeba vymazat
historii, jinak prohlížeč ukazuje starý stav. Stalo se to i tak, že `visual_diff`
vykresloval novou verzi a prohlížeč zároveň starou. Proto je v patičce razítko
`sestaveno DD. MM. RRRR HH:MM` — když nesedí s časem posledního běhu `build.py`,
dívá se prohlížeč jinam (cache, jiný klon, nebo nasazená verze na GitHub Pages).

**Návrh nepatří do repozitáře** — při výměně souborů by se smazal. Skripty ho
hledají o složku výš, v `~/Documents`, `~/Desktop`, `~/Downloads` nebo v cestě
z proměnné `DESU_DESIGN`.

**`pdftotext -bbox` u tohoto PDF poškozuje text** (vypadávají glyfy). Pro čtení
obsahu se používá `-layout`.

## Otevřená rozhodnutí pro Aleše

1. **Znění infobanneru** — teď „Od 1. 1. 2027 vznikl Úřad rozvoje území",
   tedy minulý čas u budoucího data. Schválené znění mluví o novele schválené
   Poslaneckou sněmovnou (sněmovní tisk č. 67) v podmiňovacím způsobu.
   Je to jedna konstanta `BANNER` v `build.py`.
2. **Fotografie** — `hero-budova.jpg` má vodoznak Unsplash+ a je použitá na
   dvou místech. `sidlo-uradu.jpeg` a fotky aktualit mají 400–480 px na šířku.
3. **Verze design systému** — pokud návrh stojí na nové verzi připravované
   pro DIA, měla by na ni maketa přejít dřív, než se doladí detaily.
   Nasvědčuje tomu, že ikony v návrhu nejsou z aktuální sady.
4. **Znak úřadu** — `assets/img/logo.svg` je digitální lev vektorizovaný
   z rastru dodaného Alešem. Výměna za oficiální soubor podle logo manuálu JVS
   je přepsání jednoho souboru.
5. **Konkrétní údaje** — adresy, IČO, datová schránka a jména zůstávají
   „doplní se"; plnění se předpokládá v listopadu.
6. **Vyhledávání** (str. 44–48 návrhu) — převzatá šablona pro služby gov.cz
   s fasetami Občan / Podnikatel / Právnická osoba. Než se na ni sáhne, měla
   by se vyjasnit s Cognitem.

## Jak pokračovat

Aleš se rozhodl jít **systematicky stránku po stránce** a hledat další
systémové rozdíly. Doporučené pořadí podle posledního běhu je v tabulce níže;
čísla jsou ale zastaralá (pocházejí z doby před ~17 systémovými opravami),
takže se vyplatí pustit `node tools/visual_diff.js` bez parametru a seřadit
znovu.

Klíč stránek návrhu k souborům makety je v `tools/text_diff.py` v proměnné
`MAP`. Stránky 2, 10, 25 a 35 jsou tytéž obrazovky s otevřeným menu,
13, 14 a 20 jsou jiné stavy filtrů a záložek, 38 je organizační struktura
se vzorovým textem z MZV (nepřenáší se).
