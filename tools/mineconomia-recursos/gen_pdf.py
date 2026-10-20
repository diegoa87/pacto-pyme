# Genera los PDF descargables de las mini guías (marca FAIO) con Chrome headless.
# Uso: python3 gen_pdf.py <alianzas-site>   → escribe mineconomia/recursos/<slug>/guia-<slug>.pdf
import html, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from guias_data import GUIAS, url

SITE = os.path.abspath(sys.argv[1])
LOGO_H = 'file://' + os.path.join(SITE, 'assets', 'pactopyme-imagotipo-harina.svg')
LOGO_C = 'file://' + os.path.join(SITE, 'assets', 'pactopyme-imagotipo-carbon.svg')
TMP = os.path.join(HERE, 'pdf_build'); os.makedirs(TMP, exist_ok=True)

def e(s): return html.escape(s, quote=True)

CSS = '''
@page{size:A4;margin:0}
:root{--pizarra:#233435;--botella:#385151;--loza:#CED9D9;--loza-60:#E2E8E8;--greda:#CC6C51;--harina:#F1F1F1;--carbon:#181D1A}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{margin:0;background:var(--harina)}
body{padding:14mm 16mm 18mm;-webkit-box-decoration-break:clone;box-decoration-break:clone}
body{font:400 10.5pt/1.5 "Inter",Helvetica,Arial,sans-serif;color:var(--carbon)}
h1,h2,h3,p{margin:0}a{color:inherit}
.portada{background:var(--pizarra);color:var(--harina);border-radius:6mm;padding:12mm 12mm 11mm;margin-bottom:9mm}
.portada img{height:13mm;display:block;margin-bottom:12mm}
.eyebrow{font-weight:700;font-size:8pt;letter-spacing:.2em;text-transform:uppercase;color:var(--loza);margin-bottom:3mm}
.portada h1{font-weight:500;font-size:27pt;line-height:1.08;letter-spacing:-.02em;margin-bottom:4mm}
.meta{font-weight:500;font-size:9.5pt;color:var(--loza);margin-bottom:6mm}
.portada .lede{font-size:11.5pt;line-height:1.5;color:var(--harina);margin-bottom:7mm}
.ver{display:inline-block;background:var(--greda);color:var(--carbon);font-weight:700;font-size:10pt;padding:2.6mm 5mm;border-radius:99px;text-decoration:none}
.ver span{font-weight:500}
h2{font-weight:600;font-size:15pt;letter-spacing:-.01em;color:var(--pizarra);margin:0 0 4.5mm}
h2{break-after:avoid;break-inside:avoid}h2::after{content:"";display:block;height:45mm;margin-bottom:-45mm}
section{margin-bottom:8mm}
.ideas{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm}
.idea{background:var(--loza-60);border-radius:3.5mm;padding:4mm 4.5mm;break-inside:avoid}
.idea h3{font-weight:600;font-size:10.5pt;color:var(--pizarra);margin-bottom:1.2mm}.idea p{color:var(--botella);font-size:9.5pt}
.pasos{list-style:none;margin:0;padding:0;counter-reset:p}
.pasos>li{counter-increment:p;position:relative;padding:3.6mm 0 3.6mm 14mm;border-top:.3mm solid var(--loza);break-inside:avoid}
.pasos>li:last-child{border-bottom:.3mm solid var(--loza)}
.pasos>li::before{content:counter(p);position:absolute;left:0;top:3.4mm;width:9mm;height:9mm;border-radius:50%;background:var(--greda);color:var(--carbon);font-weight:700;font-size:11pt;display:grid;place-items:center}
.pasos h3{font-weight:600;font-size:11pt;color:var(--pizarra);margin-bottom:1mm}.pasos p{color:var(--botella)}
.pasos ul{margin:1.6mm 0 0;padding-left:4.5mm;color:var(--botella)}.pasos ul li{margin-bottom:.8mm}
.check ul{list-style:none;padding-left:0}.check ul li::before{content:"";display:inline-block;width:3mm;height:3mm;border:.35mm solid var(--botella);border-radius:.6mm;margin-right:2.2mm;vertical-align:-.4mm}
.ejemplo{background:var(--botella);color:var(--harina);border-radius:4mm;padding:6mm 7mm;break-inside:avoid}
.ejemplo h2{color:var(--harina);font-size:13pt}.ejemplo ul{margin:0;padding-left:4.5mm;color:var(--loza)}.ejemplo li{margin-bottom:1.4mm}.ejemplo li::marker{color:var(--greda)}
.plantilla{break-before:page}
.plantilla .sub{color:var(--botella);margin:-2.5mm 0 5mm}
table{width:100%;border-collapse:collapse;font-size:9.5pt}
th{background:var(--pizarra);color:var(--harina);font-weight:600;text-align:left;padding:2.6mm 3mm}
td{border-bottom:.3mm solid var(--loza);height:10.5mm;padding:0 3mm;color:var(--botella)}
td.n{width:8mm;font-weight:700;color:var(--pizarra)}
.matriz{display:grid;grid-template-columns:7mm 1fr 1fr;grid-template-rows:1fr 1fr 7mm;gap:2mm;height:92mm;margin-top:7mm;break-inside:avoid}
.matriz .cel{border-radius:3mm;padding:3mm 3.5mm;font-size:8.5pt;font-weight:600;color:var(--pizarra);background:var(--loza-60)}
.matriz .cel.top{background:var(--greda);color:var(--carbon)}
.matriz .cel small{display:block;font-weight:400;color:inherit;opacity:.85}
.eje{font-size:8pt;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--botella);display:flex;align-items:center;justify-content:center}
.eje.y{writing-mode:vertical-rl;transform:rotate(180deg);grid-row:1/3}
.eje.x{grid-column:2/4}
.minutos{list-style:none;margin:0;padding:0;columns:2;column-gap:7mm}
.minutos li{break-inside:avoid;display:flex;gap:3mm;padding:1.6mm 0;border-bottom:.3mm solid var(--loza);font-size:9.5pt}
.minutos a{text-decoration:none;display:flex;gap:3mm}.minutos .t{flex:0 0 12mm;font-weight:700;color:var(--pizarra);font-variant-numeric:tabular-nums}
.nota{color:var(--botella);font-size:9pt;margin:-2.5mm 0 3.5mm}
.aviso{margin-top:3mm;background:var(--loza-60);border-radius:3mm;padding:3.5mm 4.5mm;color:var(--botella);font-size:9.5pt}
.cierre{display:flex;align-items:center;justify-content:space-between;border-top:.3mm solid var(--loza);padding-top:5mm;margin-top:4mm;break-inside:avoid}
.cierre img{height:10mm}.cierre p{font-weight:600;color:var(--pizarra)}
.pie{position:fixed;bottom:0;left:0;right:0;height:12mm;padding:0 16mm;display:flex;align-items:center;justify-content:space-between;font-size:7.5pt;font-weight:600;color:var(--botella);letter-spacing:.12em;background:var(--harina)}

.contexto p{font-size:11pt;line-height:1.6;color:var(--carbon);margin-bottom:3mm}
.errores{margin:0;padding:0;list-style:none}.errores li{position:relative;padding:2.4mm 0 2.4mm 8mm;border-bottom:.3mm solid var(--loza);color:var(--botella);break-inside:avoid}
.errores li::before{content:"";position:absolute;left:0;top:3.6mm;width:4mm;height:.9mm;background:var(--greda);border-radius:1mm}
.preguntas{margin:0;padding:0;list-style:none;display:grid;gap:3mm}.preguntas li{background:var(--loza-60);border-radius:3.5mm;padding:4mm 5mm;break-inside:avoid}
.preguntas h3{font-weight:600;font-size:10.5pt;color:var(--pizarra);margin-bottom:1.2mm}.preguntas p{color:var(--botella);font-size:9.8pt}.preguntas a{color:var(--pizarra);font-weight:600;text-decoration:none}
.glosario{display:grid;grid-template-columns:1fr 1fr;gap:3mm 6mm;margin:0}.glosario div{break-inside:avoid;border-top:.6mm solid var(--pizarra);padding-top:2mm}
.glosario dt{font-weight:700;color:var(--pizarra);margin-bottom:.8mm}.glosario dd{margin:0;color:var(--botella);font-size:9.5pt}

.hazlo{margin-bottom:8mm}.hz-cab{break-inside:avoid}
.hz-cab{background:var(--pizarra);color:var(--harina);border-radius:5mm;padding:8mm 9mm;margin-bottom:6mm}
.hz-cab .eyebrow{color:var(--greda);margin-bottom:2mm}.hz-cab h2{color:var(--harina);font-size:18pt;margin-bottom:3mm}.hz-cab p{color:var(--loza);font-size:10.5pt}
.hz-nec{background:var(--loza-60);border-radius:4mm;padding:5mm 6mm;margin-bottom:6mm;break-inside:avoid}
.hz-nec h3,.hz-prueba h3,.hz-err h3{font-weight:600;font-size:11pt;color:var(--pizarra);margin-bottom:2mm}
.hz-nec ul{margin:0;padding-left:4.5mm;color:var(--botella)}.hz-nec li{margin-bottom:1mm}
.hz-pasos>li::before{background:var(--pizarra);color:var(--harina)}
.hz-prueba{border:.4mm solid var(--greda);border-radius:4mm;padding:5mm 6mm;margin:6mm 0;break-inside:avoid}.hz-prueba p{color:var(--botella)}
.hz-err{break-inside:avoid}
.hz-fuentes{margin-top:5mm;font-size:7.5pt;color:var(--botella);word-break:break-all}
'''

