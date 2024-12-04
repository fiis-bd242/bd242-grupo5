import reflex as rx
from Ref.compo.compo import compo
from Ref.vistas.menu import menu

class State(rx.State):
    pass

# Datos de los contratos
contratos = [
    {"nro": "AR301", "inquilino": "Juan Perez", "inmueble": "Modulo 103", "fecha_inicio": "15/08/24", "fecha_fin": "15/09/24", "estado": "Activo", "monto": "$1000"},
    {"nro": "AR145", "inquilino": "XYZ", "inmueble": "Tienda 212", "fecha_inicio": "20/08/24", "fecha_fin": "20/09/24", "estado": "Activo", "monto": "$2000"},
    {"nro": "AR532", "inquilino": "Maria Rodriguez", "inmueble": "Tienda 129", "fecha_inicio": "12/08/24", "fecha_fin": "12/09/24", "estado": "Activo", "monto": "$4000"},
    {"nro": "AR167", "inquilino": "ABC S.A.", "inmueble": "Tienda 301", "fecha_inicio": "25/08/24", "fecha_fin": "25/09/24", "estado": "Activo", "monto": "$1500"},
    {"nro": "AR982", "inquilino": "Sofia Gonzalez", "inmueble": "Modulo 235", "fecha_inicio": "05/08/24", "fecha_fin": "05/09/24", "estado": "Activo", "monto": "$800"},
    {"nro": "AR125", "inquilino": "Delta Corp.", "inmueble": "Tienda 333", "fecha_inicio": "01/08/24", "fecha_fin": "01/09/24", "estado": "Activo", "monto": "$900"},
    {"nro": "AR045", "inquilino": "Pedro Martinez", "inmueble": "Modulo 276", "fecha_inicio": "18/08/24", "fecha_fin": "18/09/24", "estado": "Activo", "monto": "$1200"},
]


# Componente de tabla
def tabla_contratos():
    headers = [
        "Nro Contrato", "Inquilino", "Inmueble", 
        "Fecha Inicio", "Fecha Fin", "Estado", 
        "Monto", "Seleccionar"
    ]
    
    # Crear encabezados
    encabezados = rx.box(
        *[rx.text(header, font_weight="bold", padding="8px") for header in headers],
        display="flex",
        justify_content="space-between",
        border_bottom="1px solid #ddd",
        padding="8px",
        bg="#E9124C",
    )
    
    # Crear filas
    filas = [
        rx.box(
            rx.text(contrato["nro"]),
            rx.text(contrato["inquilino"]),
            rx.text(contrato["inmueble"]),
            rx.text(contrato["fecha_inicio"]),
            rx.text(contrato["fecha_fin"]),
            rx.text(contrato["estado"]),
            rx.text(contrato["monto"]),
            rx.checkbox(),
            display="flex",
            justify_content="space-between",
            padding="8px",
            border_bottom="1px solid #ddd",
        )
        for contrato in contratos
    ]

    return rx.box(
        encabezados,
        *filas,
        border="1px solid #ddd",
        border_radius="8px",
        overflow="hidden",
        padding="8px",
        width="80%",
        margin="0 auto",
    )


# Página principal
def index() -> rx.Component:
    return rx.vstack(
        compo(),
        menu(),
        tabla_contratos(),
        margin="0",
        height="100vh",
           
    ),


app = rx.App()
app.add_page(index)

