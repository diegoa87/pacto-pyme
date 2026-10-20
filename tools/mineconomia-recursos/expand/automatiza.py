G = dict(
    slug='automatiza',
    vid='3zM9VB6TSgA',
    titulo='Más productividad, menos esfuerzo: automatiza',
    quien='Gonzalo Sánchez, director de Tecnología e Innovación de Desafío Latam',
    dur='63 min',
    resumen=(
        'Un taller práctico con n8n, una herramienta para conectar programas entre sí sin saber programar. '
        'Muestra cómo se arma una tarea automática paso a paso y la va complicando de a poco: guardar datos en una planilla, '
        'mandar un correo desde un formulario y sumar IA para clasificar comentarios o recomendar productos.'
    ),
    contexto=[
        'En una pyme se pierde mucho tiempo copiando datos. Un pedido llega por WhatsApp, lo anotas en una planilla, '
        'le avisas a alguien y después lo pasas a otro sistema. Cada paso es corto, pero sumados se comen horas a la semana. '
        'Esta charla muestra cómo dejar ese traspaso a una herramienta que lo hace sola.',
        'Si en el Chequeo Digital te fue bien en el uso de planillas, correo o formularios, este es el paso siguiente: hacer que esas herramientas '
        'conversen entre sí. Si saliste en nivel Inicial o Novato, igual te sirve para entender qué se puede automatizar y elegir mejor '
        'qué programas usar, porque un programa que no se conecta con otros no se puede automatizar.',
        'No necesitas armar todo hoy. Basta con mirar tu semana, encontrar una tarea que repites igual cada vez y probar con ella. '
        'El ejemplo de los 20 correos mensuales del final se resuelve con tres pasos.',
    ],
    ideas=[
        ('Un asistente digital',
         'Automatizar es poner a un asistente digital a hacer las tareas repetitivas por ti. '
         'Por ejemplo, copiar datos de un correo a una planilla o avisarle a alguien cada vez que se llena un formulario.'),
        ('Algo que la active y pasos en orden',
         'Toda tarea automática (en n8n se llama flujo) parte con un gatillo: algo que la activa, como un formulario nuevo, un correo, un mensaje o una hora del día. '
         'Después vienen las acciones, que se ejecutan una tras otra. El flujo termina cuando no quedan acciones o cuando hay un error.'),
        ('Cada paso recibe y entrega',
         'Cada paso recibe información del anterior y entrega un resultado al siguiente. '
         'En n8n basta con arrastrar un dato de un paso a otro para usarlo, por ejemplo el nombre que llegó en un formulario.'),
        ('El uso más común',
         'Según el expositor, el caso típico es sacar información de una herramienta y guardarla en otra. '
         'Desde ahí aparecen las demás ideas: avisos, correos, registros de clientes.'),
        ('La IA se suma como un paso más',
         'Dentro de un flujo se puede agregar un paso que le pregunta a ChatGPT. '
         'Así la tarea puede clasificar comentarios, contestar en un chat, describir una imagen o crear una. Usar ChatGPT dentro del flujo se paga según cuánto se usa.'),
        ('La IA puede fallar',
         'En la charla, el recomendador de productos falló una vez y acertó en la siguiente con una pregunta parecida. '
         'La misma pregunta puede dar respuestas distintas. Hay que tenerlo en cuenta al diseñar un proceso de la empresa.'),
        ('El valor está en encadenar',
         'Cada paso por separado parece poca cosa. '
         'El ahorro de horas aparece cuando unes varios y conectas tus herramientas de punta a punta.'),
        ('Apaga lo que no usas',
         'Una tarea activada que se repite cada cierto tiempo sigue corriendo hasta que la apagas. '
         'En la charla, un flujo de prueba siguió agregando fechas a la planilla durante toda la sesión.'),
    ],
    pasos_titulo='Paso a paso: arma tu primera tarea automática',
    pasos=[
        ('Elige la tarea',
         'Busca una tarea que repites igual y donde copias datos de un lugar a otro. Mientras más veces a la semana la hagas, más tiempo ahorras.',
         ['Ejemplo: en un almacén, anotar en una planilla cada pedido que llega por WhatsApp.',
          'Ejemplo: en una peluquería, pasar las reservas del formulario web al cuaderno de horas.']),
        ('Define qué la activa',
         'Elige el gatillo. Puede ser un formulario que alguien llena, un correo que llega, un mensaje o una hora fija. '
         'Si la tarea se hace siempre a la misma hora, usa un gatillo de horario.',
         ['Ejemplo: en un hostal, cada mañana a las 8 se revisan las reservas del día.']),
        ('Anota los pasos en papel',
         'Escribe en orden qué tiene que pasar después del gatillo. Una acción por línea. '
         'Esto te sirve para armarlo en cualquier herramienta y para explicárselo a quien te ayude.',
         ['Ejemplo: en una ferretería, cuando llega una consulta por el formulario: guardar nombre y correo en la planilla, mandar un aviso al vendedor y responder al cliente que lo contactarán.']),
        ('Elige la herramienta',
         'La charla nombra cuatro: n8n, Zapier, Make e If This Then That. Zapier y Make tienen versiones gratis con límites. '
         'n8n se puede usar pagando en la nube, o gratis si la instalas en tu computador o en un servidor que arriendes. Instalarla requiere seguir instrucciones técnicas.',
         []),
        ('Arma y prueba por partes',
         'Prueba cada paso por separado y revisa qué entra y qué sale. En n8n se puede ejecutar un paso a la vez y los pasos se ponen verdes cuando funcionan. '
         'Haz pruebas con tu propio correo antes de mandarle algo a un cliente.',
         []),
        ('Si sumas IA, dale instrucciones cortas y revisa',
         'En la charla, para clasificar comentarios se le escribió: "Evalúa el siguiente testimonio y clasifícalo como positivo o negativo. Responde solo positivo o negativo, nada más". '
         'Pedir una respuesta corta y cerrada ayuda. Igual revisa los resultados, porque la IA puede equivocarse.',
         ['Ejemplo: en una tienda online, clasificar las reseñas de la semana como positivas o negativas y leer primero las negativas.']),
        ('Actívala y obsérvala',
         'Déjala funcionando y revisa los resultados las primeras semanas. Si algo falla, el flujo se detiene en ese paso.',
         []),
        ('Apaga lo que no uses',
         'Desactiva las tareas de prueba y las que ya no necesitas. Si no, siguen corriendo y llenando planillas.',
         []),
    ],
    ejemplo=('Un caso de la charla (54:00)', [
        'Un asistente contó que cada mes envía unos 20 correos a distintas personas pidiendo información de cada departamento.',
        'La solución propuesta: una planilla con los correos de las 20 personas.',
        'Un paso que recorre la lista y otro que envía el correo a cada una.',
        'Un gatillo de horario, por ejemplo una vez al día o cada cierta cantidad de horas.',
        'Si la lista y el correo son siempre los mismos, según el expositor son tres pasos. Si cambian, el problema se vuelve un poco más difícil.',
    ]),
    preguntas=[
        ('¿n8n es gratis o hay que pagar?',
         'Si la instalas en tu computador o en un servidor propio es gratis para siempre, con todos los pasos disponibles para armar flujos. '
         'La versión en la nube se paga y tiene límites según el plan. El expositor cuenta que en su trabajo la usan instalada hace más de un año.',
         '19:00'),
        ('¿Qué computador necesito para instalarla?',
         'Corre con bastante poco. Necesitas al menos 1 GB de memoria libre y, en lo posible, un procesador libre.',
         '11:00'),
        ('¿Se pueden enviar cotizaciones en PDF con ayuda de IA?',
         'Sí. Combinando un paso de IA con una base de datos se pueden armar cotizaciones con cierta estructura y enviarlas por correo a los clientes.',
         '23:00'),
        ('¿Puedo guardar en Google Sheets los clientes nuevos que preguntan por WhatsApp?',
         'Sí, y se hace fácil con lo que se mostró en los ejemplos. En vez de mandar los datos por correo, se van agregando a una hoja de cálculo.',
         '59:00'),
        ('¿Qué diferencia hay entre subir una imagen a ChatGPT y hacerlo en un flujo?',
         'En el flujo puedes conectar otras herramientas. Por ejemplo, tomar un documento párrafo por párrafo y generar una imagen para cada uno de forma automática. '
         'Ningún paso suelto impresiona, el ahorro aparece al conectarlos.',
         '53:00'),
    ],
    errores=[
        'Dejar activa una tarea que no necesita correr siempre. Sigue funcionando hasta que la apagas.',
        'Confiar a ciegas en la IA. La misma pregunta puede dar respuestas distintas, así que revisa lo que entrega.',
        'Diseñar un chat que espera que el cliente escriba "fin" para terminar. Lo más probable es que el cliente simplemente deje de escribir.',
        'Pensar que usar ChatGPT dentro del flujo es gratis. Se cobra por uso, y el costo crece cuando el flujo guarda conversaciones largas.',
        'Intentar instalar n8n sin experiencia técnica. Requiere seguir un documento con varios pasos. Si no te manejas, usa la versión en la nube o pide ayuda.',
    ],
    glosario=[
        ('Flujo', 'Una tarea automática armada con pasos en orden. En inglés se dice workflow.'),
        ('Gatillo', 'Lo que activa el flujo: apretar un botón, un formulario nuevo, un correo que llega o una hora del día.'),
        ('Nodo', 'Cada paso dentro del flujo. Puede ser el gatillo o una acción, como guardar en una planilla o mandar un correo.'),
        ('CRM', 'Un programa para registrar a tus clientes: datos de contacto, compras y conversaciones.'),
        ('Webhook', 'Una forma de que otro programa le avise a tu flujo que pasó algo, por ejemplo que terminó una videollamada o que alguien apretó un botón.'),
        ('Análisis de sentimiento', 'Pedirle a la IA que lea comentarios de clientes y diga si son positivos o negativos.'),
    ],
    minutos=[
        ('3:00', 'Qué es automatizar'),
        ('7:00', 'Formas de usar n8n: en la nube o instalada'),
        ('10:00', 'Cómo se compone un flujo: gatillo y acciones'),
        ('14:00', 'Primer ejemplo: guardar la fecha en una planilla'),
        ('19:00', 'Qué entra y qué sale de cada paso'),
        ('22:00', 'Casos reales en Desafío Latam'),
        ('24:00', 'De un formulario a un correo'),
        ('31:00', 'Sumar IA: un chat conectado a ChatGPT'),
        ('38:00', 'Un chat que recuerda la conversación'),
        ('43:00', 'Clasificar comentarios de clientes'),
        ('45:00', 'Recomendar productos desde una planilla'),
        ('49:00', 'Analizar y generar imágenes'),
        ('54:00', 'Enviar correos recurrentes'),
    ],
    plantilla=None,
    saltar='El inicio (0:00 a 2:00), la comparación técnica con otra herramienta (13:00 a 14:00), el ejemplo de prueba con datos de un juego (29:00 a 31:00) y la promoción de cursos (55:00 a 59:00 y desde 1:00:00). Entre medio, a los 59:00, hay una pregunta útil sobre guardar clientes de WhatsApp en una planilla.',
    aviso='Instalar n8n gratis requiere conocimientos técnicos. Zapier y Make son alternativas para empezar. Los valores que se mencionan en la charla pueden haber cambiado. Algunos ejemplos se repiten en la charla "IA: estrategias transformadoras para negocios".',
)
