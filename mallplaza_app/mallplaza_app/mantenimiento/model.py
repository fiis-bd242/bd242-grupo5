import reflex as rx
import sqlalchemy

from typing import Optional
from datetime import date, datetime
from sqlmodel import Field

from ..inquilino.model import Zona, Persona

from .. import utils

class Instalacion(rx.Model, table=True):
    id_instalacion: str = Field(primary_key=True)
    nombre_instalacion: str
    id_zona: str = Field(foreign_key="zona.id_zona")

class ProgramMantenimiento(rx.Model, table=True):
    dod_mantenimiento: int = Field(primary_key=True)
    plazo: date
    descripcion: str
    estado: str = Field(default="Pendiente")
    id_instalacion: str = Field(foreign_key="instalacion.id_instalacion")
    id_encargado: str = Field(foreign_key="empleado.id_empleado")
    prioridad: str = Field(foreign_key="prioridad.prioridad")
    cod_incidencia: int = Field(foreign_key="registro_de_incidencia.cod_incidencia", nullable=True)

class Empleado(rx.Model, table=True):
    id_empleado: str = Field(primary_key=True)
    cargo: str
    first_last_name: str
    second_last_name: str
    fecha_nacimiento: date
    id_persona: str = Field(foreign_key="persona.id_persona")
    #id_contrato_empleado: str = Field(foreign_key="contrato_empleado.id_contrato_empleado")

class RegistroIncidencia(rx.Model, table=True):
    cod_incidencia: int = Field(primary_key=True)
    descripcion: str
    fecha_hora_registro: datetime
    estado: str = Field(default="Pendiente")
    id_instalacion: str = Field(foreign_key="instalacion.id_instalacion") 
    id_empleado: str = Field(foreign_key="empleado.id_empleado")

class Prioridad(rx.Model, table=True):
    prioridad: str = Field(primary_key=True)
    descrip_prioridad: str