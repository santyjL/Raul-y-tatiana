from enum import Enum

TABLET = "@media screen and (max-width: 1024px)"
MOBILE = "@media screen and (max-width: 768px)"
MOBILE_SM = "@media screen and (max-width: 480px)"


def combinar_estilos(*estilos: dict) -> dict:
    resultado: dict = {}
    for estilo in estilos:
        for clave, valor in estilo.items():
            if (
                isinstance(clave, str)
                and clave.startswith("@media")
                and clave in resultado
                and isinstance(resultado[clave], dict)
                and isinstance(valor, dict)
            ):
                resultado[clave] = {**resultado[clave], **valor}
            else:
                resultado[clave] = valor
    return resultado


class Colores(Enum):
    BACKGROUND = "#f7f7f7"
    PRIMARIO = "#136"
    PRIMARIO_TRANSPARENTE = "#136d"
    SECUNDARIO = "#16a"
    BLANCO = "#fff"


body = {
    "margin": "0",
    "width": "100%",
    "min_height": "100vh",
    "font_family": "Oranienbaum",
    "text_align": "center",
    "background": Colores.BACKGROUND.value,
    "background_size": "cover",
    "overflow_x": "hidden",
}

navbar_style = {
    "width": "50%",
    "height": "60px",
    "background": Colores.PRIMARIO_TRANSPARENTE.value,
    "position": "fixed",
    "margin": "20px auto",
    "left": "25%",
    "border_radius": "20px",
    "z_index": "50",
    "padding": "0 1rem",
    MOBILE: {
        "width": "94%",
        "left": "3%",
        "margin": "10px auto",
        "height": "60px",
        "min_height": "52px",
        "padding": "0.5rem 0.75rem",
    },
}

navbar_inner_style = {
    "width": "100%",
    "align_items": "center",
    "justify_content": "space-between",
    MOBILE: {
        "flex_wrap": "wrap",
        "gap": "0.25rem",
    },
}

navbar_links_style = {
    "flex_wrap": "wrap",
    "justify_content": "center",
    "gap": "1rem",
    MOBILE: {
        "gap": "0.5rem",
    },
}

navbar_link_style = {
    "font_size": "2.47em",
    "color": "#fff",
    "position": "relative",
    "top": "-9px",
    MOBILE: {
        "font_size": "1.4em",
        "top": "0",
    },
    MOBILE_SM: {
        "font_size": "1.15em",
    },
}

imagen_index_style = {
    "margin": "0",
    "padding": "0",
    "width": "100%",
    "max_width": "100%",
    "height": "auto",
    "loading": "lazy",
    "z_index": "10",
}

imagen_body_style = {
    "margin": "0 auto",
    "padding": "0",
    "width": "50%",
    "max_width": "600px",
    "height": "auto",
    "loading": "lazy",
    MOBILE: {
        "width": "100%",
        "max_width": "100%",
    },
}

imagen_grid_style = {
    "width": "100%",
    "height": "400px",
    "object_fit": "cover",
    "loading": "lazy",
    "border_radius": "8px",
    "margin": "10px auto",
    TABLET: {
        "height": "320px",
    },
    MOBILE: {
        "height": "260px",
    },
    MOBILE_SM: {
        "height": "220px",
    },
}

grid_imagenes_style = {
    "width": "96%",
    "max_width": "1400px",
    "margin": "0 auto",
    "grid_template_columns": "repeat(3, 1fr)",
    TABLET: {
        "grid_template_columns": "repeat(2, 1fr)",
        "width": "94%",
    },
    MOBILE: {
        "grid_template_columns": "1fr",
        "width": "92%",
    },
}

grid_imagenes_principal_style = {
    "width": "96%",
    "max_width": "1400px",
    "margin": "0 auto",
    "grid_template_columns": "repeat(3, 1fr)",
    TABLET: {
        "grid_template_columns": "repeat(2, 1fr)",
        "width": "94%",
    },
    MOBILE: {
        "grid_template_columns": "1fr",
        "width": "92%",
    },
}

titulo_card_style = {
    "font_size": "2.4em",
    "position": "relative",
    "top": "-10px",
    MOBILE: {
        "font_size": "1.6em",
        "top": "0",
    },
}

titulo_style = {
    "margin": "10px auto",
    "max_width": "1400px",
    "font_size": "5.5em",
    "font_weight": "bold",
    "font_family": "Oranienbaum",
    "text_wrap": "pretty",
    "color": Colores.SECUNDARIO.value,
    "padding": "0 1rem",
    TABLET: {
        "font_size": "3.5em",
    },
    MOBILE: {
        "font_size": "2.4em",
    },
    MOBILE_SM: {
        "font_size": "1.9em",
    },
}

titulo_hermoso_style = {
    "margin": "10px auto",
    "max_width": "1400px",
    "font_size": "5.5em",
    "font_weight": "bold",
    "font_family": "Dancing Script",
    "text_wrap": "pretty",
    "color": Colores.PRIMARIO.value,
    "padding": "0 1rem",
    TABLET: {
        "font_size": "3.5em",
    },
    MOBILE: {
        "font_size": "2.4em",
    },
    MOBILE_SM: {
        "font_size": "1.9em",
    },
}

titulo_pagina_style = {
    "position": "relative",
    "top": "-40px",
    MOBILE: {
        "top": "-20px",
        "padding": "0 0.5rem",
    },
}

