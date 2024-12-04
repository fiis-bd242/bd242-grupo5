import reflex as rx
import sqlalchemy

from typing import Optional
from datetime import date
from sqlmodel import Field

# Clase para representar un Acuerdo relacionado con Recobros
class Acuerdo(rx.Model, table=True):
    id_acuerdo: str = Field(primary_key=True)
    descripcion: str
    fecha_creacion: date
    estado: str  # Por ejemplo: Activo, Finalizado, Pendiente
    monto: float

# Clase para representar un Proyecto de Recobros
class Proyecto_Recobros(rx.Model, table=True):
    id_proyecto: str = Field(primary_key=True)
    nombre_proyecto: str
    descripcion: str
    costo: float
    fecha_inicio: date
    fecha_fin: date
    estado: str  # Por ejemplo: Activo, Cerrado, En Evaluación

# Clase para representar una Solicitud de Recobros
class Solicitud_Recobros(rx.Model, table=True):
    id_solicitud: str = Field(primary_key=True)
    categoria: str
    fecha_solicitud: date
    estado: str  # Por ejemplo: En Proceso, Aprobada, Rechazada
    id_recobro: str = Field(foreign_key="recobros.id_recobro")
