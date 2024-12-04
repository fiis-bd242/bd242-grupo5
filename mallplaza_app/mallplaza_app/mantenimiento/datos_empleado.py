import reflex as rx
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/reflex_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener los datos del empleado
def obtener_empleado_por_id(id_empleado: str):
    session = SessionLocal()
    try:
        query = text("""
        SELECT E.id_empleado, P.nombre, E.first_last_name, E.second_last_name, E.fecha_nacimiento, E.cargo, C.estado_contrato
        FROM Empleado E
        JOIN Contrato_Empleado C ON E.id_contrato_empleado = C.id_contrato_empleado
        JOIN Persona P ON P.id_persona = E.id_persona
        WHERE E.id_empleado = :id_empleado
        """)
        empleado = session.execute(query, {'id_empleado': id_empleado}).fetchone()
        return empleado
    finally:
        session.close()

# Página que muestra los datos de un empleado con una URL estática
@rx.page(route="/datos_empleado", title="Datos empleado")
def datos_empleado() -> rx.Component:
    # ID estático del empleado
    id_empleado = "E004"  # Cambia este ID según el empleado que quieras mostrar

    # Obtener los datos del empleado usando el id_empleado (en este caso como string)
    empleado = obtener_empleado_por_id(id_empleado)

    # Verifica si se encontró el empleado
    if not empleado:
        return rx.text("Empleado no encontrado", color="red")

    # Barra lateral
    sidebar = rx.vstack(
        rx.box("mallplaza", bg="#E9124C", color="white", font_size="2xl", padding="4", font_weight="bold"),
        rx.button("Perfil de usuario", icon="user", bg="#E9124C", color="white", justify="left"),
        rx.button("Facturación", icon="credit-card", bg="#E9124C", color="white", justify="left"),
        rx.button("Arrendamientos", icon="home", bg="#E9124C", color="white", justify="left"),
        rx.button("Eventos", icon="calendar", bg="#E9124C", color="white", justify="left"),
        rx.button("Mantenimiento", icon="wrench", bg="#E9124C", color="white", justify="left"),
        rx.button("Configuración", icon="settings", bg="#E9124C", color="white", justify="left"),
        rx.button("Salir", icon="logout", bg="#E9124C", color="white", justify="left"),
        width="20%", height="100vh", padding="4", align="start", spacing="4", bg="#E9124C",
    )

    # Contenido principal con los datos del empleado
    main_content = rx.vstack(
        rx.heading(f"{empleado[1]} {empleado[2]} {empleado[3]}", color="black", font_size="100", font_weight="bold", align_self="start"),
        rx.image(
            src="https://w7.pngwing.com/pngs/178/595/png-transparent-user-profile-computer-icons-login-user-avatars-thumbnail.png",
            box_size="120px", border_radius="full", margin_top="4",
        ),
        rx.hstack(
            rx.button("Ver contrato", bg="#E9124C", color="white", padding="4"),
            rx.button("Renovar", bg="#E9124C", color="white", padding="4"),
            rx.button("Volver", bg="#E9124C", color="white", padding="4"),
            spacing="4",
            margin_top="4",
        ),
        rx.vstack(
            rx.hstack(
                rx.text("DNI:", font_weight="bold", color="black"),
                rx.text(f"{empleado[0]}", bg="#FFD4DB", padding="2", border_radius="md", color="black"),
                spacing="4"
            ),
            rx.hstack(
                rx.text("Cargo:", font_weight="bold", color="black"),
                rx.text(f"{empleado[5]}", bg="#FFD4DB", padding="2", border_radius="md", color="black"),
                spacing="4"
            ),
            rx.hstack(
                rx.text("Contratación:", font_weight="bold", color="black"),
                rx.text(f"{empleado[4]}", bg="#FFD4DB", padding="2", border_radius="md", color="black"),
                spacing="4"
            ),
            rx.hstack(
                rx.text("Estado de contrato:", font_weight="bold", color="black"),
                rx.text(f"{empleado[6]}", bg="#FFD4DB", padding="2", border_radius="md", color="black"),
                spacing="4"
            ),
            align="start",  
            spacing="4",  
            margin_top="6", 
        ),
        align="start",  
        spacing="6",  
        padding="6",  
    )

    return rx.hstack(
        sidebar,  
        main_content, 
        bg="white",
    )
