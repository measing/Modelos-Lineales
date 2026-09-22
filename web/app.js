'use strict';
const tabs = [...document.querySelectorAll('[data-tab]')];
function activateTab(name, focus = false) {
  if (!tabs.some(tab => tab.dataset.tab === name)) name = 'python';
  tabs.forEach(tab => {
    const selected = tab.dataset.tab === name;
    tab.setAttribute('aria-selected', String(selected));
    tab.tabIndex = selected ? 0 : -1;
    document.getElementById(tab.getAttribute('aria-controls')).hidden = !selected;
    if (selected && focus) tab.focus();
  });
  const frame = document.getElementById(`frame-${name}`);
  if (frame?.dataset.src) { frame.src = frame.dataset.src; delete frame.dataset.src; }
}
tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => { location.hash = tab.dataset.tab; activateTab(tab.dataset.tab); });
  tab.addEventListener('keydown', event => {
    const directions = { ArrowRight: (index + 1) % tabs.length, ArrowLeft: (index + tabs.length - 1) % tabs.length, Home: 0, End: tabs.length - 1 };
    if (event.key in directions) {
      event.preventDefault();
      const target = tabs[directions[event.key]].dataset.tab;
      location.hash = target;
      activateTab(target, true);
    }
  });
});
window.addEventListener('hashchange', () => activateTab(location.hash.slice(1)));
activateTab(location.hash.slice(1));
document.querySelectorAll('[data-view]').forEach(button => button.addEventListener('click', () => {
  const language = button.dataset.language;
  const code = button.dataset.view === 'code';
  const panel = document.getElementById(`panel-${language}`);
  panel.querySelectorAll('[data-view]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  const url = `reports/${language}${code ? '-code' : ''}.html`;
  const frame = document.getElementById(`frame-${language}`);
  frame.src = url;
  frame.title = `${code ? 'Código' : 'Informe'} de ${language === 'r' ? 'R' : 'Python'}`;
  panel.querySelector('.full-report').href = url;
}));
function showDataset(key) {
  const data = window.LAB_DATA[key];
  document.querySelectorAll('[data-dataset]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.dataset === key)));
  document.getElementById('data-summary').textContent = `${data.rows.length} observaciones · ${data.columns.length} variables · ${key}.txt`;
  const download = document.getElementById('data-download');
  download.href = `downloads/${key}.txt`;
  download.textContent = `Descargar ${key}.txt ↓`;
  const table = document.getElementById('data-table');
  table.querySelector('caption').textContent = data.title;
  const header = document.createElement('tr');
  ['N.º', ...data.columns].forEach(label => { const cell = document.createElement('th'); cell.scope = 'col'; cell.textContent = label; header.append(cell); });
  table.querySelector('thead').replaceChildren(header);
  const body = document.createDocumentFragment();
  data.rows.forEach((row, index) => {
    const tr = document.createElement('tr');
    [index + 1, ...row].forEach(value => { const td = document.createElement('td'); td.textContent = value; tr.append(td); });
    body.append(tr);
  });
  table.querySelector('tbody').replaceChildren(body);
  document.querySelector('.table-wrap').scrollTop = 0;
}
document.querySelectorAll('[data-dataset]').forEach(button => button.addEventListener('click', () => showDataset(button.dataset.dataset)));
showDataset('ventas');
