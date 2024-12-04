import reflex as rx

@rx.page(route="/renovar_contrato", title="Renovar contrato")
def renovar_contrato() -> rx.Component:
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
    
    # Formulario para la renovación de contrato
    formulario = rx.vstack(
        rx.heading("Renovación de contrato", size="md", bg="#E9124C", color="white", padding="4"),
        rx.vstack(
            rx.hstack(rx.text("Nro de contrato:", color="black"), rx.input(placeholder="Ingrese el número de contrato"), spacing="4"),
            rx.hstack(rx.text("Nombre completo:", color="black"), rx.input(placeholder="Ingrese el nombre completo"), spacing="4"),
            rx.hstack(rx.text("DNI:", color="black"), rx.input(placeholder="Ingrese el DNI"), spacing="4"),
            rx.hstack(rx.text("Dirección:", color="black"), rx.input(placeholder="Ingrese la dirección"), spacing="4"),
            rx.hstack(rx.text("Puesto:", color="black"), rx.input(placeholder="Ingrese el puesto"), spacing="4"),
            rx.hstack(rx.text("Jornada laboral:", color="black"), rx.input(placeholder="Ingrese la jornada laboral"), spacing="4"),
            rx.hstack(rx.text("Fecha de inicio:", color="black"), rx.input(type="date"), spacing="4"),
            rx.hstack(rx.text("Fecha de finalización:", color="black"), rx.input(type="date"), spacing="4"),
            rx.hstack(rx.text("Salario:", color="black"), rx.input(placeholder="Ingrese el salario"), spacing="4"),
            spacing="4",
        ),
        rx.hstack(
            rx.button("Confirmar", bg="#E9124C", color="white"),
            rx.button("Volver", bg="gray", color="white"),
            justify="end",
            spacing="4",
            padding="4",
        ),
        spacing="6",
        padding="4",
        bg="white",
        box_shadow="lg",
        border_radius="md",
        border="2px solid black",  # Marco negro
        width="70%",
    )
    
    # Contenedor principal centrado
    contenedor_central = rx.box(
        formulario,
        display="flex",
        align_items="center",
        justify_content="center",
        height="100vh",  # Altura completa de la ventana
        width="100%",  # Ancho completo
    )
    
    # Estructura principal
    return rx.hstack(
        sidebar,
        contenedor_central,
        height="100vh",
        bg="white",
    )
