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

**Textové pokrytí návrhu:** 67,5 % (`python3 tools/text_diff.py`). Dřívější
údaj 68,4 % byl zastaralý — přeměřeno na nezměněné kopii repozitáře.

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

## Systémové opravy ze str. 5 a 6

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

**Cache prohlížeče** — po výměně souborů je někdy potřeba vymazat historii,
jinak porovnání ukazuje starý stav.

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
7. **Kroky řízení na str. 5** — návrh má šest kroků, maketa sedm: krok
   „Posouzení a rozhodnutí" je v maketě rozdělený na „Posouzení záměru"
   a „Rozhodnutí". Není u toho značka připomínky, takže není jasné, jestli je to
   záměr, nebo omyl. Lhůty u kroků jsou doplněné podle návrhu (5 pracovních dnů,
   30 dnů, 60–90 dnů, odvolací 15 dnů).

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
