import reflex as rx
from mall_plaza.model import EventoModel
from typing import Optional
from datetime import datetime


class AddEvento(rx.State):
    id_espacio_comun: str
    codigo_evento: str
    nombre_evento: str
    descripcion: str
    categoria: str
    objetivo: str
    fecha_inicio: datetime
    fecha_fin: datetime
    id_inquilino: str

    @rx.event
    def add_user(self):
        with rx.session() as session:
            session.add(
                EventoModel(
                    id_espacio_comun=self.id_espacio_comun,
                    codigo_evento=self.codigo_evento,
                    nombre_evento=self.nombre_evento,
                    descripcion=self.descripcion,
                    categoria=self.categoria,
                    objetivo=self.objetivo,
                    fecha_inicio=self.fecha_inicio,
                    fecha_fin=self.fecha_fin,
                    id_inquilino=self.id_inquilino,
                )
            )
            session.commit()


class QueryEvento(rx.State):
    codigo_evento: Optional[str]
    nombre_evento: str = ""
    eventos: list[EventoModel]

    @rx.event
    def get_users(self):
        with rx.session() as session:
            if self.codigo_evento is not None:
                self.eventos = session.exec(
                    EventoModel.select().where(
                        EventoModel.codigo_evento.contains(self.codigo_evento)
                    )
                ).all()
            else:
                self.eventos = session.exec(
                    EventoModel.select().where(
                        EventoModel.nombre_evento.contains(self.nombre_evento)
                    )
                ).all()
