import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const root = path.resolve(fileURLToPath(new URL('..', import.meta.url)));
const validation = spawnSync(process.execPath, [path.join(root,'scripts','validate.mjs')], {stdio:'inherit'});
if (validation.status !== 0) process.exit(validation.status ?? 1);
const out = path.join(root, 'dist');
// Only the exact generated dist directory inside this checkout is replaced.
if (path.dirname(out) !== root || path.basename(out) !== 'dist') throw new Error('Unsafe output path');
if (fs.existsSync(out) && fs.lstatSync(out).isSymbolicLink()) throw new Error('dist must not be a symlink');
fs.rmSync(out, {recursive:true, force:true});
fs.mkdirSync(out, {recursive:true});
for (const name of ['index.html', 'style.css', 'main.js', 'assets', 'LICENSE', 'NOTICE', 'citation.bib', 'CITATION.cff', 'robots.txt', 'sitemap.xml']) {
  const source = path.join(root,name);
  if (fs.existsSync(source)) fs.cpSync(source, path.join(out,name), {recursive:true});
}
fs.writeFileSync(path.join(out, '.nojekyll'), '');
console.log('Public site staged in dist/. Internal research notes and generation scripts remain in the repository.');
