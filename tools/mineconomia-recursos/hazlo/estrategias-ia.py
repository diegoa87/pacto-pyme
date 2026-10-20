HAZLO = dict(
    titulo="Hazlo tú: analiza las ventas del mes de tu café con ChatGPT",
    intro=(
        "Vas a tomar las ventas del último mes de un café o almacén, subirlas a ChatGPT y pedirle gráficos y conclusiones en lenguaje simple. "
        "Es la misma demo de la charla (minuto 15), pero con tus datos reales. "
        "Te toma entre 30 y 45 minutos la primera vez. Antes necesitas poder sacar tus ventas de la caja o del sistema en un archivo de planilla."
    ),
    necesitas=[
        "Una cuenta de ChatGPT en chatgpt.com o en la app. El plan Gratis permite subir planillas, con un máximo de 3 archivos al día.",
        "Tus ventas del último mes en Excel (.xlsx o .xls) o CSV. Una fila por venta o por producto vendido.",
        "Un computador para limpiar la planilla. Subir y preguntar se puede hacer desde el teléfono.",
        "15 minutos para revisar los números al final.",
    ],
    pasos=[
        (
            "Exporta las ventas del mes",
            "Entra al sistema de tu caja, punto de venta o facturación y busca la opción de reportes o informes de ventas. "
            "Elige el rango de fechas del último mes y descárgalo en Excel o CSV (CSV es una planilla simple, de solo texto, que abre cualquier programa). "
            "Si tu sistema no exporta, pide el archivo a tu proveedor o anota las ventas diarias en una planilla de Google Sheets o Excel.",
            [
                "Busca palabras como Reportes, Informes, Ventas o Exportar.",
                "Si te deja elegir, pide el detalle por producto con fecha y hora.",
            ],
        ),
        (
            "Ordena la planilla",
            "Abre el archivo en Excel o Google Sheets. ChatGPT entiende mejor una tabla limpia: los nombres de columna en la primera fila y una venta por fila. "
            "Borra filas de totales, títulos decorativos y filas vacías que corten la tabla.",
            [
                "Columnas útiles: fecha, hora, producto, cantidad, precio, total, medio de pago.",
                "Usa nombres claros, por ejemplo \"Fecha\" en vez de \"F_DOC\".",
                "Deja una sola tabla por hoja.",
            ],
        ),
        (
            "Quita los datos de tus clientes",
            "Antes de subir nada, elimina las columnas con nombre del cliente, RUT, teléfono, correo, dirección o número de tarjeta. "
            "Para analizar ventas no los necesitas, y son datos personales que no debes compartir con un servicio externo. "
            "Guarda esta versión como un archivo nuevo, por ejemplo ventas_octubre_sin_clientes.xlsx.",
            [
                "Revisa también columnas de comentarios u observaciones: a veces traen nombres.",
                "Si quieres distinguir clientes frecuentes, reemplaza el nombre por un código (Cliente 1, Cliente 2).",
            ],
        ),
        (
            "Apaga el uso de tus chats para entrenar",
            "En ChatGPT abre el menú de tu cuenta, entra a Configuración y luego a Controles de datos. "
            "Desactiva la opción Mejorar el modelo para todos. Así tus conversaciones nuevas no se usan para entrenar los modelos de OpenAI.",
            [
                "En el teléfono: abre la barra lateral, toca tu ícono de perfil, Controles de datos.",
            ],
        ),
        (
            "Sube el archivo al chat",
            "Abre un chat nuevo y usa el botón para adjuntar archivos, al lado del cuadro donde escribes. Elige tu planilla sin datos de clientes. "
            "Espera a que el archivo aparezca cargado antes de enviar la primera instrucción. "
            "Recuerda que en el plan Gratis tienes 3 archivos al día: sube la versión final, no borradores.",
            [],
        ),
        (
            "Primera instrucción: dale contexto y pide el gráfico por día",
            "Como enseña la charla (minuto 10), la IA responde mejor si le cuentas quién eres y qué necesitas. Copia y ajusta esta instrucción:",
            [
                "\"Tengo un café de barrio en Concepción. Abrimos de lunes a sábado de 8:00 a 20:00. Te adjunto las ventas de octubre, una fila por producto vendido. "
                "Primero dime qué columnas encontraste, cuántas filas tiene el archivo y la suma total de ventas. Después hazme un gráfico de barras con el total vendido por día.\"",
            ],
        ),
        (
            "Pide los productos más vendidos",
            "Con el archivo ya cargado, sigue en el mismo chat. No necesitas volver a subirlo.",
            [
                "\"Hazme una tabla con los 10 productos más vendidos del mes: unidades, monto total y porcentaje del total de ventas. "
                "Ordénala de mayor a menor monto.\"",
            ],
        ),
        (
            "Busca las horas y días flojos",
            "Esta pregunta te ayuda a decidir turnos, promociones u horarios. Si tu archivo no trae la hora, pide solo el análisis por día de la semana.",
            [
                "\"Muéstrame las ventas promedio por día de la semana y por franja de una hora. "
                "Dime cuáles son los 3 momentos más flojos y los 3 más fuertes, y explícalo en palabras simples, sin términos técnicos.\"",
            ],
        ),
        (
            "Pregúntale qué más puedes analizar",
            "En la charla (minuto 17) el expositor pide sugerencias de análisis y usa una de ellas. Haz lo mismo y elige la que te sirva para una decisión concreta.",
            [
                "\"¿Qué otros análisis útiles puedes hacer con estos datos para un café chico? Dame 5 ideas y para cada una dime qué decisión me ayudaría a tomar.\"",
                "Después: \"Haz la idea número 2.\"",
            ],
        ),
        (
            "Cuadra los números con tu planilla",
            "La charla advierte (minuto 18) que la IA puede inventar respuestas. Cuando analiza un archivo usa cálculos de verdad, pero igual puede leer mal una columna o saltarse filas. "
            "Compara 3 cifras con tu planilla antes de tomar decisiones.",
            [
                "Total del mes: en Excel o Sheets selecciona la columna de total y mira la suma en la barra de abajo. Debe calzar con lo que dijo ChatGPT en el paso 6.",
                "Cantidad de filas: debe ser igual a la que informó ChatGPT.",
                "Un día al azar: filtra ese día en tu planilla y compara el total con la barra del gráfico.",
                "Si algo no calza, pídele: \"Muéstrame cómo calculaste el total del día 12 y qué filas usaste.\"",
            ],
        ),
        (
            "Guarda lo que te sirvió",
            "Descarga o copia los gráficos y tablas que vas a usar. Si quieres repetir el análisis el próximo mes, guarda tus instrucciones en una nota del teléfono. "
            "Si no vas a volver a usar ese chat, bórralo, y elimina también el archivo desde la Biblioteca de ChatGPT: borrar el chat no borra el archivo guardado ahí.",
            [],
        ),
    ],
    prueba=(
        "Funciona si el total del mes, la cantidad de filas y el total de un día al azar que te dio ChatGPT calzan con tu planilla. "
        "Si los tres calzan, puedes confiar en los gráficos de ese chat."
    ),
    errores=[
        "ChatGPT dice que no puede leer el archivo o lo analiza a medias: revisa que tenga una sola tabla, sin filas vacías ni celdas combinadas. Si es muy grande, sepáralo por semana.",
        "Los totales no calzan: suele pasar cuando quedó una fila de totales dentro de la tabla, o cuando los montos tienen el signo $ o puntos de miles como texto. Bórrala o pídele que revise esa columna.",
        "Aparece el aviso de límite de carga: en el plan Gratis puedes subir 3 archivos al día. Espera al día siguiente o trabaja en el mismo chat con el archivo que ya subiste.",
        "El gráfico no es el que querías: pide el tipo exacto (\"gráfico de líneas\", \"barras por semana\") y la columna que debe usar.",
    ],
    fuentes=[
        "https://help.openai.com/es-419/articles/8437071-data-analysis-with-chatgpt",
        "https://help.openai.com/es-419/articles/8555545-uploading-files-and-audio-to-chatgpt",
        "https://help.openai.com/es-419/articles/7730893-data-controls-in-chatgpt",
    ],
)
