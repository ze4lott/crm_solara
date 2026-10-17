import reflex as rx
from solar_crm.frontend.theme import GREEN, SURFACE, TEXT, BORDER, GREEN_DARK, BG, MUTED, GREEN_SOFT
from solar_crm.core.states.dashboard import DashboardState
from solar_crm.core.states.auth import AuthState
from solar_crm.core.states.index import IndexState



NAV_ITEMS = [
    {"label": "Resumen", "icon": "layout-dashboard", "module": "overview"},
    {"label": "Prospectos", "icon": "users", "module": "prospectos"},
    {"label": "Cotizador solar", "icon": "calculator", "module": "cotizador"},
    {"label": "Cotizaciones", "icon": "file-text", "module": "cotizaciones"},
    {"label": "Proyectos", "icon": "panels-top-left", "module": "proyectos"},
    {"label": "Actividades", "icon": "calendar-check", "module": "actividades"},
    {"label": "Configuración", "icon": "settings", "module": "configuracion"},
]




# -----------------------------------------------------------------------------
# Componentes reutilizables
# -----------------------------------------------------------------------------
def button(label: str, icon: str | None = None, on_click=None, primary: bool = False) -> rx.Component:
    children = ([rx.icon(icon, size=16), rx.text(label)] if icon else [rx.text(label)])
    return rx.button(*children, on_click=on_click, background=GREEN if primary else SURFACE,
        color="white" if primary else TEXT, border=f"1px solid {GREEN if primary else BORDER}",
        border_radius="10px", padding="10px 14px", font_weight="600", font_size="13px",
        box_shadow="0 2px 5px rgba(15,23,42,.04)", cursor="pointer", _hover={"background": GREEN_DARK if primary else BG})


def input_field(label: str, value, on_change, placeholder: str = "", input_type: str = "text") -> rx.Component:
    return rx.vstack(rx.text(label, font_size="12px", font_weight="600", color=MUTED),
        rx.input(value=value, on_change=on_change, placeholder=placeholder, type=input_type,
                 width="100%", background=SURFACE, border=f"1px solid {BORDER}", border_radius="9px",
                 padding="10px 12px", color=TEXT, font_size="13px", _focus={"border_color": GREEN, "box_shadow": f"0 0 0 3px {GREEN}18"}),
        spacing="1", align_items="stretch", width="100%")


def panel(*children, **kwargs) -> rx.Component:
    return rx.box(
        *children,
        background=SURFACE,
        border=f"1px solid {BORDER}",
        border_radius="16px",
        padding="20px",
        width="100%",
    )


def page_heading(title: str, subtitle: str, actions: rx.Component | None = None) -> rx.Component:
    return rx.hstack(rx.vstack(rx.heading(title, size="6", color=TEXT, letter_spacing="-0.04em"), rx.text(subtitle, color=MUTED, font_size="13px"), spacing="1", align_items="start"), rx.spacer(), actions if actions is not None else rx.box(), align="center", width="100%", flex_wrap="wrap", gap="12px", margin_bottom="24px")


def stat_card(label: str, value, detail: str, icon: str, color: str = GREEN) -> rx.Component:
    return panel(rx.hstack(rx.box(rx.icon(icon, size=18, color=color), background=f"{color}14", border_radius="10px", padding="10px"), rx.spacer(), rx.icon("ellipsis", size=18, color="#94A3B8"), width="100%"),
        rx.text(label, color=MUTED, font_size="12px", font_weight="600", margin_top="16px"),
        rx.heading(value, size="7", color=TEXT, letter_spacing="-0.04em", margin_top="3px"),
        rx.text(detail, color=MUTED, font_size="11px", margin_top="5px"), height="150px")


