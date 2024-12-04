import reflex as rx
from uuid import UUID, uuid4
from sqlmodel import Field
import datetime


class Evento(rx.Model, table=True):
    # Primary key
    id: UUID = Field(primary_key=True, default=uuid4())

    # Foreign key
    id_espacio_comun: str = Field(foreign_key="espacio_comun.id_espacio_comun")

    # Attributes
    codigo_evento: str = Field(unique=True)
    nombre_evento: str
    descripcion: str
    categoria: str
    objetivo: str
    fecha_inicio: datetime.datetime
    fecha_fin: datetime.datetime
    id_inquilino: str
