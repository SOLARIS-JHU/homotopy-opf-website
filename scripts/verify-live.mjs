import fs from 'node:fs/promises';
import {setTimeout as delay} from 'node:timers/promises';

const base = 'https://solaris-jhu.github.io/homotopy-opf-website/';
const files = [
  'index.html', 'style.css', 'main.js',
  'assets/solaris-acopf.svg', 'assets/solaris-acopf-animation.js',
  'assets/logos/buffalo.svg', 'assets/logos/cmu-wordmark.svg'
];
const expected = new Map(await Promise.all(files.map(async file => [file, await fs.readFile(file)])));
let failures = [];
for (let attempt = 1; attempt <= 8; attempt++) {
  failures = (await Promise.all(files.map(async file => {
    try {
      const url = new URL(file, base);
      url.searchParams.set('revision', process.env.GITHUB_SHA || 'current');
      url.searchParams.set('check', String(attempt));
      const response = await fetch(url, {signal: AbortSignal.timeout(15000), cache: 'no-store'});
      if (!response.ok) return file + ': HTTP ' + response.status;
      const actual = Buffer.from(await response.arrayBuffer());
      if (!actual.equals(expected.get(file))) return file + ': published bytes differ from committed source';
      return null;
    } catch (error) { return file + ': ' + error.message; }
  }))).filter(Boolean);
  if (!failures.length) break;
  console.log('Waiting for Pages propagation, attempt ' + attempt + ': ' + failures.join('; '));
  if (attempt < 8) await delay(5000);
}
if (failures.length) throw new Error(failures.join('\n'));
console.log('Published page and all six updated runtime assets match the deployed revision.');
