"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex_local_auth
import reflex as rx

from rxconfig import config
from .ui.base import base_page

from .auth.pages import(
    my_login_page,
    my_register_page,
    my_logout_page,
)
from .auth.state import SessionState
from . import empleados, blog, navigation, pages, contact, arrendamiento, inquilino, facturacion, recobro, mantenimiento, evento

class State(rx.State):
    label = "MallPlaza"

    def handgle_title_input_change(self, val):
        self.label=val
    
    def did_click(self):
        print("Hello world did click")
        return rx.redirect(navigation.routes.ABOUT_ROUTE)

def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading(State.label, size="9"),
            # rx.text(
            #     "Get started by editing ",
            #     rx.code(f"{config.app_name}/{config.app_name}.py"),
            #     size="5",
            # ),
            # rx.button("About us", on_click=State.did_click),
            rx.text("Sistema de Gestión de Arrendamientos y Espacios"),
            rx.link(
                rx.button("About us", bg="red"),
                href=navigation.routes.ABOUT_ROUTE
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)


app = rx.App()
app.add_page(index)

#reflex_local_auth pages
app.add_page(
    my_login_page,
    route=reflex_local_auth.routes.LOGIN_ROUTE,
    title="Login"
)
app.add_page(
    my_register_page,
    route=reflex_local_auth.routes.REGISTER_ROUTE,
    title="Register"
)
app.add_page(
    my_logout_page,
    route=navigation.routes.LOGOUT_ROUTE,
    title="Logout"
)

# my pages
app.add_page(
    pages.about_page,
    route=navigation.routes.ABOUT_ROUTE
)
app.add_page(
    pages.protected_page,
    route="/protected",
    on_load=SessionState.on_load
)
app.add_page(
    blog.blog_post_list_page,
    route=navigation.routes.BLOG_POSTS_ROUTE,
    on_load=blog.BlogPostState.load_posts
)
app.add_page(
    blog.blog_post_add_page,
    route=navigation.routes.BLOG_POST_ADD_ROUTE
)
app.add_page(
    blog.blog_post_detail_page,
    route="/blog/[blog_id]",
    on_load=blog.BlogPostState.get_post_detail
)
app.add_page(
    blog.blog_post_edit_page,
    route="/blog/[blog_id]/edit"
)
app.add_page(
    contact.contact_page,
    route=navigation.routes.CONTACT_US_ROUTE
)
app.add_page(
    contact.contact_entries_list_page,
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.list_entries
)
app.add_page(pages.pricing_page,
    route=navigation.routes.PRICING_ROUTE
)

#Módulo Empleados
app.add_page(
    empleados.about_empleados,
    route=navigation.routes.EMPLEADO_ROUTE
)

#Módulo Arrendamiento
app.add_page(
    arrendamiento.about_arrendamiento,
    route=navigation.routes.ARRENDAMIENTO_ROUTE
)

#Módulo de Inquilinos
app.add_page(
    inquilino.inquilino_page,
    route=navigation.routes.INQUILINO_ROUTE,
    on_load=inquilino.InquilinoState.get_all_inquilino
)

#Módulo facturación
app.add_page(
    facturacion.about_facturacion,
    route=navigation.routes.FACTURACION_ROUTE
)

#Módulo Recobro
app.add_page(
    recobro.about_recobro,
    route=navigation.routes.RECOBRO_ROUTE
)
#Módulo Evento
app.add_page(
    evento.about_evento,
    route=navigation.routes.EVENTO_ROUTE
)
#Módulo Mantenimiento
app.add_page(
    mantenimiento.about_mantenimiento,
    route=navigation.routes.MANTENIMIENTO_ROUTE
)