def plantilla(g):
    if g['plantilla'] == 'tareas':
        filas = ''.join(f'<tr><td class="n">{i}</td><td></td><td></td><td></td></tr>' for i in range(1, 9))
        return f'''<section class="plantilla"><h2>Para completar: tus tareas repetitivas</h2><p class="sub">Paso 1 y 2. Anota tus tareas y luego ubícalas en la matriz.</p>
<table><tr><th></th><th>Tarea que repito</th><th style="width:30mm">Horas por semana</th><th style="width:38mm">Impacto / esfuerzo</th></tr>{filas}</table>
<div class="matriz"><div class="eje y">Más impacto</div>
<div class="cel">Mucho impacto, mucho esfuerzo<small>Planifícalas después.</small></div><div class="cel top">Mucho impacto, poco esfuerzo<small>Parte por aquí.</small></div>
<div class="cel">Poco impacto, mucho esfuerzo<small>Déjalas para el final.</small></div><div class="cel">Poco impacto, poco esfuerzo<small>Si sobra tiempo.</small></div>
<div class="eje x">Más esfuerzo · · · Menos esfuerzo</div></div></section>'''
    if g['plantilla'] == 'faq':
        filas = ''.join(f'<tr><td class="n">{i}</td><td></td><td></td></tr>' for i in range(1, 11))
        return f'''<section class="plantilla"><h2>Para completar: tus preguntas frecuentes</h2><p class="sub">Paso 1. Las diez preguntas que más te hacen y lo que respondes.</p>
<table><tr><th></th><th style="width:42%">Pregunta del cliente</th><th>Tu respuesta</th></tr>{filas}</table></section>'''
    return ''

