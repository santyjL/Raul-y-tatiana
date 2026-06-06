import reflex as rx
from por_siempre_raul_y_tatiana.styles import (
    titulo_style,
    navbar_style,
    navbar_inner_style,
    navbar_links_style,
    navbar_link_style,
    combinar_estilos,
)
from por_siempre_raul_y_tatiana.routers import routers


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            style=combinar_estilos(titulo_style, navbar_link_style),
            _hover={"bg": "#48e"},
        ),
        href=url,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.desktop_only(
                rx.image(
                    src="/favicon.ico",
                    width="2.75em",
                    height="auto",
                    border_radius="25%",
                    position="relative",
                    top="-10px"
                ),
            ),
            rx.mobile_and_tablet(
                rx.image(
                src="/favicon.ico",
                width="2.75em",
                height="auto",
                border_radius="25%",
                )
            ),
            rx.hstack(
                navbar_link("Inicio", routers.PRINCIPAL.value),
                navbar_link("Recuerdos", routers.RECUERDOS.value),
                spacing="5",
                style=navbar_links_style,
            ),
            style=navbar_inner_style,
        ),
        style=navbar_style,
    )
