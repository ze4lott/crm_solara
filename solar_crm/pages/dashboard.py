import reflex as rx
from solar_crm.core.states.dashboard import DashboardState
from solar_crm.core.states.auth import AuthState
from solar_crm.frontend.componentes import (
    sidebar,
    topbar,
    page_heading,
    button,
    stat_card,
    panel,
    input_field,
    project_card,
    activity_row
)
from solar_crm.frontend.theme import BG, FONT, TEXT, MUTED, GREEN, BORDER, GREEN_SOFT, GREEN_DARK
from solar_crm.core.mock_data import DEMO_PROSPECTS, DEMO_ACTIVITIES


def money(value: float) -> str:
    return f"${value:,.2f}"

# -----------------------------------------------------------------------------
# Módulos del dashboard
# -----------------------------------------------------------------------------

def overview_module() -> rx.Component:
    return rx.vstack(
        page_heading(
            "Resumen ejecutivo",
            "Una vista clara del pipeline comercial y la operación solar.",
            button(
                "Nueva cotización",
                "plus",
                lambda: DashboardState.set_active_module("cotizador"),
                True
            )
        ),
        rx.grid(
            stat_card(
                "PROSPECTOS",
                DashboardState.prospectos.length(),
                "Registros en seguimiento",
                "users"
            ),
            stat_card(
                "PIPELINE COMERCIAL",
                DashboardState.total_pipeline.to(str),
                "Valor potencial activo · MXN",
                "trending-up",
                "#2563EB"
            ),
            stat_card(
                "COTIZACIONES",
                DashboardState.cotizaciones.length(),
                "Propuestas en el sistema",
                "file-text",
                "#7C3AED"
            ),
            stat_card(
                "CAPACIDAD COTIZADA",
                rx.text(DashboardState.capacidad_total.to(str)," kWp"),
                "Suma de propuestas",
                "sun",
                "#D97706"
            ),
            columns=rx.breakpoints(initial="1", sm="2", xl="4"),
            spacing="4",
            width="100%"
        ),
        panel(
            rx.hstack(
                rx.heading(
                    "Prospectos recientes",
                    size="4",
                    color=TEXT
                ),
                rx.spacer(),
                rx.button(
                    "Ver prospectos",
                    on_click=lambda: DashboardState.set_active_module("prospectos"),
                    variant="ghost",
                    color=GREEN
                )
            ),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Empresa"),
                        rx.table.column_header_cell("Contacto"),
                        rx.table.column_header_cell("Etapa"),
                        rx.table.column_header_cell("Valor potencial")
                    )
                ),
                rx.table.body(
                    *[
                        rx.table.row(
                            rx.table.cell(
                                rx.text(
                                    p["empresa"],
                                    font_weight="600",
                                    color=TEXT,
                                    font_size="12px"
                                )
                            ),
                            rx.table.cell(
                                rx.text(
                                    p["nombre"],
                                    color=MUTED,
                                    font_size="12px"
                                )
                            ),
                            rx.table.cell(
                                rx.badge(
                                    p["etapa"],
                                    color_scheme="green" if p["etapa"] in ["Ganado", "Cotización enviada"] else "gray"
                                )
                            ),
                            rx.table.cell(
                                rx.text(
                                    money(p["valor"]),
                                    color=TEXT,
                                    font_size="12px"
                                )
                            )
                        )
                        for p in DEMO_PROSPECTS[:5]
                    ]
                ),
                width="100%",
                variant="surface",
                size="2"
            ),
            margin_top="18px"
        ),
        spacing="4",
        width="100%"
    )

