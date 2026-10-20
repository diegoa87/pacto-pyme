# Recorta a cada expositor desde la miniatura oficial y le quita el fondo
import sys
from PIL import Image, ImageDraw
from rembg import remove, new_session
ses = new_session('u2net_human_seg')
# (archivo, caja del círculo en la miniatura 1280x720, salida)
CASOS = [
  ('yt-X90ulUkIi-E.jpg', (120, 195, 450, 525), 'gonzalo'),
  ('yt-q6EYVwyB1c4.jpg', (110, 150, 400, 445), 'andres'),
  ('yt-CVFFHd0Kazk.jpg', (118, 170, 393, 445), 'zurisadai'),
]
for f, box, out in CASOS:
    im = Image.open(f).convert('RGB').crop(box)
    im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    cut = remove(im, session=ses, post_process_mask=True)
    # el recorte de la miniatura ya viene con máscara circular: se mantiene solo lo de adentro
    m = Image.new('L', cut.size, 0); ImageDraw.Draw(m).ellipse((6, 6, cut.width - 6, cut.height - 6), fill=255)
    a = Image.composite(cut.getchannel('A'), Image.new('L', cut.size, 0), m)
    cut.putalpha(a)
    cut.save(out + '.png'); print(out, cut.size)
