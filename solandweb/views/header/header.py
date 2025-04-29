import reflex as rx
from rxconfig import config

import solandweb.styles.styles as styles 

class State(rx.State):
    """The app state."""
    pass


def navbar() -> rx.Component:
    """Navigation bar."""
    return rx.box(
        rx.hstack(
            rx.image(src="/logo.jpeg", alt="Logo", width="50px", height="50px"),  # Logo desde static
            rx.text("MiWeb", font_size="3", font_weight="bold"),
            rx.spacer(),
            rx.hstack(
                rx.link("Inicio", href="#inicio", padding="1rem"),
                rx.link("Sobre mí", href="#sobre-mi", padding="1rem"),
                rx.link("Servicios", href="#servicios", padding="1rem"),
                rx.link("Contacto", href="#contacto", padding="1rem"),
            ),
            spacing="2",
        ),
        style=styles.NAVBAR_STYLE,  # Aplicar estilos desde styles.py
    )


def hero_section() -> rx.Component:
    """Hero section."""
    return rx.box(
        rx.vstack(
            rx.heading("Bienvenido a Soland CA", size="3"),
            rx.text("Tu solución moderna para páginas web profesionales.", size="2"),
            rx.button("Contáctanos", href="#contacto", color_scheme="teal"),
            spacing="2",
            align_items="center",
        ),
        style=styles.HERO_STYLE,
        id="inicio",  # Añadir ID para el enlace de navegación
    )


def about_section() -> rx.Component:
    """About section."""
    return rx.box(
        rx.vstack(
            rx.heading("Sobre mí", size="3"),
            rx.text("Somos un equipo dedicado a crear experiencias digitales únicas y modernas."),
            spacing="3",
            align_items="center",
        ),
        style=styles.ABOUT_STYLE,  # Aplicar estilos desde styles.py    
        id="sobre-mi",  # Añadir ID para el enlace de navegación
        
    )


def services_section() -> rx.Component:
    """Services section."""
    return rx.box(
        rx.vstack(
            rx.heading("Servicios", size="3"),
            rx.hstack(
                rx.box(
                    rx.icon("laptop", size=3),
                    rx.text("Desarrollo Web"),
                    rx.text("Diseñamos y desarrollamos sitios web personalizados."),
                    align_items="center",
                    text_align="center",
                    padding="1rem",
                ),
                rx.box(
                    rx.icon("file", size=3),  # Cambiado de "mobile" a "file"
                    rx.text("Diseño Responsivo"),
                    rx.text("Tu sitio web se verá genial en cualquier dispositivo."),
                    align_items="center",
                    text_align="center",
                    padding="1rem",
                ),
                rx.box(
                    rx.icon("search", size=3),
                    rx.text("SEO"),
                    rx.text("Optimización para motores de búsqueda."),
                    align_items="center",
                    text_align="center",
                    padding="1rem",
                ),
                spacing="0",
            ),
            spacing="0",
            align_items="center",
        ),
        style=styles.SERVICES_STYLE,  # Aplicar estilos desde styles.py
        id="servicios",  # Añadir ID para el enlace de navegación
    )


def contact_section() -> rx.Component:
    """Contact section."""
    return rx.box(
        rx.vstack(
            rx.heading("Contacto", size="4"),
            rx.form(
                rx.input(placeholder="Tu nombre", name="nombre", required=True),
                rx.input(placeholder="Tu correo", type="email", name="email", required=True),
                rx.text_area(placeholder="Tu mensaje", name="mensaje", required=True),
                rx.button("Enviar", type="submit", color_scheme="teal"),
                spacing="1",
            ),
            spacing="2",
            align_items="center",
        ),
        style=styles.CONTACT_STYLE,  # Aplicar estilos desde styles.py
        id="contacto",  # Añadir ID para el enlace de navegación
    )


def footer() -> rx.Component:
    """Footer section."""
    return rx.box(
        rx.text("© 2025 MiWeb. Todos los derechos reservados.", text_align="center"),
        style=styles.FOOTER_STYLE,  # Aplicar estilos desde styles.py
    )


def index() -> rx.Component:
    """Main page."""
    return rx.container(
        navbar(),
        hero_section(),
        about_section(),
        services_section(),
        contact_section(),
        footer(),
        style=styles.GLOBAL_STYLE,  
    )


app = rx.App()
app.add_page(index)