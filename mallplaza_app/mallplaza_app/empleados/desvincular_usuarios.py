import reflex as rx
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/reflex_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Función para obtener empleados activos
def obtener_empleados_activos():
    session = SessionLocal()
    try:
        query = text("""
            SELECT E.id_empleado, E.cargo, E.first_last_name, E.second_last_name, E.fecha_nacimiento
            FROM Empleado E
            JOIN Contrato_Empleado C ON E.id_contrato_empleado = C.id_contrato_empleado
            WHERE C.estado_contrato = 'Activo';
        """)
        resultados = session.execute(query).fetchall()
        return [
            {
                "id_empleado": row[0],
                "cargo": row[1],
                "first_last_name": row[2],
                "second_last_name": row[3],
                "fecha_nacimiento": row[4],
            }
            for row in resultados
        ]
    finally:
        session.close()


# Función para desvincular empleado
def desvincular_empleado(id_empleado):
    session = SessionLocal()
    try:
        # Actualizar el estado del contrato a 'Desvinculado'
        query = text("""
            UPDATE Contrato_Empleado
            SET estado_contrato = 'Suspendido'
            WHERE id_contrato_empleado = (
                SELECT id_contrato_empleado
                FROM Empleado
                WHERE id_empleado = :id_empleado
            );
        """)
        session.execute(query, {"id_empleado": id_empleado})
        session.commit()
        print(f"Empleado {id_empleado} desvinculado correctamente.")
    except Exception as e:
        session.rollback()
        print(f"Error al desvincular empleado: {e}")
    finally:
        session.close()


# Estado de la aplicación
class DesvincularUsuarioState(rx.State):
    empleados_activos: list = []
    modal_abierto: str = ""  # ID del empleado cuyo modal está abierto
    empleado_nombre: str = ""  # Nombre del empleado actualmente seleccionado

    @staticmethod
    def cargar_usuarios_activos():
        DesvincularUsuarioState.empleados_activos = obtener_empleados_activos()

    def abrir_modal(self, id_empleado: str):
        self.modal_abierto = id_empleado
        # Encontrar y guardar el nombre completo del empleado seleccionado
        for empleado in self.empleados_activos:
            if empleado["id_empleado"] == id_empleado:
                self.empleado_nombre = f"{empleado['first_last_name']} {empleado['second_last_name']}"
                break

    def cerrar_modal(self):
        self.modal_abierto = ""
        self.empleado_nombre = ""

    def confirmar_desvinculacion(self):
        desvincular_empleado(self.modal_abierto)
        self.cerrar_modal()
        self.cargar_usuarios_activos()


# Sidebar proporcionado por el usuario
sidebar = rx.vstack(
    rx.box("mallplaza", bg="red.500", color="white", font_size="2xl", padding=4),
    rx.button("Perfil de usuario", icon="user", bg="#E9124C", color="white"),
    rx.button("Facturación", icon="credit-card", bg="#E9124C", color="white"),
    rx.button("Arrendamientos", icon="home", bg="#E9124C", color="white"),
    rx.button("Eventos", icon="calendar", bg="#E9124C", color="white"),
    rx.button("Mantenimiento", icon="wrench", bg="#E9124C", color="white"),
    rx.button("Configuración", icon="settings", bg="#E9124C", color="white"),
    rx.button("Salir", icon="logout", bg="#E9124C", color="white"),
    width="20%", height="100vh", padding=4, align="start", spacing="2", bg="#E9124C",
)


# Página con la tabla de empleados activos y el modal
@rx.page(route="/desvincular_usuarios", title="Desvincular Usuarios")
def desvincular_usuarios() -> rx.Component:
    DesvincularUsuarioState.cargar_usuarios_activos()

    # Renderizar tabla de empleados activos
    tabla_empleados = rx.vstack(
        rx.heading("Usuarios activos", size="md", color="#E9124C", padding="4"),
        *[
            rx.hstack(
                rx.text(f"{empleado['first_last_name']} {empleado['second_last_name']}", flex=1),
                rx.button(
                    "Desvincular",
                    bg="red.500",
                    color="white",
                    on_click=lambda id=empleado["id_empleado"]: DesvincularUsuarioState.abrir_modal(id),
                ),
                spacing="4",
            )
            for empleado in DesvincularUsuarioState.empleados_activos
        ],
        spacing="4",
        padding="6",
        bg="white",
        box_shadow="lg",
        border_radius="md",
        width="70%",
    )

    # Modal personalizado
    modal = rx.cond(
        DesvincularUsuarioState.modal_abierto != "",  # Mostrar solo si el modal está abierto
        rx.box(
            rx.box(
                rx.text("¿Seguro que quieres desvincular a este usuario?", font_size="lg", font_weight="bold"),
                rx.text(DesvincularUsuarioState.empleado_nombre, margin_top="4"),
                rx.hstack(
                    rx.button(
                        "Desvincular",
                        bg="red.500",
                        color="white",
                        on_click=DesvincularUsuarioState.confirmar_desvinculacion,
                    ),
                    rx.button("Volver", on_click=DesvincularUsuarioState.cerrar_modal),
                    spacing="4",
                    margin_top="4",
                ),
                padding="6",
                bg="white",
                box_shadow="lg",
                border_radius="md",
                width="50%",
                margin="auto",
            ),
            position="fixed",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
            bg="rgba(0, 0, 0, 0.5)",  # Fondo semi-transparente
            z_index="10",
        ),
    )

    return rx.hstack(sidebar, rx.vstack(tabla_empleados, modal, spacing="6"), width="100%", height="100vh")



