import reflex as rx
from por_siempre_raul_y_tatiana.styles import body

def index() -> rx.Component:
    return rx.box(
        style=body
    )

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap"
        "https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap"
    ]
)
app.add_page(index)