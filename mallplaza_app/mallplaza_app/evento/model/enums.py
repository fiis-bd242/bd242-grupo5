from enum import Enum


class Estado_espacio_comun(str, Enum):
    DISPONIBLE = "disponible"
    OCUPADO = "ocupado"
    MANTENIMIENTO = "mantenimiento"
