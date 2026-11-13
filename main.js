'use strict';

// Render paper notation with accessible KaTeX HTML + MathML.
if (typeof renderMathInElement === 'function') {
  renderMathInElement(document.body, {
    delimiters: [{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],
    throwOnError: false,
    strict: 'warn'
  });
}

const copyButton = document.querySelector('#copy-bibtex');
copyButton.hidden = false;
copyButton.addEventListener('click', async () => {
  const citation = document.querySelector('#bibtex').textContent;
  const status = document.querySelector('#copy-status');
  try {
    await navigator.clipboard.writeText(citation);
    status.textContent = 'BibTeX copied.';
  } catch {
    const range = document.createRange();
    range.selectNodeContents(document.querySelector('#bibtex'));
    const selection = window.getSelection();
    selection.removeAllRanges(); selection.addRange(range);
    status.textContent = 'Citation selected. Press Ctrl+C (or Command+C) to copy.';
  }
});

// This changes the scheduled equality tolerance in Eq. (9), not a simulated
// neural-network residual. No measured optimization trajectory is synthesized.
const slider = document.querySelector('#lambda');
const play = document.querySelector('#play');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let timer = null;
document.querySelector('.schedule-controls').hidden = false;
function updateSchedule() {
  const lambda = Number(slider.value) / 20;
  const halfWidth = 330 * (1 - lambda);
  const band = document.querySelector('#tolerance-band');
  band.setAttribute('x', String(560 - halfWidth));
  band.setAttribute('width', String(halfWidth * 2));
  for (const [selector, x] of [['#band-left',560-halfWidth],['#band-right',560+halfWidth]]) {
    const line = document.querySelector(selector);
    line.setAttribute('x1', String(x)); line.setAttribute('x2', String(x));
  }
  document.querySelector('#lambda-value').value = lambda.toFixed(2);
  document.querySelector('#epsilon-value').value = (0.01 * (1 - lambda)).toFixed(4);
  slider.setAttribute('aria-valuetext', `Lambda ${lambda.toFixed(2)}; tolerance plus or minus ${(0.01*(1-lambda)).toFixed(4)}`);
  document.querySelector('#tolerance-desc').textContent = `At lambda ${lambda.toFixed(2)}, the scheduled equality tolerance is plus or minus ${(0.01*(1-lambda)).toFixed(4)}. This is an illustration, not measured training data.`;
}
function stopSchedule() {
  if (timer !== null) clearInterval(timer);
  timer = null;
  play.textContent = reducedMotion.matches ? 'Advance one step' : 'Play schedule';
  play.setAttribute('aria-pressed', 'false');
}
function advanceSchedule() {
  slider.value = String(Number(slider.value) >= 20 ? 0 : Number(slider.value) + 1);
  updateSchedule();
}
slider.addEventListener('input', () => {stopSchedule(); updateSchedule();});
play.addEventListener('click', () => {
  if (reducedMotion.matches) {advanceSchedule(); return;}
  if (timer !== null) {stopSchedule(); return;}
  if (Number(slider.value) === 20) {slider.value = '0'; updateSchedule();}
  play.textContent = 'Pause schedule'; play.setAttribute('aria-pressed','true');
  timer = setInterval(() => {
    advanceSchedule();
    if (Number(slider.value) === 20) stopSchedule();
  }, 650);
});
reducedMotion.addEventListener('change', stopSchedule);
document.addEventListener('visibilitychange', () => {if (document.hidden) stopSchedule();});
stopSchedule(); updateSchedule();