def sidebar_item(item: dict[str, str]) -> rx.Component:
    active = DashboardState.active_module == item["module"]
    return rx.button(rx.icon(item["icon"], size=17), rx.text(item["label"], flex="1", text_align="left"),
        rx.cond(active, rx.box(width="5px", height="5px", border_radius="50%", background=GREEN), rx.box()),
        on_click=lambda: DashboardState.set_active_module(item["module"]), width="100%", display="flex", align_items="center", gap="12px",
        padding="11px 12px", border_radius="10px", border="1px solid transparent", cursor="pointer", font_size="13px", font_weight=rx.cond(active, "650", "500"),
        color=rx.cond(active, GREEN_DARK, MUTED), background=rx.cond(active, GREEN_SOFT, "transparent"),
        _hover={"background": rx.cond(active, GREEN_SOFT, BG), "color": TEXT})


def topbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(navigation_drawer(), rx.box(rx.icon("sun", size=19, color=GREEN), background=GREEN_SOFT, border_radius="10px", padding="9px"),
                  rx.vstack(rx.text("SOLARA", color=TEXT, font_size="14px", font_weight="800", letter_spacing="-.03em"), rx.text("ENERGY CRM", color=MUTED, font_size="9px", letter_spacing=".16em"), spacing="0", align_items="start"), spacing="3"),
        rx.box(rx.icon("search", size=16, color=MUTED), rx.input(value=DashboardState.search_query, on_change=DashboardState.set_search_query,
            placeholder="Buscar prospectos o cotizaciones…", border="none", outline="none", background="transparent", width="100%", font_size="13px", color=TEXT),
            rx.text("⌘ K", font_size="10px", color=MUTED, background=BG, border=f"1px solid {BORDER}", border_radius="5px", padding="3px 6px"),
            display="flex", align_items="center", gap="10px", flex="1", max_width="570px", padding="10px 12px", border=f"1px solid {BORDER}", border_radius="11px", background=BG),
        rx.spacer(),
        rx.button(rx.icon("bell", size=17), on_click=lambda: DashboardState.set_active_module("actividades"), variant="ghost", color=MUTED, border=f"1px solid {BORDER}", border_radius="10px", width="40px", height="40px"),
        rx.hstack(rx.box(rx.text(AuthState.user[:1], color=GREEN_DARK, font_weight="700"), width="36px", height="36px", display="flex", align_items="center", justify_content="center", border_radius="11px", background=GREEN_SOFT),
            rx.vstack(rx.text(AuthState.user, font_size="12px", font_weight="650", color=TEXT), rx.text("Gerencia comercial", font_size="10px", color=MUTED), spacing="0", align_items="start"), spacing="2"),
        rx.button(rx.icon("log-out", size=16), on_click=AuthState.logout, variant="ghost", color=MUTED, title="Cerrar sesión"),
        width="100%", padding="16px 28px", border_bottom=f"1px solid {BORDER}", background="rgba(255,255,255,.92)", backdrop_filter="blur(14px)", position="sticky", top="0", z_index="20", gap="18px", align="center")


def navigation_drawer() -> rx.Component:
    return rx.drawer.root(rx.drawer.trigger(rx.button(rx.icon("menu", size=20), variant="ghost", color=TEXT)),
        rx.drawer.overlay(background="rgba(15,23,42,.35)"),
        rx.drawer.portal(rx.drawer.content(rx.vstack(rx.hstack(rx.icon("sun", color=GREEN), rx.heading("SOLARA", size="5"), spacing="2"),
            rx.text("MÓDULOS", color=MUTED, font_size="10px", letter_spacing=".15em", font_weight="700", width="100%", margin_top="20px"),
            *[sidebar_item(item) for item in NAV_ITEMS], rx.spacer(), button("Cerrar sesión", "log-out", AuthState.logout), width="100%", height="100%", padding="24px", align_items="stretch"),
            width="290px", height="100%", background=SURFACE, padding="0")), direction="left")


