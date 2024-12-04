import reflex as rx
import sqlalchemy

from typing import Optional
from datetime import date
from sqlmodel import Field

from ..inquilino.model import Zona

from .. import utils

# class Instalacion(rx.Model, table=True):
#     id_instalacion: str = rx.Field(primary_key=True)
#     nombre_instalacion: str
#     id_zona: str = rx.Field(foreign_key="zona.id_zona")


