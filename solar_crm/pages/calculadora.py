import reflex as rx
from solar_crm.frontend.theme import GREEN, TEXT, MUTED, GREEN_SOFT, GREEN_DARK, BG
from solar_crm.frontend.componentes import panel, input_field, footer
from solar_crm.core.states.calculator import PublicCalculatorState
from solar_crm.frontend.componentes import header


@rx.page(route="/calculadora")
def calc_page() -> rx.Component:
    return rx.box(
        header(),
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "CALCULADORA SOLAR",
                        color=GREEN,
                        font_size="10px",
                        font_weight="800",
                        letter_spacing=".16em",
                    ),
                    rx.heading(
                        "Empieza con una estimación.",
                        size="7",
                        color=TEXT,
                        letter_spacing="-.05em",
                    ),
                    rx.text(
                        "Modifica los parámetros y observa cómo cambia el escenario.",
                        color=MUTED,
                        font_size="13px",
                    ),
                    spacing="2",
                    align_items="start",
                ),
                rx.spacer(),
                rx.box(
                    rx.icon(
                        "calculator",
                        color=GREEN,
                        size=22,
                    ),
                    background=GREEN_SOFT,
                    border_radius="12px",
                    padding="12px",
                ),
                width="100%",
                align="start",
            ),
            rx.grid(
                panel(
                    rx.heading(
                        "Datos de consumo",
                        size="4",
                        color=TEXT,
                    ),
                    rx.vstack(
                        input_field(
                            "Consumo mensual (kWh)",
                            PublicCalculatorState.consumo,
                            lambda v: PublicCalculatorState.update(
                                "consumo", v
                            ),
                            "18000",
                            "number",
                        ),
                        input_field(
                            "Tarifa eléctrica (MXN/kWh)",
                            PublicCalculatorState.tarifa,
                            lambda v: PublicCalculatorState.update(
                                "tarifa", v
                            ),
                            "2.70",
                            "number",
                        ),
                        rx.grid(
                            input_field(
                                "Panel (W)",
                                PublicCalculatorState.panel,
                                lambda v: PublicCalculatorState.update(
                                    "panel", v
                                ),
                                "600",
                                "number",
                            ),
                            input_field(
                                "Horas solares pico",
                                PublicCalculatorState.hsp,
                                lambda v: PublicCalculatorState.update(
                                    "hsp", v
                                ),
                                "5.2",
                                "number",
                            ),
                            columns="2",
                            spacing="3",
                        ),
                        rx.grid(
                            input_field(
                                "Rendimiento (0–1)",
                                PublicCalculatorState.rendimiento,
                                lambda v: PublicCalculatorState.update(
                                    "rendimiento", v
                                ),
                                "0.80",
                                "number",
                            ),
                            input_field(
                                "Cobertura objetivo (%)",
                                PublicCalculatorState.cobertura,
                                lambda v: PublicCalculatorState.update(
                                    "cobertura", v
                                ),
                                "80",
                                "number",
                            ),
                            columns="2",
                            spacing="3",
                        ),
                        spacing="4",
                        margin_top="20px",
                    ),
                ),
                panel(
                    rx.text(
                        "RESULTADO PRELIMINAR",
                        color=MUTED,
                        font_size="10px",
                        font_weight="800",
                        letter_spacing=".14em",
                    ),
                    rx.heading(
                        PublicCalculatorState.investment.to(str),
                        size="8",
                        color=GREEN_DARK,
                        letter_spacing="-.05em",
                        margin_top="12px",
                    ),
                    rx.text(
                        "MXN · inversión estimada con supuestos ilustrativos",
                        color=MUTED,
                        font_size="11px",
                    ),
                    rx.divider(margin_y="20px"),
                    rx.grid(
                        rx.vstack(
                            rx.text(
                                "Potencia instalada",
                                font_size="11px",
                                color=MUTED,
                            ),
                            rx.heading(
                                PublicCalculatorState.result[
                                    "potencia_instalada"
                                ].to(str),
                                " kWp",
                                size="4",
                                color=TEXT,
                            ),
                            spacing="1",
                        ),
                        rx.vstack(
                            rx.text(
                                "Paneles estimados",
                                font_size="11px",
                                color=MUTED,
                            ),
                            rx.heading(
                                PublicCalculatorState.result[
                                    "paneles"
                                ].to(str),
                                size="4",
                                color=TEXT,
                            ),
                            spacing="1",
                        ),
                        columns="2",
                        spacing="4",
                    ),
                    rx.grid(
                        rx.vstack(
                            rx.text(
                                "Generación anual",
                                font_size="11px",
                                color=MUTED,
                            ),
                            rx.heading(
                                PublicCalculatorState.result[
                                    "generacion_anual"
                                ].to(str),
                                " kWh",
                                size="4",
                                color=TEXT,
                            ),
                            spacing="1",
                        ),
                        rx.vstack(
                            rx.text(
                                "Ahorro anual",
                                font_size="11px",
                                color=MUTED,
                            ),
                            rx.heading(
                                PublicCalculatorState.result[
                                    "ahorro_anual"
                                ].to(str),
                                " MXN",
                                size="4",
                                color=TEXT,
                            ),
                            spacing="1",
                        ),
                        columns="2",
                        spacing="4",
                        margin_top="18px",
                    ),
                    rx.hstack(
                        rx.text(
                            "Recuperación simple estimada",
                            color=MUTED,
                            font_size="12px",
                        ),
                        rx.spacer(),
                        rx.text(
                            rx.cond(
                                PublicCalculatorState.payback > 0,
                                PublicCalculatorState.payback.to(str)
                                + " años",
                                "No estimable",
                            ),
                            color=GREEN_DARK,
                            font_weight="750",
                            font_size="13px",
                        ),
                        margin_top="22px",
                    ),
                    rx.callout(
                        "Estimación orientativa, no constituye una oferta comercial. El resultado depende del sitio, sombras, perfil horario, tarifas, ingeniería y condiciones de interconexión.",
                        icon="info",
                        color_scheme="gray",
                        size="1",
                        margin_top="20px",
                    ),
                ),
                columns={"initial": "1", "lg": "1fr .95fr"},
                spacing="5",
                width="100%",
            ),
            id="calculadora",
            spacing="5",
            width="100%",
            max_width="1180px",
            margin="0 auto",
            padding="72px 28px 84px",
        ),
        footer(),
        background=BG,
        width="100%",
    )