import test from 'node:test';
import assert from 'node:assert/strict';
import { buildTrackingEvent, recommendAgent, validateAnswers } from '../assets/agente-diagnostico.js';

test('recomienda un agente de ventas por WhatsApp cuando ese es el canal y la prioridad', () => {
  const result = recommendAgent({
    business: 'restaurante',
    priority: 'clientes',
    channel: 'whatsapp',
    repetitive: 'consultas'
  });

  assert.equal(result.id, 'ventas-whatsapp');
  assert.equal(result.route, 'Más Clientes');
});

test('recomienda un agente de inventario cuando la prioridad es reducir pérdidas', () => {
  const result = recommendAgent({
    business: 'cafeteria',
    priority: 'inventario',
    channel: 'presencial',
    repetitive: 'stock'
  });

  assert.equal(result.id, 'inventario-reposicion');
  assert.equal(result.route, 'Mejor Negocio');
});

test('recomienda un agente de promociones cuando la prioridad es crear contenido', () => {
  const result = recommendAgent({
    business: 'restaurante',
    priority: 'contenido',
    channel: 'instagram',
    repetitive: 'publicaciones'
  });

  assert.equal(result.id, 'promociones-contenido');
  assert.equal(result.route, 'Más Clientes');
});

test('detecta respuestas obligatorias ausentes antes de recomendar', () => {
  assert.deepEqual(validateAnswers({ business: 'hotel', priority: 'clientes' }), ['channel', 'repetitive']);
});

test('recomienda un agente de atención cuando el cuello de botella son reservas y consultas', () => {
  const result = recommendAgent({
    business: 'hotel',
    priority: 'atencion',
    channel: 'telefono',
    repetitive: 'reservas'
  });

  assert.equal(result.id, 'atencion-reservas');
  assert.equal(result.route, 'Más Clientes');
});

test('recomienda un agente operativo cuando la prioridad es ordenar pedidos', () => {
  const result = recommendAgent({
    business: 'catering',
    priority: 'operacion',
    channel: 'email',
    repetitive: 'pedidos'
  });

  assert.equal(result.id, 'operacion-pedidos');
  assert.equal(result.route, 'Mejor Negocio');
});

test('crea eventos anónimos sin copiar datos personales', () => {
  const event = buildTrackingEvent('completed', {
    resultId: 'operacion-pedidos',
    business: 'catering',
    email: 'persona@example.com',
    rut: '12.345.678-9'
  });

  assert.deepEqual(event, {
    event: 'pp_diagnostico_completed',
    resource: 'agente-ia-pyme',
    result_id: 'operacion-pedidos',
    business: 'catering'
  });
});
