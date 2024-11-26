import reflex as rx

from ..ui.base import base_page

def about_empleados() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Empleados", size="9"),
            rx.text(
                "Tabla de empleados",
            ),
            spacing="5",
            justify="center",
            align="stretch",
            min_height="85vh",
        )
    return base_page(my_child)