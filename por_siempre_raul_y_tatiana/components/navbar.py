import reflex as rx
from por_siempre_raul_y_tatiana.styles import titulo_style, navbar_style
from por_siempre_raul_y_tatiana.routers import routers

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            style=titulo_style,
            font_size="2.47em",
            color="#fff",
            position="relative",
            top="-9px",
            _hover={"bg" : "#48e"}
            ),
        href=url
    )

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.image(
                src="/favicon.ico",
                width="2.75em",
                height="auto",
                border_radius="25%",
                margin="7px 10px"
            ),
            justify="start",
            align_items="center"
        ),
        rx.box(
            rx.hstack(
                navbar_link("Inicio" , routers.PRINCIPAL.value),
                navbar_link("Recurdos", routers.RECUERDOS.value),
                spacing="5",
                width="100%"
            ),
            position="absolute",
            right=50
        ),
        style=navbar_style
    )