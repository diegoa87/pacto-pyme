# Contenido de las mini guías (fuente única para la web y los PDF).
# Sale de las transcripciones de cada charla; no agregar datos que la charla no diga.

def seg(t):
    p = [int(x) for x in t.split(':')]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]

def url(vid, t=None):
    return f'https://www.youtube.com/watch?v={vid}' + (f'&t={seg(t)}s' if t else '')

GUIAS = [
  dict(slug='estrategias-ia', vid='X90ulUkIi-E', titulo='IA: estrategias transformadoras para negocios',
    quien='Gonzalo Sánchez, Desafío Latam', dur='77 min',
    resumen='Qué es la inteligencia artificial, una escala para saber en qué nivel está tu empresa y ejemplos que van del chat a tareas que se hacen solas, sin programar. Cierra con cinco etapas para sumar IA a un negocio.',
    ideas=[
      ('Primero ubícate', 'La charla propone una escala: sin IA, uso manual, varias herramientas, IA dentro de tus procesos y varias tareas coordinadas. Antes de avanzar, define dónde está hoy tu empresa.'),
      ('Dale contexto', 'Explicar bien tu situación rinde más que cualquier truco de redacción. También puedes pedirle a la IA que te ayude a escribir lo que le vas a pedir.'),
      ('Verifica siempre', 'La IA puede inventar respuestas. Revisa lo que entrega, sobre todo cifras y datos.'),
      ('Cuida tus datos', 'No subas información sensible de clientes ni de la empresa, aunque pagues un plan.'),
      ('Prueba en chico', 'Parte con un caso acotado, mide el resultado y ajusta antes de armar algo grande.'),
      ('Evita los errores típicos', 'Usar IA por moda sin una necesidad real, depender por completo de un solo proveedor y subestimar el cambio en tu equipo.'),
    ],
    minutos=[
      ('6:00', 'La escala de madurez en IA'), ('10:00', 'Por qué el contexto mejora las respuestas'),
      ('15:00', 'Analizar ventas con ChatGPT a partir de una planilla'), ('18:00', 'Cuando la IA inventa'),
      ('24:00', 'Investigar a la competencia con IA'), ('25:00', 'Privacidad de los datos'),
      ('48:00', 'Clasificar reseñas de clientes en una planilla, sin programar'), ('53:00', 'Un asistente que recomienda productos'),
      ('59:00', 'Las cinco etapas para sumar IA'), ('1:05:00', 'Un caso real de respuesta equivocada'),
      ('1:11:00', 'Los "cinco por qué" antes de partir'),
    ],
    pasos_titulo='Paso a paso: suma IA a tu negocio en cinco etapas',
    pasos=[
      ('Diagnóstico', 'Ubica a tu empresa en la escala.', ['Nivel 0: no usas IA.', 'Nivel 1: le preguntas cosas sueltas a un chat de IA.', 'Nivel 2: usas distintas herramientas según la tarea.', 'Nivel 3: la IA es parte de un proceso, por ejemplo clasificar reseñas todos los días.', 'Nivel 4: varias tareas conectadas que funcionan solas.']),
      ('Aprende con tu equipo', 'Prueben un chat de IA con una tarea real del negocio. Al pedirle algo, cuéntale quién eres, qué vende tu negocio, qué necesitas y cómo quieres la respuesta.', ['Ejemplo: "Tengo una cafetería en Talca. Escríbeme tres respuestas cortas y amables para una reseña que reclama por la demora."']),
      ('Elige casos', 'Anota tres tareas donde la IA podría ayudarte. A cada una pregúntale cinco veces "¿por qué?" hasta llegar al problema real. Si no aparece un problema, descártala.', []),
      ('Prueba en chico', 'Toma una sola tarea y úsala durante dos semanas. Anota cuánto tiempo te tomaba antes y cuánto ahora. Revisa todo lo que entrega la IA.', []),
      ('Ordena y amplía', 'Si funcionó, súmala al día a día y define reglas: qué datos nunca se suben, quién revisa lo que entrega la IA y cuándo se usa.', []),
    ],
    ejemplo=('Para probar hoy (15:00 y 24:00)', ['Exporta tus ventas a una planilla, sin nombres ni datos de clientes.', 'Súbela a un chat de IA y pide: "Hazme un gráfico de las ventas por día".', 'Luego pregunta: "¿Qué otros análisis puedo hacer con estos datos?".', 'Para mirar a la competencia, pide a una IA con búsqueda en internet que compare productos o precios de tu rubro. En la charla se usa la versión pagada de ChatGPT para el análisis de datos.']),
    plantilla=None,
    saltar='El inicio (0:00 a 6:00), la parte técnica para programadores (28:00 a 40:00) y el cierre con promoción de cursos (desde 1:13:00).',
    aviso='Se grabó en 2025. Algunas herramientas y precios que se mencionan ya cambiaron.'),

  dict(slug='tareas-repetitivas', vid='q6EYVwyB1c4', titulo='El fin de las tareas repetitivas',
    quien='Andrés, director ejecutivo de Desafío Latam', dur='78 min',
    resumen='Cómo dejar de hacer a mano el trabajo que se repite. La charla insiste en ordenar primero cómo se hace la tarea y después elegir la herramienta, y entrega un método para priorizar, calcular si conviene y anticipar los costos que no se ven.',
    ideas=[
      ('El proceso va primero', 'Define dónde empieza y termina la tarea, qué pasos tiene, qué datos entran y salen, qué reglas aplican y quién participa. Un dibujo en papel basta.'),
      ('Ojo con las excepciones', 'Lo difícil son los casos especiales. Por ejemplo: "publica automáticamente, salvo que sea feriado o haya promoción".'),
      ('Pregunta si se conecta', 'Antes de contratar un programa, consulta si se puede conectar con otros. Uno aislado no se puede automatizar.'),
      ('Prioriza con una matriz', 'Ordena tus tareas según impacto y esfuerzo. Empieza por las de alto impacto y poco esfuerzo.'),
      ('Cuenta los costos ocultos', 'Errores, mantención, satisfacción de los clientes, costo de la IA cuando crece el volumen y el tiempo de ordenar los datos.'),
      ('Avanza de a poco', 'Parte por el caso más simple, pide opiniones y mejora. Las fallas casi siempre vienen del diseño o de la resistencia al cambio.'),
      ('Una persona revisa', 'En procesos delicados, deja un paso de revisión humana.'),
    ],
    minutos=[
      ('16:00', 'Cómo ordenar el proceso'), ('21:00', 'Programas que se conectan entre sí'),
      ('22:00', 'Herramientas: Zapier, Make, Power Automate y n8n'), ('26:00', 'La matriz de impacto y esfuerzo'),
      ('29:00', 'Si conviene y los costos ocultos'), ('33:00', 'Los pasos para implementar'),
      ('40:00', 'Caso simple: recordatorios de cumpleaños'), ('46:00', 'Comentarios automáticos a partir de grabaciones'),
      ('48:00', 'Un resumen diario de noticias o de la competencia'), ('50:00', 'Ordenar el correo con etiquetas automáticas'),
      ('55:00', 'Por dónde partir'), ('1:05:00', 'Seguridad'), ('1:10:00', 'Usar IA para ordenar el proceso y qué es gratis'),
    ],
    pasos_titulo='Paso a paso: automatiza tu primera tarea',
    pasos=[
      ('Haz la lista', 'Anota las tareas que repites cada semana y cuántas horas te toman. Al final de la guía en PDF tienes una tabla para completarla.', []),
      ('Elige con la matriz', 'Ubica cada tarea según cuánto te ayudaría (impacto) y cuánto cuesta armarla (esfuerzo). Basta con tu intuición. Parte por la esquina de alto impacto y poco esfuerzo.', []),
      ('Dibuja el proceso', 'En papel, responde:', ['¿Qué hace partir la tarea y cuándo termina?', '¿Qué pasos tiene y en qué orden?', '¿Qué datos entran y qué sale al final?', '¿Qué reglas o excepciones hay? (feriados, promociones, clientes especiales)', '¿Quién participa y quién revisa?']),
      ('Revisa tus herramientas', 'Confirma que los programas que usas (planilla, correo, agenda, sistema de ventas) se pueden conectar entre sí. Si vas a contratar uno nuevo, pregunta esto antes.', []),
      ('Calcula lo que no se ve', 'Antes de armarla, piensa en:', ['Cuántas veces se puede equivocar y qué pasa si lo hace.', 'Quién la va a revisar cada semana.', 'Cuánto tiempo toma ordenar los datos que necesita.', 'Si atiende clientes, cómo vas a saber si quedaron conformes.']),
      ('Parte simple', 'Arma la versión más básica, sin excepciones. Pruébala, pide opinión a quien la usa y recién ahí suma las condiciones. Para empezar, la charla recomienda Zapier o Make.', []),
      ('Cuida la seguridad', 'Activa la verificación en dos pasos en tus cuentas, no dejes planillas públicas y no pases datos sensibles por chats o bots abiertos.', []),
    ],
    ejemplo=('Un caso real de la charla (40:00)', ['Cada fila nueva en una planilla de cumpleaños creaba un evento en el calendario, usando Zapier.', 'Fallaba con los errores de tipeo al llenar la planilla.', 'La solución fue revisar la planilla a una hora fija (cada 15 minutos o una vez al día) en vez de reaccionar a cada fila.', 'La lección: cuando una persona ingresa datos a mano, la automatización tiene que tolerar errores.']),
    plantilla='tareas',
    saltar='El inicio (0:00 a 16:00), los avisos de cursos que aparecen durante la charla y el cierre (desde 1:15:00). La demostración técnica (57:00) es opcional.',
    aviso='Las cifras de estudios que se citan al comienzo son de informes de 2023 a 2025.'),

  dict(slug='primer-agente-ia', vid='CVFFHd0Kazk', titulo='Aprende a crear tu primer agente de IA',
    quien='Suri, Desafío Latam', dur='72 min',
    resumen='Qué es un agente de IA y para qué le sirve a un negocio, a partir de un caso concreto: los clientes que hacen siempre las mismas preguntas. La segunda mitad muestra cómo construir uno.',
    ideas=[
      ('Un problema conocido', 'Los clientes no leen el folleto ni las condiciones y preguntan lo mismo una y otra vez. Un agente puede responder esas consultas.'),
      ('Qué es un agente', 'Un asistente que recibe información (texto, voz o imágenes), decide qué hacer y actúa: responde, envía un correo o anota un dato.'),
      ('Empieza simple', 'Un chat que responde preguntas frecuentes con la información de tu negocio ya funciona como agente.'),
      ('Casos de negocio', 'Registrar órdenes de compra que llegan en PDF, juntar boletas para el contador o avisar a clientes del estado de un despacho.'),
      ('Deriva lo que no sabe', 'Lo que el asistente no pueda responder debe pasar a una persona, por ejemplo con un enlace para agendar una llamada.'),
      ('Acceso mínimo', 'Si lo conectas a tus datos, dale acceso solo a lo necesario, como harías con un empleado nuevo.'),
      ('WhatsApp toma tiempo', 'Para usar WhatsApp necesitas una empresa formal en WhatsApp Business y una aprobación que puede tardar de una a tres semanas.'),
    ],
    minutos=[
      ('4:10', 'El problema de las preguntas repetidas'), ('18:40', 'Qué es un agente'),
      ('23:00', 'Un chat de preguntas frecuentes como primer agente'), ('25:00', 'Ejemplos en empresas'),
      ('35:00', 'WhatsApp y otros canales'), ('42:00', 'Demostración: un asistente que responde con la información de un PDF'),
      ('48:00', 'Derivar a una persona'), ('52:50', 'Conectarlo a tu web y cuidar los datos'),
    ],
    pasos_titulo='Paso a paso: prepara tu asistente de preguntas frecuentes',
    pasos=[
      ('Junta las preguntas', 'Anota las diez preguntas que más te hacen tus clientes, con su respuesta. Al final de la guía en PDF tienes una tabla para completarla.', []),
      ('Arma un documento', 'Reúne en un PDF la información que el asistente debe conocer: productos o servicios, horarios, formas de pago, despachos y condiciones.', []),
      ('Escribe la instrucción', 'Es el texto que le dice al asistente cómo comportarse. En la charla bastó con una sola indicación. Puedes partir con esta:', ['"Eres el asistente de [nombre de tu negocio]. Responde en español, de forma breve y amable, usando solo la información del documento. Si no sabes la respuesta, invita a la persona a escribir a [teléfono o enlace para agendar]."']),
      ('Define qué pasa a una persona', 'Decide qué consultas responde siempre una persona: reclamos, cotizaciones especiales, pagos.', []),
      ('Elige dónde va a responder', 'En tu web, en Telegram (se activa de inmediato) o en WhatsApp (necesita WhatsApp Business y una aprobación de semanas).', []),
      ('Pruébalo antes de abrirlo', 'Hazle tus diez preguntas y otras que no estén en el documento. Revisa que derive bien lo que no sabe.', []),
      ('Cuida los datos', 'No incluyas en el documento datos personales de clientes. Si lo conectas a tus sistemas, dale acceso solo a lo justo.', []),
    ],
    ejemplo=('Si quieres ir más allá (requiere programar)', ['En la charla se construye con programación: se crea una clave de acceso en la plataforma de OpenAI, se carga saldo y se conecta a una página simple (42:00). La clave no se comparte con nadie.', 'Para Telegram (59:00): busca @BotFather, escribe /newbot, elige un nombre y un usuario que termine en "bot", y copia el código que te entrega.', 'El expositor dice que también se puede hacer sin programar, pero no lo muestra. Si no programas, pide ayuda o usa una herramienta sin código.']),
    plantilla='faq',
    saltar='El inicio y la historia de la IA (0:00 a 18:00), los ejemplos de inversiones y bancos extranjeros (29:00 a 33:00) y la promoción de cursos (57:50 y desde 1:05:30).',
    aviso='La demostración usa programación. Si no programas, quédate con la primera mitad y con los minutos de arriba. Se grabó en 2025.'),

  dict(slug='automatiza', vid='3zM9VB6TSgA', titulo='Más productividad, menos esfuerzo: automatiza',
    quien='Gonzalo Sánchez, Desafío Latam', dur='63 min',
    resumen='Un taller práctico con n8n, una herramienta para conectar aplicaciones sin programar. Muestra cómo se arma una tarea automática y varios ejemplos, desde guardar datos en una planilla hasta usar IA para clasificar comentarios.',
    ideas=[
      ('Un asistente digital', 'Automatizar es dejar de copiar datos a mano entre WhatsApp, planillas, correo y tu registro de clientes.'),
      ('Algo que la active y pasos', 'Toda tarea automática parte con algo que la activa, como un formulario nuevo o una hora del día, y sigue con pasos en orden.'),
      ('El uso más común', 'Sacar información de una herramienta y guardarla en otra.'),
      ('La IA varía', 'La misma pregunta puede dar respuestas distintas. Considéralo al armar el proceso.'),
      ('El valor está en encadenar', 'Cada paso suelto parece poco. El ahorro de horas aparece al unirlos.'),
      ('Apaga lo que no usas', 'Las tareas automáticas que no necesitan correr todo el tiempo conviene desactivarlas.'),
    ],
    minutos=[
      ('3:00', 'Qué es automatizar'), ('7:00', 'Opciones para usar la herramienta'),
      ('10:00', 'Cómo funciona una tarea automática'), ('14:00', 'Primer ejemplo: guardar datos en una planilla'),
      ('22:00', 'Casos reales en una empresa'), ('24:00', 'De un formulario a un correo'),
      ('31:00', 'Sumar IA a una tarea automática'), ('42:30', 'Clasificar comentarios de clientes'),
      ('45:00', 'Recomendar productos desde una planilla'), ('55:00', 'Enviar correos recurrentes'),
    ],
    pasos_titulo='Paso a paso: arma tu primera tarea automática',
    pasos=[
      ('Elige la tarea', 'Busca una donde copies datos de un lugar a otro. Por ejemplo, pasar los contactos que llegan por un formulario a una planilla.', []),
      ('Define qué la activa', 'Un formulario nuevo, un correo que llega, un mensaje o una hora del día.', []),
      ('Anota los pasos', 'Escribe en orden qué tiene que pasar después. Ejemplo: guardar los datos en la planilla, enviarte un aviso por correo.', []),
      ('Elige la herramienta', 'Zapier o Make son más simples para partir y tienen versiones gratis con límites. n8n es más completa: es gratis si la instalas tú, pero eso requiere conocimientos técnicos.', []),
      ('Arma y prueba por partes', 'Prueba cada paso por separado y revisa qué entra y qué sale. En n8n se puede ejecutar un paso a la vez.', []),
      ('Actívala y obsérvala', 'Déjala funcionando y revisa los resultados las primeras semanas.', []),
      ('Si sumas IA, revisa', 'La IA puede responder distinto ante lo mismo. Revisa lo que entrega, por ejemplo cuando clasifica comentarios como positivos o negativos.', []),
      ('Apaga lo que no uses', 'Desactiva las tareas que ya no necesitas.', []),
    ],
    ejemplo=('Un caso de la charla (55:00)', ['Necesidad: enviar un correo cada mes a 20 contactos.', 'Una planilla con los destinatarios.', 'Un paso que recorre la lista y otro que envía el correo a cada uno.', 'Se activa solo en la fecha que definas. Según el expositor, bastan tres pasos.']),
    plantilla=None,
    saltar='El inicio (0:00 a 2:00), la comparación técnica (13:00 a 14:00), el ejemplo de prueba con datos de un juego (29:00 a 31:00) y la promoción de cursos (desde 55:30).',
    aviso='Instalar n8n gratis requiere conocimientos técnicos. Zapier y Make son alternativas más simples para empezar. Algunos ejemplos se repiten en la charla "IA: estrategias transformadoras para negocios".'),
]

# Versiones extendidas (expand/<slug>.py) reemplazan a las de arriba cuando existen.
import os as _os
_EXP = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'expand')
for _i, _g in enumerate(GUIAS):
    _p = _os.path.join(_EXP, _g['slug'] + '.py')
    if _os.path.exists(_p):
        _ns = {}
        exec(open(_p, encoding='utf-8').read(), _ns)
        GUIAS[_i] = {**_g, **_ns['G']}
for _g in GUIAS:
    for _k in ('contexto', 'preguntas', 'errores', 'glosario'):
        _g.setdefault(_k, [])

# Ejemplo real de implementación (hazlo/<slug>.py), verificado contra la documentación oficial.
_HZ = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'hazlo')
for _g in GUIAS:
    _p = _os.path.join(_HZ, _g['slug'] + '.py')
    _g['hazlo'] = None
    if _os.path.exists(_p):
        _ns = {}
        exec(open(_p, encoding='utf-8').read(), _ns)
        _g['hazlo'] = _ns['HAZLO']
