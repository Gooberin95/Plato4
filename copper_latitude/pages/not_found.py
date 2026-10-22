"""Unknown routes, still on the same canvas."""

import reflex as rx

from copper_latitude.components.layout import kicker, page_shell, panel
from copper_latitude.state import NavState
from copper_latitude.theme import CREAM_SOFT, DISPLAY, FAVICON, SAFFRON


@rx.page(
    route="/404",
    title="Not found — The Copper Latitude",
    description="That page is not in The Copper Latitude.",
    image=FAVICON,
    on_load=NavState.close_menu,
)
def not_found() -> rx.Component:
    """Shown when no route matches."""
    return page_shell(
        panel(
            kicker("Off the map"),
            rx.el.h1(
                "This page is not on the route",
                font_family=DISPLAY,
                font_weight="500",
                font_size=["2.4rem", "3.4rem"],
                letter_spacing="-0.03em",
                line_height="0.98",
            ),
            rx.el.p(
                "The journal does not have a page here. The dispatches, the atlas, and the field kit are all still where you left them.",
                margin_top="1rem",
                max_width="36rem",
                font_size="1.12rem",
                line_height="1.5",
                color=CREAM_SOFT,
            ),
            rx.link(
                "Back to the journal",
                href="/",
                underline="none",
                text_decoration="none",
                display="inline-block",
                margin_top="1.2rem",
                font_family=DISPLAY,
                font_size="0.78rem",
                letter_spacing="0.14em",
                text_transform="uppercase",
                color=SAFFRON,
            ),
            soft=True,
        ),
    )