def hazlo(g):
    h = g.get('hazlo')
    if not h: return ''
    nec = ''.join(f'<li>{e(x)}</li>' for x in h['necesitas'])
    pasos = ''.join(f'<li><h3>{e(t)}</h3><p>{e(d)}</p>' + (('<ul>' + ''.join(f'<li>{e(x)}</li>' for x in sub) + '</ul>') if sub else '') + '</li>' for t, d, sub in h['pasos'])
    err = ''.join(f'<li>{e(x)}</li>' for x in h['errores'])
    from urllib.parse import urlparse
    fu = ' · '.join(e(d) for d in dict.fromkeys(urlparse(x).netloc.replace('www.', '') for x in h['fuentes']))
    return f'''<section class="hazlo"><div class="hz-cab"><p class="eyebrow">Ejemplo real de implementación</p><h2>{e(h["titulo"])}</h2><p>{e(h["intro"])}</p></div>
<div class="hz-nec"><h3>Antes de partir necesitas</h3><ul>{nec}</ul></div>
<ol class="pasos hz-pasos">{pasos}</ol>
<div class="hz-prueba"><h3>Cómo saber que funciona</h3><p>{e(h["prueba"])}</p></div>
<div class="hz-err"><h3>Si algo falla</h3><ul class="errores">{err}</ul></div>
<p class="hz-fuentes">Pasos revisados en la documentación oficial (octubre 2026). Las pantallas pueden cambiar. Fuentes: {fu}</p></section>'''

