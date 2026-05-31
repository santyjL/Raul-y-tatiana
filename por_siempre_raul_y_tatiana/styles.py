from enum import Enum

class Colores(Enum):
    BACKGROUND= "#fff"
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

titulo_style=dict[str,str](
    margin="10px auto",
    max_width="900px",
    font_size="7.5em",
    font_weight="bold",
    font_family="Oranienbaum",
    text_wrap="pretty",
    color=Colores.PRIMARIO.value,
)

texto_style=dict[str,str](
    margin="10px auto",
    max_width="1100px",
    font_size="4.5em",
    font_weight="bold",
    font_family="Oranienbaum",
    text_wrap="pretty",
    color=Colores.PRIMARIO.value,
)