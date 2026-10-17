import reflex as rx
from solar_crm.frontend.theme import GREEN, GREEN_DARK, GREEN_SOFT, TEXT, MUTED, SURFACE, BG, BORDER, FONT
from solar_crm.core.states.auth import AuthState
from solar_crm.frontend.componentes import panel, input_field, header, footer

@rx.page(route="/login", title="Acceso | Solara")
def login_page() -> rx.Component:
    return rx.box(
        header(),

        rx.center(
            rx.box(
                panel(
                    rx.center(
                        rx.box(
                            rx.icon(
                                "lock-keyhole",
                                color=GREEN,
                                size=22,
                            ),
                            background=GREEN_SOFT,
                            border_radius="12px",
                            padding="12px",
                        ),
                    ),
                    rx.heading(
                        "Qué gusto verte.",
                        size="6",
                        color=TEXT,
                        text_align="center",
                        margin_top="16px",
                    ),
                    rx.text(
                        "Accede al espacio comercial de Solara.",
                        color=MUTED,
                        font_size="12px",
                        text_align="center",
                        margin_y="5px",
                        margin_bottom="15px"
                    ),

                    rx.form(
                        rx.vstack(
                            input_field(
                                "Usuario o correo",
                                AuthState.user,
                                AuthState.set_user,
                                "tu.usuario",
                            ),

                            rx.vstack(
                                rx.hstack(
                                    rx.text(
                                        "Contraseña",
                                        font_size="12px",
                                        font_weight="600",
                                        color=MUTED,
                                    ),
                                    rx.spacer(),
                                    rx.button(
                                        rx.cond(
                                            AuthState.show_password,
                                            "Ocultar",
                                            "Mostrar",
                                        ),
                                        on_click=AuthState.toggle_password,
                                        variant="ghost",
                                        size="1",
                                        color=GREEN,
                                        type="button",
                                    ),
                                    width="100%",
                                ),
                                rx.input(
                                    value=AuthState.password,
                                    on_change=AuthState.set_password,
                                    type=rx.cond(
                                        AuthState.show_password,
                                        "text",
                                        "password",
                                    ),
                                    placeholder="Ingresa tu contraseña",
                                    width="100%",
                                    background=SURFACE,
                                    border=f"1px solid {BORDER}",
                                    border_radius="9px",
                                    padding="10px 12px",
                                    color=TEXT,
                                    font_size="13px",
                                ),
                                spacing="1",
                                align_items="stretch",
                                width="100%",
                            ),

                            rx.cond(
                                AuthState.error != "",
                                rx.callout(
                                    AuthState.error,
                                    icon="alert-circle",
                                    color_scheme="red",
                                    width="100%",
                                ),
                                rx.box(),
                            ),

                            rx.button(
                                rx.hstack(
                                    rx.text("Iniciar sesión"),
                                    rx.icon("arrow-right", size=16),
                                    spacing="2",
                                ),
                                type="submit",
                                width="100%",
                                justify_content="center",
                                background=GREEN,
                                color="white",
                                border_radius="10px",
                                padding="12px",
                                font_weight="650",
                                _hover={"background": GREEN_DARK},
                            ),
                            spacing="4",
                            width="100%",
                        ),
                        on_submit=AuthState.login,
                        width="100%",
                    ),

                    rx.divider(margin_y="20px"),

                    rx.hstack(
                        rx.icon("shield-check", color=MUTED, size=15),
                        rx.text(
                            "Modo demostración",
                            font_size="10px",
                            color=MUTED,
                        ),
                        justify="center",
                        spacing="2",
                    ),

                    width="100%",
                    padding="24px",
                    box_shadow="0 16px 40px rgba(15,23,42,.06)",
                ),
                width="100%",
                max_width="360px",
            ),
            width="100%",
            padding="40px 16px",
            flex="1",
        ),

        footer(),
        width="100%",
        min_height="100vh",
        display="flex",
        flex_direction="column",
        background=BG,
        font_family=FONT,
    )