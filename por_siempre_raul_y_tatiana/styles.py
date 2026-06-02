from enum import Enum

class Colores(Enum):
    BACKGROUND= "#f7f7f7"
    PRIMARIO="#136"
    SECUNDARIO="#16a"

    BLANCO="#fff"

body= dict[str, str](
    margin=0,
    width="100%",
    min_height="100vh",
    font_family="Oranienbaum",
    text_align="center",
    background=Colores.BACKGROUND.value,
    background_size="cover"
)

imagen_index_style= dict[str,str](
    margin=0,
    padding=0,
    width="100%",
    height="auto",
    loading="lazy"
)

imagen_body_style= dict[str,str](
    margin=0,
    padding=0,
    width="50%",
    height="auto",
    loading="lazy"
)

titulo_style=dict[str,str](
    margin="10px auto",
    max_width="1400px",
    font_size="5.5em",
    font_weight="bold",
    font_family="Oranienbaum",
    text_wrap="pretty",
    color=Colores.SECUNDARIO.value,
)
titulo_hermoso_style=dict[str,str](
    margin="10px auto",
    max_width="1400px",
    font_size="5.5em",
    font_weight="bold",
    font_family="Dancing Script",
    text_wrap="pretty",
    color=Colores.PRIMARIO.value,
)

texto_style=dict[str,str](
    margin="10px auto",
    max_width="1100px",
    font_size="4.5em",
    font_family="Oranienbaum",
    text_wrap="pretty",
    color=Colores.PRIMARIO.value,
)

texto_pequeño_style=dict[str,str](
    margin="10px auto",
    max_width="1100px",
    font_size="3.5em",
    font_family="Oranienbaum",
    text_wrap="pretty",
    text_align="justify",
    color=Colores.PRIMARIO.value,
)

iconos_plantilla_style=dict[str,str](
    margin="10px auto",
    min_width="128px",
    min_height="128px",
    color=Colores.PRIMARIO.value,
    background_color=Colores.BACKGROUND.value,
    padding="10px",
    display="flex",
    justify_content="center",
    align_items="center",
)