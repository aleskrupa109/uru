// Vizuální porovnání makety s návrhem.
//
// Vykreslí každou stránku makety v Chromiu při šířce 1440 px (stejný rám jako
// export z Figmy), vyrenderuje odpovídající stránku návrhu z PDF na stejnou
// šířku a porovná je pixel po pixelu. Výstupem je tabulka odlišnosti a u každé
// stránky trojice obrázků: maketa, návrh a teplotní mapa rozdílů.
//
// Instalace (jednorázově, ve složce repozitáře):
//     npm init -y
//     npm install -D playwright pixelmatch pngjs
//     npx playwright install chromium
//
// Spuštění:
//     node tools/visual_diff.js                 # všechny stránky
//     node tools/visual_diff.js --page 8        # jedna stránka návrhu
//     node tools/visual_diff.js --open          # rovnou otevřít přehled
//
// Cesta k návrhu se bere z proměnné DESU_DESIGN, jinak se hledá DESU_design.pdf
// v repozitáři nebo o úroveň výš.

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const ROOT = path.join(__dirname, '..');
const OUT = path.join(ROOT, 'tools', 'vizualni-diff');
const WIDTH = 1440;

// Stránka návrhu → soubor makety. Musí odpovídat mapování v tools/text_diff.py.
const MAP = {
  1: 'index.html',
  3: 'vyhrazene-stavby/index.html',
  4: 'vyhrazene-stavby/co-spada-pod-uru.html',
  5: 'vyhrazene-stavby/jak-probiha-rizeni.html',
  6: 'vyhrazene-stavby/jak-probiha-rizeni-ucastnici.html',
  7: 'vyhrazene-stavby/dokumenty-a-formulare.html',
  8: 'vyhrazene-stavby/portal-stavebnika.html',
  9: 'vyhrazene-stavby/caste-dotazy.html',
  11: 'metodicka-podpora/index.html',
  12: 'metodicka-podpora/metodicka-stanoviska.html',
  15: 'metodicka-podpora/stanovisko-detail.html',
  16: 'metodicka-podpora/caste-dotazy.html',
  17: 'metodicka-podpora/caste-dotazy-dotcene-organy.html',
  18: 'metodicka-podpora/prechodove-obdobi.html',
  19: 'metodicka-podpora/standardizace.html',
  21: 'metodicka-podpora/konzultacni-stredisko.html',
  22: 'metodicka-podpora/tisic-otazek.html',
  23: 'metodicka-podpora/tisic-otazek-seznam.html',
  24: 'metodicka-podpora/tisic-otazek-heslo.html',
  26: 'uzemni-rozvoj/index.html',
  27: 'uzemni-rozvoj/uzemni-planovani.html',
  28: 'uzemni-rozvoj/evidence-upc.html',
  29: 'uzemni-rozvoj/informacni-web-up.html',
  30: 'uzemni-rozvoj/politika-uzemniho-rozvoje.html',
  31: 'uzemni-rozvoj/mezinarodni-spoluprace.html',
  32: 'kariera/index.html',
  33: 'kariera/otevrene-pozice.html',
  34: 'kariera/detail-pozice.html',
  36: 'o-uradu/index.html',
  37: 'o-uradu/kdo-jsme.html',
  39: 'o-uradu/pro-media.html',
  40: 'o-uradu/povinne-informace.html',
  41: 'kontakty.html',
  42: 'clanek.html',
  43: 'mapa-webu.html',
};

function findPdf() {
  const cands = [
    process.env.DESU_DESIGN,
    path.join(ROOT, 'DESU_design.pdf'),
    path.join(ROOT, '..', 'DESU_design.pdf'),
  ].filter(Boolean);
  for (const c of cands) if (fs.existsSync(c)) return c;
  throw new Error('Nenalezen DESU_design.pdf. Nastav proměnnou DESU_DESIGN.');
}

