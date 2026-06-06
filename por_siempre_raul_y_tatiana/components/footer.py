import reflex as rx
from reflex_components_core.el import footer
from por_siempre_raul_y_tatiana.routers import routers
from por_siempre_raul_y_tatiana.components.componentes import tiempo_transcurrido, footer_boton

def pie_de_pagina () -> rx.Component:
    return rx.container(
        tiempo_transcurrido(),
        footer_boton("Viaja A Recuerdos Maravillosos ➡", routers.RECUERDOS.value ),
        background_image=f"url({rx.asset("pagina-principal/BACKGROUND_FINAL.png")})",
        background_color= "#cccccc",
        width="100%",
        height="900px",
        background_size="cover"
    ),

def pie_de_pagina_2 () -> rx.Component:
    return rx.container(
        tiempo_transcurrido(),
        footer_boton("Mira Mas Recuerdos Maravillosos ➡", routers.RECUERDOS.value ),
        footer_boton("Regresa donde todo inicio ➡", routers.PRINCIPAL.value ),
        background_image=f"url({rx.asset("pagina-principal/BACKGROUND_FINAL.png")})",
        background_color= "#cccccc",
        width="100%",
        height="900px",
        background_size="cover"
    ),