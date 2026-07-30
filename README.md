# Maketa webu ÚRÚ

Klikatelná HTML maketa webu Úřadu rozvoje území. Vychází z návrhu designu (`DESU_design.pdf`)
a má zapracované připomínky označené v komentářovém dokumentu **zeleně**.

Statické HTML, žádný build ani závislosti. Stačí otevřít `index.html`.

## Nasazení na GitHub Pages

1. Nahraj obsah tohoto adresáře do repozitáře.
2. Settings → Pages → Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
3. Web bude na `https://<uživatel>.github.io/<repozitář>/`.

Soubor `.nojekyll` je součástí repozitáře — bez něj by GitHub Pages ignoroval některé cesty.

### Omezení nahrávání přes web

Repozitář má 103 souborů. Webové rozhraní GitHubu zvládne jedním přetažením nejvýš 100 souborů
a **v Safari přetažení celé složky nefunguje vůbec**. Řešení:

- použij Chrome nebo Firefox a nahraj obsah nadvakrát — nejdřív soubory z korene složky
  (60 souborů), potom celou složku `assets` (43 souborů);
- nebo použij GitHub Desktop, kde žádný z těchto limitů neplatí. Při opakovaných úpravách
  se to vyplatí, protože každá změna vzhledu přegeneruje všech 52 HTML souborů.

## Jak upravovat texty

Maketa má dva režimy. **Prezentační** je výchozí — chová se jako běžný web, bez nástrojů
a bez zelených značek připomínek. V této podobě ji lze poslat komukoli.

**Pracovní režim** zapneš tím, že k adrese přidáš `?edit=1`:

```
https://<uživatel>.github.io/<repozitář>/?edit=1
```

Volba se uloží do prohlížeče, takže parametr stačí použít jednou a dál se maketa prochází
normálně. Vypneš ji parametrem `?edit=0`. V pracovním režimu se nahoře objeví černá lišta:

- *Upravit texty* — zapne editaci přímo na stránce
- *Stáhnout texty* — exportuje změny do `uru-texty.json`
- *Načíst texty* — nahraje JSON zpět (jiný počítač, předání kolegovi)
- *Zahodit úpravy* — smaže lokální změny
- *Skrýt značky* — schová bublinky se zapracovanými připomínkami

**Není to zabezpečení.** Kdo zná parametr `?edit=1`, režim si zapne také. Nemá to ale žádný
dopad na ostatní: úpravy textů se ukládají jen do prohlížeče toho, kdo je dělá (localStorage),
nikam se neodesílají a v repozitáři se nic nemění. Nikdo tedy nemůže změnit to, co vidí druzí.
Smyslem přepínače je, aby maketa u třetí strany vypadala jako web a nesváděla k experimentům.

Finální znění textů vzniká úpravou HTML souborů v repozitáři — v naklonované složce na disku
nebo přes tužku na GitHubu. Prohlížečový režim je na rychlé připomínkování a předání textů.

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
assets/gov/             design systém gov.cz (CSS, písmo, ikony)
assets/uru-tokens.css   přemapování primární palety na barvy ÚRÚ
assets/gov-fonts.css    deklarace řezů Roboto
assets/uru.css          projektová vrstva (hlavička, navigace, patička, layout)
assets/uru.js           navigace, filtry, režim úprav
build.py, pages_*.py    generátor (nepovinný — viz níže)
```

## Generátor

Obrazovky jsou vygenerované z `pages_*.py` přes `python3 build.py`. Generátor je v repozitáři kvůli
hromadným zásahům (změna navigace, patičky, přidání sekce). **Pozor:** `build.py` přepíše všechny
`.html` soubory. Pokud upravuješ texty přímo v HTML, build už nespouštěj, nebo změny nejdřív
přenes do `pages_*.py`.

## Vizuál — design systém gov.cz

Maketa stojí na **design systému gov.cz** (`@gov-design-system-ce`, verze 4.6.5). Balíčky jsou
uložené přímo v repozitáři, takže nasazení nepotřebuje npm, build ani připojení k CDN:

```
assets/gov/styles/   tokens.css, styles.css, layout.css, content.css,
                     animations.css, components.css
assets/gov/fonts/    Roboto (woff2) z balíčku fonts — 4 řezy bez kurzivy
assets/gov/icons/    ikony použité v maketě
```

Aktualizace na novější verzi je stažení balíčků z npm a přepsání těchto adresářů.

### Bez běhového prostředí web komponent

CSS design systému cílí zároveň na element i na třídu a varianty čte z atributů `data-*`.
Maketa proto používá skutečné komponenty design systému v čistém HTML, bez JavaScriptu:

```html
<span class="gov-button" data-color="primary" data-type="solid" data-size="m">
  <a class="element" href="...">Zobrazit</a>
