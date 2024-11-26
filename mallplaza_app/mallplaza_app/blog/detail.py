import reflex as rx

from ..ui.base import base_page

from . import state

def blog_post_detail_page() -> rx.Component:
    can_edit = True
    edit_link = rx.link("Edit", href=f"/blog/{state.BlogPostState.blog_post_id}/edit")
    edit_link_el = rx.cond(
        can_edit,
        edit_link,
        rx.fragment("") 
    )
    my_child = rx.vstack(
            rx.hstack(
                rx.heading(state.BlogPostState.post.title, size="9"),
                edit_link_el,
                align='end'
            ),
            rx.text(state.BlogPostState.post.publish_date),
            rx.text(
                state.BlogPostState.post.content,
                white_space='pre-wrap'
            ),
            spacing="5",
            align="stretch",
            min_height="85vh",
            id='my-child'
    )
    return base_page(my_child)