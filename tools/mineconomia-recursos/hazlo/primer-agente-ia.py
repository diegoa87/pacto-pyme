HAZLO = dict(
  titulo="Hazlo tú: un asistente que responde las preguntas frecuentes de tu hostal",
  intro=(
    "Vas a armar, sin programar, un asistente que contesta las preguntas típicas de un hostal "
    "(horarios, precios referenciales, políticas) leyendo un documento tuyo, y que deriva a una persona lo que no sabe. "
    "Usaremos Gemini Notebook (antes se llamaba NotebookLM), de Google, porque hoy tiene plan gratuito con una cuenta de Gmail y permite compartir el asistente con un enlace. "
    "Elegimos esta opción porque los GPT personalizados de ChatGPT ya no se pueden crear con cuentas personales (solo cuentas Business, Enterprise o Edu) "
    "y las Gems de Gemini se están reemplazando por otra función desde noviembre de 2026. "
    "Con el documento listo, armarlo te toma alrededor de una hora (es una estimación, la documentación no lo indica)."
  ),
  necesitas=[
    "Una cuenta de Google (Gmail). El plan gratuito de Gemini Notebook basta para este ejemplo.",
    "Un computador con navegador. Los pasos de la ayuda oficial son para computador.",
    "Un documento con la información pública de tu negocio (Google Docs, Word o PDF).",
    "Un teléfono, WhatsApp o enlace de contacto al que el asistente pueda derivar.",
  ],
  pasos=[
    ("Escribe el documento del negocio",
     "Abre un documento nuevo en Google Docs o Word y titúlalo, por ejemplo, \"Información Hostal Los Aromos\". "
     "Escribe la información en frases simples, como se la dirías a un huésped. Pon fecha de actualización arriba, así sabes cuándo revisarlo.",
     ["Horarios: recepción, check-in, check-out, desayuno.",
      "Precios referenciales por tipo de pieza, con la frase \"precios referenciales, sujetos a disponibilidad\".",
      "Políticas: reservas, abonos, cancelación, mascotas, niños, estacionamiento.",
      "Cómo llegar y qué hay cerca.",
      "El contacto para derivar: \"Para reservas o casos especiales, escribe al WhatsApp +56 9 XXXX XXXX\"."]),
    ("Agrega una sección de preguntas frecuentes",
     "Anota las 10 a 20 preguntas que más te hacen por WhatsApp o en recepción, cada una con su respuesta corta. "
     "Escribe la pregunta tal como la hace la gente (\"¿Puedo llegar después de las 11 de la noche?\"). Así el asistente las encuentra más fácil.",
     []),
    ("Limpia los datos sensibles",
     "Antes de subir nada, borra del documento cualquier dato de clientes: nombres, RUT, teléfonos, correos, reservas o pagos. "
     "Tampoco pongas claves de wifi internas, datos bancarios ni información de tus trabajadores. "
     "Quien abra tu asistente compartido podría llegar a ver el documento completo, así que solo debe tener información que pondrías en tu página web.",
     []),
    ("Entra a Gemini Notebook y crea un cuaderno",
     "Desde el computador, entra a notebooklm.google con tu cuenta de Google. Un \"cuaderno\" es el espacio donde vive tu asistente: guarda tus documentos y el chat. "
     "Crea un cuaderno nuevo con el botón para crear cuaderno y ponle el nombre de tu negocio.",
     []),
    ("Sube tu documento como fuente",
     "Una \"fuente\" es el material que el asistente puede leer para responder. En el panel de la izquierda, haz clic en \"Agregar fuentes\" "
     "y elige tu archivo desde el computador o desde Google Drive. Acepta Google Docs, Word (docx), PDF, TXT y otros formatos.",
     ["Sube solo el documento del negocio. Si agregas otras cosas, el asistente también las usará para responder.",
      "Si después cambias precios u horarios, actualiza la fuente para que el asistente no quede con datos viejos."]),
    ("Escribe las instrucciones del asistente",
     "En el panel \"Chat\", selecciona \"Configurar el chat\". Elige el estilo \"Personalizado\" y escribe cómo debe comportarse. "
     "Elige una longitud de respuesta corta y haz clic en \"Guardar\".",
     ["Ejemplo de instrucciones: \"Eres el asistente del Hostal Los Aromos. Responde en español de Chile, con trato de usted, en 2 o 3 frases. "
      "Usa solo la información del documento. Si la respuesta no está en el documento, dilo con honestidad y pide que escriban al WhatsApp +56 9 XXXX XXXX. "
      "No inventes precios, disponibilidad ni descuentos. No confirmes reservas: para reservar, deriva siempre al WhatsApp.\"",
      "Mantén las instrucciones breves. Si algo falla en las pruebas, ajusta una frase a la vez."]),
    ("Prueba con preguntas que sí están en el documento",
     "En el chat del cuaderno, haz preguntas como lo haría un huésped: \"¿A qué hora es el check-out?\", \"¿Aceptan mascotas?\", \"¿Cuánto cuesta una pieza doble?\". "
     "Compara cada respuesta con tu documento. Gemini Notebook muestra de qué parte de la fuente sacó la respuesta, úsalo para revisar.",
     []),
    ("Prueba con preguntas que no están",
     "Ahora pregunta cosas que no escribiste: \"¿Tienen piscina temperada?\", \"¿Me hacen precio por 10 noches?\", \"¿Hay pieza libre el sábado?\". "
     "El asistente debe decir que no tiene esa información y entregar tu WhatsApp. Si inventa algo, refuerza esa parte de las instrucciones o agrega el dato al documento.",
     []),
    ("Compártelo con un enlace",
     "Pulsa el botón \"Compartir\" en la esquina superior derecha y cambia el acceso para que cualquier persona que tenga el vínculo pueda entrar. "
     "Luego usa \"Copiar vínculo a la vista de chat\": esa vista muestra solo el chat y esconde las fuentes. "
     "Pega el enlace en tu WhatsApp Business, Instagram o página web.",
     ["Cada visitante necesita una cuenta de Google para abrir el cuaderno.",
      "La vista de chat esconde el documento, pero la ayuda de Google advierte que un visitante igual podría llegar a él. Por eso el paso 3 es obligatorio.",
      "Un ícono de globo junto a \"Compartir\" te indica que el cuaderno es público."]),
    ("Revisa, actualiza o apágalo",
     "Pregúntale al asistente cada semana un par de cosas y revisa que siga respondiendo bien, sobre todo después de cambiar precios o temporadas. "
     "Si dejas de usarlo, o algo salió mal, vuelve a \"Compartir\" y déjalo en \"Restringido\": el enlace deja de funcionar para visitantes nuevos. "
     "Los cambios que hagas en el cuaderno se ven en el enlace público sin crear uno nuevo.",
     []),
  ],
  prueba=(
    "Abre el enlace de la vista de chat desde otra cuenta de Google (la de un familiar, por ejemplo) y haz 3 preguntas que estén en el documento y 3 que no. "
    "Funciona si las primeras coinciden con tu documento y en las otras el asistente entrega tu WhatsApp sin inventar nada."
  ),
  errores=[
    "El asistente inventa precios o promete disponibilidad: agrega en las instrucciones \"usa solo la información del documento y no confirmes reservas\", y revisa que el documento diga \"precios referenciales\".",
    "Responde con datos viejos: actualizaste el archivo en tu computador, pero no la fuente en el cuaderno. Sube de nuevo la versión nueva y borra la anterior.",
    "Un cliente no puede abrir el enlace: necesita entrar con una cuenta de Google, o el cuaderno quedó en \"Restringido\". Revisa el acceso en \"Compartir\".",
    "Deja de responder a mitad del día: el plan gratuito tiene límites diarios de uso del chat (la ayuda de Google los indica y dice que pueden cambiar). Se reinician a las 24 horas.",
  ],
  fuentes=[
    "https://support.google.com/notebooklm/answer/16215270?hl=es-419",
    "https://support.google.com/notebooklm/answer/16179559?hl=es-419",
    "https://support.google.com/notebooklm/answer/16322204?hl=es-419",
    "https://support.google.com/notebooklm/answer/16213268?hl=es-419",
    "https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/",
    "https://support.google.com/gemini/answer/15146780?hl=en",
    "https://support.google.com/gemini/answer/16504957?hl=es-419",
    "https://help.openai.com/en/articles/8554397",
  ],
)
