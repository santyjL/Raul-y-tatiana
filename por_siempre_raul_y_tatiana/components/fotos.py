import reflex as rx
from reflex_image_zoom import image_zoom
from por_siempre_raul_y_tatiana.styles import (
    body,
    combinar_estilos,
    contenedor_pagina_style,
    espaciador_style,
    grid_imagenes_principal_style,
    grid_imagenes_style,
    imagen_grid_style,
    titulo_card_style,
    titulo_hermoso_style,
    titulo_pagina_style,
)
from por_siempre_raul_y_tatiana.components.imagenes import imagen_index
from por_siempre_raul_y_tatiana.components.footer import pie_de_pagina_2
from por_siempre_raul_y_tatiana.components.navbar import navbar
from por_siempre_raul_y_tatiana.routers import routers
from por_siempre_raul_y_tatiana.listas import (
    imagenes_bailes,
    imagenes_decoracion,
    imagenes_entrada,
    imagenes_entrada_iglesia,
    imagenes_fiesta,
    imagenes_iglesia,
    imagenes_mesas,
    imagenes_palabras,
    imagenes_ramo,
    imagenes_recuerdos,
    links_imagenes,
    titulos_lista,
)

IMAGEN_CABECERA = "pagina-principal/nuestra_boda.png"

def espaciador() -> rx.Component:
    return rx.divider(style=espaciador_style)

def titulo_pagina(texto: str) -> rx.Component:
    return rx.heading(
        texto,
        style=combinar_estilos(titulo_hermoso_style, titulo_pagina_style),
    )

def cabecera_boda() -> rx.Component:
    return imagen_index(url=IMAGEN_CABECERA, texto_alternativo="Nuestra boda")

def pagina_fotos(titulo: str, contenido: rx.Component) -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            cabecera_boda(),
            espaciador(),
            titulo_pagina(titulo),
            contenido,
            espaciador(),
            pie_de_pagina_2(),
            spacing="4",
            style=contenedor_pagina_style,
        ),
        style=body,
    )

def grid_imagenes_principal(
    lista_imagenes: list[str],
    links: list[str],
    titulos: list[str],
) -> rx.Component:
    return rx.grid(
        *[
            rx.card(
                rx.link(
                    rx.image(
                        src=rx.asset(url),
                        alt=url.split("/")[-1],
                        style=imagen_grid_style,
                    ),
                    rx.center(
                        rx.heading(
                            titulo,
                            style=combinar_estilos(titulo_hermoso_style, titulo_card_style),
                        )
                    ),
                    href=link,
                ),
                variant="classic",
                size="1",
            )
            for url, link, titulo in zip(lista_imagenes, links, titulos)
        ],
        spacing="4",
        style=grid_imagenes_principal_style,
    )

def grid_imagenes(lista_imagenes: list[str]) -> rx.Component:
    return rx.grid(
        *[
            image_zoom(
                rx.image(
                    src=rx.asset(url),
                    alt=url.split("/")[-1],
                    style=imagen_grid_style,
                    _hover={"box-shadow": "0 0 40px 0 #48e"},
                ),
            )
            for url in lista_imagenes
        ],
        spacing="4",
        style=grid_imagenes_style,
    )


@rx.page(routers.RECUERDOS.value)
def recuerdos() -> rx.Component:
    return pagina_fotos(
        "Recuerdos",
        rx.center(
            grid_imagenes_principal(imagenes_recuerdos, links_imagenes, titulos_lista),
        ),
    )

@rx.page(routers.ENTRADA_IGLESIA.value)
def entrada_iglesia() -> rx.Component:
    return pagina_fotos("El Recorrido", grid_imagenes(imagenes_entrada_iglesia))

@rx.page(routers.IGLESIA.value)
def iglesia() -> rx.Component:
    return pagina_fotos("El Amor", grid_imagenes(imagenes_iglesia))

@rx.page(routers.DECORACION.value)
def decoracion() -> rx.Component:
    return pagina_fotos("La Decoracion", grid_imagenes(imagenes_decoracion))

@rx.page(routers.ENTRADA_NOVIOS.value)
def entrada_novios() -> rx.Component:
    return pagina_fotos("La Gran Entrada", grid_imagenes(imagenes_entrada))

@rx.page(routers.INVITADOS.value)
def invitados() -> rx.Component:
    return pagina_fotos("Los Invitados", grid_imagenes(imagenes_mesas))

@rx.page(routers.PALABRAS.value)
def palabras() -> rx.Component:
    return pagina_fotos("Las Palabras", grid_imagenes(imagenes_palabras))

@rx.page(routers.RAMO.value)
def ramo() -> rx.Component:
    return pagina_fotos("El Ramo", grid_imagenes(imagenes_ramo))

@rx.page(routers.BAILES.value)
def bailes() -> rx.Component:
    return pagina_fotos("Los Bailes", grid_imagenes(imagenes_bailes))

@rx.page(routers.FIESTA.value)
def fiesta() -> rx.Component:
    return pagina_fotos("La Fiesta", grid_imagenes(imagenes_fiesta))
