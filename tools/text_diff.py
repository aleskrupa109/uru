# -*- coding: utf-8 -*-
"""Strukturní porovnání textů návrhu a makety.

Proti dřívějšímu fuzzy porovnání řádků řeší tři věci:

1. Porovnává **bloky** (nadpis / odstavec / položka seznamu), ne řádky. Text v PDF
   je rozsekaný na řádky a slova bývají rozdělená, takže porovnání po řádcích
   propadává celé odstavce.
2. Porovnává **oba směry** — hlásí i obsah, který maketa má a návrh ne.
3. Vidí **pořadí** — sekvenční diff odliší chybějící blok od bloku přesunutého.

Použití:
    python3 tools/text_diff.py             # souhrn za všechny stránky
    python3 tools/text_diff.py --detail    # výpis jednotlivých rozdílů
    python3 tools/text_diff.py --page 8    # jen jedna stránka návrhu

Vrací nenulový návratový kód, pokud zbývá aspoň jeden neschválený rozdíl —
lze tedy použít jako kontrolu před předáním.
"""
import argparse
import difflib
import os
import re
import subprocess
import sys
import unicodedata
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Návrh se hledá v repozitáři, o úroveň výš, nebo v cestě z proměnné DESU_DESIGN.
def _find_pdf():
    home = os.path.expanduser("~")
    for p in (os.environ.get("DESU_DESIGN"),
              os.path.join(ROOT, "DESU_design.pdf"),
              os.path.join(ROOT, "..", "DESU_design.pdf"),
              os.path.join(ROOT, "..", "..", "DESU_design.pdf"),
              os.path.join(home, "Documents", "DESU_design.pdf"),
              os.path.join(home, "Desktop", "DESU_design.pdf"),
              os.path.join(home, "Downloads", "DESU_design.pdf"),
              "/mnt/user-data/uploads/DESU_design.pdf"):
        if p and os.path.exists(p):
            return p
    return os.path.join(ROOT, "DESU_design.pdf")


PDF = _find_pdf()

# Mapování stránek návrhu na soubory makety. Stránky s otevřeným rozbalovacím
# menu (2, 10, 25, 35) a stránky bez obsahu se nemapují.
MAP = {
    3: "vyhrazene-stavby/index.html",
    4: "vyhrazene-stavby/co-spada-pod-uru.html",
    5: "vyhrazene-stavby/jak-probiha-rizeni.html",
    6: "vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html",
    7: "vyhrazene-stavby/dokumenty-a-formulare.html",
    8: "vyhrazene-stavby/portal-stavebnika.html",
    9: "vyhrazene-stavby/caste-dotazy.html",
    11: "metodicka-podpora/index.html",
    12: "metodicka-podpora/metodicka-stanoviska.html",
    15: "metodicka-podpora/stanovisko-detail.html",
    16: "metodicka-podpora/caste-dotazy.html",
    17: "metodicka-podpora/caste-dotazy-dotcene-organy.html",
    18: "metodicka-podpora/prechodove-obdobi.html",
    19: "metodicka-podpora/standardizace.html",
    21: "metodicka-podpora/konzultacni-stredisko.html",
    22: "metodicka-podpora/tisic-otazek.html",
    23: "metodicka-podpora/tisic-otazek-seznam.html",
    24: "metodicka-podpora/tisic-otazek-heslo.html",
    26: "uzemni-rozvoj/index.html",
    27: "uzemni-rozvoj/uzemni-planovani.html",
    28: "uzemni-rozvoj/evidence-upc.html",
    29: "uzemni-rozvoj/informacni-web-up.html",
    30: "uzemni-rozvoj/politika-uzemniho-rozvoje.html",
    31: "uzemni-rozvoj/mezinarodni-spoluprace.html",
    32: "kariera/index.html",
    33: "kariera/otevrene-pozice.html",
    34: "kariera/detail-pozice.html",
    36: "o-uradu/index.html",
    37: "o-uradu/kdo-jsme.html",
    39: "o-uradu/pro-media.html",
    40: "o-uradu/povinne-informace.html",
    41: "kontakty.html",
    42: "clanek.html",
    43: "mapa-webu.html",
    1: "index.html",
}

