import reflex as rx
from reflex_image_zoom import image_zoom
from por_siempre_raul_y_tatiana.styles import body, imagen_grid_style, titulo_hermoso_style
from por_siempre_raul_y_tatiana.components.imagenes import imagen_index
from por_siempre_raul_y_tatiana.components.footer import pie_de_pagina_2
from por_siempre_raul_y_tatiana.listas import *
from por_siempre_raul_y_tatiana.routers import routers


def grid_imagenes_principal(lista_imagenes: list[str], link:list[str],titulos:list[str], columnas: str = "3") -> rx.Component:
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
                            style=titulo_hermoso_style,
                            font_size="2.4em",
                            position="relative",
                            top="-10px"
                        )
                    ),
                    href=link   
                ),
                variant="classic",
                size="1"
            )
            for url,link,titulo in  zip(lista_imagenes,link,titulos)
        ],
        columns=columnas,
        spacing="4",
        width="98vw",
    )

def grid_imagenes(lista_imagenes: list[str], columnas: str = "3") -> rx.Component:
    return rx.grid(
        *[
            image_zoom(
                rx.image(
                    src=rx.asset(url),
                    alt=url.split("/")[-1],
                    style=imagen_grid_style,
                    _hover={"box-shadow" : "0 0 40px 0 #48e"}
                ),
                
            )for url in lista_imagenes
        ],
        columns=columnas,
        spacing="4",
        width="98vw",
    )

@rx.page(routers.RECUERDOS.value)
def recuerdos() -> rx.Component:
    return rx.box(
        rx.vstack(
            imagen_index(
                url="pagina-principal/nuestra_boda.png",
                texto_alternativo="Nuestra boda"
            ),
            rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
            rx.heading(
                    "Recuerdos",
                    style=titulo_hermoso_style,
                    position="relative",
                    top="-40px"
                ),
            rx.center(
                grid_imagenes_principal(
                    imagenes_recuerdos,
                    links_imagenes,
                    titulos_lista
                ),
            ),
            rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
            pie_de_pagina_2()
        ),
        style=body,
    )

@rx.page(routers.ENTRADA_IGLESIA.value)
def entrada_iglesia() -> rx.Component:
    return rx.box(
        rx.vstack(
            imagen_index(
                url="pagina-principal/nuestra_boda.png",
                texto_alternativo="Nuestra boda"
            ),
            rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
            rx.heading(
                    "El Recorrido",
                    style=titulo_hermoso_style,
                    position="relative",
                    top="-40px"
                ),
            grid_imagenes(imagenes_entrada_iglesia),
            rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
            pie_de_pagina_2()
        ),
        style=body,
    )

@rx.page(routers.IGLESIA.value)
def iglesia() -> rx.Component:
    return rx.box(
        imagen_index(
            url="pagina-principal/nuestra_boda.png",
            texto_alternativo="Nuestra boda"
        ),
        rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
        rx.heading(
                "El Amor",
                style=titulo_hermoso_style,
                position="relative",
                top="-40px"
            ),
        grid_imagenes(imagenes_iglesia),
        rx.divider(
            height="250px",
            width="100%",
            background="transparent",
        ),
        pie_de_pagina_2(),
        style=body,
    )

@rx.page(routers.DECORACION.value)
def decoracion() -> rx.Component:
    return rx.box(
        imagen_index(
            url="pagina-principal/nuestra_boda.png",
            texto_alternativo="Nuestra boda"
        ),
        rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
        rx.heading(
                "La Decoracion",
                style=titulo_hermoso_style,
                position="relative",
                top="-40px"
            ),
        grid_imagenes(imagenes_decoracion),
        rx.divider(
            height="250px",
            width="100%",
            background="transparent",
        ),
        pie_de_pagina_2(),
        style=body,
    )

@rx.page(routers.ENTRADA_NOVIOS.value)
def entrada_novios() -> rx.Component:
    return rx.box(
        imagen_index(
            url="pagina-principal/nuestra_boda.png",
            texto_alternativo="Nuestra boda"
        ),
        rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
        rx.heading(
                "La Gran Entrada",
                style=titulo_hermoso_style,
                position="relative",
                top="-40px"
            ),
        grid_imagenes(imagenes_entrada),
        rx.divider(
            height="250px",
            width="100%",
            background="transparent",
        ),
        pie_de_pagina_2(),
        style=body,
    )

@rx.page(routers.INVITADOS.value)
def invitados() -> rx.Component:
    return rx.box(
        imagen_index(
            url="pagina-principal/nuestra_boda.png",
            texto_alternativo="Nuestra boda"
        ),
        rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
        rx.heading(
                "Los Invitados",
                style=titulo_hermoso_style,
                position="relative",
                top="-40px"
            ),
        grid_imagenes(imagenes_mesas),
        rx.divider(
            height="250px",
            width="100%",
            background="transparent",
        ),
        pie_de_pagina_2(),
        style=body,
    )

@rx.page(routers.PALABRAS.value)
def palabras() -> rx.Component:
    return rx.box(
        imagen_index(
            url="pagina-principal/nuestra_boda.png",
            texto_alternativo="Nuestra boda"
        ),
        rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
        rx.heading(
                "Las Palabras",
                style=titulo_hermoso_style,
                position="relative",
                top="-40px"
            ),
        grid_imagenes(imagenes_palabras),
        rx.divider(
            height="250px",
            width="100%",
            background="transparent",
        ),
        pie_de_pagina_2(),
        style=body,
    )

@rx.page(routers.RAMO.value)
def ramo() -> rx.Component:
    return rx.box(
        imagen_index(
            url="pagina-principal/nuestra_boda.png",
            texto_alternativo="Nuestra boda"
        ),
        rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
        rx.heading(
                "El Ramo",
                style=titulo_hermoso_style,
                position="relative",
                top="-40px"
            ),
        grid_imagenes(imagenes_ramo),
        rx.divider(
            height="250px",
            width="100%",
            background="transparent",
        ),
        pie_de_pagina_2(),
        style=body,
    )

@rx.page(routers.BAILES.value)
def bailes() -> rx.Component:
    return rx.box(
        imagen_index(
            url="pagina-principal/nuestra_boda.png",
            texto_alternativo="Nuestra boda"
        ),
        rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
        rx.heading(
                "Los Bailes",
                style=titulo_hermoso_style,
                position="relative",
                top="-40px"
            ),
        grid_imagenes(imagenes_bailes),
        rx.divider(
            height="250px",
            width="100%",
            background="transparent",
        ),
        pie_de_pagina_2(),
        style=body,
    )

@rx.page(routers.FIESTA.value)
def fiesta() -> rx.Component:
    return rx.box(
        imagen_index(
            url="pagina-principal/nuestra_boda.png",
            texto_alternativo="Nuestra boda"
        ),
        rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
        rx.heading(
                "La Fiesta",
                style=titulo_hermoso_style,
                position="relative",
                top="-40px"
            ),
        grid_imagenes(imagenes_fiesta),
        rx.divider(
            height="250px",
            width="100%",
            background="transparent",
        ),
        pie_de_pagina_2(),
        style=body,
    )
