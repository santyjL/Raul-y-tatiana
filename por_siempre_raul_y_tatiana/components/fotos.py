import reflex as rx
from por_siempre_raul_y_tatiana.styles import body, imagen_grid_style, titulo_hermoso_style
from por_siempre_raul_y_tatiana.components.imagenes import imagen_index
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

links_imagenes:list[str] = [
    routers.ENTRADA_IGLESIA.value,
    routers.IGLESIA.value,
    routers.DECORACION.value,
    routers.ENTRADA_NOVIOS.value,
    routers.INVITADOS.value,
    routers.PALABRAS.value,
    routers.RAMO.value,
    routers.BAILES.value,
    routers.FIESTA.value
]

titulos_lista:list[str] = [
    "El Recorrido",
    "El Amor",
    "La Decoracion",
    "La Gran Entrada",
    "Los Invitados",
    "Las Palabras",
    "El Ramo",
    "Los Bailes",
    "La fiesta"
]

imagenes_bailes: list[str] = [
    "imagenes_bailes/foto67(1).jpg",
    "imagenes_bailes/foto68(1).jpg",
    "imagenes_bailes/foto69(1).jpg",
    "imagenes_bailes/foto70(1).jpg",
    "imagenes_bailes/foto71(1).jpg",
    "imagenes_bailes/foto72(1).jpg",
    "imagenes_bailes/foto73(1).jpg",
    "imagenes_bailes/foto74(1).jpg",
    "imagenes_bailes/foto75(1).jpg",
    "imagenes_bailes/foto76(1).jpg",
    "imagenes_bailes/foto77(1).jpg",
    "imagenes_bailes/foto78(1).jpg",
    "imagenes_bailes/foto79(1).jpg",
    "imagenes_bailes/foto80(1).jpg",
    "imagenes_bailes/foto81(1).jpg",
    "imagenes_bailes/foto82(1).jpg",
    "imagenes_bailes/foto83(1).jpg",
    "imagenes_bailes/foto84(1).jpg",
    "imagenes_bailes/foto85(1).jpg",
]

imagenes_decoracion: list[str] = [
    "imagenes_decoracion/foto29(1).jpg",
    "imagenes_decoracion/foto30(1).jpg",
    "imagenes_decoracion/foto31(1).jpg",
    "imagenes_decoracion/foto32(1).jpg",
    "imagenes_decoracion/foto33(1).jpg",
    "imagenes_decoracion/foto34(1).jpg",
]

imagenes_entrada: list[str] = [
    "imagenes_entrada/foto35(1).jpg",
    "imagenes_entrada/foto36(1).jpg",
    "imagenes_entrada/foto37(1).jpg",
    "imagenes_entrada/foto38(1).jpg",
    "imagenes_entrada/foto39(1).jpg",
    "imagenes_entrada/foto40(1).jpg",
]

imagenes_entrada_iglesia: list[str] = [
    "imagenes_entrada_iglesia/foto115(1).jpg",
    "imagenes_entrada_iglesia/foto116(1).jpg",
    "imagenes_entrada_iglesia/foto117(1).jpg",
    "imagenes_entrada_iglesia/foto118(1).jpg",
    "imagenes_entrada_iglesia/foto119(1).jpg",
    "imagenes_entrada_iglesia/foto120(1).jpg",
    "imagenes_entrada_iglesia/foto121(1).jpg",
    "imagenes_entrada_iglesia/foto122(1).jpg",
    "imagenes_entrada_iglesia/foto123(1).jpg",
    "imagenes_entrada_iglesia/foto124(1).jpg",
    "imagenes_entrada_iglesia/foto125(1).jpg",
    "imagenes_entrada_iglesia/foto126(1).jpg",
    "imagenes_entrada_iglesia/foto127(1).jpg",
    "imagenes_entrada_iglesia/foto128(1).jpg",
    "imagenes_entrada_iglesia/foto129(1).jpg",
    "imagenes_entrada_iglesia/foto130(1).jpg",
    "imagenes_entrada_iglesia/foto131(1).jpg",
    "imagenes_entrada_iglesia/foto132(1).jpg",
    "imagenes_entrada_iglesia/foto133(1).jpg",
    "imagenes_entrada_iglesia/foto134(1).jpg",
    "imagenes_entrada_iglesia/foto135(1).jpg",
    "imagenes_entrada_iglesia/foto136(1).jpg",
    "imagenes_entrada_iglesia/foto137(1).jpg",
]

imagenes_fiesta: list[str] = [
    "imagenes_fiesta/foto104(1).jpg",
    "imagenes_fiesta/foto105(1).jpg",
    "imagenes_fiesta/foto106(1).jpg",
    "imagenes_fiesta/foto107(1).jpg",
    "imagenes_fiesta/foto108(1).jpg",
    "imagenes_fiesta/foto109(1).jpg",
    "imagenes_fiesta/foto110(1).jpg",
    "imagenes_fiesta/foto111(1).jpg",
    "imagenes_fiesta/foto112(1).jpg",
    "imagenes_fiesta/foto113(1).jpg",
    "imagenes_fiesta/foto114(1).jpg",
]

