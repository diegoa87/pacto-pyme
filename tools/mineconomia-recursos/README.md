# Recursos de /mineconomia

Generadores de las páginas de recursos (`alianzas-site/mineconomia/recursos/`), sus guías en PDF y sus miniaturas.
Viven fuera de `alianzas-site/` para que Cloudflare Pages no los publique.

| Archivo | Qué hace |
|---|---|
| `guias_data.py` | Contenido de las 4 guías. Las versiones extendidas están en `expand/` y los ejemplos "Hazlo tú" en `hazlo/` |
| `gen_guias.py` | Páginas web de cada recurso (`index.html` + `guias.css`) |
| `gen_pdf.py` | Guías en PDF (Chrome headless) |
| `gen_thumbs.py` | Miniaturas 1280x720 con la marca FAIO (fotos recortadas en `fotos/`) |
| `recortar.py` | Recorta a los expositores desde las miniaturas de YouTube (requiere `rembg`) |
| `setup_chequeo_digital_crm.rb` | Crea en el CRM el form "Registro pymes — Chequeo Digital" (ya aplicado el 19-oct-2026) |

Desde la raíz del repo:

```sh
python3 tools/mineconomia-recursos/gen_thumbs.py alianzas-site
python3 tools/mineconomia-recursos/gen_guias.py alianzas-site
python3 tools/mineconomia-recursos/gen_pdf.py alianzas-site
```

El contenido sale de las transcripciones de cada charla. Los ejemplos "Hazlo tú" se revisaron contra la
documentación oficial de cada herramienta en octubre de 2026: las pantallas cambian, conviene revisarlos cada cierto tiempo.
