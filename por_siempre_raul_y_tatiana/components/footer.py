import reflex as rx
from por_siempre_raul_y_tatiana.routers import routers
from por_siempre_raul_y_tatiana.styles import footer_container_style
from por_siempre_raul_y_tatiana.components.componentes import tiempo_transcurrido, footer_boton


def pie_de_pagina() -> rx.Component:
    return rx.container(
        tiempo_transcurrido(),
        footer_boton("Viaja A Recuerdos Maravillosos ➡", routers.RECUERDOS.value),
        background_image=f"url({rx.asset('pagina-principal/BACKGROUND_FINAL.png')})",
        style=footer_container_style,
    )


def pie_de_pagina_2() -> rx.Component:
    return rx.container(
        tiempo_transcurrido(),
        footer_boton("Mira Mas Recuerdos Maravillosos ➡", routers.RECUERDOS.value),
        footer_boton("Regresa donde todo inicio ➡", routers.PRINCIPAL.value),
        background_image=f"url({rx.asset('pagina-principal/BACKGROUND_FINAL.png')})",
        style=footer_container_style,
    )