</span>
```

Díky tomu jde maketa otevřít i dvojklikem z disku, váží 1,2 MB místo 20 MB a nemá shadow DOM,
takže filtrovací skript makety si na obsah dosáhne. Použité komponenty: Tile (rozcestníky),
Button, Tag, Chip (aktivní filtry), Message (zvýrazněné boxy), Accordion (FAQ), Infobar
(oznámení v hlavičce), Breadcrumbs a Empty (prázdné stavy výpisů).

### Co dodává design systém a co projekt

Komponenty, typografii, barvy, rozestupy a rádiusy dodává design systém. Projektová vrstva
v `assets/uru.css` obsahuje jen to, co design systém záměrně neobsahuje — hlavičku, hlavní
navigaci s rozbalovacím panelem, patičku, levé submenu, hero a několik výpisů. Jsou to
organismy, které si podle pravidel design systému staví každý projekt sám; i tak jsou
postavené výhradně na jeho tokenech. Stejné dělení bude mít i finální web.

Rozbalovací panel navigace má dvě podoby, obě odměřené z návrhu. Výchozí je **jeden sloupec
o šířce 296 px** zarovnaný na střed pod svou položkou menu; panel je ukotvený k položce menu,
takže polohu řeší čistě CSS. Sekce s velkým počtem položek — v maketě jen Územní rozvoj —
dostane **širokou variantu se čtyřmi sloupci** zarovnanou na obsahový sloupec; její vodorovnou
pozici dopočítá skript. Přepínač je v `build.py`: devět a více položek v sekci znamená širokou
variantu.

Design systém přidává k položkám seznamů odrážku přes `::before`. V obsahu je to správně,
u navigace, patičky a výpisů ne — konstrukční seznamy proto mají třídu `gov-list--plain`
a projektová vrstva odrážky u nich vypíná.


### Ikony a fotografie

V `assets/gov/icons/complex/` je 28 ilustračních ikon design systému — jen ty, které maketa
skutečně používá. Ikony se do stránek vkládají inline (používají `currentColor`, aby se obarvily
tokenem primární barvy), takže za běhu nejsou soubory potřeba vůbec — v repozitáři jsou jen
kvůli generátoru.

Přiřazení ikony k dlaždici je v `build.py` v tabulce `TILE_ICON`, klíčem je cesta cílové stránky.
Výměna ikony je jeden řádek. Celou sadu (42 základních a 131 ilustračních) dostaneš takto:

```
npm install @gov-design-system-ce/icons
cp node_modules/@gov-design-system-ce/icons/lib/complex/*.svg assets/gov/icons/complex/
```

Fotografie jsou v `assets/img/`:

- `hero-budova.jpg` — kruhový vizuál v úvodním banneru. **Soubor má vodoznak Unsplash+**, pro
  spuštění bude potřeba licencovaná verze nebo vlastní fotografie.
- `aktualita-metodiky.jpg`, `aktualita-vyberova-rizeni.jpg` — fotografie ve dvou menších
  aktualitách. Velká aktualita používá tentýž soubor jako banner (`hero-budova.jpg`), protože
  úřad dodal stejný snímek pro obě místa — pokud se mají rozejít, přidej druhý soubor a změň
  jeden řádek v `pages_home.py`.
- `sidlo-uradu.jpeg` — fotografie sídla v bloku Informace o úřadu. Má jen 400 × 225 px, takže se
  na šířku sloupce roztahuje a rozostřuje. Pro spuštění bude potřeba snímek alespoň 1200 px na šířku.
- `logo.svg` — **znak úřadu, digitální lev.** Vektorizovaný z rastrového podkladu dodaného
  úřadem: pixelová kresba je převedená na mřížku 18 × 24 obdélníků, shoda s předlohou 0,98.
  Vkládá se do hlavičky inline, takže barvu bere z tokenu primární barvy (`currentColor`).
  Výměna za oficiální soubor podle logo manuálu JVS = přepsat tento soubor a spustit `build.py`.

### Úprava primitiv

Barvy návrhu se nekryjí s výchozí paletou design systému — ten má `--color-primary-600`
na `#00469B`, návrh používá `#2362A2`. Neutrální odstíny naopak sedí přesně, včetně pozadí
`#F6F6F6` a textu `#262626`.

Podle [pravidel pro modifikaci](https://designsystem.gov.cz/pravidla/pravidla-pro-modifikaci-design-systemu)
se to řeší úpravou kolekce Primitives. V maketě je to soubor `assets/uru-tokens.css`, který
přepisuje primární škálu na hodnoty odměřené z návrhu:

| Token | Hodnota | Kde v návrhu |
|---|---|---|
| `--color-primary-600` | `#2362A2` | oznámení v hlavičce, ikony, tlačítka, aktivní prvky |
| `--color-primary-700` | `#1E5086` | odkazy v hlavní navigaci a v levém submenu |
| `--color-primary-800` | `#1D3C5D` | patička |
| `--color-primary-200` | `#C5DBF2` | linka pod hlavičkou |

Smazáním toho souboru se maketa vrátí k výchozí paletě design systému. Projektové rozměry
(`--uru-wrap` 1152 px, `--uru-header-h` 72 px, `--uru-nav-h` 64 px) jsou ve stejném souboru
a odpovídají odměřeným hodnotám z rámu 1440 px.

Písmo je **Roboto** z balíčku `@gov-design-system-ce/fonts`, tedy standard design systému.
Návrh má písmo vektorizované, takže jeho název z PDF vyčíst nejde.

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
