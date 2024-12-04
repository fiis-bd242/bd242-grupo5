import reflex as rx
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/reflex_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener el siguiente ID disponible
def obtener_siguiente_id(tabla: str, prefix: str) -> str:
    session = SessionLocal()
    try:
        query = text(f"SELECT MAX(CAST(SUBSTRING(id_{tabla}, 2) AS INT)) FROM {tabla}")
        max_id = session.execute(query).scalar()
        if max_id is None:
            return f"{prefix}001"  # Si no hay registros, iniciar en 001
        return f"{prefix}{str(max_id + 1).zfill(3)}"  # Incrementar y formatear a tres dígitos
    finally:
        session.close()

# Función para insertar datos en la base de datos
# Función para insertar datos en la base de datos
def insertar_empleado(data: dict):
    session = SessionLocal()

    # Mapas para valores válidos
    estado_contrato_map = {"activo": "Activo", "finalizado": "Finalizado", "suspendido": "Suspendido"}
    jornada_laboral_map = {"completa": "Completa", "parcial": "Parcial", "turno rotativo": "Turno rotativo"}

    try:
        # Validar y mapear los valores de estado_contrato y jornada_laboral
        estado_contrato_valido = estado_contrato_map.get(data.get("estado_contrato", "").lower(), "Activo")
        jornada_laboral_valida = jornada_laboral_map.get(data.get("jornada_laboral", "").lower(), "Completa")

        # 1. Insertar en la tabla Contrato_Empleado
        id_contrato_empleado = obtener_siguiente_id("Contrato_Empleado", "C")
        session.execute(text("""
            INSERT INTO Contrato_Empleado (id_contrato_empleado, descripcion_cargo, fecha_inicio, fecha_fin, estado_contrato, jornada_laboral)
            VALUES (:id_contrato_empleado, :descripcion_cargo, :fecha_inicio, :fecha_fin, :estado_contrato, :jornada_laboral)
        """), {
            "id_contrato_empleado": id_contrato_empleado,
            "descripcion_cargo": data.get("puesto", ""),
            "fecha_inicio": data.get("fecha_inicio"),  # None si está vacío
            "fecha_fin": data.get("fecha_fin"),  # None si está vacío
            "estado_contrato": estado_contrato_valido,
            "jornada_laboral": jornada_laboral_valida,
        })

        # 2. Insertar en la tabla Persona
        id_persona = obtener_siguiente_id("Persona", "P")
        session.execute(text("""
            INSERT INTO Persona (id_persona, nombre, nro_domicilio, ciudad, nro_documento, tipo_documento)
            VALUES (:id_persona, :nombre, :nro_domicilio, :ciudad, :nro_documento, :tipo_documento)
        """), {
            "id_persona": id_persona,
            "nombre": data.get("nombres", ""),
            "nro_domicilio": data.get("nro_domicilio", 0),
            "ciudad": data.get("ciudad", ""),
            "nro_documento": data.get("nro_documento", ""),
            "tipo_documento": "DNI",  # Asumiendo un tipo de documento fijo
        })

        # 3. Insertar en la tabla Empleado
        id_empleado = obtener_siguiente_id("Empleado", "E")
        session.execute(text("""
            INSERT INTO Empleado (id_empleado, cargo, first_last_name, second_last_name, fecha_nacimiento, id_persona, id_contrato_empleado)
            VALUES (:id_empleado, :cargo, :first_last_name, :second_last_name, :fecha_nacimiento, :id_persona, :id_contrato_empleado)
        """), {
            "id_empleado": id_empleado,
            "cargo": data.get("puesto", ""),
            "first_last_name": data.get("first_last_name", ""),
            "second_last_name": data.get("second_last_name", ""),
            "fecha_nacimiento": data.get("fecha_nacimiento", None),  # None si está vacío
            "id_persona": id_persona,
            "id_contrato_empleado": id_contrato_empleado,
        })

        # Confirmar la transacción
        session.commit()
        print("Datos insertados correctamente en Persona, Empleado y Contrato_Empleado.")
    except Exception as e:
        session.rollback()
        print(f"Error al insertar datos: {e}")
    finally:
        session.close()



