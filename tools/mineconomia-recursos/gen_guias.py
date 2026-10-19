# Genera la página de cada charla en alianzas-site/mineconomia/recursos/<slug>/index.html
# La página muestra solo: miniatura con el video, resumen y descarga de la guía en PDF.
import html, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guias_data import GUIAS, url, seg

OUT = sys.argv[1]
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'guias.css'), encoding='utf-8').read()
import hashlib
CSS_V = hashlib.sha1(CSS.encode()).hexdigest()[:8]  # rompe la caché cuando cambia el CSS

def e(s): return html.escape(s, quote=True)

LOGO = '<img src="/assets/pactopyme-imagotipo-carbon.svg" alt="Pacto Pyme" width="72" height="34">'
LOGO_CLARO = '<img src="/assets/pactopyme-imagotipo-harina.svg" alt="Pacto Pyme" width="72" height="34">'

def mini(slug):
    # miniatura con versión según su contenido, para que el navegador no muestre una vieja
    f = os.path.join(OUT, 'mineconomia', 'recursos', slug, 'miniatura.jpg')
    v = hashlib.sha1(open(f, 'rb').read()).hexdigest()[:8] if os.path.exists(f) else '0'
    return f'/mineconomia/recursos/{slug}/miniatura.jpg?v={v}'

def pdf_name(g): return f'guia-{g["slug"]}.pdf'

# Al tocar la miniatura se carga el reproductor (youtube-nocookie no deja cookies hasta reproducir)
NAV_JS = '''<script>
/* La píldora pasa a Pizarra cuando queda encima de una sección oscura (igual que en pactopyme.cl) */
(function(){
  var nav=document.querySelector('.nav'); if(!nav) return;
  var oscuras=[].slice.call(document.querySelectorAll('.hero-oscuro,footer'));
  function revisar(){
    var y=nav.getBoundingClientRect().top+38;
    nav.classList.toggle('is-dark',oscuras.some(function(s){var r=s.getBoundingClientRect();return r.top<=y&&r.bottom>=y;}));
  }
  addEventListener('scroll',revisar,{passive:true}); addEventListener('resize',revisar); revisar();
})();
</script>'''

JS = '''<script>
(function(){
  function play(b,t){var f=document.createElement('iframe');
    f.src='https://www.youtube-nocookie.com/embed/'+b.dataset.vid+'?autoplay=1&rel=0'+(t?'&start='+t:'');
    f.title=b.dataset.titulo;f.allow='autoplay; encrypted-media; picture-in-picture; fullscreen';f.allowFullscreen=true;
    var w=document.createElement('div');w.className='video';w.id='video';w.dataset.vid=b.dataset.vid;w.dataset.titulo=b.dataset.titulo;w.appendChild(f);b.replaceWith(w);return w;}
  var v=document.querySelector('a.video[data-vid]');
  if(v)v.addEventListener('click',function(ev){ev.preventDefault();play(v,0);});
  document.querySelectorAll('[data-t]').forEach(function(a){a.addEventListener('click',function(ev){
    ev.preventDefault();var cur=document.getElementById('video');var w=play(cur,a.dataset.t);
    w.scrollIntoView({behavior:'smooth',block:'center'});});});
})();
</script>'''

