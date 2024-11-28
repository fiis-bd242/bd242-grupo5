import reflex as rx
import sqlalchemy

from typing import Optional
from datetime import date
from sqlmodel import Field

from .. import utils

class Persona(rx.Model, table=True):
    id_persona: str = Field(primary_key=True)
    nombre: str
    nro_domicilio: int 
    ciudad: str 
    nro_documento: str
    tipo_documento: str

class Zona(rx.Model, table=True):
    id_zona: str = Field(primary_key=True)
    piso: int
    referencia: str
    nombre_zona: str

class Espacio_Comercial(rx.Model, table=True):
    id_espacio_comercial: str = Field(primary_key=True)
    tipo_inmueble: str
    estado: str
    area: float
    tarifa: float
    id_zona: str = Field(foreign_key="zona.id_zona")

class Inquilino(rx.Model, table=True):
    id_inquilino: str = Field(primary_key=True)
    razon_social: str
    fecha_eliminacion: Optional[date]
    fecha_registro: date
    estado_inquilino: str
    id_persona: str = Field(foreign_key="persona.id_persona")
    id_espacio_comercial: str = Field(foreign_key="espacio_comercial.id_espacio_comercial")
