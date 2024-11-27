import reflex as rx

from ..database import SessionLocal
from ..ui.base import base_page

from sqlalchemy.future import select
from sqlalchemy import Column, CHAR, VARCHAR, Date, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship, declarative_base

#from ..models import Inquilino

def about_inquilino() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Inquilino", size="9"),
            rx.text(
                "Tabla de inquilino",
            ),
            spacing="5",
            justify="center",
            align="stretch",
            min_height="85vh",
        )
    return base_page(my_child)

# Base = declarative_base()  # Base para definir tus modelos
# # Crear una sesión
# session = SessionLocal()
# # Consultar todos los registros de la tabla `Inquilino`
# result = session.query(Inquilino).all()
# for inquilino in result:
#     print(f"ID: {inquilino.id_inquilino}, Razón Social: {inquilino.razon_social}")
# # Cerrar la sesión
# session.close()

# with rx.session() as session:
#     result = session.exec(select(inquilino)).all()
#     print(result)