# Text, který je na každé stránce návrhu a nepatří do obsahu (hlavička, navigace,
# patička) nebo je to výplň z Figmy.
CHROME = [
    "hledejte v nazvu", "vyhrazene stavby", "metodicka podpora", "uzemni rozvoj",
    "kariera", "uredni deska", "o uradu", "kontakty", "domu", "od 1 7 2026 vznikl",
    "sokolovsk", "loremipsum", "lorem ipsum", "oznamovatel", "verze 2 0",
    "uzivatelske navody", "praha 9", "email com", "prohlaseni o pristupnosti",
    "ochrana osobnich", "povinne zverejnovane informace", "financovano", "narodni plan",
    "mapa webu", "design system", "list item", "consectetuer", "placeholder",
    "article heading", "nazev clanku", "scelerisque", "pellentesque", "voluptas",
    "possimus", "eligendi", "ligula", "sagittis", "facilisis", "impedit",
    "repellendus", "assumenda", "soluta nobis", "dictum", "faucibus", "tempore",
    "adipiscing", "zjistit vice", "urad rozvoje uzemi metodicka",
    "becny dotaz", "obecny dotaz", "konzultacni stredisko knihovna",
    "tisic otazek mapovy portal", "souvisejici lo",
]

# Prvky makety, které nejsou obsahem stránky.
VOID_TAGS = {"br", "img", "input", "meta", "link", "hr", "source", "path", "rect",
             "col", "area", "base", "embed", "track", "wbr", "svg", "circle", "use"}
SKIP_CLASSES = {"mockbar", "site-header", "mainnav", "site-footer", "subnav",
                "dropdown", "crumbs", "infobanner", "cmt", "mock-note"}
BLOCK_TAGS = {"h1", "h2", "h3", "h4", "p", "li", "td", "th", "summary", "figcaption",
              "dt", "dd", "button", "option", "label", "legend", "a"}
# Třídy, které v komponentách design systému nesou samostatný text — bez nich by
# se text celé dlaždice slil do jednoho bloku.
BLOCK_CLASSES = {"gov-tile__title", "gov-tile__annotation", "tile-order",
                 "gov-message__content", "gov-accordion-item__title",
                 "gov-accordion-item__content", "name", "fmeta", "role", "agenda"}


