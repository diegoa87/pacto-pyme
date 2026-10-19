HAZLO = dict(
    titulo="Hazlo tú: un formulario para pedir hora que llena tu planilla y te avisa por correo",
    intro=(
        "Vas a armar en n8n un formulario para una peluquería: el cliente deja su nombre, su teléfono y la hora que quiere. "
        "Cada respuesta queda guardada como una fila nueva en Google Sheets y a ti te llega un correo de aviso desde Gmail. "
        "Con calma, te toma alrededor de una hora la primera vez. Conviene hacerlo desde un computador, porque el editor de n8n es incómodo en el teléfono."
    ),
    necesitas=[
        "Una cuenta de Google (Gmail) que puedas usar para el negocio.",
        "Una planilla de Google Sheets nueva, con estos títulos en la primera fila: Fecha, Nombre, Teléfono, Servicio, Hora deseada.",
        "Una cuenta en n8n Cloud. Se parte con una prueba gratis de 14 días; después hay que elegir un plan pagado o n8n borra el espacio de trabajo.",
        "Un computador con navegador (Chrome, Edge o similar).",
    ],
    pasos=[
        (
            "Crea tu cuenta en n8n",
            "Entra a n8n.io y regístrate en la versión en la nube (n8n Cloud). Así no tienes que instalar nada. "
            "La prueba dura 14 días con las funciones del plan Pro y, si no pagas al final, vence sola sin cobros.",
            [
                "Anota en tu calendario el día en que termina la prueba.",
                "Si no vas a seguir, descarga tus workflows antes de que se borre el espacio.",
            ],
        ),
        (
            "Crea un workflow nuevo",
            "Un workflow es la receta: una lista de pasos que n8n hace solo, en orden. "
            "En el menú de la izquierda elige Personal y luego el botón Create workflow, arriba a la derecha. "
            "Haz clic en el nombre del workflow y cámbialo por algo claro, como \"Reservas peluquería\".",
            [],
        ),
        (
            "Agrega el disparador: el formulario",
            "El disparador es lo que hace partir la receta. Aquí parte cada vez que alguien envía el formulario. "
            "Haz clic en Add first step, busca \"form\" y elige el disparador On form submission (el nodo se llama n8n Form Trigger). "
            "Un nodo es cada cuadrito del dibujo: hace una sola cosa.",
            [
                "En Form Title escribe el título que verá el cliente, por ejemplo \"Pide tu hora en Peluquería Rosita\".",
                "En Form Description pon una frase corta: \"Te confirmamos por WhatsApp\".",
            ],
        ),
        (
            "Arma las preguntas del formulario",
            "En Form Elements usa Add Form Element para agregar cada pregunta. "
            "Para cada una eliges el texto que verá el cliente (Field Label) y el tipo de respuesta (Element Type).",
            [
                "Nombre: tipo Text, con Required Field activado (obligatorio).",
                "Teléfono: tipo Text, obligatorio.",
                "Servicio: tipo Dropdown (lista para elegir) con Corte, Tintura, Peinado.",
                "Día y hora deseada: tipo Date para el día y un campo Text para la hora.",
                "No pidas RUT, datos de salud ni datos bancarios. Para pedir hora no los necesitas.",
            ],
        ),
        (
            "Prueba el formulario solo",
            "Dentro del nodo aprieta Execute step. Se abre el formulario de prueba en otra pestaña: llénalo con datos inventados y envíalo. "
            "Vuelve a n8n y mira el panel de la derecha (la salida del nodo): ahí aparecen tus respuestas. "
            "Cada nodo tiene una entrada (lo que recibe, a la izquierda) y una salida (lo que entrega, a la derecha). Esa salida es la que usarás en los pasos siguientes.",
            [],
        ),
        (
            "Agrega Google Sheets y conecta tu cuenta",
            "Cierra el nodo con la x, aprieta el + que aparece después del formulario y busca \"Google Sheets\". Elige la acción para agregar una fila (Append Row). "
            "En Credential to connect with crea una credencial nueva y aprieta Sign in with Google. Una credencial es el permiso guardado para que n8n use tu cuenta; en n8n Cloud basta con iniciar sesión y aceptar.",
            [
                "Revisa en la ventana de Google qué permisos pide antes de aceptar.",
                "Usa la cuenta del negocio, no tu cuenta personal con todos tus archivos, si puedes.",
            ],
        ),
        (
            "Elige la planilla y arrastra los datos",
            "En Document elige tu planilla y en Sheet la pestaña. En Mapping Column Mode elige Map Each Column Manually: aparece una casilla por cada título de tu planilla. "
            "Ahora el paso clave: en el panel INPUT de la izquierda están las respuestas del formulario. Arrastra cada dato a su casilla (Nombre a Nombre, Teléfono a Teléfono). n8n escribe solo la referencia entre llaves.",
            [
                "Si no ves datos en INPUT, vuelve al paso 5 y envía otra prueba.",
                "Para la columna Fecha puedes arrastrar el campo de fecha de envío que trae el formulario, si aparece.",
            ],
        ),
        (
            "Prueba la planilla",
            "Aprieta Execute step dentro del nodo de Google Sheets y abre tu planilla: debería aparecer una fila nueva con los datos de prueba. "
            "Si salió en la columna equivocada, corrige el arrastre y prueba otra vez.",
            [],
        ),
        (
            "Agrega el aviso por Gmail",
            "Aprieta el + después de Google Sheets, busca \"Gmail\" y elige enviar un mensaje (Send a message). Conecta tu cuenta con Sign in with Google, igual que antes. "
            "En To pon tu correo, en Subject algo como \"Nueva reserva\" y en Message escribe el texto y arrastra desde INPUT el nombre, el teléfono y la hora.",
            [
                "En Email Type elige Text, que es lo más simple.",
                "En las opciones puedes apagar Append n8n attribution para que el correo no lleve la firma de n8n.",
            ],
        ),
        (
            "Prueba todo el recorrido",
            "Vuelve al dibujo y aprieta Execute workflow. Se abre el formulario de prueba: llénalo y envíalo. "
            "Los nodos se ponen verdes a medida que funcionan. Revisa que llegó la fila a la planilla y el correo a tu bandeja.",
            [],
        ),
        (
            "Publica el workflow",
            "Aprieta Publish en la parte de arriba del dibujo y confirma. Recién ahí funciona la dirección definitiva del formulario (Production URL), que encuentras dentro del nodo del formulario. "
            "Esa es la que compartes por WhatsApp, Instagram o en un código QR. El enlace de prueba (Test URL) solo funciona mientras tienes n8n abierto probando.",
            [
                "Las respuestas reales ya no aparecen en el editor: las ves en la pestaña Executions del workflow.",
            ],
        ),
        (
            "Apágalo cuando no lo uses",
            "Si cierras por vacaciones o cambias de sistema, despublica el workflow: en la parte de arriba toca Published y elige Unpublish (también está en la flecha junto al botón Publish). "
            "Así nadie sigue enviando reservas que nadie atiende y no gastas ejecuciones de tu plan.",
            [],
        ),
    ],
    prueba=(
        "Abre la Production URL desde tu teléfono, como si fueras un cliente, y envía una reserva. "
        "En menos de un minuto debería aparecer la fila en tu planilla y el correo en tu bandeja; si no, revisa la pestaña Executions para ver en qué paso se detuvo."
    ),
    errores=[
        "Compartiste el enlace de prueba en vez del definitivo. El Test URL deja de funcionar al cerrar la prueba; comparte la Production URL y confirma que el workflow está publicado.",
        "Cambiaste los títulos de la planilla después de configurar el nodo y los datos ya no calzan. Vuelve a elegir Mapping Column Mode en el nodo de Google Sheets para que lea los títulos nuevos y arrastra los campos otra vez.",
        "El panel INPUT sale vacío y no tienes qué arrastrar. Falta ejecutar el paso anterior: aprieta Execute step en el formulario, envía una prueba y vuelve a abrir el nodo.",
        "Se terminó la prueba gratis y el formulario dejó de responder. Si sigues usándolo, elige un plan antes del día 14; si no, avisa a tus clientes y saca el enlace de tus redes.",
    ],
    fuentes=[
        "https://docs.n8n.io/try-it-out/quickstart/",
        "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.formtrigger/",
        "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations/",
        "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues/",
        "https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations/",
        "https://docs.n8n.io/integrations/builtin/credentials/google/oauth-single-service/",
        "https://docs.n8n.io/data/data-mapping/data-mapping-ui/",
        "https://docs.n8n.io/workflows/publish/",
        "https://docs.n8n.io/deploy/use-n8n-cloud/start-your-free-trial/",
    ],
)