def doc(g):
    ideas = ''.join(f'<div class="idea"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in g['ideas'])
    pasos = ''.join(
        f'<li{" class=check" if t.startswith("Calcula") else ""}><h3>{e(t)}</h3><p>{e(d)}</p>' + (('<ul>' + ''.join(f'<li>{e(x)}</li>' for x in sub) + '</ul>') if sub else '') + '</li>'
        for t, d, sub in g['pasos'])
    ej_t, ej = g['ejemplo']
    contexto = ''.join(f'<p>{e(x)}</p>' for x in g['contexto'])
    contexto = f'<section class="contexto"><h2>Por qué te sirve</h2>{contexto}</section>' if contexto else ''
    errores = ''.join(f'<li>{e(x)}</li>' for x in g['errores'])
    errores = f'<section><h2>Errores comunes</h2><ul class="errores">{errores}</ul></section>' if errores else ''
    preg = ''.join(f'<li><h3>{e(q)}</h3><p>{e(r)} <a href="{e(url(g["vid"], m))}">({m})</a></p></li>' for q, r, m in g['preguntas'])
    preg = f'<section><h2>Lo que preguntó el público</h2><ul class="preguntas">{preg}</ul></section>' if preg else ''
    glos = ''.join(f'<div><dt>{e(t)}</dt><dd>{e(d)}</dd></div>' for t, d in g['glosario'])
    glos = f'<section><h2>Palabras que vas a escuchar</h2><dl class="glosario">{glos}</dl></section>' if glos else ''
    mins = ''.join(f'<li><a href="{e(url(g["vid"], t))}"><span class="t">{t}</span><span>{e(d)}</span></a></li>' for t, d in g['minutos'])
    return f'''<!doctype html><html lang="es-CL"><head><meta charset="utf-8"><title>Guía · {e(g["titulo"])} · Pacto Pyme</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<div class="pie"><span>PACTO PYME · GUÍA DE LA CHARLA</span><span>pactopyme.cl</span></div>
<div class="portada"><img src="{LOGO_H}" alt="Pacto Pyme"><p class="eyebrow">Guía de la charla</p><h1>{e(g["titulo"])}</h1>
<p class="meta">{e(g["quien"])} · {e(g["dur"])}</p><p class="lede">{e(g["resumen"])}</p>
<a class="ver" href="{e(url(g["vid"]))}">Ver la charla <span>· youtube.com/watch?v={g["vid"]}</span></a></div>
{contexto}
<section><h2>Ideas para llevar</h2><div class="ideas">{ideas}</div></section>
<section><h2>{e(g["pasos_titulo"])}</h2><ol class="pasos">{pasos}</ol></section>
<section class="ejemplo"><h2>{e(ej_t)}</h2><ul>{"".join(f"<li>{e(x)}</li>" for x in ej)}</ul></section>
{hazlo(g)}
{errores}
{preg}
{glos}
<section><h2>Mira estos minutos</h2><p class="nota">Toca cada minuto para abrir el video en ese punto. Son aproximados.</p><ul class="minutos">{mins}</ul></section>
<section><h2>Puedes saltarte</h2><p>{e(g["saltar"])}</p><p class="aviso">{e(g["aviso"])}</p></section>
{plantilla(g)}
<div class="cierre"><img src="{LOGO_C}" alt="Pacto Pyme"><p>Si las pymes crecen, Chile crece.</p></div>
</body></html>'''

for g in GUIAS:
    src = os.path.join(TMP, g['slug'] + '.html')
    open(src, 'w', encoding='utf-8').write(doc(g))
    out = os.path.join(SITE, 'mineconomia', 'recursos', g['slug'], f'guia-{g["slug"]}.pdf')
    subprocess.run(['google-chrome', '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--allow-file-access-from-files',
                    '--virtual-time-budget=8000', f'--print-to-pdf={out}', 'file://' + src],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('pdf ok', g['slug'], os.path.getsize(out) // 1024, 'KB')