def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon("sun", size=20, color=GREEN),
                    background=GREEN_SOFT,
                    border_radius="11px",
                    padding="10px"
                ),
                rx.vstack(
            rx.text("SOLARA", font_size="15px", font_weight="800", color=TEXT, letter_spacing="-.04em"),
                rx.text("ENERGY CRM", font_size="9px", color=MUTED, letter_spacing=".16em"),
                spacing="0", align_items="start"
                ),
            spacing="3",
            padding="4px 4px 26px"
            ),
        rx.text("ESPACIO DE TRABAJO", font_size="9px", font_weight="700", letter_spacing=".14em", color="#94A3B8", padding="0 12px 8px"),
        *[sidebar_item(item) for item in NAV_ITEMS], rx.spacer(),
        panel(rx.hstack(rx.icon("zap", color=GREEN, size=17), rx.text("Cotizador inteligente", font_size="12px", font_weight="650", color=TEXT)),
              rx.text("Cálculos preliminares en tiempo real", font_size="11px", color=MUTED, margin_top="7px"), background=BG, padding="13px", border_radius="12px"),
        rx.hstack(rx.box(rx.text(AuthState.user[:1].upper(), color=GREEN_DARK, font_weight="700"), background=GREEN_SOFT, border_radius="10px", width="38px", height="38px", display="flex", align_items="center", justify_content="center"),
                  rx.vstack(rx.text(AuthState.user, color=TEXT, font_size="12px", font_weight="650"), rx.text("Sesión de demostración", color=MUTED, font_size="10px"), spacing="0", align_items="start"), rx.spacer(), rx.button(rx.icon("log-out", size=15), on_click=AuthState.logout, variant="ghost", color=MUTED), padding="12px 4px 0", align="center", width="100%"),
        height="100vh", padding="24px 18px 18px", align_items="stretch", spacing="2", background=SURFACE, border_right=f"1px solid {BORDER}"), width="250px", min_width="250px", height="100vh", position="sticky", top="0")


def navbar_link(text: str, page, url: str, tamano: int) -> rx.Component:
    return rx.link(
        rx.button(text,
                  variant="ghost",
                  size="4",
                  color_scheme=rx.cond(IndexState.active_page == page, "lime", "grass"),
                  on_click=IndexState.set_active(page),
                  transition="all 0.2s ease-in-out",
                  font_size=tamano,
                  border_radius="75px"
                  ),
        href=url
    )