imagenes_ramo: list[str] = [
    "imagenes_flor/foto86(1).jpg",
    "imagenes_flor/foto87(1).jpg",
    "imagenes_flor/foto88(1).jpg",
    "imagenes_flor/foto89(1).jpg",
    "imagenes_flor/foto90(1).jpg",
    "imagenes_flor/foto91(1).jpg",
    "imagenes_flor/foto92(1).jpg",
    "imagenes_flor/foto93(1).jpg",
    "imagenes_flor/foto94(1).jpg",
    "imagenes_flor/foto95(1).jpg",
    "imagenes_flor/foto96(1).jpg",
    "imagenes_flor/foto97(1).jpg",
    "imagenes_flor/foto98(1).jpg",
    "imagenes_flor/foto99(1).jpg",
    "imagenes_flor/foto100(1).jpg",
    "imagenes_flor/foto101(1).jpg",
    "imagenes_flor/foto102(1).jpg",
    "imagenes_flor/foto103(1).jpg",
]

imagenes_iglesia: list[str] = [
    "imagenes_iglesia/foto1(1).jpg",
    "imagenes_iglesia/foto2(1).jpg",
    "imagenes_iglesia/foto3(1).jpg",
    "imagenes_iglesia/foto4(1).jpg",
    "imagenes_iglesia/foto5(1).jpg",
    "imagenes_iglesia/foto6(1).jpg",
    "imagenes_iglesia/foto7(1).jpg",
    "imagenes_iglesia/foto8(1).jpg",
    "imagenes_iglesia/foto9(1).jpg",
    "imagenes_iglesia/foto10(1).jpg",
    "imagenes_iglesia/foto11(1).jpg",
    "imagenes_iglesia/foto12(1).jpg",
    "imagenes_iglesia/foto13(1).jpg",
    "imagenes_iglesia/foto14(1).jpg",
    "imagenes_iglesia/foto15(1).jpg",
    "imagenes_iglesia/foto16(1).jpg",
    "imagenes_iglesia/foto17(1).jpg",
    "imagenes_iglesia/foto18(1).jpg",
    "imagenes_iglesia/foto19(1).jpg",
    "imagenes_iglesia/foto20(1).jpg",
    "imagenes_iglesia/foto21(1).jpg",
    "imagenes_iglesia/foto22(1).jpg",
    "imagenes_iglesia/foto23(1).jpg",
    "imagenes_iglesia/foto24(1).jpg",
    "imagenes_iglesia/foto25(1).jpg",
    "imagenes_iglesia/foto26(1).jpg",
    "imagenes_iglesia/foto27(1).jpg",
    "imagenes_iglesia/foto28(1).jpg",
]

imagenes_mesas: list[str] = [
    "imagenes_mesas/foto41(1).jpg",
    "imagenes_mesas/foto42(1).jpg",
    "imagenes_mesas/foto43(1).jpg",
    "imagenes_mesas/foto44(1).jpg",
    "imagenes_mesas/foto45(1).jpg",
    "imagenes_mesas/foto46(1).jpg",
    "imagenes_mesas/foto47(1).jpg",
    "imagenes_mesas/foto48(1).jpg",
    "imagenes_mesas/foto49(1).jpg",
    "imagenes_mesas/foto50(1).jpg",
    "imagenes_mesas/foto51(1).jpg",
]

imagenes_palabras: list[str] = [
    "imagenes_palabras/foto52(1).jpg",
    "imagenes_palabras/foto53(1).jpg",
    "imagenes_palabras/foto54(1).jpg",
    "imagenes_palabras/foto55(1).jpg",
    "imagenes_palabras/foto56(1).jpg",
    "imagenes_palabras/foto57(1).jpg",
    "imagenes_palabras/foto58(1).jpg",
    "imagenes_palabras/foto59(1).jpg",
    "imagenes_palabras/foto60(1).jpg",
    "imagenes_palabras/foto61(1).jpg",
    "imagenes_palabras/foto62(1).jpg",
    "imagenes_palabras/foto63(1).jpg",
    "imagenes_palabras/foto64(1).jpg",
    "imagenes_palabras/foto65(1).jpg",
    "imagenes_palabras/foto66(1).jpg",
]

imagenes_recuerdos: list[str] = [
    "imagenes_entrada_iglesia/foto115(1).jpg",
    "imagenes_iglesia/foto1(1).jpg",
    "imagenes_decoracion/foto29(1).jpg",
    "imagenes_entrada/foto35(1).jpg",
    "imagenes_mesas/foto41(1).jpg",
    "imagenes_palabras/foto52(1).jpg",
    "imagenes_flor/foto86(1).jpg",
    "imagenes_bailes/foto67(1).jpg",
    "imagenes_fiesta/foto104(1).jpg",
]

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
