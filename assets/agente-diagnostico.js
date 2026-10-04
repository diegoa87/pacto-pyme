const RECOMMENDATIONS = {
  'ventas-whatsapp': {
    id: 'ventas-whatsapp',
    route: 'Más Clientes',
    title: 'Agente de ventas por WhatsApp',
    summary: 'Responde consultas frecuentes, ordena oportunidades y ayuda a dar seguimiento sin reemplazar la atención humana.',
    tasks: ['Responder preguntas repetidas', 'Preparar respuestas según el tipo de consulta', 'Recordar seguimientos pendientes'],
    firstStep: 'Reúne las diez preguntas que más recibes y las respuestas que hoy entrega tu equipo.'
  },
  'inventario-reposicion': {
    id: 'inventario-reposicion',
    route: 'Mejor Negocio',
    title: 'Agente de inventario y reposición',
    summary: 'Ayuda a registrar faltantes, anticipar reposiciones y detectar productos con riesgo de merma.',
    tasks: ['Ordenar alertas de stock', 'Priorizar productos por revisar', 'Preparar una propuesta de reposición'],
    firstStep: 'Identifica tus veinte insumos más importantes y registra su consumo durante una semana.'
  },
  'promociones-contenido': {
    id: 'promociones-contenido',
    route: 'Más Clientes',
    title: 'Agente de promociones y contenido',
    summary: 'Convierte una oferta concreta en mensajes consistentes para WhatsApp y redes sociales.',
    tasks: ['Proponer promociones', 'Adaptar mensajes por canal', 'Organizar un calendario breve de publicaciones'],
    firstStep: 'Elige un producto, una audiencia y un objetivo comercial para la primera campaña.'
  },
  'atencion-reservas': {
    id: 'atencion-reservas',
    route: 'Más Clientes',
    title: 'Agente de atención y reservas',
    summary: 'Ordena consultas, propone respuestas y deriva a una persona cuando la conversación necesita criterio humano.',
    tasks: ['Clasificar consultas', 'Responder preguntas frecuentes', 'Preparar reservas para confirmación'],
    firstStep: 'Documenta horarios, condiciones de reserva, tiempos de respuesta y situaciones que siempre debe atender una persona.'
  },
  'operacion-pedidos': {
    id: 'operacion-pedidos',
    route: 'Mejor Negocio',
    title: 'Agente para ordenar pedidos y operación',
    summary: 'Estructura solicitudes, detecta información faltante y prepara cada pedido para revisión del equipo.',
    tasks: ['Registrar pedidos con un formato común', 'Detectar datos incompletos', 'Preparar resúmenes diarios'],
    firstStep: 'Define los datos mínimos de un pedido correcto y reúne ejemplos de casos simples y excepcionales.'
  }
};

export function buildTrackingEvent(name, context = {}) {
  const event = {
    event: `pp_diagnostico_${name}`,
    resource: 'agente-ia-pyme'
  };
  if (context.resultId) event.result_id = context.resultId;
  if (context.business) event.business = context.business;
  return event;
}

export function validateAnswers(answers) {
  return ['business', 'priority', 'channel', 'repetitive'].filter((key) => !answers[key]);
}

export function recommendAgent(answers) {
  if (answers.priority === 'inventario' || answers.repetitive === 'stock') {
    return RECOMMENDATIONS['inventario-reposicion'];
  }
  if (answers.priority === 'contenido' || answers.repetitive === 'publicaciones') {
    return RECOMMENDATIONS['promociones-contenido'];
  }
  if (answers.priority === 'atencion' || answers.repetitive === 'reservas') {
    return RECOMMENDATIONS['atencion-reservas'];
  }
  if (answers.priority === 'operacion' || answers.repetitive === 'pedidos') {
    return RECOMMENDATIONS['operacion-pedidos'];
  }
  if (answers.priority === 'clientes' && answers.channel === 'whatsapp') {
    return RECOMMENDATIONS['ventas-whatsapp'];
  }
  return RECOMMENDATIONS['ventas-whatsapp'];
}
