import reflex as rx

from ..ui.base import base_page

def about_recobro() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Recobros", size="9"),
            rx.text(
                "Tabla de recobros",
            ),
            spacing="5",
            justify="center",
            align="stretch",
            min_height="85vh",
        )
    return base_page(my_child)