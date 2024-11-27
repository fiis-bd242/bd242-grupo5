import reflex as rx
from .. import navigation

import reflex_local_auth

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    ) # <a href=


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/logo-blanco.png",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    rx.link(
                        rx.heading(
                            "MallPlaza", size="7", weight="bold", color="white"
                        ),
                        href=navigation.routes.HOME_ROUTE
                    ),
                    align_items="center"
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_ROUTE),
                    navbar_link("Blog", navigation.routes.BLOG_POSTS_ROUTE),
                    navbar_link("Pricing", navigation.routes.PRICING_ROUTE),
                    navbar_link("Contact", navigation.routes.CONTACT_US_ROUTE),
                    spacing="5",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Sign Up",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.REGISTER_ROUTE
                    ),
                    rx.link(
                        rx.button(
                            "Log in",
                            size="3",
                            variant="outline",
                        ),
                        href=reflex_local_auth.routes.LOGIN_ROUTE
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                id='my-nav-bar-hstack-desktop',
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo-blanco.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Mallplaza", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item(
                            "Home",
                            on_click=navigation.NavState.to_home
                        ),
                        rx.menu.item("About",
                            on_click=navigation.NavState.to_about_us
                        ),
                        rx.menu.item("Blog",
                            on_click=navigation.NavState.to_blog
                        ),
                        rx.menu.item("Pricing",
                            on_click=navigation.NavState.to_pricing
                        ),
                        rx.menu.item("Contact",
                            on_click=navigation.NavState.to_contact),
                        rx.menu.separator(),
                        rx.menu.item("Log in", on_click=navigation.NavState.to_login),
                        rx.menu.item("Sign up", on_click=navigation.NavState.to_register),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("red",10),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        id='my-main-nav'
    )