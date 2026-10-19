# Crea (idempotente) el formulario "Registro pymes — Chequeo Digital" en el proyecto Pacto Pyme
# de la org proyectos-adl, para los registros de alianzas.pactopyme.cl/mineconomia.
#
# Los leads quedan en el MISMO proyecto que los de pactopyme.cl y se distinguen por
# pp_origen = "Chequeo Digital". Reusa las propiedades de empresa de HORECA (pp_empresa_*,
# pp_razon_social, pp_autoriza_*), así el dato cae en el mismo campo de la ficha y no se duplica.
# Solo crea tres propiedades nuevas: pp_origen, pp_chequeo_nivel y pp_desafio_digital.
#
# En seco por defecto (todo se revierte). Para aplicar: -e APPLY=1
#   scp tools/mineconomia-recursos/setup_chequeo_digital_crm.rb root@65.109.64.130:/tmp/
#   ssh root@65.109.64.130 'C=$(docker ps --format "{{.Names}}" | grep "^crm-backend-rails" | head -1); \
#     docker cp /tmp/setup_chequeo_digital_crm.rb $C:/tmp/ && \
#     docker exec -e APPLY=1 $C bin/rails runner /tmp/setup_chequeo_digital_crm.rb'
APPLY = ENV["APPLY"] == "1"
ORG = "fcadc554-1412-467a-ba4b-275859456bda".freeze
TITLE = "Registro pymes — Chequeo Digital (Mineconomía)".freeze

NIVELES = ["Inicial", "Novato", "Competente", "Avanzado", "Experto", "No lo recuerdo"].freeze
DESAFIOS = ["Vender más por canales digitales", "Ordenar procesos y ahorrar tiempo", "Usar inteligencia artificial",
            "Gestionar datos para tomar decisiones", "Mejorar ciberseguridad", "Capacitar al equipo",
            "Elegir e implementar tecnología", "Otro"].freeze

# Propiedades nuevas (las demás ya existen y no se tocan)
NUEVAS = [
  { name: "pp_origen", label: "Origen del registro (Pacto Pyme)", options: ["Chequeo Digital"] },
  { name: "pp_chequeo_nivel", label: "Nivel obtenido en Chequeo Digital", options: NIVELES },
  { name: "pp_desafio_digital", label: "Principal desafío digital", options: DESAFIOS },
].freeze

# Campos del form, en el orden del landing. Las opciones de los select son las de la propiedad.
REUSADAS = %w[pp_empresa_rubro pp_empresa_tamano pp_empresa_region].freeze

RlsTenant.with_tenant(ORG) do
  # requires_new: with_tenant ya abre una transacción y un Rollback anidado sin savepoint se ignora
  ActiveRecord::Base.transaction(requires_new: true) do
    project = Project.find_by!(organization_id: ORG, slug: "pacto-pyme")
    puts "PROJECT  #{project.name} #{project.id}"

    NUEVAS.each do |n|
      d = CustomFieldDefinition.find_by(organization_id: ORG, entity: "contact", name: n[:name])
      if d
        union = ((d.options || []) + n[:options]).uniq
        d.update!(options: union, field_type: "enumeration") if union != (d.options || [])
        puts "DEF      ya existía #{n[:name]}"
      else
        CustomFieldDefinition.create!(organization_id: ORG, name: n[:name], label: n[:label], entity: "contact",
                                      field_type: "enumeration", options: n[:options], group_name: "Pacto Pyme",
                                      access: "Todos pueden ver y editar", is_required: false, hubspot_defined: false)
        puts "DEF      creada #{n[:name]}"
      end
    end

    opt = ->(k) { CustomFieldDefinition.find_by!(organization_id: ORG, entity: "contact", name: k).options }
    REUSADAS.each { |k| puts "REUSA    #{k} (#{opt.(k).size} opciones)" }

    fields = [
      { "key" => "pp_empresa_rut", "type" => "text", "label" => "RUT de la empresa", "required" => true, "format" => "rut" },
      { "key" => "pp_razon_social", "type" => "text", "label" => "Nombre de la empresa", "required" => true },
      { "key" => "pp_empresa_rubro", "type" => "select", "label" => "Rubro", "required" => true, "options" => opt.("pp_empresa_rubro") },
      { "key" => "pp_empresa_tamano", "type" => "select", "label" => "Tamaño de empresa", "required" => true, "options" => opt.("pp_empresa_tamano") },
      { "key" => "pp_empresa_region", "type" => "select", "label" => "Región", "required" => true, "options" => opt.("pp_empresa_region") },
      { "key" => "pp_empresa_comuna", "type" => "text", "label" => "Comuna", "required" => true },
      { "key" => "pp_chequeo_nivel", "type" => "select", "label" => "Nivel obtenido en Chequeo Digital", "required" => true, "options" => NIVELES },
      { "key" => "pp_desafio_digital", "type" => "select", "label" => "Principal desafío digital", "required" => true, "options" => DESAFIOS },
      { "key" => "firstname", "type" => "text", "label" => "Nombres", "required" => true },
      { "key" => "lastname", "type" => "text", "label" => "Apellidos", "required" => true },
      { "key" => "email", "type" => "email", "label" => "Correo", "required" => true },
      { "key" => "phone", "type" => "text", "label" => "Teléfono o WhatsApp", "required" => true, "format" => "phone" },
      { "key" => "pp_autoriza_datos", "type" => "text", "label" => "Autoriza el tratamiento de sus datos", "required" => true },
      { "key" => "pp_autoriza_comunicaciones", "type" => "text", "label" => "Quiere recibir novedades de Pacto Pyme", "required" => false },
    ]

    form = Form.find_by(organization_id: ORG, title: TITLE)
    if form
      form.update!(fields: fields, project_id: project.id, status: "published", redirect_url: nil)
      puts "FORM     actualizado"
    else
      form = Form.create!(organization_id: ORG, project_id: project.id, title: TITLE, fields: fields,
                          status: "published", created_by: "Rene Parada", updated_by: "Rene Parada")
      puts "FORM     creado"
    end
    puts "FORM_ID  #{form.id}"
    puts "CAMPOS   #{form.fields.size}"
    raise ActiveRecord::Rollback unless APPLY
  end
end
puts(APPLY ? "APLICADO" : "SECO: no se guardó nada (usar -e APPLY=1)")