def norm(text):
    """Klíč pro porovnání: bez diakritiky, bez interpunkce, bez mezer.

    Zahození mezer je záměrné — PDF rozděluje slova uprostřed ("v robny",
    "ú činnosti"), takže porovnání se slovy propadává."""
    t = unicodedata.normalize("NFKD", text.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", t)


def norm_words(text):
    t = unicodedata.normalize("NFKD", text.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def is_chrome(text):
    n = norm_words(text)
    return any(c in n for c in CHROME)


# --------------------------------------------------------------------------
# bloky z návrhu
# --------------------------------------------------------------------------
def design_blocks(page):
    """Bloky obsahu ze stránky návrhu.

    Používá `pdftotext -layout`, ne `-bbox`. U tohoto PDF (export z Figmy s Type 3
    fonty) vrací -bbox poškozený text — vypadávají jednotlivé glyfy, takže z
    „Připravte projektovou dokumentaci" zůstane „Při ravte rojektovou dokumentaci".
    Režim -layout text vrací celý a sloupce zachovává odsazením, což zároveň řeší
    míchání levého submenu s obsahem."""
    out = subprocess.run(["pdftotext", "-layout", "-f", str(page), "-l", str(page), PDF, "-"],
                         capture_output=True, text=True).stdout
    rows = out.split("\n")
    # Patička začíná řádkem, kde jsou vedle sebe názvy jejích sloupců. Vše od
    # tohoto řádku dolů je patička, ne obsah stránky.
    half = len(rows) // 2
    for i, r in enumerate(rows):
        if i < half:                       # tentýž výčet je i v horní navigaci
            continue
        n = norm_words(r)
        if ("vyhrazene stavby" in n and "metodicka podpora" in n
                and "uzemni rozvoj" in n and "kariera" not in n):
            rows = rows[:i]
            break

    # buňky: úsek textu oddělený třemi a více mezerami; offset = číslo sloupce
    cells = []
    for r_i, row in enumerate(rows):
        for m in re.finditer(r"\S(?:.*?\S)?(?=\s{3,}|$)", row):
            txt = m.group(0).strip()
            if txt:
                cells.append({"row": r_i, "col_x": m.start(), "text": txt})
    if not cells:
        return []

    # Hranice obsahového sloupce: většina dlouhých buněk (tělo textu) začíná na
    # stejném offsetu. Kratší buňky před touto hranicí jsou levé submenu.
    longs = sorted(c["col_x"] for c in cells if len(c["text"]) > 40)
    boundary = longs[len(longs) // 2] if longs else 0
    content = [c for c in cells if c["col_x"] >= boundary - 6]
    if len(content) < 4:                      # stránka bez submenu (rozcestník)
        content = cells

    # bloky: navazující řádky obsahu; prázdný řádek blok uzavírá
    blocks, prev_row = [], None
    for c in sorted(content, key=lambda c: (c["row"], c["col_x"])):
        if prev_row is not None and c["row"] - prev_row <= 1:
            blocks[-1]["text"] += " " + c["text"]
        else:
            blocks.append({"text": c["text"], "col": 0, "row": c["row"]})
        prev_row = c["row"]

    blocks.sort(key=lambda b: (b["col"], b["row"]))
    return [b for b in blocks
            if len(norm(b["text"])) >= 12 and not is_chrome(b["text"])]


# --------------------------------------------------------------------------
# bloky z makety
# --------------------------------------------------------------------------
class Blocks(HTMLParser):
    """Vytáhne obsahové bloky ze stránky makety v pořadí, v jakém jsou v DOM.

    Přeskakuje hlavičku, navigaci, drobečky, patičku, lištu makety, levé submenu,
    infobanner a poznámky. Přeskakování řeší hloubkou, ne zásobníkem značek —
    nepárové značky tak nemohou rozhodit párování."""

    def __init__(self):
        super().__init__()
        self.blocks = []
        self.depth = 0
        self.skip_at = None      # hloubka, ve které začal přeskakovaný uzel
        self.hide_at = None      # hloubka zavřeného <details> — obsah není vidět
        self.sum_at = None       # hloubka <summary> — ten vidět je
        self.buf = []
        self.tag = None
        self.in_main = False

    def handle_starttag(self, tag, attrs):
        if tag in VOID_TAGS:
            return
        a = dict(attrs)
        cls = set((a.get("class") or "").split())
        if tag == "main":
            self.in_main = True
        self.depth += 1
        if tag == "details" and "open" not in a and self.hide_at is None:
            self.hide_at = self.depth
        if tag == "summary" and self.sum_at is None:
            self.sum_at = self.depth
        if self.skip_at is None and (
                cls & SKIP_CLASSES
                or tag in ("script", "style", "nav", "header", "footer", "select")):
            self.flush()
            self.skip_at = self.depth
            return
        if self.skip_at is None and (tag in BLOCK_TAGS or cls & BLOCK_CLASSES):
            self.flush()
            self.tag = tag

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if self.skip_at is None and tag in BLOCK_TAGS:
            self.flush()
        if self.skip_at is not None and self.depth == self.skip_at:
            self.skip_at = None
        if self.hide_at is not None and self.depth == self.hide_at:
            self.flush()
            self.hide_at = None
        if self.sum_at is not None and self.depth == self.sum_at:
            self.flush()
            self.sum_at = None
        self.depth = max(0, self.depth - 1)

    def handle_data(self, data):
        if self.skip_at is None and self.in_main and data.strip():
            self.buf.append(data.strip())

    def flush(self):
        if self.buf:
            text = " ".join(self.buf).strip()
            if len(norm(text)) >= 12:
                self.blocks.append({"text": text, "tag": self.tag or "p",
                                    "hidden": self.hide_at is not None and self.sum_at is None})
        self.buf = []
        self.tag = None


def mockup_blocks(path):
    p = os.path.join(ROOT, path)
    if not os.path.exists(p):
        return None
    b = Blocks()
    b.feed(open(p, encoding="utf-8").read())
    b.flush()
    return [x for x in b.blocks if not is_chrome(x["text"])]


# --------------------------------------------------------------------------
# schválené odchylky
# --------------------------------------------------------------------------
def load_waivers():
    path = os.path.join(ROOT, "tools", "odchylky.yaml")
    if not os.path.exists(path):
        return {}
    import yaml
    data = yaml.safe_load(open(path, encoding="utf-8")) or {}
    out = {}
    for item in data.get("odchylky", []):
        out.setdefault(item["stranka"], []).append(
            (norm(item["text"]), item.get("duvod", "")))
    return out


def waived(waivers, path, text):
    key = norm(text)
    for frag, _ in waivers.get(path, []) + waivers.get("*", []):
        if frag and frag in key:
            return True
    return False


# --------------------------------------------------------------------------
def tokens(text):
    return {w for w in norm_words(text).split() if len(w) > 3}


def compare(page, path, waivers, detail=False):
    """Spáruje bloky návrhu s bloky makety podle překryvu významových slov.

    - chybí   … blok návrhu, ke kterému se nenašel odpovídající blok makety
    - přebývá … blok makety, který v návrhu nemá oporu
    - pořadí  … počet převrácení v posloupnosti spárovaných bloků
    """
    d = design_blocks(page)
    m = mockup_blocks(path)
    if m is None:
        return None
    m_tok = [tokens(b["text"]) for b in m]
    m_norm = [norm(b["text"]) for b in m]
    m_all = set().union(*m_tok) if m_tok else set()
    d_all = set().union(*[tokens(b["text"]) for b in d]) if d else set()

    def by_letters(text):
        """Spárování podle písmen bez mezer.

        Export z Figmy láme slova uprostřed („P řílohy", „N ah l í žení"),
        takže porovnání podle slov propadává, i když je text totožný.
        Klíč z norm() mezery zahazuje, takže se takový blok pozná."""
        key = norm(text)
        if len(key) < 12:
            return -1
        best, best_ratio = -1, 0.0
        for j, mk in enumerate(m_norm):
            if not mk:
                continue
            if key == mk:
                return j
            if len(mk) >= 12 and (key in mk or mk in key):
                ratio = min(len(key), len(mk)) / max(len(key), len(mk))
                if ratio > best_ratio:
                    best, best_ratio = j, ratio
        return best if best_ratio >= 0.7 else -1

    missing, matched = [], []
    for b in d:
        tk = tokens(b["text"])
        if not tk:
            continue
        j = by_letters(b["text"])
        if j >= 0:
            matched.append(j)
            continue
        best, best_score = -1, 0.0
        for j, mt in enumerate(m_tok):
            if not mt:
                continue
            score = len(tk & mt) / len(tk)
            if score > best_score:
                best, best_score = j, score
        if best_score >= 0.6:
            matched.append(best)
        elif len(tk & m_all) / len(tk) >= 0.75:
            pass                      # obsah je na stránce, jen jinak rozdělený
        elif not waived(waivers, path, b["text"]):
            missing.append(b["text"])

    used = set(matched)
    # Odpověď v zavřeném akordeonu není v návrhu vidět, takže ji nelze hlásit
    # jako přebývající. Ze strany návrhu se spárovat může — tam, kde návrh
    # ukazuje akordeon otevřený.
    extra = [b["text"] for j, b in enumerate(m)
             if j not in used and len(m_tok[j]) >= 4
             and not b.get("hidden")
             and (not d_all or len(m_tok[j] & d_all) / len(m_tok[j]) < 0.5)
             and not waived(waivers, path, b["text"])]

    inversions = sum(1 for i in range(len(matched) - 1) if matched[i] > matched[i + 1])

    if detail and (missing or extra or inversions):
        print(f"\n=== str. {page} → {path}")
        for t in missing:
            print(f"  CHYBÍ    {t[:150]}")
        for t in extra:
            print(f"  PŘEBÝVÁ  {t[:150]}")
        if inversions:
            print(f"  POŘADÍ   {inversions} převrácení v posloupnosti bloků")
    return len(missing), len(extra), len(d), inversions


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detail", action="store_true", help="vypsat jednotlivé rozdíly")
    ap.add_argument("--page", type=int, help="jen jedna stránka návrhu")
    args = ap.parse_args()

    if not os.path.exists(PDF):
        print(f"Nenalezen návrh: {PDF}")
        print("Očekává se DESU_design.pdf v nadřazeném adresáři repozitáře.")
        return 2

    waivers = load_waivers()
    pages = [args.page] if args.page else sorted(MAP)
    rows, tot_m, tot_e, tot_b, tot_o = [], 0, 0, 0, 0
    for pg in pages:
        if pg not in MAP:
            continue
        res = compare(pg, MAP[pg], waivers, args.detail)
        if res is None:
            continue
        miss, extra, blocks, order = res
        if blocks == 0:
            print(f"POZOR: str. {pg} nevrátila z návrhu žádný text — pdftotext"
                  f" na tom PDF občas selže a celkové číslo pak tiše klesne."
                  f" Spusťte porovnání znovu.", file=sys.stderr)
        tot_m += miss
        tot_e += extra
        tot_b += blocks
        tot_o += order
        if miss or extra or order:
            rows.append((miss + extra + order, miss, extra, order, blocks, MAP[pg]))

    print("\n{:<48} {:>6} {:>8} {:>7} {:>7}".format(
        "stránka", "chybí", "přebývá", "pořadí", "bloků"))
    print("-" * 80)
    for _, miss, extra, order, blocks, path in sorted(rows, reverse=True):
        print(f"{path:<48} {miss:>6} {extra:>8} {order:>7} {blocks:>7}")
    print("-" * 80)
    shoda = 100.0 * (1 - tot_m / tot_b) if tot_b else 100.0
    print(f"{'CELKEM':<48} {tot_m:>6} {tot_e:>8} {tot_o:>7} {tot_b:>7}")
    print(f"\npokrytí obsahu návrhu: {shoda:.1f} %"
          f"   ({tot_b - tot_m} z {tot_b} bloků)")
    if waivers:
        n = sum(len(v) for v in waivers.values())
        print(f"schválených odchylek v tools/odchylky.yaml: {n}")
    return 1 if (tot_m or tot_e or tot_o) else 0


if __name__ == "__main__":
    sys.exit(main())
