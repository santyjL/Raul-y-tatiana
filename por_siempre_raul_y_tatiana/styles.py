from enum import Enum

class Colores(Enum):
    BACKGROUND= "#fff"
    PRIMARIO="#136"
    SECUNDARIO="#16a"

    BLANCO="#fff"

body= dict[str, str](
    margin=0,
    width="100%",
    height="100vh",
    font_family="Montserrat",
    background=Colores.BACKGROUND.value
)

imagen_index_style= dict[str,str](
    margin=0,
    padding=0,
    width="100%",
    height="auto",
    loading="lazy"
)