texto_style = {
    "margin": "10px auto",
    "max_width": "1100px",
    "font_size": "4.5em",
    "font_family": "Oranienbaum",
    "text_wrap": "pretty",
    "color": Colores.PRIMARIO.value,
    "padding": "0 1.5rem",
    TABLET: {
        "font_size": "3em",
    },
    MOBILE: {
        "font_size": "2em",
        "padding": "0 1rem",
    },
    MOBILE_SM: {
        "font_size": "1.5em",
    },
}

texto_pequeño_style = {
    "margin": "10px auto",
    "max_width": "1100px",
    "font_size": "3.5em",
    "font_family": "Oranienbaum",
    "text_wrap": "pretty",
    "text_align": "justify",
    "color": Colores.PRIMARIO.value,
    "padding": "0 1.5rem",
    TABLET: {
        "font_size": "2.4em",
    },
    MOBILE: {
        "font_size": "1.6em",
        "padding": "0 1rem",
        "text_align": "center",
    },
    MOBILE_SM: {
        "font_size": "1.25em",
    },
}

iconos_plantilla_style = {
    "margin": "10px auto",
    "min_width": "128px",
    "min_height": "128px",
    "color": Colores.PRIMARIO.value,
    "background_color": Colores.BACKGROUND.value,
    "padding": "10px",
    "display": "flex",
    "justify_content": "center",
    "align_items": "center",
    MOBILE: {
        "min_width": "96px",
        "min_height": "96px",
    },
}

seccion_hstack_style = {
    "width": "100%",
    "align_items": "center",
    "justify_content": "center",
    "flex_wrap": "wrap",
    "gap": "1rem",
    "padding": "0 1rem",
    MOBILE: {
        "flex_direction": "column",
    },
}

seccion_contenido_style = {
    "width": "50%",
    MOBILE: {
        "width": "100%",
    },
}

espaciador_style = {
    "height": "250px",
    "width": "100%",
    "background": "transparent",
    TABLET: {
        "height": "160px",
    },
    MOBILE: {
        "height": "100px",
    },
    MOBILE_SM: {
        "height": "60px",
    },
}

tiempo_transcurrido_caja_style = {
    "max_width": "500px",
    "min_width": "500px",
    "height": "280px",
    "margin": "200px auto",
    "border": "2px solid #48e",
    "border_radius": "15px",
    "box_shadow": "0 0 90px 10px #48eb",
    "pointer": "focus",
    "background": Colores.PRIMARIO.value,
    "z_index": "20",
    TABLET: {
        "min_width": "unset",
        "width": "90%",
        "max_width": "450px",
        "margin": "120px auto 60px",
    },
    MOBILE: {
        "width": "92%",
        "height": "auto",
        "min_height": "240px",
        "margin": "80px auto 40px",
        "padding": "1rem 0.5rem",
    },
}

tiempo_transcurrido_style = {
    "width": "120px",
    "height": "130px",
    "margin": "2px 10px",
    "border": "2px solid #fff",
    "border_radius": "10px",
    "text_align": "center",
    "background": Colores.SECUNDARIO.value,
    "font_family": "Oranienbaum",
    "font_size": "6em",
    MOBILE: {
        "width": "80px",
        "height": "90px",
        "font_size": "3.5em",
        "margin": "2px 4px",
    },
    MOBILE_SM: {
        "width": "68px",
        "height": "78px",
        "font_size": "2.8em",
    },
}

tiempo_transcurrido_titulo_style = {
    "font_size": "4.4em",
    MOBILE: {
        "font_size": "2.6em",
    },
    MOBILE_SM: {
        "font_size": "2em",
    },
}

tiempo_transcurrido_label_style = {
    "font_size": "32px",
    MOBILE: {
        "font_size": "20px",
    },
    MOBILE_SM: {
        "font_size": "16px",
    },
}

tiempo_transcurrido_hstack_style = {
    "margin": "0 auto",
    "flex_wrap": "wrap",
    "justify_content": "center",
    "gap": "0.5rem",
}

footer_container_style = {
    "background_color": "#cccccc",
    "width": "100%",
    "min_height": "900px",
    "height": "auto",
    "background_size": "cover",
    "background_position": "center",
    "padding": "2rem 1rem 4rem",
    "display": "flex",
    "flex_direction": "column",
    "align_items": "center",
    "justify_content": "center",
    "gap": "1.5rem",
    TABLET: {
        "min_height": "700px",
    },
    MOBILE: {
        "min_height": "550px",
        "padding": "1.5rem 0.75rem 3rem",
    },
}

boton_pagina_recuerdos_style = {
    "font_size": "1.7em",
    "font_family": "Dancing Script",
    "max_width": "400px",
    "width": "90%",
    "height": "60px",
    "color": "#fff",
    "margin": "5px auto",
    "border": "2px solid #fff",
    "border_radius": "15px",
    "padding": "10px 0",
    "box_shadow": "0 0 40px 10px #48eb",
    "background": Colores.PRIMARIO.value,
    "transform": "padding 1s ease",
    MOBILE: {
        "font_size": "1.3em",
        "max_width": "100%",
        "height": "auto",
        "min_height": "52px",
    },
    MOBILE_SM: {
        "font_size": "1.1em",
    },
}

footer_boton_style = {
    "position": "relative",
    "top": "-180px",
    "width": "100%",
    "display": "flex",
    "justify_content": "center",
    TABLET: {
        "top": "-100px",
    },
    MOBILE: {
        "top": "0",
        "margin": "0.5rem 0",
    },
}

contenedor_pagina_style = {
    "width": "100%",
    "align_items": "center"
}
