import reflex as rx
from por_siempre_raul_y_tatiana.styles import texto_style

def texto_plantilla(texto:str) -> rx.Component:
    return rx.text(
        texto,
        style= texto_style
    )

def Titulo_plantilla(texto:str) -> rx.Component:
    return rx.text(
        texto,
        style= titulo_style
    )