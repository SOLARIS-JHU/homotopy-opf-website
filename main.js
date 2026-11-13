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

// Reuse the approved SOLARIS v13 AC-OPF artwork and its original updater.
// This is an explanatory animation, separate from the reported experiments.
const abstractObject = document.querySelector('#solaris-abstract');
const abstractPlay = document.querySelector('#abstract-play');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let abstractSvg, animationTime = 2, previousFrame = null, lastPaint = 0;
let animationPaused = reducedMotion.matches, abstractVisible = false;

function syncAnimationControl() {
  abstractPlay.textContent = animationPaused ? 'Play animation' : 'Pause animation';
  abstractPlay.setAttribute('aria-pressed', String(!animationPaused));
}
function initializeAbstract() {
  const svg = abstractObject.contentDocument?.querySelector('svg');
  if (!svg || svg === abstractSvg) return;
  abstractSvg = svg;
  window.renderSolarisAcopf(abstractSvg, animationTime);
  document.querySelector('.abstract-controls').hidden = false;
  syncAnimationControl();
}
abstractObject.addEventListener('load', initializeAbstract);
initializeAbstract();
new IntersectionObserver(entries => {
  abstractVisible = entries.some(entry => entry.isIntersecting);
  previousFrame = null;
}, {threshold: 0.05}).observe(abstractObject);
function animateAbstract(now) {
  const dt = previousFrame === null ? 0 : Math.min((now - previousFrame) / 1000, 0.1);
  previousFrame = now;
  if (abstractSvg && !animationPaused && abstractVisible && !document.hidden) {
    animationTime += dt;
    if (now - lastPaint >= 33) {
      window.renderSolarisAcopf(abstractSvg, animationTime);
      lastPaint = now;
    }
  }
  requestAnimationFrame(animateAbstract);
}
requestAnimationFrame(animateAbstract);
abstractPlay.addEventListener('click', () => {
  animationPaused = !animationPaused;
  previousFrame = null;
  syncAnimationControl();
});
document.querySelector('#abstract-restart').addEventListener('click', () => {
  animationTime = 0;
  if (abstractSvg) window.renderSolarisAcopf(abstractSvg, animationTime);
});
reducedMotion.addEventListener('change', event => {
  if (event.matches) animationPaused = true;
  syncAnimationControl();
});
document.addEventListener('visibilitychange', () => { previousFrame = null; });
