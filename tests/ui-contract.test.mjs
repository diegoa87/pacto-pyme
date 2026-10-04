import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const page = await readFile(new URL('../recursos/agentes-ia-para-pymes/index.html', import.meta.url), 'utf8');
const home = await readFile(new URL('../index.html', import.meta.url), 'utf8');

const productionLogo = /<svg[^>]*viewBox="0 0 100 100"[\s\S]*?<span class="wm">Pacto<span>Pyme<\/span><\/span>/;

test('oculta de forma efectiva los controles con atributo hidden', () => {
  assert.match(page, /\[hidden\]\s*\{\s*display\s*:\s*none\s*!important\s*;?\s*\}/);
});

test('usa en el diagnóstico el mismo logo de la portada de Pacto Pyme', () => {
  assert.match(home, productionLogo);
  assert.match(page, productionLogo);
  assert.doesNotMatch(page, /pactopyme-horizontal-color\.svg/);
});

test('la portada enlaza la sección pública de recursos', () => {
  assert.match(home, /href="\/recursos\/?"/);
});

test('usa coral accesible para botones y tarjetas activas', () => {
  assert.match(home, /--coral-action:#BE4A31/);
  assert.match(home, /\.btn\{background:var\(--coral-action\)/);
  assert.match(home, /\.cap--live\{background:var\(--coral-action\)/);
  assert.match(home, /\.cap--live\{color:#fff\}/);
  assert.match(home, /\.cap--live \.n\{color:#fff\}/);
  assert.match(home, /\.eyebrow\{[^}]*color:var\(--coral-hover\)/);
});

test('el catálogo de recursos enlaza el diagnóstico de agentes de IA', async () => {
  const resources = await readFile(new URL('../recursos/index.html', import.meta.url), 'utf8');
  assert.match(resources, productionLogo);
  assert.match(resources, /href="\/recursos\/agentes-ia-para-pymes\/?"/);
});
