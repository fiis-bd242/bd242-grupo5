import reflex as rx
from sqlmodel import Field
from typing import Optional
from datetime import date


class Inquilino(rx.Model, table=True):
    # Primary key
    id_inquilino: str = Field(primary_key=True)

    # Foreign Key
    id_persona: str = Field(foreign_key="persona.id_persona")
    id_espacio_comercial: str = Field(
        foreign_key="espacio_comercial.id_espacio_comercial"
    )

    # Attributes
    razon_social: str
    fecha_eliminacion: Optional[date]
    fecha_registro: date
    estado_inquilino: str
