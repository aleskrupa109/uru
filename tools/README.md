# Porovnání makety s návrhem

Dva nástroje a jeden seznam odchylek. Cílem je, aby věrnost návrhu byla číslo,
které nemůže tiše zdegradovat — po každé změně se pustí a je vidět, kam se to posunulo.

```
tools/text_diff.py       porovnání textů (běží kdekoli, jen potřebuje pdftotext)
tools/visual_diff.js     pixelové porovnání vzhledu (potřebuje Node + Chromium)
tools/odchylky.yaml      schválené odchylky, které se nehlásí
```

## Textové porovnání

```
python3 tools/text_diff.py                 # souhrnná tabulka
python3 tools/text_diff.py --detail        # jednotlivé rozdíly
python3 tools/text_diff.py --page 8        # jedna stránka návrhu
```

Návratový kód je nenulový, pokud zbývá aspoň jeden neschválený rozdíl — dá se
tedy použít jako kontrola před předáním.

Skript hlásí tři druhy rozdílů:

| Druh | Význam |
|---|---|
| **chybí** | blok návrhu, ke kterému se v maketě nenašel odpovídající text |
| **přebývá** | blok makety, který v návrhu nemá oporu |
| **pořadí** | počet převrácení v posloupnosti spárovaných bloků |

### Proč porovnává bloky, ne řádky

První verze porovnávala řádky a byla nepřesná: text v PDF je rozsekaný na řádky,
slova bývají rozdělená a odstavce se tak nedaly spolehlivě porovnat. Především ale
kontrolovala jen jeden směr — obsah, který maketa má a návrh ne, vůbec neviděla.

Skript proto skládá slova do **bloků** (odstavec, nadpis, položka seznamu),
porovnává je podle překryvu významových slov a hlásí oba směry.

### Proč `-layout` a ne `-bbox`

Návrh je export z Figmy s vektorizovanými fonty. Režim `pdftotext -bbox`, který
by dával souřadnice a velikost písma, u tohoto PDF **poškozuje text** — vypadávají
jednotlivé glyfy, takže z „Připravte projektovou dokumentaci" zůstane
„Při ravte rojektovou dokumentaci". Skript proto používá `-layout`, který text
vrací celý a sloupce zachovává odsazením.

Důsledkem je, že skript nezná velikost písma a nemůže spolehlivě rozlišit nadpis
od odstavce. Pořadí proto kontroluje na posloupnosti spárovaných bloků, ne na
posloupnosti nadpisů.

### Co skript vynechává

Hlavičku, hlavní navigaci, drobečky, infobanner, levé submenu a patičku — ty
maketa vykresluje z jedné definice a porovnávat je po stránkách nemá smysl.
Patička se odřezává podle řádku, kde jsou vedle sebe názvy jejích sloupců.
Dále výplňový obsah návrhu (Lorem ipsum, „List item", „Link") a vzorová data.

### Přesnost

Číslo ber jako **nástroj na určení priorit, ne jako absolutní skóre**. Rozsekaná
slova v PDF a mnohosloupcové mřížky způsobují šum v jednotkách bloků na stránku.
Spolehlivé je pořadí stránek v tabulce — nejvyšší číslo znamená největší mezeru.

## Vizuální porovnání

### Kam položit návrh designu

Nedávej `DESU_design.pdf` dovnitř repozitáře — při výměně souborů za novou verzi
se smaže spolu se zbytkem a musel bys ho pokaždé kopírovat zpět. **Polož ho o složku
výš**, tedy vedle složky repozitáře; oba skripty ho tam hledají automaticky.

Prohledávaná místa v pořadí: proměnná `DESU_DESIGN`, kořen repozitáře, jedna a dvě
složky nad ním, pak `~/Documents`, `~/Desktop` a `~/Downloads`.

### Vizuální porovnání

Předpoklady: **Node.js 18+** a **poppler** (kvůli `pdftoppm`, kterým se renderuje
návrh). Na macOS: `brew install poppler`.

```
npm init -y
npm install -D playwright pixelmatch pngjs
npx playwright install chromium

node tools/visual_diff.js            # všechny stránky
node tools/visual_diff.js --page 8   # jedna stránka
node tools/visual_diff.js --open     # rovnou otevřít přehled
```

Skript vykreslí každou stránku makety v Chromiu při šířce 1440 px (stejný rám
jako export z Figmy), vyrenderuje odpovídající stránku návrhu z PDF na stejnou
šířku a porovná je pixel po pixelu. Do `tools/vizualni-diff/` uloží u každé
stránky tři obrázky — maketu, návrh a teplotní mapu rozdílů — a přehledovou
stránku `index.html` s tabulkou odlišnosti.

**Toto je nástroj, který musíš spustit ty.** V prostředí, kde maketu vyvíjím,
není prohlížeč, takže vzhled nedokážu vykreslit ani zkontrolovat. Všechny
grafické úpravy jsem dělal jednosměrně: odměřil hodnotu z návrhu, napsal CSS
a čekal na tvou zpětnou vazbu z prohlížeče. Proto se stalo, že jsem u infobanneru
dvakrát tvrdil, že je opravený. Pošli mi tabulku a teplotní mapy a opravím CSS
podle nich.

Realistický cíl je odlišnost **pod 10 %**, ne nula — návrh má vlastní výplňový
text, jiné fotografie a vzorová data.

## Seznam odchylek

`tools/odchylky.yaml` drží odchylky, které jsou v pořádku, aby zbylé číslo bylo
čistý počet defektů. U každé je stránka, text a důvod:

| Důvod | Význam |
|---|---|
| `zelena` | zapracovaná zelená připomínka, číslo v poli `pripominka` |
| `vypln` | výplňový obsah návrhu, nepřenáší se |
| `doplni_se` | konkrétní údaj, který dodá úřad |
| `navrh_chyba` | zjevná chyba v návrhu, maketa ji nepřenáší |

Položka se stránkou `"*"` platí pro všechny stránky.

## Doporučený postup opravování

**U vzhledu odshora dolů podle záběru.** Nejdřív tokeny — jedna hodnota spraví
desítky stránek. Pak komponenty. Teprve nakonec jednotlivé stránky. Většina chyb,
které jsme zatím našli, byla na úrovni tokenů a komponent: barva boxu, velikost
ikony, náhradní pravidlo design systému pro nehydratovaný stav.

**U textů po sekcích a výhradně v `pages_*.py`**, nikdy ve vygenerovaném HTML —
`build.py` přepíše všech 52 souborů.

Po každé dávce pustit oba skripty a porovnat čísla s předchozím stavem.