# Clase de estado para gestionar los datos del formulario
class FormState(rx.State):
    nombres: str = ""
    first_last_name: str = ""
    second_last_name: str = ""
    nro_documento: str = ""
    nro_domicilio: int = 0
    ciudad: str = ""
    fecha_nacimiento: str = ""
    puesto: str = ""
    estado_contrato: str = "Activo"
    fecha_inicio: str = ""
    fecha_fin: str = ""
    jornada_laboral: str = "Completa"

    def submit_form(self):
        print("Validando datos del formulario...")  # Depuración
        data = {
            "nombres": self.nombres,
            "first_last_name": self.first_last_name,
            "second_last_name": self.second_last_name,
            "nro_documento": self.nro_documento,
            "nro_domicilio": self.nro_domicilio,
            "ciudad": self.ciudad,
            "fecha_nacimiento": self.fecha_nacimiento or None,  # Validar si está vacío
            "puesto": self.puesto,
            "estado_contrato": self.estado_contrato or "Activo",  # Valor predeterminado
            "fecha_inicio": self.fecha_inicio or None,  # Validar si está vacío
            "fecha_fin": self.fecha_fin or None,  # Validar si está vacío
            "jornada_laboral": self.jornada_laboral,
        }

        print("Datos validados:", data)  # Depuración
        insertar_empleado(data)

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

@rx.page(route="/registrar_empleado", title="Registrar empleado")
def registrar_empleado() -> rx.Component:
    formulario = rx.vstack(
        rx.heading("Agregar empleado", size="lg", padding="4", color="#E9124C"),
        rx.vstack(
            rx.hstack(rx.text("Nombres:"), rx.input(on_change=FormState.set_nombres, placeholder="Ingrese los nombres"), spacing="4"),
            rx.hstack(rx.text("Apellido Paterno:"), rx.input(on_change=FormState.set_first_last_name, placeholder="Ingrese el apellido paterno"), spacing="4"),
            rx.hstack(rx.text("Apellido Materno:"), rx.input(on_change=FormState.set_second_last_name, placeholder="Ingrese el apellido materno"), spacing="4"),
            rx.hstack(rx.text("DNI:"), rx.input(on_change=FormState.set_nro_documento, placeholder="Ingrese el DNI"), spacing="4"),
            rx.hstack(rx.text("Dirección:"), rx.input(on_change=FormState.set_nro_domicilio, placeholder="Ingrese el número de domicilio"), spacing="4"),
            rx.hstack(rx.text("Ciudad:"), rx.input(on_change=FormState.set_ciudad, placeholder="Ingrese la ciudad"), spacing="4"),
            rx.hstack(rx.text("Fecha de nacimiento:"), rx.input(type="date", on_change=FormState.set_fecha_nacimiento), spacing="4"),
            rx.hstack(rx.text("Puesto:"), rx.input(on_change=FormState.set_puesto, placeholder="Ingrese el puesto"), spacing="4"),
            rx.hstack(rx.text("Estado del contrato:"), rx.select(["Activo", "Finalizado", "Suspendido"], on_change=FormState.set_estado_contrato), spacing="4"),
            rx.hstack(rx.text("Fecha de inicio:"), rx.input(type="date", on_change=FormState.set_fecha_inicio), spacing="4"),
            rx.hstack(rx.text("Fecha de finalización:"), rx.input(type="date", on_change=FormState.set_fecha_fin), spacing="4"),
            rx.hstack(rx.text("Jornada laboral:"), rx.select(["Completa", "Parcial", "Turno rotativo"], on_change=FormState.set_jornada_laboral), spacing="4"),
            spacing="4",
        ),
        rx.hstack(
            rx.button("Confirmar", bg="#E9124C", color="white", on_click=FormState.submit_form),
            justify="end",
            spacing="4",
        ),
        spacing="6",
        padding="6",
        bg="white",
        box_shadow="lg",
        border_radius="md",
        border="1px ", 
        width="70%",
    )

    # Coloca el sidebar y el formulario en un hstack
    return rx.hstack(sidebar, formulario, width="100%", height="100vh")


