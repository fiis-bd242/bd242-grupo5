import reflex as rx

@rx.page(route="/eliminar_empleado", title="Eliminar empleado")
def eliminar_empleado() -> rx.Component:
    # Barra lateral
    sidebar = rx.vstack(
        rx.box("mallplaza", bg="#E9124C", color="white", font_size="2xl", padding="4", font_weight="bold"),
        rx.button("Perfil de usuario", icon="user", bg="#E9124C", color="white", justify="left"),
        rx.button("Facturación", icon="credit-card", bg="#E9124C", color="white", justify="left"),
        rx.button("Arrendamientos", icon="home", bg="#E9124C", color="white", justify="left"),
        rx.button("Eventos", icon="calendar", bg="#E9124C", color="white", justify="left"),
        rx.button("Configuración", icon="settings", bg="#E9124C", color="white", justify="left"),
        rx.button("Salir", icon="logout", bg="#E9124C", color="white", justify="left"),
        width="20%", height="100vh", padding="4", align="start", spacing="4", bg="#E9124C",
    )

    # Lista de usuarios
    usuarios = [
        "Jairo Kazuo del Rio Gutierrez",
        "Jordan Cesar Laureano Quispe",
        "Alfredo Joel Quispe Mitma",
        "Anthony Bob Calderon Damian",
        "Edward Jose Diaz Vergaray",
        "Eduardo Cesar Quispe Quispe",
        "Luis Mamani Ramirez",
        "Elias Roger Ortiz Sosaya",
        "Leonardo Ramirez Villaverde",
    ]

    # Encabezado de usuarios
    encabezado = rx.hstack(
        rx.text("Nombre", font_weight="bold", flex="1", padding="2"),
        rx.text("Acción", font_weight="bold", flex="0.3", padding="2", text_align="center"),
        bg="#F8F8F8",  # Fondo gris claro para el encabezado
        padding="4",
    )

    # Fila de usuarios
    filas = [
        rx.hstack(
            rx.text(nombre, flex="1", padding="2"),
            rx.button(
                "Desvincular",
                bg="#E9124C",
                color="white",
                size="sm",
                border_radius="full",
                _hover={"bg": "#C10D3F"},  # Color al pasar el cursor
                flex="0.3",
            ),
            padding="4",
            border_bottom="1px solid #E0E0E0",
        )
        for nombre in usuarios
    ]

    # Tabla completa
    tabla_usuarios = rx.vstack(
        encabezado,
        *filas,
        border="1px solid black",
        border_radius="md",
        overflow="hidden",
        width="80%",
        bg="white",
        color="black"
    )

    # Contenedor central
    contenedor_central = rx.box(
        tabla_usuarios,
        display="flex",
        align_items="center",
        justify_content="center",
        height="100vh",  
        width="100%", 
    )

    return rx.hstack(
        sidebar,
        contenedor_central,
        height="100vh",
        bg="white",
    )
