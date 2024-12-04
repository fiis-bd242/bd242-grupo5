import reflex as rx
from Ref.compo.compof import compof
from Ref.vistas.menu import menu


contratos = [
    {"nro": "FAC301", "inquilino": "Juan Perez", "inmueble": "Modulo 103", "fecha_inicio": "15/08/24", "fecha_fin": "15/09/24", "estado": "Pendiente", "monto": "$1000"},
    {"nro": "FAC145", "inquilino": "XYZ", "inmueble": "Tienda 212", "fecha_inicio": "20/08/24", "fecha_fin": "20/09/24", "estado": "Pendiente", "monto": "$2000"},
    {"nro": "FAC532", "inquilino": "Maria Rodriguez", "inmueble": "Tienda 129", "fecha_inicio": "12/08/24", "fecha_fin": "12/09/24", "estado": "Pendiente", "monto": "$4000"},
    {"nro": "FAC167", "inquilino": "ABC S.A.", "inmueble": "Tienda 301", "fecha_inicio": "25/08/24", "fecha_fin": "25/09/24", "estado": "Pendiente", "monto": "$1500"},
    {"nro": "FAC982", "inquilino": "Sofia Gonzalez", "inmueble": "Modulo 235", "fecha_inicio": "05/08/24", "fecha_fin": "05/09/24", "estado": "Pendiente", "monto": "$800"},
    {"nro": "FAC125", "inquilino": "Delta Corp.", "inmueble": "Tienda 333", "fecha_inicio": "01/08/24", "fecha_fin": "01/09/24", "estado": "Pendiente", "monto": "$900"},
    {"nro": "FAC045", "inquilino": "Pedro Martinez", "inmueble": "Modulo 276", "fecha_inicio": "18/08/24", "fecha_fin": "18/09/24", "estado": "Pendiente", "monto": "$1200"},
]

# Componente de tabla para contratos
def tabla_facturas():
    headers = [
        "Nro Factura", "Inquilino", "Inmueble", 
        "Fecha Inicio", "Fecha Fin", "Estado", 
        "Monto", "Seleccionar"
    ]
    
    # Crear encabezados
    encabezados = rx.box(
        *[rx.text(header, font_weight="bold", padding="10px") for header in headers],
        display="flex",
        justify_content="space-between",
        border_bottom="1px solid #ddd",
        padding="10px",
        bg="#E9124C",
    )
    
    # Crear filas
    filas = [
        rx.box(
            rx.text(contrato["nro"], flex="1"),
            rx.text(contrato["inquilino"], flex="1"),
            rx.text(contrato["inmueble"], flex="1"),
            rx.text(contrato["fecha_inicio"], flex="1"),
            rx.text(contrato["fecha_fin"], flex="1"),
            rx.text(contrato["estado"], flex="1"),
            rx.text(contrato["monto"], flex="1"),
            rx.checkbox(flex="1"),
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
        position ="absolute",
        left="400px",
        top="110px"
    )


@rx.page(route="/Facturas",title="Facturas")
def Facturas()->rx.Component:
    return rx.vstack(
        compof(),
        menu(),
        tabla_facturas(),
        margin="0",
        height="100vh",
        

        
    ),