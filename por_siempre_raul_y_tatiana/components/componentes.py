import reflex as rx
from por_siempre_raul_y_tatiana.styles import (iconos_plantilla_style, tiempo_transcurrido_caja_style,
                                            tiempo_transcurrido_style, titulo_hermoso_style,boton_pagina_recuerdos_style)
from por_siempre_raul_y_tatiana.components.estados import tiempoTranscurridoDeLaBoda

def iconos_plantilla(icono:str) -> rx.Component:
    return rx.icon(
        tag=icono,
        style=iconos_plantilla_style
        )

años_transcurridos = tiempoTranscurridoDeLaBoda.años
meses_transcurridos = tiempoTranscurridoDeLaBoda.meses
dias_transcurridos = tiempoTranscurridoDeLaBoda.dias 

def tiempo_transcurrido() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Cuanto Tiempo...",
                style=titulo_hermoso_style,
                color="#fff",
                margin="20px auto",
                font_size="4.4em"
            ),
            rx.hstack(
                rx.vstack(
                    rx.box(
                        f"{años_transcurridos}",
                        style=tiempo_transcurrido_style
                        ),
                    rx.text(
                        "Años",
                        margin="0 auto",
                        padding="0",
                        font_size="32px",
                        font_family="Oranienbaum",
                        )
                    ),
                rx.vstack(
                    rx.box(
                        f"{meses_transcurridos}",
                        style=tiempo_transcurrido_style
                        ),
                    rx.text(
                        "Meses",
                        margin="0 auto",
                        padding="0",
                        font_size="32px",
                        font_family="Oranienbaum",
                        )
                    ),
                rx.vstack(
                    rx.box(
                        f"{dias_transcurridos}",
                        style=tiempo_transcurrido_style
                        ),
                    rx.text(
                        "Dias",
                        margin="0 auto",
                        padding="0",
                        font_size="32px",
                        font_family="Oranienbaum",
                        )
                    ),
                margin="0 auto"
            ),
            style=tiempo_transcurrido_caja_style
        )
    )

def footer_boton(texto:str, link:str) -> rx.Component:
    return rx.link(
        rx.text(
            texto,
            style=boton_pagina_recuerdos_style,
            _hover= {"padding" : "14px"}
        ),
        position="relative",
        top="-180px",
        heigth="60px",
        href=link,
        
    )