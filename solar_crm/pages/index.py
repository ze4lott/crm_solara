import reflex as rx
from solar_crm.frontend.componentes import button, header, footer, client_card
from solar_crm.frontend.theme import BG, BORDER, GREEN, GREEN_SOFT, GREEN_DARK, TEXT, MUTED, SURFACE, FONT

@rx.page(route="/")
def index_page() -> rx.Component:
    return rx.box(
        rx.box(
            header(),
            border_bottom=f"1px solid {BORDER}",
            background="rgba(255,255,255,.88)"
        ),
        rx.box(
            rx.vstack(
                rx.box(
                    rx.hstack(
                        rx.text(
                            "ENERGÍA INTELIGENTE · DECISIONES CLARAS",
                            color=GREEN_DARK,
                            font_size="10px",
                            font_weight="750",
                            letter_spacing=".13em"
                        ),
                        spacing="2",
                        align="center"
                    ),
                    background=GREEN_SOFT,
                    padding="8px 12px",
                    border_radius="99px"
                ),
                rx.heading(
                    "Tu energía.\nTu inversión.\nTus números claros.",
                    size="9",
                    color=TEXT,
                    letter_spacing="-.065em",
                    line_height="1.03",
                    white_space="pre-line",
                    max_width="800px"
                ),
                rx.text(
                    "Explora el potencial de la energía solar para tu negocio con una estimación inicial de capacidad, inversión y ahorro.",
                    color=MUTED,
                    font_size="17px",
                    line_height="1.8",
                    max_width="650px"
                ),
                rx.hstack(
                    rx.link(
                        button(
                            "Calcular mi proyecto",
                            "calculator",
                            None,
                            True
                        ),
                        href="/calculadora"
                    ),
                    spacing="5",
                    align="center",
                    flex_wrap="wrap"
                ),
                rx.grid(
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "01",
                                color=GREEN,
                                font_size="12px",
                                font_weight="800",
                            ),
                            background=GREEN_SOFT,
                            padding="8px 12px",
                            border_radius="10px",
                        ),
                        rx.text(
                            "Dimensionamiento",
                            color=TEXT,
                            font_size="14px",
                            font_weight="700",
                        ),
                        rx.text(
                            "Una referencia inicial de capacidad.",
                            color=MUTED,
                            font_size="12px",
                            line_height="1.6",
                        ),
                        align_items="start",
                        spacing="2",
                        width="100%",
                        padding="18px",
                        background=SURFACE,
                        border=f"1px solid {BORDER}",
                        border_radius="16px",
                        height="100%",
                    ),
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "02",
                                color=GREEN,
                                font_size="12px",
                                font_weight="800",
                            ),
                            background=GREEN_SOFT,
                            padding="8px 12px",
                            border_radius="10px",
                        ),
                        rx.text(
                            "Inversión estimada",
                            color=TEXT,
                            font_size="14px",
                            font_weight="700",
                        ),
                        rx.text(
                            "Costos preliminares transparentes.",
                            color=MUTED,
                            font_size="12px",
                            line_height="1.6",
                        ),
                        align_items="start",
                        spacing="2",
                        width="100%",
                        padding="18px",
                        background=SURFACE,
                        border=f"1px solid {BORDER}",
                        border_radius="16px",
                        height="100%",
                    ),
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "03",
                                color=GREEN,
                                font_size="12px",
                                font_weight="800",
                            ),
                            background=GREEN_SOFT,
                            padding="8px 12px",
                            border_radius="10px",
                        ),
                        rx.text(
                            "Ahorro potencial",
                            color=TEXT,
                            font_size="14px",
                            font_weight="700",
                        ),
                        rx.text(
                            "Una primera mirada al retorno.",
                            color=MUTED,
                            font_size="12px",
                            line_height="1.6",
                        ),
                        align_items="start",
                        spacing="2",
                        width="100%",
                        padding="18px",
                        background=SURFACE,
                        border=f"1px solid {BORDER}",
                        border_radius="16px",
                        height="100%",
                    ),
                    columns=rx.breakpoints(initial="1", sm="3"),
                    spacing="4",
                    width="100%",
                    max_width="900px",
                    margin_top="28px",
                ),
                align_items="start",
                spacing="6",
                padding="78px 0 84px",
                width="100%",
                max_width="1180px",
                margin="0 auto",
                background_color=SURFACE
            ),
            padding="0 28px",
            background_color=SURFACE
        ),

        # Segunda sección
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "PROYECTOS SOLARES",
                            color=GREEN,
                            font_size="10px",
                            font_weight="800",
                            letter_spacing=".15em",
                        ),
                        rx.heading(
                            "Soluciones para distintas escalas.",
                            size="7",
                            color=TEXT,
                            letter_spacing="-.05em",
                        ),
                        rx.text(
                            "Ejemplos ilustrativos de cómo la energía solar "
                            "puede adaptarse a diferentes operaciones.",
                            color=MUTED,
                            font_size="13px",
                            line_height="1.7",
                            max_width="560px",
                        ),
                        align_items="start",
                        spacing="3",
                    ),
                    rx.spacer(),
                    rx.link(
                        rx.hstack(
                            rx.text("Ver proyectos", font_size="12px", font_weight="700"),
                            rx.icon("arrow-up-right", size=15),
                            spacing="2",
                            align="center",
                        ),
                        href="/proyectos",
                        color=GREEN,
                        underline="none",
                    ),
                    align="end",
                    width="100%",
                    flex_wrap="wrap",
                    spacing="4",
                ),
                rx.grid(
                    # Proyecto 1
                    client_card(
                        imagen="/imagen1.jpeg",
                        icono="factory",
                        nombre="Industrias del Centro",
                        ubicacion="Planta de manufactura · Querétaro",
                        capacidad="250 kWp",
                        enfoque="Autoconsumo",
                    ),
                    client_card(
                        imagen="/imagen2.webp",
                        icono="warehouse",
                        nombre="Logistica Horizonte",
                        ubicacion="Centro de distribución · Nuevo León",
                        capacidad="180 kWp",
                        enfoque="Demanda diurna",
                    ),
                    client_card(
                        imagen="/imagen3.jpg",
                        icono="building-2",
                        nombre="Corporativo Vértice",
                        ubicacion="Complejo de oficinas · Ciudad de México",
                        capacidad="195 kWp",
                        enfoque="Costos operativos",
                    ),
                    columns=rx.breakpoints(initial="1", md="2", lg="3"),
                    spacing="4",
                    width="100%",
                ),
                rx.text(
                    "Nombres, ubicaciones y capacidades ficticios para fines de demostración; "
                    "no representan instalaciones ejecutadas ni resultados verificados.",
                    color=MUTED,
                    font_size="10px",
                    line_height="1.6",
                ),
                align_items="start",
                spacing="5",
                width="100%",
                max_width="1180px",
                margin="0 auto",
                padding="68px 28px 84px",
            ),
            id="proyectos-destacados",
            width="100%",
            background=BG,
        ),

        # Tercera sección
        rx.box(
            rx.vstack(
                rx.vstack(
                    rx.text(
                        "POR QUÉ SOLARA",
                        color=GREEN,
                        font_size="11px",
                        font_weight="800",
                        letter_spacing=".16em",
                    ),
                    rx.heading(
                        "Decisiones energéticas con mayor claridad.",
                        size="7",
                        color=TEXT,
                        max_width="680px",
                        text_align="center",
                    ),
                    rx.text(
                        "Evalúa el potencial solar de tu instalación "
                        "antes de dar el siguiente paso.",
                        color=MUTED,
                        font_size="14px",
                        text_align="center",
                        max_width="560px",
                        line_height="1.8",
                    ),
                    align_items="center",
                    spacing="3",
                    width="100%",
                ),
                rx.grid(
                    rx.vstack(
                        rx.box(
                            rx.icon("chart-no-axes-combined", size=22, color=GREEN),
                            background=GREEN_SOFT,
                            padding="12px",
                            border_radius="12px",
                        ),
                        rx.heading(
                            "Análisis inicial",
                            size="4",
                            color=TEXT,
                        ),
                        rx.text(
                            "Comprende tu consumo y dimensiona "
                            "una posible solución solar.",
                            color=MUTED,
                            font_size="12px",
                            line_height="1.7",
                        ),
                        align_items="start",
                        spacing="3",
                        width="100%",
                        padding="22px",
                        background=SURFACE,
                        border=f"1px solid {BORDER}",
                        border_radius="18px",
                        height="100%",
                    ),
                    rx.vstack(
                        rx.box(
                            rx.icon("wallet", size=22, color=GREEN),
                            background=GREEN_SOFT,
                            padding="12px",
                            border_radius="12px",
                        ),
                        rx.heading(
                            "Visibilidad financiera",
                            size="4",
                            color=TEXT,
                        ),
                        rx.text(
                            "Consulta una inversión preliminar, "
                            "ahorro potencial y recuperación estimada.",
                            color=MUTED,
                            font_size="12px",
                            line_height="1.7",
                        ),
                        align_items="start",
                        spacing="3",
                        width="100%",
                        padding="22px",
                        background=SURFACE,
                        border=f"1px solid {BORDER}",
                        border_radius="18px",
                        height="100%",
                    ),
                    rx.vstack(
                        rx.box(
                            rx.icon("leaf", size=22, color=GREEN),
                            background=GREEN_SOFT,
                            padding="12px",
                            border_radius="12px",
                        ),
                        rx.heading(
                            "Enfoque sostenible",
                            size="4",
                            color=TEXT,
                        ),
                        rx.text(
                            "Explora alternativas para reducir "
                            "tu dependencia de la red eléctrica.",
                            color=MUTED,
                            font_size="12px",
                            line_height="1.7",
                        ),
                        align_items="start",
                        spacing="3",
                        width="100%",
                        padding="22px",
                        background=SURFACE,
                        border=f"1px solid {BORDER}",
                        border_radius="18px",
                        height="100%",
                    ),
                    columns={"initial": "1", "md": "3"},
                    spacing="4",
                    width="100%",
                ),
                align_items="center",
                spacing="7",
                width="100%",
                max_width="1180px",
                margin="0 auto",
                padding="80px 28px",
            ),
            background=BG,
            width="100%",
        ),
        footer(),
    )