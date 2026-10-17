

DEMO_PROSPECTS = [
    {"id": 1, "nombre": "Mariana López", "empresa": "Frío Norte Industrial", "correo": "mariana@ejemplo.mx", "telefono": "55 5555 0101", "ciudad": "Querétaro, Qro.", "sector": "Industrial", "consumo": 48500, "tarifa": 2.72, "etapa": "Cotización enviada", "valor": 1280000},
    {"id": 2, "nombre": "Jorge Ramírez", "empresa": "Agroexport del Bajío", "correo": "jorge@ejemplo.mx", "telefono": "55 5555 0102", "ciudad": "León, Gto.", "sector": "Agroindustrial", "consumo": 22000, "tarifa": 2.48, "etapa": "Calificado", "valor": 690000},
    {"id": 3, "nombre": "Ana Torres", "empresa": "Plaza Alameda", "correo": "ana@ejemplo.mx", "telefono": "55 5555 0103", "ciudad": "Pachuca, Hgo.", "sector": "Comercial", "consumo": 13600, "tarifa": 2.91, "etapa": "Nuevo", "valor": 420000},
    {"id": 4, "nombre": "Ricardo Méndez", "empresa": "Empaques del Centro", "correo": "ricardo@ejemplo.mx", "telefono": "55 5555 0104", "ciudad": "Puebla, Pue.", "sector": "Industrial", "consumo": 61200, "tarifa": 2.65, "etapa": "Negociación", "valor": 1740000},
    {"id": 5, "nombre": "Sofía Hernández", "empresa": "Hotel Sierra", "correo": "sofia@ejemplo.mx", "telefono": "55 5555 0105", "ciudad": "San Miguel de Allende, Gto.", "sector": "Comercial", "consumo": 17400, "tarifa": 2.83, "etapa": "Visita técnica", "valor": 530000},
    {"id": 6, "nombre": "Luis Castillo", "empresa": "Riego Sustentable MX", "correo": "luis@ejemplo.mx", "telefono": "55 5555 0106", "ciudad": "Celaya, Gto.", "sector": "Agroindustrial", "consumo": 30500, "tarifa": 2.32, "etapa": "Contactado", "valor": 860000},
    {"id": 7, "nombre": "Paola Vega", "empresa": "Logística Horizonte", "correo": "paola@ejemplo.mx", "telefono": "55 5555 0107", "ciudad": "Toluca, Edo. Méx.", "sector": "Industrial", "consumo": 39000, "tarifa": 2.76, "etapa": "Ganado", "valor": 1120000},
    {"id": 8, "nombre": "Daniel Flores", "empresa": "Clínicas Vital", "correo": "daniel@ejemplo.mx", "telefono": "55 5555 0108", "ciudad": "CDMX", "sector": "Servicios", "consumo": 9700, "tarifa": 2.95, "etapa": "Perdido", "valor": 310000},
    {"id": 9, "nombre": "Fernanda Ruiz", "empresa": "Textiles Aurora", "correo": "fernanda@ejemplo.mx", "telefono": "55 5555 0109", "ciudad": "Aguascalientes, Ags.", "sector": "Industrial", "consumo": 27600, "tarifa": 2.58, "etapa": "Cotización en preparación", "valor": 790000},
    {"id": 10, "nombre": "Miguel Santos", "empresa": "Centro de Distribución Uno", "correo": "miguel@ejemplo.mx", "telefono": "55 5555 0110", "ciudad": "Tula, Hgo.", "sector": "Logística", "consumo": 52300, "tarifa": 2.69, "etapa": "Calificado", "valor": 1490000},
    {"id": 11, "nombre": "Claudia Pineda", "empresa": "Alimentos La Huerta", "correo": "claudia@ejemplo.mx", "telefono": "55 5555 0111", "ciudad": "Morelia, Mich.", "sector": "Alimentos", "consumo": 18900, "tarifa": 2.62, "etapa": "Nuevo", "valor": 580000},
    {"id": 12, "nombre": "Roberto Silva", "empresa": "Parque Empresarial Sur", "correo": "roberto@ejemplo.mx", "telefono": "55 5555 0112", "ciudad": "Cuernavaca, Mor.", "sector": "Inmobiliario", "consumo": 34200, "tarifa": 2.88, "etapa": "Negociación", "valor": 980000},
]
DEMO_QUOTES = [
    {"folio": "SOL-2026-001", "cliente": "Frío Norte Industrial", "kwp": 286.8, "total": 1280000, "estado": "Enviada"},
    {"folio": "SOL-2026-002", "cliente": "Agroexport del Bajío", "kwp": 154.2, "total": 690000, "estado": "Borrador"},
    {"folio": "SOL-2026-003", "cliente": "Empaques del Centro", "kwp": 390.0, "total": 1740000, "estado": "En negociación"},
    {"folio": "SOL-2026-004", "cliente": "Hotel Sierra", "kwp": 118.8, "total": 530000, "estado": "En revisión"},
    {"folio": "SOL-2026-005", "cliente": "Logística Horizonte", "kwp": 250.8, "total": 1120000, "estado": "Aceptada"},
    {"folio": "SOL-2026-006", "cliente": "Textiles Aurora", "kwp": 176.4, "total": 790000, "estado": "Borrador"},
    {"folio": "SOL-2026-007", "cliente": "Centro de Distribución Uno", "kwp": 333.0, "total": 1490000, "estado": "Enviada"},
    {"folio": "SOL-2026-008", "cliente": "Plaza Alameda", "kwp": 93.6, "total": 420000, "estado": "Borrador"},
]
DEMO_PROJECTS = [
    {"nombre": "Planta fotovoltaica LN-01", "cliente": "Logística Horizonte", "kwp": 250.8, "etapa": "Instalación", "avance": 68},
    {"nombre": "Sistema solar AG-02", "cliente": "Agroexport del Bajío", "kwp": 154.2, "etapa": "Ingeniería", "avance": 32},
    {"nombre": "Techo solar FN-03", "cliente": "Frío Norte Industrial", "kwp": 286.8, "etapa": "Planeación", "avance": 15},
    {"nombre": "Sistema EMP-04", "cliente": "Empaques del Centro", "kwp": 390.0, "etapa": "Preparación", "avance": 45},
    {"nombre": "Hotel Sierra HS-05", "cliente": "Hotel Sierra", "kwp": 118.8, "etapa": "Puesta en marcha", "avance": 88},
]
DEMO_ACTIVITIES = [
    {"titulo": "Seguimiento de propuesta", "cliente": "Frío Norte Industrial", "tipo": "Llamada", "fecha": "Hoy · 11:30", "estado": "Pendiente"},
    {"titulo": "Validar recibos eléctricos", "cliente": "Agroexport del Bajío", "tipo": "Correo", "fecha": "Hoy · 13:00", "estado": "Pendiente"},
    {"titulo": "Visita de levantamiento", "cliente": "Hotel Sierra", "tipo": "Visita técnica", "fecha": "Mañana · 10:00", "estado": "Pendiente"},
    {"titulo": "Revisar condiciones comerciales", "cliente": "Empaques del Centro", "tipo": "Reunión", "fecha": "Mañana · 16:00", "estado": "Pendiente"},
    {"titulo": "Enviar ficha técnica", "cliente": "Plaza Alameda", "tipo": "Correo", "fecha": "14 oct · 09:00", "estado": "Completada"},
    {"titulo": "Confirmar visita a planta", "cliente": "Riego Sustentable MX", "tipo": "Llamada", "fecha": "15 oct · 12:00", "estado": "Pendiente"},
    {"titulo": "Actualizar propuesta", "cliente": "Textiles Aurora", "tipo": "Cotización", "fecha": "16 oct · 15:00", "estado": "Pendiente"},
    {"titulo": "Revisar factibilidad", "cliente": "Centro de Distribución Uno", "tipo": "Ingeniería", "fecha": "17 oct · 11:00", "estado": "Pendiente"},
    {"titulo": "Enviar agradecimiento", "cliente": "Clínicas Vital", "tipo": "Correo", "fecha": "Ayer · 16:30", "estado": "Completada"},
    {"titulo": "Calificar oportunidad", "cliente": "Alimentos La Huerta", "tipo": "Llamada", "fecha": "18 oct · 10:30", "estado": "Pendiente"},
]