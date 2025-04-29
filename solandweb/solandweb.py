
import reflex as rx
import solandweb.styles.styles as styles
from solandweb.styles.styles import Size as Size
from solandweb.views.header.header import navbar
from solandweb.views.header.header import hero_section
from solandweb.views.header.header import about_section
from solandweb.views.header.header import services_section
from solandweb.views.header.header import contact_section
from solandweb.views.header.header import footer


    
class State(rx.State):
    pass

def index() -> rx.Component:
    
    return rx.box(
        rx.center(
            rx.vstack(
                navbar(),         
                width="100%", 
                max_width="100%",
                margin_y=Size.BIG.value
            ),
        ),
          rx.center(
            rx.vstack(
                hero_section(),         
                width="100%", 
                height="50vh",
                margin_y=Size.BIG.value
            ),
        ),
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)

app.add_page(
    index,
    title="Soland | WEB",
    image="logo.png"
)