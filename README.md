# Maketa webu ÚRÚ

Klikatelná HTML maketa webu Úřadu rozvoje území. Vychází z návrhu designu (`DESU_design.pdf`)
a má zapracované připomínky označené v komentářovém dokumentu **zeleně**.

Statické HTML, žádný build ani závislosti. Stačí otevřít `index.html`.

## Nasazení na GitHub Pages

1. Nahraj obsah tohoto adresáře do repozitáře.
2. Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. Web bude na `https://<uživatel>.github.io/<repozitář>/`.

Soubor `.nojekyll` je součástí repozitáře — bez něj by GitHub Pages ignoroval některé cesty.

## Jak upravovat texty

**Přímo v HTML.** Soubory jsou čitelné a jeden soubor = jedna obrazovka. Editace přes GitHub
(tužka u souboru) funguje bez klonování. Toto je způsob, kterým vzniká finální znění.

**V prohlížeči.** V černé liště nahoře je tlačítko *Upravit texty*. Zapne editaci přímo na stránce,
změny se ukládají do prohlížeče (localStorage) — nikam se neodesílají a nevidí je nikdo jiný.

- *Stáhnout texty* — exportuje všechny změny do `uru-texty.json`
- *Načíst texty* — nahraje JSON zpět (např. na jiném počítači nebo po předání kolegovi)
- *Zahodit úpravy* — smaže lokální změny a vrátí původní znění
- *Skrýt značky* — schová zelené bublinky se zapracovanými připomínkami

Prohlížečový režim je vhodný na rychlé připomínkování a předání textů. Až bude znění hotové,
přenes ho do HTML souborů (nebo do `pages_*.py`), aby bylo v repozitáři.

## Struktura

```
index.html              úvodní stránka
aktuality.html          výpis aktualit a tiskových zpráv
uredni-deska.html       provizorní výpis (obrazovka není navržená)
kontakty.html           centrální stránka kontaktů
vyhledavani.html        výsledky vyhledávání
clanek.html             šablona článku
mapa-webu.html          mapa webu
vyhrazene-stavby/       7 obrazovek
metodicka-podpora/      14 obrazovek
uzemni-rozvoj/          14 obrazovek
kariera/                4 obrazovky
o-uradu/                5 obrazovek
assets/uru.css          styly
assets/uru.js           navigace, filtry, režim úprav
build.py, pages_*.py    generátor (nepovinný — viz níže)
```

## Generátor

Obrazovky jsou vygenerované z `pages_*.py` přes `python3 build.py`. Generátor je v repozitáři kvůli
hromadným zásahům (změna navigace, patičky, přidání sekce). **Pozor:** `build.py` přepíše všechny
`.html` soubory. Pokud upravuješ texty přímo v HTML, build už nespouštěj, nebo změny nejdřív
přenes do `pages_*.py`.

## Vizuál

Barvy, rozměry a proporce jsou odměřené přímo z návrhu designu (rám 1440 px), ne odhadnuté.
Všechny jsou v `assets/uru.css` jako proměnné v `:root`, takže přemapování na novou verzi
design systému gov je změna na jednom místě.

| Token | Hodnota | Kde v návrhu |
|---|---|---|
| `--primary` | `#2362A2` | infobanner, ikony dlaždic, tlačítka, aktivní prvky |
| `--primary-dark` | `#1E5086` | odkazy v hlavní navigaci a v levém submenu |
| `--primary-deep` | `#1D3C5D` | patička |
| `--hairline` | `#C5DBF2` | linka pod hlavičkou |
| `--ink` | `#262626` | nadpisy i běžný text |
| `--bg` | `#F6F6F6` | pozadí stránky |
| `--wrap` | `1152px` | obsahový sloupec (okraje 144 px při rámu 1440) |
| `--gutter` | `24px` | mezera mezi dlaždicemi (4 x 270 px + 3 x 24 px = 1152) |
| `--header-h` / `--nav-h` | `72px` / `64px` | výška hlavičky a navigace |

Písmo je **Roboto** (standard design systému gov), načítané z Google Fonts se systémovým
zálohovým řetězcem. Návrh má písmo vektorizované, takže název z PDF vyčíst nejde — pokud
finální design systém předepíše jiné, změní se jeden řádek v `body { font-family }`.

Navigace odpovídá návrhu: sedm položek bez pozadí, rozbalovací panel jako bílá karta přes
celou šířku se čtyřmi sloupci prostých odkazů, aktivní sekce podtržená. Rozcestníkové dlaždice
jsou bílé bez rámečku, jen s jemným stínem. Hero je diagonální modrý přechod s kruhovým
vizuálem vpravo. Stránky se submenu mají levý sloupec na šedém pozadí a obsah v bílém panelu,
stejně jako návrh.