def header() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.center(
                rx.vstack(
                    rx.hstack(
                        # Logo
                        rx.hstack(
                            rx.box(
                                rx.icon("sun", size=21, color=GREEN),
                                background=GREEN_SOFT,
                                border_radius="11px",
                                padding="9px",
                            ),
                            rx.center(
                                rx.heading(
                                    "SOLARA",
                                    size="5",
                                    color=TEXT,
                                    letter_spacing="-.04em",
                                ),
                                margin_top="4px",
                                width="100%",
                            ),
                            spacing="3",
                            align="center",
                        ),

                        # Navegación centrada
                        rx.center(
                            rx.hstack(
                                navbar_link("Inicio", "home", "/", 16),
                                navbar_link(
                                    "Quiénes somos", "about", "/about", 16
                                ),
                                navbar_link(
                                    "Proyectos", "proyectos", "/proyectos", 16
                                ),
                                navbar_link(
                                    "Calculadora",
                                    "calculadora",
                                    "/calculadora",
                                    16,
                                ),
                                spacing="8",
                                align="center",
                                justify="center",
                            ),
                            flex="1",
                            width="100%",
                        ),

                        # Acceso a la derecha
                        rx.link(
                            button(
                                "Iniciar sesión",
                                "log_in",
                                rx.redirect("/login"),
                                True
                            ),
                            href="/login",
                        ),

                        width="100%",
                        align="center",
                        justify="between",
                        spacing="4",
                        background="white",
                        padding_x=rx.breakpoints(
                            md="24px",
                            lg="40px",
                            xl="56px",
                        ),
                        padding_y="14px",
                        border_bottom="1px solid #E8EEE8",
                    ),
                    spacing="0",
                    width="100%",
                    align="center",
                ),
                width="100%",
            )
        ),

        # Navegación móvil
        rx.mobile_and_tablet(
            rx.vstack(
                rx.hstack(
                    rx.hstack(
                        rx.box(
                            rx.icon("sun", size=21, color=GREEN),
                            background=GREEN_SOFT,
                            border_radius="11px",
                            padding="8px",
                        ),
                        rx.center(
                            rx.heading(
                                "SOLARA",
                                size="5",
                                color=TEXT,
                                letter_spacing="-.04em",
                            ),
                            margin_top="3px",
                            width="100%",
                        ),
                        spacing="3",
                        align="center",
                    ),

                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Iniciar sesión",
                                variant="outline",
                                color=GREEN,
                                border=f"1px solid {GREEN}",
                                border_radius="999px",
                                size="2",
                                background="white",
                                _hover={
                                    "background": GREEN_SOFT,
                                },
                            ),
                            href="/login",
                        ),
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.center(
                                    rx.icon(
                                        "menu",
                                        size=28,
                                        color=GREEN,
                                    ),
                                    width="100%",
                                )
                            ),
                            rx.menu.content(
                                rx.menu.item(
                                    navbar_link("Inicio", "home", "/", 16)
                                ),
                                rx.menu.item(
                                    navbar_link(
                                        "Quiénes somos",
                                        "about",
                                        "/about",
                                        16,
                                    )
                                ),
                                rx.menu.item(
                                    navbar_link(
                                        "Proyectos",
                                        "proyectos",
                                        "/proyectos",
                                        16,
                                    )
                                ),
                                rx.menu.item(
                                    navbar_link(
                                        "Calculadora",
                                        "calculadora",
                                        "/calculadora",
                                        16,
                                    )
                                ),
                            ),
                        ),
                        spacing="3",
                        align="center",
                    ),

                    width="100%",
                    align="center",
                    justify="between",
                ),
                spacing="0",
                width="100%",
                padding_x="18px",
                padding_y="12px",
                background="white",
                border_bottom="1px solid #E8EEE8",
            ),
        ),

        width="100%",
        padding="0px",
        background="white",
    )


def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.grid(
                rx.vstack(
                    rx.heading(
                        "SOLARA",
                        size="6",
                        color=TEXT,
                        font_weight="800",
                    ),
                    rx.text(
                        "Energía inteligente para un futuro sostenible.",
                        color=MUTED,
                        font_size="13px",
                    ),
                    align_items="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "CONTACTO",
                        color=TEXT,
                        font_size="11px",
                        font_weight="800",
                        letter_spacing=".12em",
                    ),
                    rx.hstack(
                        rx.icon("phone", size=15, color=GREEN),
                        rx.text(
                            "+52 55 1234 5678",
                            color=MUTED,
                            font_size="12px",
                        ),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("mail", size=15, color=GREEN),
                        rx.text(
                            "contacto@solara.example",
                            color=MUTED,
                            font_size="12px",
                        ),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("map-pin", size=15, color=GREEN),
                        rx.text(
                            "Av. Reforma 250, Ciudad de México, México",
                            color=MUTED,
                            font_size="12px",
                        ),
                        align="start",
                        spacing="2",
                    ),
                    align_items="start",
                    spacing="3",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "EXPLORA",
                        color=TEXT,
                        font_size="11px",
                        font_weight="800",
                        letter_spacing=".12em",
                    ),
                    rx.link(
                        "Inicio",
                        href="/",
                        color=MUTED,
                        font_size="12px",
                    ),
                    rx.link(
                        "Quiénes somos",
                        href="/about",
                        color=MUTED,
                        font_size="12px",
                    ),
                    rx.link(
                        "Proyectos",
                        href="/proyectos",
                        color=MUTED,
                        font_size="12px",
                    ),
                    rx.link(
                        "Calculadora solar",
                        href="/calculadora",
                        color=MUTED,
                        font_size="12px",
                    ),
                    align_items="start",
                    spacing="3",
                    width="100%",
                ),
                columns={"initial": "1", "md": "2", "lg": "3"},
                spacing="6",
                width="100%",
            ),
            rx.divider(color=BORDER),
            rx.hstack(
                rx.text(
                    "© 2026 SOLARA · Energía solar",
                    color=MUTED,
                    font_size="11px",
                ),
                rx.spacer(),
                rx.text(
                    "Diseñado para un futuro más limpio.",
                    color=MUTED,
                    font_size="11px",
                ),
                width="100%",
                align="center",
                flex_wrap="wrap",
            ),
            spacing="5",
            width="100%",
            max_width="1180px",
            margin="0 auto",
            padding="36px 28px 24px",
        ),
        border_top=f"1px solid {BORDER}",
        background=SURFACE,
        width="100%",
    )


