# Genera las miniaturas 1280x720 de cada charla con la marca FAIO de Pacto Pyme.
# Uso: python3 gen_thumbs.py <alianzas-site>  → mineconomia/recursos/<slug>/miniatura.jpg
import os, subprocess, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(sys.argv[1])
FOTOS = os.path.join(HERE, 'fotos')
TMP = os.path.join(HERE, 'thumb_build'); os.makedirs(TMP, exist_ok=True)
LOGO = 'file://' + os.path.join(SITE, 'assets', 'pactopyme-imagotipo-harina.svg')

THUMBS = [
  dict(slug='estrategias-ia', foto='gonzalo', titulo='IA: estrategias <em>transformadoras</em> para negocios',
       nombre='Gonzalo Sánchez', cargo='Director de Tecnología e Innovación, Desafío Latam', dur='77 min'),
  dict(slug='tareas-repetitivas', foto='andres', titulo='El fin de las <em>tareas repetitivas</em>',
       nombre='Andrés Gallardo', cargo='CEO, Desafío Latam', dur='78 min'),
  dict(slug='primer-agente-ia', foto='zurisadai', titulo='Aprende a crear tu primer <em>agente de IA</em>',
       nombre='Zurisadai Velázquez', cargo='Gerente Sr. de Modelos de Riesgos e IA', dur='72 min'),
  dict(slug='automatiza', foto='gonzalo', titulo='Más productividad, menos esfuerzo: <em>automatiza</em>',
       nombre='Gonzalo Sánchez', cargo='Director de Tecnología e Innovación, Desafío Latam', dur='63 min'),
]

CSS = '''
*{box-sizing:border-box;margin:0}
html,body{width:1280px;height:720px;overflow:hidden}
body{font-family:"Inter",Helvetica,Arial,sans-serif;background:#233435;color:#F1F1F1;position:relative}
.brillo{position:absolute;inset:0;background:radial-gradient(620px 520px at 1010px 470px,#385151 0%,rgba(56,81,81,0) 70%),radial-gradient(420px 300px at 1180px 120px,rgba(204,108,81,.22) 0%,rgba(204,108,81,0) 70%)}
.disco{position:absolute;right:86px;top:118px;width:470px;height:470px;border-radius:50%;background:#385151;overflow:hidden;box-shadow:0 0 0 14px rgba(206,217,217,.10)}
.foto{position:absolute;left:50%;bottom:0;transform:translateX(-50%);width:430px;height:auto}
.texto{position:absolute;left:84px;top:78px;width:620px;height:564px;display:flex;flex-direction:column;justify-content:flex-end}
.logo{position:fixed;left:56px;top:46px;height:96px;width:auto}
.eyebrow{font-weight:700;font-size:20px;letter-spacing:.2em;text-transform:uppercase;color:#CED9D9;margin-bottom:22px}
h1{font-weight:500;font-size:64px;line-height:1.04;letter-spacing:-.025em;margin-bottom:34px}
h1 em{font-style:normal;color:#CC6C51}
.pie{display:flex;align-items:center;gap:22px}
.dur{background:#CC6C51;color:#181D1A;font-weight:700;font-size:22px;padding:12px 24px;border-radius:999px;white-space:nowrap}
.quien b{display:block;font-weight:700;font-size:26px;color:#F1F1F1}
.quien span{display:block;font-weight:400;font-size:19px;color:#CED9D9;margin-top:2px}
'''

def html(t, foto):
    return f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<div class="brillo"></div><div class="disco"><img class="foto" src="file://{foto}" alt=""></div>
<div class="texto"><img class="logo" src="{LOGO}" alt=""><p class="eyebrow">Charla grabada</p><h1>{t["titulo"]}</h1>
<div class="pie"><span class="dur">▶ {t["dur"]}</span><p class="quien"><b>{t["nombre"]}</b><span>{t["cargo"]}</span></p></div></div>
</body></html>'''

for t in THUMBS:
    # foto recortada: se ajusta al alto del lienzo y se apoya en el borde inferior
    src = Image.open(os.path.join(FOTOS, t['foto'] + '-ok.png'))
    bbox = src.getchannel('A').point(lambda v: 255 if v > 20 else 0).getbbox()
    src = src.crop(bbox)
    foto = os.path.join(TMP, t['foto'] + '-crop.png'); src.save(foto)
    h = os.path.join(TMP, t['slug'] + '.html'); open(h, 'w', encoding='utf-8').write(html(t, foto))
    png = os.path.join(TMP, t['slug'] + '.png')
    subprocess.run(['google-chrome', '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                    '--window-size=1280,720', '--virtual-time-budget=6000', f'--screenshot={png}', 'file://' + h],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    out = os.path.join(SITE, 'mineconomia', 'recursos', t['slug'], 'miniatura.jpg')
    Image.open(png).convert('RGB').save(out, quality=86, optimize=True, progressive=True)
    print('miniatura ok', t['slug'], os.path.getsize(out) // 1024, 'KB')
