import reflex as rx

from ..ui.base import base_page

from .model import RegistroIncidencia

class IncidenciaState(rx.State):
    RegistroIncidencia:list[RegistroIncidencia]
    registro_buscar: str
    error: str = ''

def incidencia_page() -> rx.Component:
    my_child = rx.flex(
            rx.heading("Inquilino", align="center"),
            rx.hstack(
                #buscar_inquilino_component(),
                #create_inquilino_dialog_component(),
                justify='center',
                style={'margin-top': '30px'}
            ),
            table_incidencia(IncidenciaState.RegistroIncidencia),
            # rx.cond(
            #     IncidenciaState.error != '',
            #     notify_component(InquilinoState.error, 'shield-alert','yellow')
            # ),
            IncidenciaState.error != '',
            direction='column',
            style={"width": "60vw", "margin":"auto"}
        )
    
    return base_page(my_child)

def table_incidencia(list_incidencia: list[RegistroIncidencia]):
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Código de Incidencia"),
                rx.table.column_header_cell("Descripcion"),
                rx.table.column_header_cell("fecha_hora_registro"),
                rx.table.column_header_cell("Estado"),
                rx.table.column_header_cell("Accion")
            )
        ),
        rx.table.body(
            rx.foreach(list_incidencia, row_table)
        )
    )

def row_table(incidencia: RegistroIncidencia) -> rx.Component:
    return rx.table.row(
        rx.table.cell(incidencia.cod_incidencia),
        rx.table.cell(incidencia.descripcion),
        rx.table.cell(incidencia.fecha_hora_registro),
        rx.table.cell(incidencia.estado),
        rx.table.cell(rx.hstack(
            delete_incidencia_dialog_component(incidencia.cod_incidencia)
        )),
    )

def delete_incidencia_dialog_component(cod_incidencia: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon("trash-2"))),
        rx.dialog.content(
            rx.dialog.title('Eliminar incidencia'),
            rx.dialog.description("¿Está seguro de querer eliminar la incidencia " + str(cod_incidencia)),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        'Cancelar',
                        color_scheme='gray',
                        variant='soft'
                    )
                ),
                rx.dialog.close(
                    rx.button(
                        'Confirmar',
                        #on_click=IncidenciaState.delete_incidencia_by_name(cod_incidencia)
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            )
        )
    )