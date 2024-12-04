import reflex as rx
#from .model.espacio_comercial_model import Espacio_comercial
#from .model.contrato_alquiler_model import Contrato_alquiler
#from .Service.espacio_comercial_service import select_all_espacio_comercial_service, select_ec_by_tipo_inmueble_service, order_ec_by_tarifa_service, order_ec_by_area_service, select_ec_figma_service
from ..ui.base import base_page

def about_arrendamiento() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Arrendamiento", size="9"),
            rx.text(
                "Tabla de arrendamientos",
            ),
            spacing="5",
            justify="center",
            align="stretch",
            min_height="85vh",
        )
    return base_page(my_child)
    
'''
class Espacio_comercialState(rx.State):
    #states
    espacios_comerciales:list[Espacio_comercial]
    contratos_alquiler:list[Contrato_alquiler]
    espacio_comercial_buscar: str
    filtro: str = "Ninguno" 

    @rx.background
    async def get_all_espacio_comercial(self):
        async with self:
            self.espacios_comerciales = select_all_espacio_comercial_service()


    @rx.background
    async def get_ec_by_tipo_inmueble(self):
        async with self:
            self.espacios_comerciales = select_ec_by_tipo_inmueble_service(self.espacio_comercial_buscar) 

    def buscar_on_change(self, value: str):
        self.espacio_comercial_buscar = value

    @rx.event 
    def change_filtro(self, filtro: str):
        """Change the select value var."""
        self.filtro = filtro 
        if filtro == "tarifa":
            self.espacios_comerciales = order_ec_by_tarifa_service()
        elif filtro == "area":
            self.espacios_comerciales = order_ec_by_area_service()
        else:
            self.espacios_comerciales = select_all_espacio_comercial_service()
        
@rx.page(route='/espacio_comercial', title='espacio_comercial', on_load=Espacio_comercialState.get_all_espacio_comercial)
def espacio_comercial_page() -> rx.Component:
    return rx.flex(
        rx.heading('Espacios comerciales', align='center'),
        rx.hstack(
            select_intro(), 
            buscar_ec_component(),
            justify='start',
            style={'margin-top': '30px'}
        ),
        table_espacio_comercial(Espacio_comercialState.espacios_comerciales),
        direction='column',
        style={"width": "60vw", "margin": "auto"}

    )

def table_espacio_comercial(list_espacio_comercial: list[Espacio_comercial]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell('ID'),
                rx.table.column_header_cell('Tipo de inmueble'),
                rx.table.column_header_cell('estado'),
                rx.table.column_header_cell('area'),
                rx.table.column_header_cell('tarifa'),
                rx.table.column_header_cell('zona')
            )
        ),
        rx.table.body(
            rx.foreach(list_espacio_comercial, row_table)
        )
    )



def row_table(espacio_comercial: Espacio_comercial) -> rx.Component:
    return rx.table.row(
        rx.table.cell(espacio_comercial.id_espacio_comercial),
        rx.table.cell(espacio_comercial.tipo_inmueble),
        rx.table.cell(espacio_comercial.estado),
        rx.table.cell(espacio_comercial.area),
        rx.table.cell(espacio_comercial.tarifa),
        rx.table.cell(espacio_comercial.nombre_zona)
    )

def buscar_ec_component()-> rx.Component:
    return rx.hstack(
        rx.input(placeholder='Ingrese tipo de inmueble', on_change=Espacio_comercialState.buscar_on_change),
        rx.button('Buscar espacio comercial', on_click=Espacio_comercialState.get_ec_by_tipo_inmueble)
    )



def select_intro():
    return rx.center(
        rx.select(
            ["Ninguno", "area", "tarifa"],
            value=Espacio_comercialState.filtro,
            on_change=Espacio_comercialState.change_filtro,
        ),
    )
'''
    
