import reflex as rx
from sqlmodel import Field


class Zona(rx.Model, table=True):
    # Primary key
    id_zona: str = Field(primary_key=True)

    # Foreign key

    # Attributes
    piso: int
    referencia: str
    nombre_zona: str
