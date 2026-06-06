import reflex as rx
from por_siempre_raul_y_tatiana.styles import body, imagen_grid_style, titulo_hermoso_style
from por_siempre_raul_y_tatiana.components.imagenes import imagen_index
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
            rx.image(
                src=rx.asset(url),
                alt=url.split("/")[-1],
                style=imagen_grid_style,
            
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
            rx.center(
                grid_imagenes_principal(
                    imagenes_recuerdos,
                    links_imagenes,
                    titulos_lista
                ),
            )
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
            grid_imagenes(imagenes_entrada_iglesia),
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
        grid_imagenes(imagenes_iglesia),
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
        grid_imagenes(imagenes_decoracion),
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
        grid_imagenes(imagenes_entrada),
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
        grid_imagenes(imagenes_mesas),
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
        grid_imagenes(imagenes_palabras),
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
        grid_imagenes(imagenes_ramo),
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
        grid_imagenes(imagenes_bailes),
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
        grid_imagenes(imagenes_fiesta),
        style=body,
    )
