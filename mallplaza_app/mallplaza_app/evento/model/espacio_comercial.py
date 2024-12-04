import reflex as rx
from sqlmodel import Field


class Espacio_Comercial(rx.Model, table=True):
    # Primary Key
    id_espacio_comercial: str = Field(primary_key=True)

    # Foreign Key
    id_zona: str = Field(foreign_key="zona.id_zona")

    # Attributes
    tipo_inmueble: str
    estado: str
    area: float
    tarifa: float
