import reflex as rx

def compo() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Generar Facturas", 
            color="black",
            position = "absolute",font_size="32px",left="400px"
        ),
        rx.text(
            "Seleccione los inquilinos para generar facturas:",
            position = "absolute",top="70px", left="400px"),

        
        rx.button("Generar facturas", bg="#E9124C",position = "absolute",top="550px", left="700px")
       
        

        
    ),
