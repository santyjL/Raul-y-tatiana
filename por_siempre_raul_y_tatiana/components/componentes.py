import reflex as rx
from por_siempre_raul_y_tatiana.styles import (
    iconos_plantilla_style,
    tiempo_transcurrido_caja_style,
    tiempo_transcurrido_style,
    titulo_hermoso_style,
    boton_pagina_recuerdos_style,
    tiempo_transcurrido_titulo_style,
    tiempo_transcurrido_label_style,
    tiempo_transcurrido_hstack_style,
    footer_boton_style,
    combinar_estilos,
)
from por_siempre_raul_y_tatiana.components.estados import tiempoTranscurridoDeLaBoda


def iconos_plantilla(icono: str) -> rx.Component:
    return rx.icon(
        tag=icono,
        style=iconos_plantilla_style,
    )


años_transcurridos = tiempoTranscurridoDeLaBoda.años
meses_transcurridos = tiempoTranscurridoDeLaBoda.meses
dias_transcurridos = tiempoTranscurridoDeLaBoda.dias


def _unidad_tiempo(valor: int, etiqueta: str) -> rx.Component:
    return rx.vstack(
        rx.box(f"{valor}", style=tiempo_transcurrido_style),
        rx.text(
            etiqueta,
            margin="0 auto",
            padding="0",
            font_family="Oranienbaum",
            style=tiempo_transcurrido_label_style,
        ),
    )


def tiempo_transcurrido() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Cuanto Tiempo...",
                style=combinar_estilos(titulo_hermoso_style, tiempo_transcurrido_titulo_style),
                color="#fff",
                margin="20px auto",
            ),
            rx.hstack(
                _unidad_tiempo(años_transcurridos, "Años"),
                _unidad_tiempo(meses_transcurridos, "Meses"),
                _unidad_tiempo(dias_transcurridos, "Dias"),
                style=tiempo_transcurrido_hstack_style,
            ),
            style=tiempo_transcurrido_caja_style,
        )
    )


def footer_boton(texto: str, link: str) -> rx.Component:
    return rx.link(
        rx.text(
            texto,
            style=boton_pagina_recuerdos_style,
            _hover={"padding": "14px"},
        ),
        href=link,
        style=footer_boton_style,
    )
