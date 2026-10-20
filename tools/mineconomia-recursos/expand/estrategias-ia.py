G = dict(
    slug='estrategias-ia',
    vid='X90ulUkIi-E',
    titulo='IA: estrategias transformadoras para negocios',
    quien='Gonzalo Sánchez, director de Tecnología e Innovación de Desafío Latam',
    dur='77 min',
    resumen=(
        'Qué es la inteligencia artificial y una escala de cinco niveles para saber dónde está tu empresa. '
        'La charla muestra ejemplos en vivo que van de hacerle preguntas a un chat hasta tareas que se hacen solas con n8n, sin programar. '
        'Cierra con cinco etapas para sumar IA a un negocio y los errores que conviene evitar.'
    ),
    contexto=[
        'El Chequeo Digital te dijo qué tan digital es tu negocio. Esta charla da el paso siguiente: dónde puede ayudarte la IA y por dónde partir. '
        'La primera etapa que propone el expositor es justo un diagnóstico. Pregunta si tienes datos, si usas una planilla, si tienes algo automatizado o si todo está en papel.',
        'Muchas tareas de una pyme se repiten todos los días. Responder las mismas consultas, revisar comentarios de clientes, ordenar ventas en una planilla, escribir descripciones de productos. '
        'Esas tareas repetitivas y basadas en texto son las que la charla señala como buenas candidatas para la IA. Cada una que dejas andando sola te devuelve tiempo.',
        'La charla también es honesta con los límites. La IA se equivoca, inventa respuestas y no sirve para todo. '
        'Por eso recomienda partir con una prueba chica, en una tarea de bajo riesgo, y revisar lo que entrega antes de confiarle algo importante.',
    ],
    ideas=[
        ('Primero ubícate',
         'La charla propone una escala: nivel 0 sin IA, nivel 1 uso manual en un chat, nivel 2 varias herramientas según la tarea, nivel 3 IA dentro de tus programas y nivel 4 varias tareas coordinadas. '
         'Saber en qué nivel estás te ayuda a elegir el siguiente paso sin saltarte etapas.'),
        ('Dale contexto',
         'Para preguntas simples basta con preguntar directo. Para algo más específico, explica tu situación completa: entre mejor la explicas, mejor respuesta obtienes. '
         'También puedes pedirle a la IA que te ayude a escribir lo que le vas a pedir y después lo corriges tú.'),
        ('Analiza tus datos sin programar',
         'Algunos chats de IA pueden leer una planilla, hacer gráficos y sugerir qué más mirar. Tú escribes en palabras normales, incluso con errores de ortografía. '
         'Como la IA hace el cálculo de verdad por detrás, se equivoca menos que cuando responde de memoria.'),
        ('Verifica siempre',
         'La IA puede inventar respuestas que suenan muy reales. El expositor contó que una vez le dio los pasos para usar una herramienta que nunca existió. '
         'Revisa cifras, nombres y datos antes de usarlos.'),
        ('Investiga a tu competencia',
         'Hay chats de IA con búsqueda en internet que leen varias páginas y te entregan un resumen. '
         'Puedes pedirle que compare tu producto con otros parecidos: ventajas, precios y cómo estás tú frente a ellos.'),
        ('Cuida tus datos',
         'Ni siquiera los planes pagados te aseguran que lo que subes queda privado. '
         'No subas información sensible de tus clientes ni de tu empresa.'),
        ('Tareas que se hacen solas',
         'Con n8n se arman flujos uniendo cajitas: llega un mensaje, la IA responde y el resultado se guarda o se envía por correo. '
         'En la charla se clasificaron reseñas de clientes en una planilla y se armó un asistente que recomienda productos, todo sin escribir código.'),
        ('Prueba en chico',
         'Antes de mandar a construir un programa, prueba la idea con una herramienta como n8n. '
         'Parte con un caso acotado, mide el resultado y ajusta.'),
    ],
    pasos_titulo='Paso a paso: suma IA a tu negocio en cinco etapas',
    pasos=[
        ('Ubica a tu empresa en la escala',
         'Revisa en qué nivel estás hoy. Mira también qué tienes ordenado: si hay planillas, si usas un sistema de clientes o si todo está en cuadernos. '
         'Sin datos ordenados, la IA tiene poco con qué trabajar.',
         ['Nivel 0: no usas IA.',
          'Nivel 1: le preguntas cosas sueltas a un chat de IA, por ejemplo que te escriba un correo.',
          'Nivel 2: usas distintas herramientas según la tarea y comparas respuestas.',
          'Nivel 3: la IA es parte de tus programas, por ejemplo un chat que responde a clientes o que escribe descripciones de productos.',
          'Nivel 4: varias tareas conectadas que funcionan solas y se pasan el trabajo entre ellas.']),
        ('Define qué quieres lograr',
         'Busca los procesos repetitivos, lentos o donde tomas muchas decisiones. Luego elige un objetivo: bajar costos, vender más o atender mejor a tus clientes. '
         'La charla destaca que mejorar la atención al cliente es uno de los objetivos más comunes.',
         ['Ejemplo: en una peluquería, contestar a mano cada mensaje para pedir hora puede tomar una hora al día. El objetivo sería responder más rápido sin quitarle tiempo a la atención.']),
        ('Aprende con tu equipo',
         'Antes de sumar herramientas, entiende qué puede y qué no puede hacer la IA. Prueben un chat de IA con tareas reales del negocio. '
         'Al pedirle algo, cuéntale quién eres, qué vende tu negocio, qué necesitas y cómo quieres la respuesta.',
         ['Ejemplo: "Tengo una cafetería en Talca. Escríbeme tres respuestas cortas y amables para una reseña que reclama por la demora."',
          'Conversen qué tareas nunca le dejarían a la IA sin revisar.']),
        ('Elige casos de uso',
         'Anota tres tareas donde la IA podría ayudarte. Prefiere las repetitivas, basadas en texto y de bajo riesgo. '
         'Revisa que tengas los datos para hacerlas. A cada una pregúntale cinco veces "¿por qué?" hasta llegar al problema real; si no aparece, descártala.',
         ['Bajo riesgo: ordenar en una planilla los comentarios que hoy anotas a mano.',
          'Alto riesgo: cambiar un proceso crítico del que dependen muchos otros pasos.',
          'Ejemplo: una ferretería que recibe muchas consultas de stock por WhatsApp puede empezar con un asistente que lea la planilla de productos y responda si hay o no.']),
        ('Prueba en chico',
         'Arma una versión simple con una herramienta como n8n, sin programar. Úsala un par de semanas y anota cuánto tiempo te tomaba antes y cuánto ahora. '
         'Revisa todo lo que entrega la IA y ajusta lo que falle.',
         ['Ejemplo: un hostal puede cargar sus reseñas en una planilla y dejar que la IA marque cada una como positiva o negativa. Así ve rápido qué reclamos se repiten.',
          'Si no quieres armarlo tú, puedes contratar a alguien por un tiempo solo para la prueba.']),
        ('Ordena y amplía',
         'Si funcionó, súmala al día a día. Define reglas claras: qué datos nunca se suben, quién revisa lo que entrega la IA y cuándo se usa. '
         'Si el proceso crece mucho, ahí puede convenir mandar a construir un programa hecho a la medida.',
         ['Nombra a una persona responsable de estas herramientas en tu equipo.']),
    ],
    ejemplo=('Para probar hoy: analiza tus ventas y mira a la competencia (15:00 y 24:00)', [
        'Exporta tus ventas a una planilla, sin nombres ni datos de clientes.',
        'Súbela a un chat de IA que pueda leer archivos y pide: "Hazme un gráfico de las ventas por día".',
        'Luego pregunta: "¿Qué otros análisis puedo hacer con estos datos?" y prueba una de las ideas, como cuál es el producto que más se repite.',
        'Para mirar a la competencia, pide a una IA con búsqueda en internet que compare productos parecidos al tuyo: ventajas y precios.',
        'Revisa las fuentes que muestra antes de tomar decisiones. En la charla se usa ChatGPT para los datos y Grok para la búsqueda.',
    ]),
    preguntas=[
        ('¿Necesito pagar para que la IA haga cosas por mí?',
         'Para hacerle preguntas a un chat, no siempre. Para conectar la IA con tus propios programas sí suele haber un cobro, aunque hay versiones que se pueden descargar y usar gratis en tu computador.',
         '12:00'),
        ('¿Cómo se asegura la privacidad de lo que le envío?',
         'Los servicios en línea, incluso los pagados, no te aseguran que tu información quede privada. Algunos planes más caros prometen reservarla, pero igual hay que cuidar lo que se envía.',
         '25:00'),
        ('¿Cómo hago que ChatGPT sepa de mi tema en particular?',
         'La forma simple es entregarle toda la información necesaria cada vez que le pides algo. La otra es entrenarlo con muchos casos, pero eso es caro.',
         '29:00'),
        ('¿Se puede evitar que la IA le dé una respuesta equivocada a un cliente?',
         'Se puede reducir eligiendo bien la herramienta, pero la posibilidad de error siempre existe. Por eso hay que decidir en qué temas usarla según cuánto estás dispuesto a que falle.',
         '1:05:00'),
        ('Soy independiente: ¿cómo conecto atención a clientes, agenda y pagos?',
         'Esas conexiones cuesta afinarlas. El expositor recomienda probar primero con n8n para entender bien el proceso y, cuando ya lo tengas claro, mandar a construir un programa para eso.',
         '1:09:00'),
    ],
    errores=[
        'Usar IA por moda, solo para decir que la usas, sin una necesidad real.',
        'Creer que la IA es magia y puede resolverlo todo.',
        'Confiar en sus respuestas sin revisarlas: puede inventar con mucha seguridad.',
        'Depender por completo de un proveedor externo sin aprender en tu propio equipo.',
        'Subestimar el cambio que significa para tu equipo trabajar con estas herramientas.',
    ],
    glosario=[
        ('Alucinar', 'Cuando la IA inventa una respuesta que suena real pero es falsa.'),
        ('Búsqueda profunda', 'Función de algunos chats de IA que lee varias páginas de internet y te entrega un resumen con las fuentes.'),
        ('n8n', 'Programa para armar tareas automáticas uniendo cajitas, sin escribir código.'),
        ('Gatillo', 'Lo que pone en marcha una tarea automática: un mensaje de chat, un formulario o un WhatsApp.'),
        ('Análisis de sentimiento', 'Clasificar un comentario como positivo o negativo según lo que expresa.'),
        ('Piloto', 'Una prueba chica de una idea antes de usarla en todo el negocio.'),
    ],
    minutos=[
        ('6:00', 'La escala de madurez en IA'),
        ('10:00', 'Por qué el contexto mejora las respuestas'),
        ('15:00', 'Analizar ventas con ChatGPT a partir de una planilla'),
        ('18:00', 'Cuando la IA inventa'),
        ('24:00', 'Investigar a la competencia con búsqueda en internet'),
        ('25:00', 'Privacidad de los datos'),
        ('40:00', 'Primer flujo en n8n: dos cajitas y una respuesta'),
        ('43:00', 'Enviar la respuesta de la IA por correo'),
        ('48:00', 'Clasificar reseñas de clientes en una planilla, sin programar'),
        ('53:00', 'Un asistente que recomienda productos'),
        ('59:00', 'Las cinco etapas para sumar IA'),
        ('1:05:00', 'Un caso real de respuesta equivocada'),
        ('1:11:00', 'Los "cinco por qué" antes de partir'),
    ],
    plantilla=None,
    saltar='El inicio (0:00 a 6:00), la parte técnica para programadores (28:00 a 40:00) y el cierre con promoción de cursos (desde 1:13:00).',
    aviso='Se grabó en 2025. Algunas herramientas y precios que se mencionan ya cambiaron.',
)
