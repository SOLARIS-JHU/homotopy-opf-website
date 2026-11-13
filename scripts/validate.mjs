import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(fileURLToPath(new URL('..', import.meta.url)));
const errors = [];
const fail = message => errors.push(message);
const exists = p => fs.existsSync(path.join(root, p));
const read = p => fs.readFileSync(path.join(root, p), 'utf8');
const attrs = tag => Object.fromEntries([...tag.matchAll(/([\w:-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g)].map(m => [m[1].toLowerCase(), m[2] ?? m[3]]));
const required = ['index.html', 'style.css', 'main.js', 'LICENSE', 'NOTICE'];
for (const name of required) if (!exists(name)) fail(`Missing required file: ${name}`);

function walk(directory) {
  if (!fs.existsSync(directory)) return [];
  return fs.readdirSync(directory, {withFileTypes:true}).flatMap(entry => {
    const file = path.join(directory, entry.name);
    if (entry.isSymbolicLink()) { fail(`Symlinks are not deployable: ${file}`); return []; }
    return entry.isDirectory() ? walk(file) : [file];
  });
}

function reference(value, from, ids) {
  if (!value || /^(?:https?:|mailto:|tel:|data:|blob:)/i.test(value)) return;
  if (/^javascript:/i.test(value)) { fail(`JavaScript URL in ${from}`); return; }
  if (value.startsWith('//') || value.startsWith('/')) {
    fail(`Use repository-relative asset paths for GitHub Pages: ${from} → ${value}`); return;
  }
  let url;
  try { url = decodeURIComponent(value.split('?')[0]); }
  catch { fail(`Malformed URL: ${from} → ${value}`); return; }
  const [file, fragment] = url.split('#');
  if (!file) {
    if (fragment && ids && !ids.has(fragment)) fail(`Missing fragment #${fragment} in ${from}`);
    return;
  }
  const resolved = path.resolve(root, path.dirname(from), file);
  if (!resolved.startsWith(root + path.sep)) { fail(`Path escapes site: ${from} → ${value}`); return; }
  if (!fs.existsSync(resolved)) fail(`Broken local reference: ${from} → ${value}`);
  if (fragment && /\.html?$/.test(file) && fs.existsSync(resolved)) {
    const target = fs.readFileSync(resolved, 'utf8');
    const targetIds = new Set([...target.matchAll(/\bid\s*=\s*["']([^"']+)["']/g)].map(m => m[1]));
    if (!targetIds.has(fragment)) fail(`Missing target fragment: ${from} → ${value}`);
  }
}

// Dependency-free well-formed XML validation for the static SVG documents.
// Handles quoted attributes, comments, processing instructions, and CDATA.
function validateSvg(file) {
  const source = fs.readFileSync(file, 'utf8');
  const clean = source.replace(/<!--[\s\S]*?-->|<\?[\s\S]*?\?>|<!\[CDATA\[[\s\S]*?\]\]>/g, '');
  const tagPattern = /<(?:"[^"]*"|'[^']*'|[^'">])*>/g;
  const stack = [];
  let topCount = 0;
  let rootTag;
  for (const match of clean.matchAll(tagPattern)) {
    const tag = match[0];
    if (/^<!DOCTYPE\b/i.test(tag)) continue;
    const name = tag.match(/^<\/?\s*([A-Za-z_][\w:.-]*)/)?.[1];
    if (!name) { fail(`Invalid XML tag in ${file}`); continue; }
    if (/^<\//.test(tag)) {
      if (stack.pop() !== name) fail(`Unbalanced SVG tag </${name}> in ${file}`);
    } else {
      if (!stack.length) { topCount++; rootTag ??= name; }
      if (!/\/\s*>$/.test(tag)) stack.push(name);
    }
  }
  if (stack.length || topCount !== 1 || rootTag !== 'svg') fail(`Malformed SVG document: ${file}`);
  if (!/\bviewBox\s*=/.test(source)) fail(`SVG needs a viewBox: ${file}`);
}

if (exists('index.html')) {
  const html = read('index.html');
  if (!/<html\b[^>]*\blang=["']en["']/i.test(html)) fail('Set the page language to English.');
  if (!/<meta\b[^>]*name=["']viewport["']/i.test(html)) fail('Missing responsive viewport metadata.');
  if ((html.match(/<h1\b/gi) || []).length !== 1) fail('The page must have exactly one h1.');
  if (!/<title>[^<]+<\/title>/i.test(html)) fail('Missing page title.');
  if (!/<meta\b[^>]*name=["']description["'][^>]*content=["'][^"']+/i.test(html)) fail('Missing page description.');
  const ids = new Set();
  const tags = [...html.matchAll(/<[^!][^>]*>/g)].map(m => m[0]);
  for (const tag of tags) {
    const a = attrs(tag);
    if (a.id) { if (ids.has(a.id)) fail(`Duplicate id: ${a.id}`); ids.add(a.id); }
  }
  for (const tag of tags) {
    const a = attrs(tag);
    if (/^<img\b/i.test(tag) && !Object.hasOwn(a, 'alt')) fail(`Image has no alt attribute: ${a.src ?? tag}`);
    if (a.target === '_blank' && !/noopener/.test(a.rel || '')) fail(`External tab link needs rel=noopener: ${a.href}`);
    for (const key of ['src','href','poster']) if (a[key]) reference(a[key], 'index.html', ids);
    if (a.srcset && !a.srcset.startsWith('data:')) for (const item of a.srcset.split(',')) reference(item.trim().split(/\s+/)[0], 'index.html', ids);
  }
  for (const match of html.matchAll(/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)) {
    try { JSON.parse(match[1]); } catch (error) { fail(`Invalid scholarly JSON-LD: ${error.message}`); }
  }
}

const assets = walk(path.join(root, 'assets'));
const cssFiles = [path.join(root, 'style.css'), ...assets.filter(f => f.endsWith('.css'))].filter(fs.existsSync);
for (const file of cssFiles) {
  const from = path.relative(root, file);
  for (const match of fs.readFileSync(file, 'utf8').matchAll(/url\(\s*["']?([^"')]+)["']?\s*\)/g)) reference(match[1].trim(), from);
}
for (const file of assets.filter(f => f.endsWith('.svg'))) validateSvg(file);
for (const file of assets.filter(f => f.endsWith('.json'))) {
  try { JSON.parse(fs.readFileSync(file, 'utf8')); } catch (error) { fail(`Invalid asset JSON ${file}: ${error.message}`); }
}
if (errors.length) {
  console.error(errors.map(e => `ERROR: ${e}`).join('\n'));
  process.exitCode = 1;
} else {
  console.log(`Static validation passed: relative resources, anchors, metadata, image alternatives, and ${assets.filter(f=>f.endsWith('.svg')).length} SVG documents.`);
}