def prospects_module() -> rx.Component:
    return rx.vstack(
        page_heading("Prospectos", "Organiza contactos y oportunidades desde el primer acercamiento."),
        rx.cond(DashboardState.toast != "", rx.callout(DashboardState.toast, icon="check-circle", color_scheme="green", width="100%"), rx.box()),
        panel(
            rx.heading("Nuevo prospecto", size="4", color=TEXT),
            rx.grid(
                input_field("Nombre de contacto", DashboardState.nuevo_nombre, lambda v: DashboardState.set_form_value("nuevo_nombre", v), "Nombre completo"),
                input_field("Empresa", DashboardState.nueva_empresa, lambda v: DashboardState.set_form_value("nueva_empresa", v), "Empresa o razón social"),
                input_field("Correo", DashboardState.nuevo_correo, lambda v: DashboardState.set_form_value("nuevo_correo", v), "correo@empresa.mx"),
                input_field("Consumo mensual (kWh)", DashboardState.nuevo_consumo, lambda v: DashboardState.set_form_value("nuevo_consumo", v), "10000", "number"),
                rx.vstack(rx.text("Sector", font_size="12px", font_weight="600", color=MUTED), rx.select(["Industrial", "Comercial", "Residencial", "Agroindustrial", "Logística", "Servicios"], value=DashboardState.nuevo_sector, on_change=lambda v: DashboardState.set_form_value("nuevo_sector", v), width="100%"), spacing="1", align_items="stretch"),
                columns={"initial": "1", "md": "2", "lg": "3"}, spacing="3", margin_top="16px"),
            rx.hstack(rx.spacer(), button("Guardar prospecto", "plus", DashboardState.create_prospect, True), width="100%", margin_top="14px")),
        panel(
            rx.hstack(rx.heading("Todos los prospectos", size="4", color=TEXT), rx.spacer(), rx.text(DashboardState.filtered_prospectos.length(), " registros", font_size="12px", color=MUTED)),
            rx.box(rx.table.root(
                rx.table.header(rx.table.row(rx.table.column_header_cell("Empresa / contacto"), rx.table.column_header_cell("Sector"), rx.table.column_header_cell("Consumo mensual"), rx.table.column_header_cell("Etapa"), rx.table.column_header_cell("Valor potencial"), rx.table.column_header_cell("Acciones"))),
                rx.table.body(rx.foreach(DashboardState.filtered_prospectos, lambda p: rx.table.row(
                rx.table.cell(rx.vstack(rx.text(p["empresa"], font_size="12px", color=TEXT, font_weight="650"), rx.text(p["nombre"], font_size="11px", color=MUTED), spacing="1", align_items="start")),
                rx.table.cell(rx.text(p["sector"], font_size="12px", color=MUTED)),
                rx.table.cell(rx.text(p["consumo"].to(str), " kWh", font_size="12px", color=TEXT)),
                rx.table.cell(rx.badge(p["etapa"], color_scheme="green")),
                rx.table.cell(rx.text("$", p["valor"].to(str), font_size="12px", color=TEXT)),
                rx.table.cell(rx.hstack(
                    rx.button(rx.icon("arrow-right", size=14), on_click=DashboardState.advance_prospect(p["id"]), variant="ghost", size="1", title="Avanzar etapa"),
                    rx.button(rx.icon("trash-2", size=14), on_click=DashboardState.delete_prospect(p["id"]), variant="ghost", color="#DC2626", size="1", title="Eliminar"),
                )),
            ))), width="100%", variant="surface", size="2"), overflow_x="auto", margin_top="16px")),
        spacing="4", width="100%")

