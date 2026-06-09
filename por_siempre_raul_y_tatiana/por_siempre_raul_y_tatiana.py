import reflex as rx
from por_siempre_raul_y_tatiana.styles import (
    body,
    contenedor_pagina_style,
    espaciador_style,
    seccion_contenido_style,
    seccion_hstack_style,
)
from por_siempre_raul_y_tatiana.components.imagenes import imagen_index, imagen_body
from por_siempre_raul_y_tatiana.components.texto import (
    texto_plantilla,
    texto_pequeño_plantilla,
    titulo_plantilla,
    titulo_plantilla_hersmoso,
)
from por_siempre_raul_y_tatiana.components.componentes import iconos_plantilla
from por_siempre_raul_y_tatiana.components.footer import pie_de_pagina
from por_siempre_raul_y_tatiana.components.fotos import *
from por_siempre_raul_y_tatiana.components.navbar import navbar

titulo="Raul & Tatiana por siempre"
descripcion="""Recuerda los momentos inolvidables de un dia tan especial
                como lo fue nuestra boda, te invitamos a darte un recorrido
                por todo lo que sucedio en aquel maravilloso dia"""
preview=rx.assent("pagina-principal/preview.png")

def espaciador() -> rx.Component:
    return rx.divider(style=espaciador_style)

@rx.page(
    route=routers.PRINCIPAL.value,
    title=titulo,
    description=descripcion,
    image=preview,
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": titulo},
        {"name": "og:description", "content": descripcion},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@santyjL"},
    ],
)
def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            imagen_index(
                url="pagina-principal/nuestra_boda.png",
                texto_alternativo="Nuestra boda",
            ),
            texto_plantilla("Te invitamos a recordar la alegria de unir nuestras vidas el dia"),
            imagen_index(
                url="pagina-principal/fecha.png",
                texto_alternativo="14 de septiembre del 2024",
            ),
            titulo_plantilla("NUESTRA HISTORIA"),
            imagen_index(
                url="pagina-principal/decoracion.png",
                texto_alternativo="nuestra historia",
            ),
            texto_pequeño_plantilla(
                """Hay días en la vida que son especiales por sí solos.
                Compartirlos con las personas que quieres los convierte
                en inolvidables.""",
            ),
            texto_pequeño_plantilla(
                """Aquel 14 de Septiembre de 2015, se marcó el inicio
                de esta historia 9 años después. hemos decidido unir
                nuestras vidas para siempre.""",
            ),
            espaciador(),
            rx.hstack(
                imagen_body(
                    url="pagina-principal/PRIMERA.png",
                    texto_alternativo="Nuestra boda",
                ),
                rx.vstack(
                    titulo_plantilla("Ceremonia Religiosa"),
                    titulo_plantilla_hersmoso("Parroquia San Juan Pablo II"),
                    iconos_plantilla("church"),
                    style=seccion_contenido_style,
                ),
                style=seccion_hstack_style,
            ),
            espaciador(),
            rx.hstack(
                rx.vstack(
                    titulo_plantilla("Recepción"),
                    titulo_plantilla_hersmoso("Restaurante Pikitos Nica-Mex"),
                    iconos_plantilla("party-popper"),
                    style=seccion_contenido_style,
                ),
                imagen_body(
                    url="pagina-principal/RECEPCION.png",
                    texto_alternativo="Recepción",
                ),
                style=seccion_hstack_style,
            ),
            espaciador(),
            pie_de_pagina(),
            spacing="4",
            style=contenedor_pagina_style,
        ),
        style=body,
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap",
        "https://fonts.googleapis.com/css2?family=Oranienbaum&display=swap",
    ]
)
app.add_page(index)
app.add_page(recuerdos)
app.add_page(entrada_iglesia)
app.add_page(iglesia)
app.add_page(decoracion)
app.add_page(entrada_novios)
app.add_page(invitados)
app.add_page(palabras)
app.add_page(ramo)
app.add_page(bailes)
app.add_page(fiesta)
