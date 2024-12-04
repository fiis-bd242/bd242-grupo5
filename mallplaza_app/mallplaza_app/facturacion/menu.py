import reflex as rx

def menu() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/mall.png",
            alt="Logo Mall Plaza",
            background_color="#E9124C",  
            width="150px",  # Ajusta el ancho
            height="auto",  # Mantén la proporción
            position="relative",
            left="73px",
            top="20px" 
        ),
        rx.flex(
            rx.icon("bolt", size=25,position="absolute",left="63px",top="434px"),
            rx.icon("credit_card", size=25,position="absolute",left="63px",top="297px"),
            rx.icon("user", size=25,position="absolute",left="63px",top="200px"),
            rx.icon("bell_ring", size=25,position="absolute",left="63px",top="388px"),
            rx.icon("eye", size=25,position="absolute",left="63px",top="343px"),
            rx.icon("log_out", size=25,position="absolute",left="63px",top="478px"),
            rx.icon("file_text", size=25,position="absolute",left="63px",top="250px"),


            align="center",
            gap="2",
        ),
        rx.text("Perfil de usuario", padding="0px",color="white",position="relative",left="90px",top="30px"),
        rx.text("Generar Facturas",  padding="0px",color="white",position="relative",left="90px",top="40px"),
        rx.text("Registrar Pagos",  padding="0px",color="white",position="relative",left="90px",top="50px"),
        rx.text("Enviar Facturas",padding="0px",color="white",position="relative",left="90px",top="60px"),
        rx.text("Enviar Recordatorios", padding="0px",color="white",position="relative",left="90px",top="70px"),
        rx.text("Configuración", padding="0px",color="white",position="relative",left="90px",top="80px"),
        rx.text("Salir", padding="0px",color="white",position="relative",left="90px",top="90px"),
        position="absolute",
        background_color="#E9124C",  
        width="22%",  # Ancho de la barra lateral
        height="100vh",  # Alto completo de la pantalla
        ),


    



    