def quote_calculator() -> rx.Component:
    return rx.vstack(page_heading("Cotizador solar", "Dimensionamiento preliminar y propuesta económica reactiva."),
        rx.cond(DashboardState.toast != "", rx.callout(DashboardState.toast, icon="check-circle", color_scheme="green", width="100%"), rx.box()),
        rx.grid(panel(rx.heading("Parámetros del sistema", size="4", color=TEXT), rx.text("Ajusta los datos para recalcular la propuesta al instante.", font_size="12px", color=MUTED),
            rx.vstack(input_field("Cliente / empresa", DashboardState.quote_cliente, lambda v: DashboardState.set_form_value("quote_cliente", v)),
                rx.grid(input_field("Consumo mensual (kWh)", DashboardState.quote_consumo, lambda v: DashboardState.set_form_value("quote_consumo", v, ), input_type="number"), input_field("Tarifa eléctrica (MXN/kWh)", DashboardState.quote_tarifa, lambda v: DashboardState.set_form_value("quote_tarifa", v), input_type="number"), columns="2", spacing="3"),
                rx.grid(input_field("Potencia del panel (W)", DashboardState.quote_panel, lambda v: DashboardState.set_form_value("quote_panel", v), input_type="number"), input_field("Horas solares pico", DashboardState.quote_hsp, lambda v: DashboardState.set_form_value("quote_hsp", v), input_type="number"), columns="2", spacing="3"),
                rx.grid(input_field("Factor de rendimiento (0–1)", DashboardState.quote_rendimiento, lambda v: DashboardState.set_form_value("quote_rendimiento", v), input_type="number"), input_field("Cobertura objetivo (%)", DashboardState.quote_cobertura, lambda v: DashboardState.set_form_value("quote_cobertura", v), input_type="number"), columns="2", spacing="3"),
                rx.grid(input_field("Margen comercial (%)", DashboardState.quote_margen, lambda v: DashboardState.set_form_value("quote_margen", v), input_type="number"), input_field("Descuento (%)", DashboardState.quote_descuento, lambda v: DashboardState.set_form_value("quote_descuento", v), input_type="number"), columns="2", spacing="3"),
                input_field("IVA configurable (%)", DashboardState.quote_iva, lambda v: DashboardState.set_form_value("quote_iva", v), input_type="number"), spacing="4", margin_top="20px")),
            panel(rx.hstack(rx.box(rx.icon("sun", color=GREEN, size=19), background=GREEN_SOFT, padding="10px", border_radius="11px"), rx.vstack(rx.text("RESUMEN DE PROPUESTA", color=MUTED, font_size="10px", font_weight="700", letter_spacing=".12em"), rx.text("Estimación fotovoltaica", color=TEXT, font_weight="650", font_size="15px"), spacing="1", align_items="start"), spacing="3"),
                rx.text("Inversión estimada", font_size="12px", color=MUTED, margin_top="24px"), rx.heading(DashboardState.quote_total.to(str), size="8", color=GREEN_DARK, letter_spacing="-.04em"),
                rx.text("MXN · impuestos incluidos", font_size="11px", color=MUTED), rx.divider(margin_y="18px"),
                rx.grid(rx.vstack(rx.text("Potencia instalada", font_size="11px", color=MUTED), rx.heading(DashboardState.quote_results["potencia_instalada"].to(str), " kWp", size="4", color=TEXT), spacing="1"), rx.vstack(rx.text("Paneles requeridos", font_size="11px", color=MUTED), rx.heading(DashboardState.quote_results["paneles"].to(str), size="4", color=TEXT), spacing="1"), columns="2", spacing="4"),
                rx.grid(rx.vstack(rx.text("Generación anual", font_size="11px", color=MUTED), rx.heading(DashboardState.quote_results["generacion_anual"].to(str), " kWh", size="4", color=TEXT), spacing="1"), rx.vstack(rx.text("Cobertura teórica", font_size="11px", color=MUTED), rx.heading(DashboardState.quote_results["cobertura_real"].to(str), "%", size="4", color=TEXT), spacing="1"), columns="2", spacing="4", margin_top="20px"),
                rx.divider(margin_y="18px"), rx.hstack(rx.text("Ahorro anual estimado", font_size="12px", color=MUTED), rx.spacer(), rx.text(DashboardState.quote_results["ahorro_anual"].to(str), " MXN", font_size="13px", font_weight="700", color=GREEN_DARK)),
                rx.hstack(rx.text("Recuperación simple", font_size="12px", color=MUTED), rx.spacer(), rx.text(rx.cond(DashboardState.quote_results["payback"] > 0, DashboardState.quote_results["payback"].to(str) + " años", "No estimable"), font_size="13px", font_weight="700", color=TEXT), margin_top="10px"),
                rx.callout("Estimación ilustrativa. La generación, inversión, ahorro e interconexión requieren validación técnica y comercial.", icon="info", color_scheme="gray", size="1", margin_top="20px"), button("Guardar cotización", "save", DashboardState.save_quote, True), spacing="3"), columns={"initial": "1", "lg": "1.05fr .95fr"}, spacing="4", width="100%"), spacing="4", width="100%")

