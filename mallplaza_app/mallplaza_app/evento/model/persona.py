import reflex as rx
from sqlmodel import Field


class Persona(rx.Model, table=True):
    # Primary key
    id_persona: str = Field(primary_key=True)

    # Foreign key

    # Attributes
    nombre: str
    nro_domicilio: int
    ciudad: str
    nro_documento: str
    tipo_documento: str
