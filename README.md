# Solara CRM — frontend-only con Reflex

MVP de CRM solar con exactamente tres rutas: `/`, `/login` y `/dashboard`.

## Características

- Landing minimalista con calculadora solar pública.
- Login de demostración que acepta cualquier usuario y contraseña no vacíos.
- Dashboard modular con sidebar y drawer responsive.
- Módulos internos: resumen, prospectos, cotizador, cotizaciones, proyectos, actividades y configuración.
- Cálculos energéticos y económicos en Python/Reflex State.
- Datos ficticios en memoria; no hay base de datos ni persistencia al reiniciar.

## Ejecutar

Requiere Python 3.10 o superior.

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate      # Windows
pip install -e .
reflex init
reflex run
```

Si `reflex init` solicita sobrescribir archivos, conserva `rxconfig.py` y el paquete `solar_crm`.

## Notas

- Los precios y parámetros incluidos son ilustrativos, no cotizaciones de mercado.
- El login no es seguro y solo sirve para demostración.
- Los cálculos solares son preliminares y deben validarse con ingeniería, tarifas y condiciones reales.
- Las modificaciones se conservan únicamente en el estado de la sesión.
# crm_solara