def quotes_module() -> rx.Component:
    return rx.vstack(page_heading("Cotizaciones", "Controla versiones, importes y estado de cada propuesta.", button("Crear cotización", "plus", lambda: DashboardState.set_active_module("cotizador"), True)),
        rx.cond(DashboardState.toast != "", rx.callout(DashboardState.toast, icon="check-circle", color_scheme="green", width="100%"), rx.box()),
        panel(rx.hstack(rx.heading("Registro de cotizaciones", size="4", color=TEXT), rx.spacer(), rx.text(DashboardState.filtered_cotizaciones.length(), " propuestas", color=MUTED, font_size="12px")),
            rx.table.root(rx.table.header(rx.table.row(rx.table.column_header_cell("Folio"), rx.table.column_header_cell("Cliente"), rx.table.column_header_cell("Capacidad"), rx.table.column_header_cell("Total"), rx.table.column_header_cell("Estado"), rx.table.column_header_cell("Acciones"))),
                rx.foreach(DashboardState.filtered_cotizaciones, lambda q: rx.table.row(
                    rx.table.cell(rx.text(q["folio"], font_size="12px", font_weight="650", color=TEXT)),
                    rx.table.cell(rx.text(q["cliente"], font_size="12px", color=MUTED)),
                    rx.table.cell(rx.text(q["kwp"].to(str), " kWp", font_size="12px", color=TEXT)),
                    rx.table.cell(rx.text("$", q["total"].to(str), font_size="12px", color=TEXT)),
                    rx.table.cell(rx.select(["Borrador", "En revisión", "Enviada", "En negociación", "Aceptada", "Rechazada", "Vencida"], value=q["estado"], on_change=lambda status: DashboardState.set_quote_status(q["folio"], status), size="1", width="140px")),
                    rx.table.cell(rx.hstack(rx.button(rx.icon("copy", size=14), on_click=DashboardState.duplicate_quote(q["folio"]), variant="ghost", size="1", title="Duplicar"), rx.button(rx.icon("trash-2", size=14), on_click=DashboardState.delete_quote(q["folio"]), variant="ghost", color="#DC2626", size="1", title="Eliminar")))
                )), width="100%", variant="surface", size="2"), overflow_x="auto", margin_top="16px"), spacing="4", width="100%")

def projects_module() -> rx.Component:
    return rx.vstack(page_heading("Proyectos", "Seguimiento de instalaciones derivadas de oportunidades ganadas."),
        rx.grid(rx.foreach(DashboardState.proyectos, project_card), columns={"initial": "1", "md": "2", "xl": "3"}, spacing="4", width="100%"), spacing="4", width="100%")