def pagina(g):
    nombre, _, cargo = g['quien'].partition(', ')
    cargo = cargo[:1].upper() + cargo[1:]
    otras = ''.join(
        f'<li><a href="/mineconomia/recursos/{o["slug"]}/"><img src="{mini(o["slug"])}" alt="" width="640" height="360" loading="lazy"><span>{e(o["titulo"])}</span></a></li>'
        for o in GUIAS if o['slug'] != g['slug'])
    return f'''<!doctype html>
<html lang="es-CL">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>{e(g["titulo"])} · Charla grabada | Pacto Pyme</title>
  <meta name="description" content="{e(g["resumen"])}">
  <meta name="robots" content="noindex">
  <meta name="theme-color" content="#233435">
  <meta property="og:title" content="{e(g["titulo"])}">
  <meta property="og:description" content="{e(g["resumen"])}">
  <meta property="og:image" content="https://alianzas.pactopyme.cl/mineconomia/recursos/{g["slug"]}/miniatura.jpg">
  <link rel="icon" type="image/svg+xml" href="/assets/pactopyme-faio-isotipo-greda.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/mineconomia/recursos/guias.css?v={CSS_V}">
</head>
<body>
<nav class="nav">
  <div class="nav-in">
    <a href="https://pactopyme.cl/" aria-label="Pacto Pyme, inicio"><img class="logo logo-oscuro" src="/assets/pactopyme-imagotipo-carbon.svg" alt="Pacto Pyme" width="106" height="50"><img class="logo logo-claro" src="/assets/pactopyme-imagotipo-harina.svg" alt="" aria-hidden="true" width="106" height="50"></a>
    <div class="nav-links">
      <a href="https://pactopyme.cl/#programas">Programas</a>
      <a href="https://pactopyme.cl/empresas">Para empresas</a>
      <a href="https://pactopyme.cl/semanadelapyme">Semana de la Pyme</a>
    </div>
    <a class="m-btn" href="https://pactopyme.cl/horeca">Ver la beca</a>
  </div>
</nav>
<main>
  <section class="hero hero-oscuro"><div class="shell hero-grid">
    <div class="hero-texto"><p class="eyebrow">Charla grabada · {e(g["dur"])}</p>
    <h1>{e(g["titulo"])}</h1>
    <p class="quien">{e(g["quien"])}</p></div>
    <a class="video" href="{e(url(g["vid"]))}" target="_blank" rel="noopener" data-vid="{g["vid"]}" data-titulo="{e(g["titulo"])}" aria-label="Reproducir la charla {e(g["titulo"])}">
      <img src="{mini(g["slug"])}" alt="" width="1280" height="720"><span class="play" aria-hidden="true"></span>
    </a>
  </div></section>
  <div class="shell cuerpo">
    <dl class="datos">
      <div><dt>Duración</dt><dd>{e(g["dur"])}</dd></div>
      <div><dt>Formato</dt><dd>Charla grabada, online</dd></div>
      <div><dt>Expositor</dt><dd>{e(nombre)}<small>{e(cargo)}</small></dd></div>
      <div><dt>Costo</dt><dd>Gratis</dd></div>
    </dl>
    <div class="curso">
      <section class="sobre-wrap"><h2>Sobre la charla</h2><p class="sobre">{e(g["resumen"])}</p></section>
      <aside class="ficha-guia" aria-label="Guía descargable"><p class="eyebrow">Guía descargable</p>
        <p>Paso a paso con ejemplos para tu negocio, preguntas del público y plantillas para completar.</p>
        <a class="btn" href="/mineconomia/recursos/{g["slug"]}/{pdf_name(g)}" download>Descargar PDF ↓</a>
        <a class="ficha-yt" href="{e(url(g["vid"]))}" target="_blank" rel="noopener">Ver en YouTube ↗</a></aside>
    </div>
  </div>
  <div class="shell otras-wrap"><section class="bloque otras"><h2>Otras charlas</h2><ul>{otras}</ul></section></div>
</main>
<footer><div class="shell footer-in"><a class="brand" href="https://pactopyme.cl/" aria-label="Pacto Pyme, inicio">{LOGO_CLARO}</a><span class="firma">Si las pymes crecen, Chile crece.</span><nav class="footer-links" aria-label="Enlaces"><a href="https://pactopyme.cl/">Sitio principal</a><a href="https://pactopyme.cl/politica-de-privacidad.html">Privacidad</a></nav></div></footer>
{JS}
</body>
</html>
'''

if __name__ == '__main__':
    base = os.path.join(OUT, 'mineconomia', 'recursos')
    os.makedirs(base, exist_ok=True)
    open(os.path.join(base, 'guias.css'), 'w', encoding='utf-8').write(CSS)
    for g in GUIAS:
        d = os.path.join(base, g['slug']); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(pagina(g))
        print('web ok', g['slug'])
