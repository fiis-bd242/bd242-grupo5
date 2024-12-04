import reflex as rx
import requests as rq

@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return rx.center(  
        rx.box(
            rx.vstack(
                rx.heading("INICIO DE SESIÓN", align="center", color="red"),
                rx.input(placeholder="Usuario", width="100%"), 
                rx.input(type_="password", placeholder="Contraseña", width="100%"),
                rx.button("Ingresar", color_scheme="purple", width="100%"),
                spacing="3"
            ),
            padding="6",  
            max_width="400px",  
            width="90%",  
            min_height="300px",  
            height="auto",  
        ),
        height="100vh", 
    )