def activities_module() -> rx.Component:
    return rx.vstack(page_heading("Actividades", "Mantén cada seguimiento comercial en movimiento."),
        rx.cond(DashboardState.toast != "", rx.callout(DashboardState.toast, icon="check-circle", color_scheme="green", width="100%"), rx.box()),
        panel(rx.heading("Nueva actividad", size="4", color=TEXT), rx.grid(input_field("Título", DashboardState.actividad_titulo, lambda v: DashboardState.set_form_value("actividad_titulo", v), "Ej. Seguimiento de propuesta"),
            rx.vstack(rx.text("Cliente", font_size="12px", font_weight="600", color=MUTED), rx.select([p["empresa"] for p in DEMO_PROSPECTS], value=DashboardState.actividad_cliente, on_change=lambda v: DashboardState.set_form_value("actividad_cliente", v), width="100%"), spacing="1", align_items="stretch"),
            rx.vstack(rx.text("Tipo", font_size="12px", font_weight="600", color=MUTED), rx.select(["Llamada", "Correo", "Reunión", "Visita técnica", "Cotización", "Ingeniería"], value=DashboardState.actividad_tipo, on_change=lambda v: DashboardState.set_form_value("actividad_tipo", v), width="100%"), spacing="1", align_items="stretch"), columns={"initial": "1", "md": "3"}, spacing="3"), rx.hstack(rx.spacer(), button("Agregar actividad", "plus", DashboardState.add_activity, True), width="100%", margin_top="14px")),
        panel(rx.heading("Agenda y seguimiento", size="4", color=TEXT), rx.vstack(rx.foreach(DashboardState.actividades, activity_row), spacing="0", margin_top="10px")), spacing="4", width="100%")

def config_module() -> rx.Component:
    return rx.vstack(page_heading("Configuración", "Ajusta supuestos y costos predeterminados del cotizador."),
        rx.cond(DashboardState.toast != "", rx.callout(DashboardState.toast, icon="check-circle", color_scheme="green", width="100%"), rx.box()),
        panel(rx.hstack(rx.box(rx.icon("sliders-horizontal", color=GREEN, size=20), background=GREEN_SOFT, border_radius="10px", padding="11px"), rx.vstack(rx.heading("Parámetros energéticos y comerciales", size="4", color=TEXT), rx.text("Valores demostrativos; valida con los costos reales de la empresa.", font_size="12px", color=MUTED), spacing="1", align_items="start"), spacing="3"),
            rx.grid(input_field("Precio de instalación por kWp (MXN)", DashboardState.config_precio_kwp, lambda v: DashboardState.set_form_value("config_precio_kwp", v), input_type="number"), input_field("IVA (%)", DashboardState.config_iva, lambda v: DashboardState.set_form_value("config_iva", v), input_type="number"), input_field("Horas solares pico diarias", DashboardState.config_hsp, lambda v: DashboardState.set_form_value("config_hsp", v), input_type="number"), input_field("Factor de rendimiento (0–1)", DashboardState.config_rendimiento, lambda v: DashboardState.set_form_value("config_rendimiento", v), input_type="number"), columns={"initial": "1", "md": "2"}, spacing="4", margin_top="24px"), rx.hstack(rx.spacer(), button("Guardar configuración", "save", DashboardState.save_config, True), width="100%", margin_top="22px")), spacing="4", width="100%")


# -----------------------------------------------------------------------------
# Content
# -----------------------------------------------------------------------------
def module_content() -> rx.Component:
    return rx.match(DashboardState.active_module,
        ("overview", overview_module()),
        ("prospectos", prospects_module()),
        ("cotizador", quote_calculator()),
        ("cotizaciones", quotes_module()),
        ("proyectos", projects_module()),
        ("actividades", activities_module()),
        ("configuracion", config_module()),
        overview_module())


# -----------------------------------------------------------------------------
# Page
# -----------------------------------------------------------------------------
@rx.page(
    route="/dashboard",
    title="Dashboard | Solara",
    on_load=[
        AuthState.require_auth,
        DashboardState.on_load
    ]
)
def dashboard_page() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            topbar(),
            rx.box(
                module_content(),
                width="100%",
                max_width="1600px",
                margin="0 auto",
                padding="28px",
                flex="1"
            ), width="100%",
            min_width="0",
            spacing="0",
            align_items="stretch",
            background=BG,
            min_height="100vh"
        ),
        width="100%",
        align="start",
        spacing="0",
        background=BG,
        font_family=FONT
    )

