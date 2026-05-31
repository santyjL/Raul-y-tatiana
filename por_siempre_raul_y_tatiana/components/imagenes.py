import reflex as rx
from por_siempre_raul_y_tatiana.styles import imagen_index_style


def imagen_index(url:str, texto_alternativo:str) -> rx.Component:
    return rx.image(
        src=rx.asset(url),
        alt=texto_alternativo,
        style=imagen_index_style
    )