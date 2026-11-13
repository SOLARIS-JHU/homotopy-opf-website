import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(fileURLToPath(new URL('..', import.meta.url)), 'dist');
if (!fs.existsSync(path.join(root,'index.html'))) throw new Error('Run node scripts/build.mjs before previewing.');
const port = Number(process.env.PORT || 4173);
const base = '/homotopy-opf-website/';
const mime = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.woff2':'font/woff2','.woff':'font/woff','.json':'application/json','.bib':'text/plain; charset=utf-8'};
http.createServer((req,res) => {
  let pathname;
  try { pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname); } catch { res.writeHead(400).end(); return; }
  if (pathname === '/') { res.writeHead(302,{Location:base}).end(); return; }
  if (!pathname.startsWith(base)) { res.writeHead(404).end('Not found'); return; }
  const relative = pathname.slice(base.length) || 'index.html';
  const file = path.resolve(root, relative);
  if (!file.startsWith(root + path.sep) || !fs.existsSync(file) || !fs.statSync(file).isFile()) { res.writeHead(404).end('Not found'); return; }
  res.writeHead(200, {'Content-Type':mime[path.extname(file)] || 'application/octet-stream','Cache-Control':'no-store'});
  fs.createReadStream(file).pipe(res);
}).listen(port,'127.0.0.1',()=>console.log(`Local: http://127.0.0.1:${port}${base}`));
