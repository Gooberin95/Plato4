"""The dispatch book: every filed piece, each with its own page."""

import reflex as rx

from copper_latitude.components.layout import kicker, page_shell, panel, story_card
from copper_latitude.data import POSTS
from copper_latitude.state import NavState
from copper_latitude.theme import CREAM_SOFT, DISPLAY, FAVICON


@rx.page(
    route="/dispatches",
    title="Dispatches — The Copper Latitude",
    description="Every filed dispatch in The Copper Latitude, the field journal of Inez Marlow.",
    image=FAVICON,
    on_load=NavState.close_menu,
)
def dispatches() -> rx.Component:
    """Index of dispatches."""
    return page_shell(
        panel(
            kicker("The book"),
            rx.el.h1(
                "Dispatches",
                font_family=DISPLAY,
                font_weight="560",
                font_size=["3rem", "4.2rem", "5rem"],
                letter_spacing="-0.035em",
                line_height="0.9",
            ),
            rx.el.p(
                "Six pieces from the current book. Each one has its own page. They are filed in the order she typed them, newest first, which is the only order a notebook understands.",
                margin_top="1rem",
                max_width="40rem",
                font_size="1.15rem",
                line_height="1.5",
                color=CREAM_SOFT,
            ),
            soft=True,
        ),
        *[
            panel(story_card(post, featured=index == 0))
            for index, post in enumerate(POSTS)
        ],
    )
