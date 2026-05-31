import reflex as rx
from por_siempre_raul_y_tatiana.styles import body
from por_siempre_raul_y_tatiana.components.imagenes import imagen_index
from por_siempre_raul_y_tatiana.components.texto import texto_plantilla, texto_pequeño_plantilla, titulo_plantilla

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
        ),
        style=body
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap"
        "https://fonts.googleapis.com/css2?family=Oranienbaum&display=swap"
    ]
)
app.add_page(index)