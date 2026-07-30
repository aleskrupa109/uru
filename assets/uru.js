/* ÚRÚ – klikatelná maketa
   1) rozbalovací navigace
   2) živé filtry a řazení ve výpisech
   3) režim úprav textů (contenteditable + localStorage + export/import JSON)
*/
(function () {
  'use strict';

  var STORE = 'uru-maketa-texty';
  var page = (location.pathname.split('/').slice(-1)[0] || 'index.html');
  var dir = location.pathname.split('/').slice(-2, -1)[0] || '';
  var PAGEKEY = (dir && dir !== 'uru' ? dir + '/' : '') + page;

  /* ---------------- navigace ---------------- */
  /* Úzký panel se zarovnává na střed pod svou položkou menu čistě v CSS.
     Široká varianta (Územní rozvoj) je ukotvená k položce menu, ale má se
     zarovnat na obsahový sloupec — to dopočítáme. */
  function placeDropdown(li) {
    var dd = li.querySelector('.dropdown.wide');
    if (!dd) return;
    if (window.getComputedStyle(dd).position !== 'absolute') { dd.style.left = ''; return; }
    var wrap = li.closest('.mainnav').querySelector('.wrap');
    dd.style.left = Math.round(wrap.getBoundingClientRect().left
                             - li.getBoundingClientRect().left) + 'px';
  }

  function initNav() {
    var items = document.querySelectorAll('.mainnav li.has-drop');
    items.forEach(function (li) {
      var a = li.querySelector(':scope > a');
      a.addEventListener('click', function (e) {
        if (li.classList.contains('open')) return; // druhý klik projde na stránku sekce
        e.preventDefault();
        items.forEach(function (x) { if (x !== li) x.classList.remove('open'); });
        li.classList.add('open');
        placeDropdown(li);
      });
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.mainnav')) items.forEach(function (x) { x.classList.remove('open'); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') items.forEach(function (x) { x.classList.remove('open'); });
    });
    window.addEventListener('resize', function () {
      items.forEach(function (li) { if (li.classList.contains('open')) placeDropdown(li); });
    });
  }

  /* ---------------- infobanner ---------------- */
  function initBanner() {
    var b = document.querySelector('.infobanner');
    if (!b) return;
    var btn = b.querySelector('.close');
    if (sessionStorage.getItem('uru-banner') === 'off') b.style.display = 'none';
    if (btn) btn.addEventListener('click', function () {
      b.style.display = 'none';
      sessionStorage.setItem('uru-banner', 'off');
    });
  }

  /* ---------------- filtry výpisů ---------------- */
  function initFilters() {
    var wrap = document.querySelector('[data-filterable]');
    if (!wrap) return;
    var list = document.querySelector('[data-list]');
    if (!list) return;
    var rows = Array.prototype.slice.call(list.children);
    var selects = wrap.querySelectorAll('select[data-key]');
    var q = wrap.querySelector('input[data-q]');
    var counter = document.querySelector('[data-count]');
    var chips = document.querySelector('[data-chips]');
    var sort = document.querySelector('select[data-sort]');
    var perPage = document.querySelector('select[data-per]');

    function apply() {
      var active = [];
      var visible = rows.filter(function (r) {
        var ok = true;
        selects.forEach(function (s) {
          if (!s.value) return;
          if ((r.dataset[s.dataset.key] || '') !== s.value) ok = false;
        });
        if (q && q.value.trim()) {
          var needle = q.value.trim().toLowerCase();
          if (r.textContent.toLowerCase().indexOf(needle) === -1) ok = false;
        }
        return ok;
      });

      if (sort && sort.value === 'date') {
        visible.sort(function (a, b) { return (b.dataset.date || '').localeCompare(a.dataset.date || ''); });
      }
      var limit = perPage ? parseInt(perPage.value, 10) : 999;

      rows.forEach(function (r) { r.style.display = 'none'; });
      visible.slice(0, limit).forEach(function (r) { r.style.display = ''; list.appendChild(r); });

      if (counter) counter.textContent = visible.length;
      var emptyBox = document.querySelector('[data-empty]');
      if (emptyBox) emptyBox.style.display = visible.length ? 'none' : '';

      if (chips) {
        chips.innerHTML = '';
        var makeChip = function (label, onClear) {
          var wrap = document.createElement('span');
          wrap.className = 'gov-chip';
          wrap.setAttribute('data-hydrated', '');
          wrap.setAttribute('data-type', 'outlined');
          wrap.setAttribute('data-color', 'primary');
          wrap.setAttribute('data-size', 'm');
          var b = document.createElement('button');
          b.className = 'element';
          b.type = 'button';
          b.textContent = label + ' \u00d7';
          b.addEventListener('click', onClear);
          wrap.appendChild(b);
          chips.appendChild(wrap);
        };
        selects.forEach(function (s) {
          if (!s.value) return;
          makeChip(s.options[s.selectedIndex].text, function () { s.value = ''; apply(); });
        });
        if (q && q.value.trim()) {
          makeChip('\u201e' + q.value.trim() + '\u201c', function () { q.value = ''; apply(); });
        }
      }
      active.length;
    }

    selects.forEach(function (s) { s.addEventListener('change', apply); });
    if (q) q.addEventListener('input', apply);
    if (sort) sort.addEventListener('change', apply);
    if (perPage) perPage.addEventListener('change', apply);
    var reset = wrap.querySelector('[data-reset]');
    if (reset) reset.addEventListener('click', function () {
      selects.forEach(function (s) { s.value = ''; });
      if (q) q.value = '';
      apply();
    });
    apply();
  }

  /* ---------------- režim úprav ---------------- */
  var SEL = 'main h1, main h2, main h3, main h4, main p, main li, main td, main th, ' +
            'main dd, main dt, main figcaption, main .date, main .tile-order, ' +
            'main .gov-button .element, main .gov-tag .element, ' +
            'main .gov-tile__link, main .gov-tile__annotation, ' +
            'main [slot="label"], main .gov-message__content > p';

  function editable() {
    return Array.prototype.slice.call(document.querySelectorAll(SEL))
      .filter(function (el) { return !el.closest('.subnav, .mainnav, .site-footer, .mockbar, .crumbs'); });
  }

  function keyFor(el, i) { return PAGEKEY + '#' + el.tagName.toLowerCase() + i; }

  function loadStore() {
    try { return JSON.parse(localStorage.getItem(STORE) || '{}'); } catch (e) { return {}; }
  }
  function saveStore(o) { localStorage.setItem(STORE, JSON.stringify(o)); }

  function applyStored() {
    var data = loadStore();
    editable().forEach(function (el, i) {
      var k = keyFor(el, i);
      if (data[k] !== undefined) el.innerHTML = data[k];
    });
  }

  function initEdit() {
    var bar = document.querySelector('.mockbar');
    if (!bar) return;
    var btn = bar.querySelector('[data-edit-toggle]');
    var status = bar.querySelector('[data-edit-status]');
    var on = false;

    function setStatus(t) { if (status) status.textContent = t; }

    btn.addEventListener('click', function () {
      on = !on;
      document.body.classList.toggle('editing', on);
      btn.classList.toggle('on', on);
      btn.textContent = on ? 'Ukončit úpravy' : 'Upravit texty';
      editable().forEach(function (el, i) {
        el.contentEditable = on ? 'true' : 'false';
        if (on && !el.dataset.edit) {
          el.dataset.edit = keyFor(el, i);
          el.addEventListener('input', function () {
            var data = loadStore();
            data[el.dataset.edit] = el.innerHTML;
            saveStore(data);
            setStatus('uloženo v prohlížeči');
          });
        }
      });
      setStatus(on ? 'klikni do textu a piš' : '');
    });

    var exp = bar.querySelector('[data-export]');
    if (exp) exp.addEventListener('click', function () {
      var data = loadStore();
      var blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'uru-texty.json';
      a.click();
    });

    var imp = bar.querySelector('[data-import]');
    if (imp) imp.addEventListener('change', function (e) {
      var f = e.target.files[0];
      if (!f) return;
      var r = new FileReader();
      r.onload = function () {
        try { saveStore(JSON.parse(r.result)); location.reload(); }
        catch (err) { alert('Soubor se nepodařilo načíst.'); }
      };
      r.readAsText(f);
    });

    var clr = bar.querySelector('[data-clear]');
    if (clr) clr.addEventListener('click', function () {
      if (confirm('Opravdu zahodit všechny úpravy textů uložené v tomto prohlížeči?')) {
        localStorage.removeItem(STORE); location.reload();
      }
    });

    var cmt = bar.querySelector('[data-cmt-toggle]');
    if (cmt) {
      if (localStorage.getItem('uru-cmt') === 'off') document.body.classList.add('hide-cmt');
      cmt.addEventListener('click', function () {
        var off = document.body.classList.toggle('hide-cmt');
        localStorage.setItem('uru-cmt', off ? 'off' : 'on');
      });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    initNav();
    initBanner();
    initFilters();
    applyStored();
    initEdit();
  });
})();
