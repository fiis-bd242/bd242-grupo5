import reflex as rx

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