## Co je v maketě jinak než v návrhu

Zeleně označené připomínky jsou zapracované a v maketě označené zelenou bublinkou s číslem
(najetím myší se zobrazí znění připomínky). Přehled:

| č. | Zapracováno |
|---|---|
| 2 | Infobanner je zavíratelný, zavření platí do konce relace; doplněna poznámka o době zobrazení |
| 3 | Vznikl výpis aktualit jako cíl odkazu „Zobrazit vše" |
| 4 | Na úvodní stránce jsou Aktuality a Rychlé odkazy nad blokem Informace o úřadu |
| 7, 98 | Vyhledávací pole i stránka výsledků uvádějí, že se prohledává obsah PDF |
| 11, 12 | Dlaždice „Co změní novela SZ" je první; pořadí dlaždic odpovídá submenu |
| 14 | Na stránce Co spadá pod ÚRÚ je funkční ověření příslušnosti podle typu záměru |
| 15 | Box „Co se mění" odkazuje na stránku o novele místo samostatného textu |
| 16 | Doplněno datum poslední aktualizace přehledu kategorií |
| 17 | Zobrazení pro účastníky řízení má vlastní adresu i položku v submenu |
| 19 | Správní poplatky mají jedno primární místo, druhé odkazuje |
| 22, 23 | Formuláře mají filtr podle typu stavby a řízení a metadata (verze, platnost) |
| 26, 43 | Vyhledávání v FAQ ve Vyhrazených stavbách i v Metodické podpoře |
| 31 | Vznikla stránka Kontakty na metodiky včetně dlaždice v rozcestníku |
| 34 | Platnost a aktuálnost jsou dvě nezávislé osy filtrů, doplněno vysvětlení |
| 36 | Doplněno řazení výsledků a počet položek na stránku |
| 37 | Nahrazené dokumenty mají ve výpisu odkaz na novější verzi |
| 38 | Detail stanoviska má levé submenu sekce |
| 39 | U souvisejících dokumentů je uvedený typ vztahu |
| 40 | Doplněna historie verzí dokumentu |
| 41 | Třetí záložka FAQ pro úřady územního plánování |
| 44, 45, 46 | Přechodové období provázané s novelou, doplněna delimitace, vzory jen odkazem |
| 50 | Konzultační středisko má strukturovaný formulář dotazu |
| 53, 54 | Tisíc otázek — přepínač rozsahu hledání a trvalý odkaz na otázku |
| 56 | STP a Konference doplněny do navigace Územního rozvoje |
| 61 | Přehled dotčených orgánů v Metodické podpoře + křížový odkaz z Územního plánování |
| 62 | Vznikla obrazovka Územně analytické podklady s filtrem živý / ukončený ročník |
| 64 | Na Evidenci ÚP činnosti jsou vstupy do iLAS a iKAS nahoře |
| 67 | Politika územního rozvoje je označená jako vzorová dokumentová stránka |
| 74, 75 | Filtr platové třídy; typ poměru je první filtr |
| 77 | Vznikla obrazovka přihlášky, tlačítko z detailu pozice na ni vede |
| 78 | Detail pozice odkazuje na oficiální text výběrového řízení na úřední desce |
| 83 | Rozcestník O úřadu obsahuje odkaz na Kontakty |
| 87 | Aktuality a tiskové zprávy mají jeden výpis rozlišený typem |
| 89 | U povinných informací je vyznačeno, co má vlastní podstránku |
| 91, 92 | Kontakty členěné podle agendy; centrální stránka je jediný zdroj dat |
| 94 | Štítky vedou na výpis aktualit |
| 96 | Vyhledávání má fasety podle obsahu ÚRÚ místo šablony pro služby |

### Obrazovky bez návrhu

Tyto obrazovky jsou v seznamu připomínek označené oranžově (ke zvážení), ale bez nich by maketa
končila slepým odkazem. Jsou proto vytvořené v provizorní podobě a označené zeleným boxem
„Tato obrazovka zatím není navržená":

- `uredni-deska.html`
- `vyhrazene-stavby/co-meni-novela.html`

### Co maketa neřeší

- Vizuál je pracovní. Barvy, typografie i komponenty se přemapují na novou verzi design systému gov.
- Obsah je návrh k dopracování — právní správnost textů se v této fázi neposuzovala.
- Neveřejná sekce, jazykové verze a chybové stavy nejsou zapracované (připomínky ke zvážení).
