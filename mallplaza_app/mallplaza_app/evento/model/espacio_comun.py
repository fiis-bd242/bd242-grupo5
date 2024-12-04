import reflex as rx
from sqlmodel import Field


class Espacio_comun(rx.Model, table=True):
    # Primary Key
    id_espacio_comun: str = Field(primary_key=True)

    # Foreign Key
    id_zona: str = Field(foreign_key="zona.id_zona")

    # Attributes
    estado: str
    area: float
    precio_por_dia: float
    motivo_de_uso: str
