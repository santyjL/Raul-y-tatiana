import reflex as rx
from por_siempre_raul_y_tatiana.styles import texto_style , texto_pequeño_style, titulo_style, titulo_hermoso_style

def texto_plantilla(texto:str, weight="bold") -> rx.Component:
    return rx.text(
        texto,
        font_weight=weight,
        style= texto_style
    )

def texto_pequeño_plantilla(texto:str) -> rx.Component:
    return rx.text(
        texto,
        font_weight=300,
        style= texto_pequeño_style
    )

def titulo_plantilla(texto:str) -> rx.Component:
    return rx.text(
        texto,
        style= titulo_style
    )

def titulo_plantilla_hersmoso(texto:str) -> rx.Component:
    return rx.text(
        texto,
        style= titulo_hermoso_style
    )