import reflex as rx

from ..database import SessionLocal
from ..ui.base import base_page
from .model import Inquilino
from .notify import notify_component
import asyncio

from sqlalchemy.future import select
from sqlalchemy.orm import relationship, declarative_base
from .service import select_all_inquilino_service, select_inquilino_by_name_service, create_inquilino_service, delete_inquilino_service

#from ..models import Inquilino

# def about_inquilino() -> rx.Component:
#     my_child = rx.vstack(
#             rx.heading("Inquilino", size="9"),
#             rx.text(
#                 "Tabla de inquilino",
#             ),
#             spacing="5",
#             justify="center",
#             align="stretch",
#             min_height="85vh",
#         )
#     return base_page(my_child)

class InquilinoState(rx.State):
    inquilino:list[Inquilino]
    inquilino_buscar: str
    error: str = ''

    @rx.background
    async def get_all_inquilino(self):
        async with self:
            self.inquilino = select_all_inquilino_service()

    @rx.background
    async def get_inquilino_by_name(self):
        async with self:
            self.inquilino = select_inquilino_by_name_service(self.inquilino_buscar)

    async def handleNotify(self):
        async with self:
            await asyncio.sleep(2)
            self.error = ''

    @rx.background
    async def create_inquilino(self, data: dict):
        async with self:
            try:
                self.inquilino=create_inquilino_service(id_inquilino=data['id_inquilino'], razon_social=data['razon_social'], fecha_registro=data['fecha_registro'],estado_inquilino=data['estado_inquilino'], id_persona=data['id_persona'], id_espacio_comercial=['id_espacio_comercial'])
            except BaseException as be:
                print(be.args)
                self.error = be.args
        await self.handleNotify()

    def buscar_on_change(self, value: str):
        self.inquilino_buscar = value

    @rx.background
    async def delete_inquilino_by_name(self, razon_social):
        async with self:
            self.inquilino = delete_inquilino_service(razon_social)

#Main
def inquilino_page() -> rx.Component:
    return rx.flex(
        rx.heading("Inquilino", align="center"),
        rx.hstack(
            buscar_inquilino_component(),
            create_inquilino_dialog_component(),
            justify='center',
            style={'margin-top': '30px'}
        ),
        table_inquilino(InquilinoState.inquilino),
        rx.cond(
            InquilinoState.error != '',
            notify_component(InquilinoState.error, 'shield-alert','yellow')
        ),
        direction='column',
        style={"width": "60vw", "margin":"auto"}
    )

def table_inquilino(list_inquilino: list[Inquilino]):
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Fecha Registro"),
                rx.table.column_header_cell("Estado"),
                rx.table.column_header_cell("Espacio Comercial"),
                rx.table.column_header_cell("Accion")
            )
        ),
        rx.table.body(
            rx.foreach(list_inquilino, row_table)
        )
    )

def row_table(inquilino: Inquilino) -> rx.Component:
    return rx.table.row(
        rx.table.cell(inquilino.razon_social),
        rx.table.cell(inquilino.fecha_registro),
        rx.table.cell(inquilino.estado_inquilino),
        rx.table.cell(inquilino.id_espacio_comercial),
        rx.table.cell(rx.hstack(
            delete_inquilino_dialog_component(inquilino.razon_social)
        )),
    )

def buscar_inquilino_component() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ingrese nombre", on_change=InquilinoState.buscar_on_change),
        rx.button('Buscar inquilino', on_click=InquilinoState.get_inquilino_by_name)
    )



def create_inquilino_form() -> rx. Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder='id',
                name="id_inquilino",
            ),
            rx.input(
                placeholder='razon_social',
                name="razon_social"
            ),
            rx.input(
                type= "date",
                name="fecha_registro"
            ),
            rx.input(
                placeholder='Estado',
                name="estado_inquilino"
            ),
            rx.input(
                placeholder='Código de persona',
                name="id_persona"
            ),
            rx.input(
                placeholder='Código Espacio Comercial',
                name="id_espacio_comercial"
            ),
            rx.dialog.close(
                rx.button('Guardar', type='submit')
            ),
        ),
        on_submit=InquilinoState.create_inquilino,
    )

def create_inquilino_dialog_component() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button('Crear Inquilino')),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Crear Inquilino"),
                create_inquilino_form(),
                justify="center",
                align="center",
                direction="column",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
            style={"width": "400px"},
        ),
    )

def delete_inquilino_dialog_component(razon_social: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button(rx.icon("trash-2"))),
        rx.dialog.content(
            rx.dialog.title('Eliminar inquilino'),
            rx.dialog.description("¿Está seguro de querer eliminar el inquilino " + razon_social),
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
                        on_click=InquilinoState.delete_inquilino_by_name(razon_social)
                    )
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            )
        )
    )