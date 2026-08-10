# Maketa webu ÚRÚ — shrnutí pro Claude Design

Orientační souhrn pro případ, že se na projektu bude pokračovat jinde. Provozní
detaily (příkazy, pasti nástrojů, stav jednotlivých stránek) jsou v `PREDANI.md`;
tenhle soubor popisuje, o co jde a jak se pracuje.

## Zadání

Úřad rozvoje území (ÚRÚ) vzniká sloučením agend DESÚ a ÚÚR. Dodavatel Cognito
odevzdal návrh webu ve Figmě, exportovaný jako **PDF o 48 obrazovkách**. Aleš
k němu napsal **111 připomínek** a roztřídil je barevně: 46 zelených
(k zapracování), 46 červených, 29 oranžových ke zvážení.

Úkolem bylo z těch dvou vstupů — návrhu a připomínek — udělat **klikatelnou
a editovatelnou maketu**, která slouží ke třem věcem:

1. ukázat návrh v prohlížeči, ne v PDF, aby šel proklikat,
2. ukázat, jak návrh vypadá **se zapracovanými zelenými připomínkami**,
3. posloužit jako podklad dodavateli, který bude web stavět.

## Co existuje

**52 statických HTML stránek** generovaných Pythonem, postavených na
**design systému gov.cz 4.6.5** (vendorovaném v repozitáři). Nasazené na GitHub
Pages. Obsah je v modulech `pages_*.py` a `content_*.py`, generátor `build.py`
z nich skládá stránky a převádí zjednodušené značky na komponenty design systému
(`.btn` → `.gov-button`, `.card` → `.gov-tile`, `.box` → `.gov-message`).

Vygenerované HTML se nikdy needituje ručně — `build.py` ho přepíše.

**Nástroje pro porovnání s návrhem:**

- `tools/visual_diff.js` — vykreslí stránku makety v prohlížeči a překryje ji
  odpovídající stranou návrhu; výstupem je snímek a procento odlišných pixelů
- `tools/text_diff.py` — porovná text: co v maketě chybí, co přebývá, jak je
  přeházené pořadí bloků
- `tools/odchylky.yaml` — 37 schválených odchylek, aby se vědomé rozdíly
  nehlásily jako chyby

## Jak práce probíhá

Smyčka: Aleš pustí porovnání a pošle snímek → rozdíly se **odměří přímo
v PDF** (rasterizace `pdftoppm`, analýza pixelů) → oprava jde do generátoru
nebo do CSS → nový balíček → nové porovnání.

Tři zásady, které se osvědčily a stály nejvíc chyb, než se usadily:

**Neodhadovat, měřit.** Velikost písma se pozná z výšky verzálky (děleno 0,72),
rozestupy z hran barevných boxů, barvy vzorkováním pixelu a porovnáním s tokeny
design systému. Skoro každá oprava, která vznikla odhadem, se ukázala jako
špatná — velikost písma v řádku souboru, šířka vyhledávacího pole, barva boxů.

**Dívat se na návrh jako na obrázek, ne jen na výpis textu.** Textové porovnání
nepozná barvu, rozvržení ani to, že je odstavec přeformulovaný. Jednou jsem
z výpisu usoudil, že jsou boxy žluté, a byly plné modré.

**Procento odlišnosti je vodítko, ne měřítko.** Když se doplní chybějící obsah,
stránka se prodlouží, všechno pod tím se posune a číslo vyroste — přestože je
maketa nově správně. U stránek se schválenými přídavky (filtr, formulář, tabulka
delimitace) zůstane číslo trvale vysoké a je to v pořádku.

## Pravidlo věrnosti

Maketa má odpovídat návrhu obsahem i vzhledem **s výjimkou míst, kde návrh mění
zeleně schválená připomínka**. Takové místo se označuje značkou `cmt(číslo)` —
zelené kolečko, které se zobrazuje jen v pracovním režimu. Zapracovaných
připomínek je v obsahu 41.

Kde maketa od návrhu odchýlená byla **bez značky**, srovnávalo se to podle
návrhu — s výjimkou případů, kdy by to znamenalo zásah do struktury webu
(osiřelé stránky, položky v navigaci). Ty jsou zapsané mezi odchylkami
k vyjasnění.

## Stav

Textové pokrytí návrhu je **74 %**. Prošly stránky 4, 5, 6, 7, 8, 11, 12, 15,
16, 18, 19, 21, 22, 24, 26 a šablona článku; většina z nich je textově na 100 %
a zbytek rozdílu tvoří schválené odchylky.

Z jednotlivých stránek vzešly systémové opravy, které se propsaly do celého webu
— rozestupy nadpisů a odstavců, rozestupy odrážek, řádek souboru, seznam kroků,
záložky, ikony boxů. To je hlavní přínos té práce: chyby se nacházely na jedné
stránce a opravovaly se na všech.

Otevřená rozhodnutí (znění infobanneru, verze design systému, oficiální znak
úřadu, konkrétní údaje, obrazovky vyhledávání) jsou v `PREDANI.md`.

## Co by v Claude Design dávalo smysl

Ne pokračování téhle práce — ta je z podstaty repozitářová a měřicí: čte se PDF,
počítají se pixely, upravuje se generátor, spouští se porovnání. Na to je
namístě prostředí, které umí pracovat se soubory a spouštět kód.

Kde by naopak canvas pomohl:

- **návrh obrazovek, které v podkladu chybí** — vyhledávání (str. 44–48 návrhu
  je převzatá šablona gov.cz, kterou je potřeba vyjasnit), nebo obrazovky
  pro agendy, které maketa má a návrh ne (Stavebně technická prevence,
  Konference a semináře)
- **varianty řešení k rozhodnutí** — například dvě podoby infobanneru podle
  toho, jak dopadne novela, nebo podoba dlaždic rozcestníku
- **podklad pro jednání s Cognitem** — přehled nalezených nesrovnalostí
  v návrhu samotném: nejednotné odstupy nadpisů mezi stránkami, ikony mimo
  aktuální sadu design systému, záložka odkazující na obsah, který návrh nemá

Společné je, že jde o **tvorbu nového vizuálu**, ne o dolaďování existující
implementace proti pevnému podkladu.
