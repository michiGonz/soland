# Estilos globales
import reflex as rx
from enum import Enum
from .fonts import Font as Font
from .colors import Color as Color

# Base style
STYLESHEETS = []

#constants
MAX_WIDTH="600px"

#sizes
class Size(Enum):
    SMALL = "1"
    MEDIUM = "2"
    DEFAULT = "3"
    LARGE = "4"
    BIG = "5"

STYLESHEETS =[
    "https://fonts.googleapis.com/css?family=Roboto:wght@300&display=swap"
]

BASE_STYLE ={
    "font_family": Font.DEFAULT.value, #fuente general
    "background_color": Color.BACKGROUND.value, #color de fondo general
    "scroll_behavior": "smooth",  # Habilita el desplazamiento suave
}

GLOBAL_STYLE = {
    "margin": "0",  # Eliminar margen externo
    "padding": "0",  # Eliminar relleno externo
    "box_sizing": "border-box",  # Asegurar que el tamaño incluya bordes y relleno
}

# Estilos generales
NAVBAR_STYLE = {
    "padding": "1rem",
    "background_image": "linear-gradient(to right, yellow, black)",  # Degradado de amarillo a negro
    "color": "white",
    "display": "flex",
    "width": "100%",
    "justify_content": "space-between",  # Ajusta los elementos en la barra
}


HERO_STYLE = {
    "height": "100vh",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "width": "100%",
    "background_image": "url('/header.png')",
    "background_size": "cover",
    "background_position": "center",
    "margin_bottom": "2rem",
    "background_repeat": "no-repeat",
    "color": "white",
    "id": "inicio",
    "flex": "1",  # Ocupa proporcionalmente el mismo espacio
}

ABOUT_STYLE = {
    "padding": "4rem",
    "background_image": "url('/imagen2.jpg')",
    "background_size": "cover",
    "background_position": "center",
    "background_repeat": "no-repeat",
    "color": "white",
    "id": "sobre-mi",
    "flex": "1",
}

SERVICES_STYLE = {
    "padding": "4rem",
    "background_image": "url('/imagen1.jpg')",
    "background_size": "cover",
    "background_position": "center",
    "background_repeat": "no-repeat",
    "color": "white",
    "id": "servicios",
    "flex": "1",
}

CONTACT_STYLE = {
    "padding": "4rem",
    "background_image": "url('/imagen3.jpg')",
    "background_size": "cover",
    "background_position": "center",
    "background_repeat": "no-repeat",
    "color": "white",
    "id": "contacto",
    "flex": "1",
}

FOOTER_STYLE = {
    "padding": "1rem",
    "background_color": "gray.800",
    "color": "white",
    "text_align": "center",  # Centra el contenido del pie de página
}
