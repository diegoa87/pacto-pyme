export async function onRequest(context) {
  const { request, env } = context;
  if (request.method === 'GET') {
    return json({ ok: true, service: 'pacto-pyme-registro', storage: Boolean(env.DB) }, 200);
  }
  if (request.method !== 'POST') return json({ error: 'Método no permitido.' }, 405);
  if (!env.DB) return json({ error: 'El registro no está disponible temporalmente.' }, 503);

  const type = request.headers.get('content-type') || '';
  if (!type.includes('application/json')) return json({ error: 'Formato no permitido.' }, 415);
  let body;
  try { body = await request.json(); } catch { return json({ error: 'Solicitud inválida.' }, 400); }
  if (!body || typeof body !== 'object' || Array.isArray(body)) return json({ error: 'Solicitud inválida.' }, 400);
  if (String(body.website || '').trim()) return json({ ok: true, id: 'PP-RECIBIDO' }, 200);

  const started = Number(body.started_at || 0);
  if (!started || Date.now() - started < 1800) return json({ error: 'No pudimos validar el envío. Recarga la página e intenta nuevamente.' }, 400);

  const value = (name, max = 160) => String(body[name] || '').trim().replace(/[<>]/g, '').slice(0, max);
  const data = {
    rut: normalizeRut(value('rut', 20)), empresa: value('empresa'), rubro: value('rubro'), tamano: value('tamano'),
    region: value('region'), comuna: value('comuna'), madurez: value('madurez'), desafio: value('desafio'),
    nombre: value('nombre'), email: value('email', 180).toLowerCase(), telefono: value('telefono', 40),
    source: value('source', 100) || 'mineconomia-chequeo-digital', referrer: value('referrer', 300),
    comunicaciones: body.comunicaciones === true, acepta: body.acepta === true
  };
  const required = ['rut','empresa','rubro','tamano','region','comuna','madurez','desafio','nombre','email','telefono'];
  if (required.some(k => !data[k]) || !data.acepta) return json({ error: 'Revisa los campos obligatorios.' }, 400);
  if (!validRut(data.rut)) return json({ error: 'El RUT ingresado no es válido.' }, 400);
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) return json({ error: 'El correo ingresado no es válido.' }, 400);
  if (!['mineconomia-chequeo-digital','mineconomia-cursoia'].includes(data.source)) return json({ error: 'El origen del registro no es válido.' }, 400);
  if (!['Inicial','Novato','Competente','Avanzado','Experto','No lo recuerdo'].includes(data.madurez)) return json({ error: 'El nivel de madurez no es válido.' }, 400);

  try {
    const ipHash = await sha256(request.headers.get('CF-Connecting-IP') || 'unknown');
    const bucket = String(Math.floor(Date.now() / 60000));
    const rate = await env.DB.prepare(
      'INSERT INTO rate_limits (bucket, ip_hash, attempts) VALUES (?, ?, 1) ON CONFLICT(bucket, ip_hash) DO UPDATE SET attempts = attempts + 1 RETURNING attempts'
    ).bind(bucket, ipHash).first();
    if (Number(rate?.attempts || 1) > 5) return json({ error: 'Demasiados intentos. Espera un minuto e intenta nuevamente.' }, 429);

    const existing = await env.DB.prepare(
      'SELECT id FROM registrations WHERE source = ? AND rut = ? AND email = ? LIMIT 1'
    ).bind(data.source, data.rut, data.email).first();
    if (existing?.id) return json({ ok: true, id: existing.id, duplicate: true }, 200);

    const now = new Date().toISOString();
    const id = `PP-${now.slice(0,10).replaceAll('-','')}-${crypto.randomUUID().slice(0,8).toUpperCase()}`;
    const utm = Object.fromEntries(Object.entries(body).filter(([k]) => /^utm_(source|medium|campaign|content|term)$/.test(k)).map(([k,v]) => [k, String(v).slice(0,120)]));
    try {
      await env.DB.prepare(
        'INSERT INTO registrations (id, source, rut, empresa, rubro, tamano, region, comuna, madurez, desafio, nombre, email, telefono, comunicaciones, referrer, utm_json, country, created_at, consent_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
      ).bind(id, data.source, data.rut, data.empresa, data.rubro, data.tamano, data.region, data.comuna, data.madurez, data.desafio, data.nombre, data.email, data.telefono, data.comunicaciones ? 1 : 0, data.referrer, JSON.stringify(utm), request.cf?.country || null, now, now).run();
    } catch (error) {
      const raced = await env.DB.prepare('SELECT id FROM registrations WHERE source = ? AND rut = ? AND email = ? LIMIT 1').bind(data.source, data.rut, data.email).first();
      if (raced?.id) return json({ ok: true, id: raced.id, duplicate: true }, 200);
      throw error;
    }
    return json({ ok: true, id }, 201);
  } catch (error) {
    console.error('registration storage error', error instanceof Error ? error.message : 'unknown');
    return json({ error: 'No pudimos guardar el registro en este momento. Intenta nuevamente.' }, 503);
  }
}

function json(payload, status) {
  return new Response(JSON.stringify(payload), { status, headers: { 'Content-Type':'application/json; charset=utf-8', 'Cache-Control':'no-store', 'X-Content-Type-Options':'nosniff' } });
}
function normalizeRut(v) { return v.replace(/[^0-9kK]/g,'').toUpperCase(); }
function validRut(v) {
  if (!/^[0-9]{7,8}[0-9K]$/.test(v)) return false;
  const body=v.slice(0,-1), dv=v.slice(-1); let sum=0,m=2;
  for(let i=body.length-1;i>=0;i--){sum+=Number(body[i])*m;m=m===7?2:m+1;}
  const x=11-(sum%11), calc=x===11?'0':x===10?'K':String(x); return dv===calc;
}
async function sha256(text) {
  const bytes=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(text));
  return [...new Uint8Array(bytes)].map(b=>b.toString(16).padStart(2,'0')).join('');
}