def project_card(p: rx.Var) -> rx.Component:
    return panel(
        rx.hstack(rx.box(rx.icon("sun", color=GREEN), background=GREEN_SOFT, border_radius="10px", padding="10px"), rx.spacer(), rx.badge(p["etapa"], color_scheme="green")),
        rx.heading(p["nombre"], size="4", color=TEXT, margin_top="16px"), rx.text(p["cliente"], color=MUTED, font_size="12px"),
        rx.hstack(rx.text(p["kwp"].to(str), " kWp", color=TEXT, font_size="13px", font_weight="650"), rx.spacer(), rx.text(p["avance"].to(str), "%", color=GREEN, font_size="12px", font_weight="700"), margin_top="16px"),
        rx.box(rx.box(width=p["avance"].to(str) + "%", height="6px", background=GREEN, border_radius="99px"), background=BG, width="100%", height="6px", border_radius="99px", margin_top="8px"), height="190px")


def activity_row(a: rx.Var) -> rx.Component:
    return rx.hstack(
        rx.box(rx.icon("calendar-clock", color="#64748B", size=18), background=BG, border_radius="10px", padding="11px"),
        rx.vstack(rx.text(a["titulo"], color=TEXT, font_size="13px", font_weight="650"), rx.text(a["cliente"], " · ", a["tipo"], color=MUTED, font_size="11px"), rx.text(a["fecha"], color=MUTED, font_size="10px"), spacing="1", align_items="start"),
        rx.spacer(), rx.badge(a["estado"], color_scheme="green"),
        rx.button(rx.icon("check", size=14), on_click=DashboardState.complete_activity_title(a["titulo"]), variant="outline", size="1", title="Completar"),
        width="100%", padding="13px 0", border_bottom=f"1px solid {BORDER}", align="center")


def client_card(
    imagen: str,
    icono: str,
    nombre: str,
    ubicacion: str,
    capacidad: str,
    enfoque: str,
) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.image(
                src=imagen,
                width="100%",
                height="150px",
                object_fit="cover",
            ),
            rx.icon(
                icono,
                size=30,
                color=GREEN,
                position="absolute",
                top="12px",
                left="12px",
                background=BG,
                padding="6px",
                border_radius="8px",
            ),
            width="100%",
            position="relative",
            border_radius="14px",
            overflow="hidden",
        ),
        rx.vstack(
            rx.text(
                nombre,
                color=TEXT,
                font_size="16px",
                font_weight="700",
            ),
            rx.text(
                ubicacion,
                color=MUTED,
                font_size="11px",
            ),
            rx.divider(color=BORDER),
            rx.hstack(
                rx.vstack(
                    rx.text("CAPACIDAD", color=MUTED, font_size="9px"),
                    rx.heading(capacidad, size="5", color=TEXT),
                    align_items="start",
                    spacing="1",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.text("ENFOQUE", color=MUTED, font_size="9px"),
                    rx.text(
                        enfoque,
                        color=TEXT,
                        font_size="12px",
                        font_weight="600",
                    ),
                    align_items="start",
                    spacing="1",
                ),
                width="100%",
                align="center",
            ),
            align_items="start",
            spacing="3",
            width="100%",
            padding="18px",
        ),
        background=SURFACE,
        border=f"1px solid {BORDER}",
        border_radius="18px",
        spacing="0",
        width="100%",
        overflow="hidden",
    )
