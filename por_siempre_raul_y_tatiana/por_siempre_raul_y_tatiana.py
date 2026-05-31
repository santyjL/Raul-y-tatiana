import reflex as rx
from por_siempre_raul_y_tatiana.styles import body
from por_siempre_raul_y_tatiana.components.imagenes import imagen_index

def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            imagen_index(
                url="pagina-principal/nuestra_boda.png",
                texto_alternativo="Nuestra boda"
            )
        ),
        style=body
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap"
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap"
    ]
)
app.add_page(index)