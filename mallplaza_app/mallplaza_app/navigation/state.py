import reflex as rx
import reflex_local_auth

from . import routes

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)
    def to_register(self):
        return rx.redirect(reflex_local_auth.routes.REGISTER_ROUTE)
    def to_login(self):
        return rx.redirect(reflex_local_auth.routes.LOGIN_ROUTE)
    def to_logout(self):
        return rx.redirect(routes.LOGOUT_ROUTE)
    def to_about_us(self):
        return rx.redirect(routes.ABOUT_ROUTE)
    def to_blog(self):
        return rx.redirect(routes.BLOG_POSTS_ROUTE)
    def to_blog_add(self):
        return rx.redirect(routes.BLOG_POST_ADD_ROUTE)
    def to_contact(self):
        return rx.redirect(routes.CONTACT_US_ROUTE)
    def to_pricing(self):
        return rx.redirect(routes.PRICING_ROUTE)
    def to_empleado(self):
        return rx.redirect(routes.EMPLEADO_ROUTE)
    def to_arrendamiento(self):
        return rx.redirect(routes.ARRENDAMIENTO_ROUTE)
    def to_inquilino(self):
        return rx.redirect(routes.INQUILINO_ROUTE)
    def to_facturacion(self):
        return rx.redirect(routes.FACTURACION_ROUTE)
    def to_recobro(self):
        return rx.redirect(routes.RECOBRO_ROUTE)
    def to_evento(self):
        return rx.redirect(routes.EVENTO_ROUTE)
    def to_mantenimiento(self):
        return rx.redirect(routes.MANTENIMIENTO_ROUTE)