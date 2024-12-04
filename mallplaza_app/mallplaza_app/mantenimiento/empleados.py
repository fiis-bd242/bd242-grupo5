import reflex as rx
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dataclasses import dataclass
from typing import List, Optional

# Configuración de la base de datos
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/reflex_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener empleados según filtros
def obtener_empleados(activos=False, desvinculados=False):
    session = SessionLocal()
    try:
        if activos:
            query = text("""
            SELECT E.id_empleado, E.cargo, E.first_last_name, E.second_last_name, E.fecha_nacimiento
            FROM Empleado E
            JOIN Contrato_Empleado C ON E.id_contrato_empleado = C.id_contrato_empleado
            WHERE C.estado_contrato = 'Activo';
            """)
        elif desvinculados:
            query = text("""
            SELECT E.id_empleado, E.cargo, E.first_last_name, E.second_last_name, E.fecha_nacimiento
            FROM Empleado E
            JOIN Contrato_Empleado C ON E.id_contrato_empleado = C.id_contrato_empleado
            WHERE C.estado_contrato IN ('Finalizado', 'Suspendido');
            """)
        else:
            query = text("""
            SELECT p.nombre, e.cargo FROM Empleado e JOIN 
                Persona p ON e.id_persona = p.id_persona
            """)

        empleados = session.execute(query).fetchall()
        return [{"id": empleado[0], "name": f"{empleado[2]} {empleado[3]}", "role": empleado[1]} for empleado in empleados]
    finally:
        session.close()

# Modelo de datos para empleados
@dataclass
class Empleado:
    id: int
    name: str
    role: str
    fecha_nacimiento: Optional[str] = None

# Estado global para manejar los empleados
class EmpleadosState(rx.State):
    empleados_data: List[Empleado] = []  # Lista tipada de empleados
    selected_empleado: Empleado = None  # Empleado seleccionado para detalles

    def cargar_empleados_activos(self):
        # Convertimos los datos obtenidos a objetos de tipo Empleado
        self.empleados_data = [
            Empleado(**empleado) for empleado in obtener_empleados(activos=True)
        ]

    def cargar_empleados_desvinculados(self):
        # Convertimos los datos obtenidos a objetos de tipo Empleado
        self.empleados_data = [
            Empleado(**empleado) for empleado in obtener_empleados(desvinculados=True)
        ]

    def set_selected_empleado(self, empleado_id: int):
        # Establece el empleado seleccionado según el ID
        empleado = next((emp for emp in self.empleados_data if emp.id == empleado_id), None)
        if empleado:
            self.selected_empleado = empleado


@rx.page(route="/empleados", title="Empleados")
def empleados() -> rx.Component:
    def user_card(empleado: Empleado):
        return rx.box(
            rx.text(empleado.name, font_weight="bold", color="#000000"),
            rx.text(empleado.role, font_size="sm", color="#000000"),
            bg="gray.200", padding=4, border_radius="md", width="100%", align="center",
            on_click=lambda: rx.redirect(f"/datos_empleado/{empleado.id}"),  # Aquí pasa el id correctamente
        )

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

    header = rx.heading("Usuarios", size="2xl", margin_bottom=4, color="#000000")
    tabs = rx.hstack(
        rx.button(
            "Activos",
            icon="user",
            bg="#FFFFFF",
            color="#E9124C",
            font_size=20,
            on_click=EmpleadosState.cargar_empleados_activos,
        ),
        rx.button(
            "Desvinculados",
            icon="credit-card",
            bg="#FFFFFF",
            color="#E9124C",
            font_size=20,
            on_click=EmpleadosState.cargar_empleados_desvinculados,
        ),
        spacing="4",
    )

    user_grid = rx.foreach(
        EmpleadosState.empleados_data,
        lambda user: user_card(user),  # Pasamos el objeto empleado completo a la card
    )

    buttons = rx.hstack(
        rx.button("Registrar", color="white", bg="#E9124C"),
        rx.button("Desvincular", bg="#E9124C", color="white"),
        spacing="4",
    )

    main_content = rx.vstack(
        header,
        tabs,
        user_grid,
        buttons,
        spacing="6",
        padding=4,
    )

    return rx.hstack(
        sidebar,
        main_content,
    )


# Configuración de la aplicación
app = rx.App(state=EmpleadosState)
app.add_page(empleados)  
app._compile()  # Ahora usando _compile como requiere Reflex