async function main() {
  const args = process.argv.slice(2);
  const onlyPage = args.includes('--page')
    ? Number(args[args.indexOf('--page') + 1]) : null;

  const { chromium } = require('playwright');
  const pixelmatch = require('pixelmatch');
  const { PNG } = require('pngjs');

  const pdf = findPdf();
  fs.mkdirSync(OUT, { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: WIDTH, height: 1200 },
    deviceScaleFactor: 1,
  });

  const rows = [];
  const pages = onlyPage ? [onlyPage] : Object.keys(MAP).map(Number).sort((a, b) => a - b);

  for (const pg of pages) {
    const rel = MAP[pg];
    if (!rel || !fs.existsSync(path.join(ROOT, rel))) continue;
    const base = rel.replace(/[\/]/g, '_').replace(/\.html$/, '');

    // 1) maketa — celá stránka, prezentační režim (bez lišty a poznámek)
    await page.goto('file://' + path.join(ROOT, rel));
    // vypnout animace a plovoucí prvky, aby byl snímek stabilní
    await page.addStyleTag({
      content: `*{animation:none!important;transition:none!important}
                .subnav{position:static!important}`,
    });
    const shotMock = path.join(OUT, base + '_maketa.png');
    await page.screenshot({ path: shotMock, fullPage: true });

    // 2) návrh — stránka PDF vyrenderovaná na stejnou šířku
    const shotDesign = path.join(OUT, base + '_navrh.png');
    execFileSync('pdftoppm', ['-png', '-r', '72', '-f', String(pg), '-l', String(pg),
      pdf, path.join(OUT, base + '_navrh_tmp')]);
    const tmp = fs.readdirSync(OUT).find(f => f.startsWith(base + '_navrh_tmp'));
    fs.renameSync(path.join(OUT, tmp), shotDesign);

    // 3) porovnání na společné výšce (návrh je jedna dlouhá stránka)
    const a = PNG.sync.read(fs.readFileSync(shotMock));
    const b = PNG.sync.read(fs.readFileSync(shotDesign));
    const w = Math.min(a.width, b.width);
    const h = Math.min(a.height, b.height);
    const crop = (src) => {
      const out = new PNG({ width: w, height: h });
      PNG.bitblt(src, out, 0, 0, w, h, 0, 0);
      return out;
    };
    const A = crop(a), B = crop(b);
    const diff = new PNG({ width: w, height: h });
    const changed = pixelmatch(A.data, B.data, diff.data, w, h,
      { threshold: 0.12, includeAA: true, alpha: 0.25 });
    const shotDiff = path.join(OUT, base + '_diff.png');
    fs.writeFileSync(shotDiff, PNG.sync.write(diff));

    const pct = 100 * changed / (w * h);
    rows.push({
      pg, rel, pct,
      hMock: a.height, hDesign: b.height,
      files: [base + '_maketa.png', base + '_navrh.png', base + '_diff.png'],
    });
    console.log(`str. ${String(pg).padEnd(3)} ${rel.padEnd(48)} `
      + `odlišnost ${pct.toFixed(1).padStart(5)} %   `
      + `výška maketa ${a.height} / návrh ${b.height}`);
  }

  await browser.close();

  rows.sort((x, y) => y.pct - x.pct);
  const html = `<!doctype html><meta charset="utf-8">
<title>Vizuální porovnání makety s návrhem</title>
<style>body{font:15px Roboto,system-ui,sans-serif;margin:24px;color:#262626}
h1{font-size:26px;font-weight:500}table{border-collapse:collapse;margin:18px 0}
td,th{padding:6px 12px;border-bottom:1px solid #e7e7e7;text-align:left}
.bad{color:#b50817;font-weight:500}figure{margin:28px 0}figcaption{font-weight:500;margin-bottom:8px}
img{max-width:32%;border:1px solid #d1d1d1;vertical-align:top}</style>
<h1>Vizuální porovnání makety s návrhem</h1>
<p>Šířka rámu ${WIDTH} px. Odlišnost je podíl pixelů, které se liší. Realistický
cíl je pod 10 % — návrh má vlastní výplňový text, jiné fotografie a vzorová data.</p>
<table><tr><th>str.</th><th>stránka</th><th>odlišnost</th><th>výška maketa / návrh</th></tr>
${rows.map(r => `<tr><td>${r.pg}</td><td>${r.rel}</td>`
    + `<td class="${r.pct > 10 ? 'bad' : ''}">${r.pct.toFixed(1)} %</td>`
    + `<td>${r.hMock} / ${r.hDesign}</td></tr>`).join('\n')}
</table>
${rows.map(r => `<figure><figcaption>${r.rel} — ${r.pct.toFixed(1)} %</figcaption>`
    + r.files.map(f => `<img src="${f}" loading="lazy">`).join('') + '</figure>').join('\n')}`;
  fs.writeFileSync(path.join(OUT, 'index.html'), html);
  console.log(`\nPřehled: tools/vizualni-diff/index.html`);
  if (args.includes('--open')) {
    const cmd = process.platform === 'darwin' ? 'open' : 'xdg-open';
    execFileSync(cmd, [path.join(OUT, 'index.html')]);
  }
}

main().catch(e => { console.error(e.message); process.exit(2); });
