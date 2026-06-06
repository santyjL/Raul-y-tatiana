import reflex as rx
from por_siempre_raul_y_tatiana.styles import body
from por_siempre_raul_y_tatiana.components.imagenes import imagen_index, imagen_body
from por_siempre_raul_y_tatiana.components.texto import texto_plantilla, texto_pequeño_plantilla, titulo_plantilla, titulo_plantilla_hersmoso
from por_siempre_raul_y_tatiana.components.componentes import iconos_plantilla,tiempo_transcurrido, pagina_recuerdos_boton
from por_siempre_raul_y_tatiana.components.fotos import *

def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            imagen_index(
                url="pagina-principal/nuestra_boda.png",
                texto_alternativo="Nuestra boda"
            ),
            texto_plantilla("Te invitamos a recordar la alegria de unir nuestras vidas el dia"),
            imagen_index(
                url="pagina-principal/fecha.png",
                texto_alternativo="14 de septiembre del 2024"
            ),
            titulo_plantilla("NUESTRA HISTORIA"),
            imagen_index(
                url="pagina-principal/decoracion.png",
                texto_alternativo="nuestra historia"
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
            rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
            rx.hstack(
                imagen_body(
                    url="pagina-principal/PRIMERA.png",
                    texto_alternativo="Nuestra boda"
                ),
                rx.vstack(
                    titulo_plantilla(
                        "Ceremonia Religiosa"
                        ),
                    titulo_plantilla_hersmoso(
                        "Parroquia San Juan Pablo II"
                    ),
                    iconos_plantilla(
                        "church"
                    ),
                    width="50%",
                )
            ),
            rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
            rx.hstack(
                rx.vstack(
                    titulo_plantilla(
                        "Recepción"
                        ),
                    titulo_plantilla_hersmoso(
                        "Restaurante Pikitos Nica-Mex"
                    ),
                    iconos_plantilla(
                        "party-popper"
                    ),
                    width="50%",
                ),
                imagen_body(
                    url="pagina-principal/RECEPCION.png",
                    texto_alternativo="Recepción"
                ),
            ),
            rx.divider(
                height="250px",
                width="100%",
                background="transparent",
            ),
            rx.container(
                tiempo_transcurrido(),
                pagina_recuerdos_boton(),
                background_image=f"url({rx.asset("pagina-principal/BACKGROUND_FINAL.png")})",
                background_color= "#cccccc",
                width="100%",
                height="800px",
                background_size="cover"
            ),
            style=body
        )
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap"
        "https://fonts.googleapis.com/css2?family=Oranienbaum&display=swap"
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