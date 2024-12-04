import reflex as rx

def compof() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Enviar Facturas", 
            color="black",
            position = "absolute",font_size="32px",left="400px"
        ),
        rx.text(
            "Seleccione los inquilinos para enviar facturas:",
            position = "absolute",top="70px", left="400px"),

        
        rx.button("Enviar facturas", bg="#E9124C",position = "absolute",top="550px", left="700px")
        
    ),
    