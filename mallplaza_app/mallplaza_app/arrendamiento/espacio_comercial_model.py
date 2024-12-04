'''
import reflex as rx
from sqlmodel import Field

class Espacio_comercial(rx.Model, table=True):
    id_espacio_comercial: str = Field(primary_key=True)  # Llave primaria
    tipo_inmueble: str
    estado: str
    area: float  # Usamos float para valores numéricos con decimales
    tarifa: float
    nombre_zona: str
'''
