import reflex as rx
from por_siempre_raul_y_tatiana.styles import iconos_plantilla_style

def iconos_plantilla(icono:str) -> rx.Component:
    return rx.icon(
        tag=icono,
        style=iconos_plantilla_style
        )
        