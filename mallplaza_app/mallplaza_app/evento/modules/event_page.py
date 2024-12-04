import reflex as rx
from mall_plaza.repository import QueryEvento
from mall_plaza.model import EventoModel


@rx.page(route="/evento/search", title="Ver Eventos")
def evento_page() -> rx.Component:
    return rx.flex(
        rx.heading("Usuarios", align="center"),
        rx.hstack(
            buscar_evento(),
            justify='center',
            style={'margin-top': '30px'}
        ),
        table_eventos(QueryEvento.eventos),
    )


def table_eventos(lista_evento: list[EventoModel]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Codigo"),
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Descripcion"),
                rx.table.column_header_cell("Categoria"),
                rx.table.column_header_cell("Objetivo"),
                rx.table.column_header_cell("Inicio"),
                rx.table.column_header_cell("Fin"),
            )
        ),
        rx.table.body(rx.foreach(lista_evento, row_table)),
    )


def row_table(evento: EventoModel) -> rx.Component:
    return rx.table.row(
        rx.table.cell(evento.codigo_evento),
        rx.table.cell(evento.nombre_evento),
        rx.table.cell(evento.descripcion),
        rx.table.cell(evento.categoria),
        rx.table.cell(evento.objetivo),
        rx.table.cell(evento.fecha_inicio),
        rx.table.cell(evento.fecha_fin),
    )


def buscar_evento() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ingrese codigo del evento",
                 on_change=QueryEvento.codigo_evento),
        rx.input(placeholder="Ingrese nombre del evento",
                 on_change=QueryEvento.nombre_evento),
        rx.button('Buscar Eventos', on_click=QueryEvento.get_users())
    )
