"""Destinations, filtered by continent."""

import reflex as rx

from copper_latitude.components.layout import kicker, page_shell, panel
from copper_latitude.data import CONTINENTS
from copper_latitude.state import AtlasState, NavState
from copper_latitude.theme import (
    CREAM,
    CREAM_SOFT,
    DISPLAY,
    FAVICON,
    INK,
    LINE,
    SAFFRON,
)


def _chip(name: str) -> rx.Component:
    selected = AtlasState.continent == name
    return rx.el.button(
        name,
        type="button",
        on_click=AtlasState.choose(name),
        cursor="pointer",
        border=rx.cond(
            selected,
            f"1px solid {SAFFRON}",
            "1px solid rgba(246, 241, 231, 0.28)",
        ),
        background_color=rx.cond(selected, SAFFRON, "rgba(8, 6, 12, 0.35)"),
        color=rx.cond(selected, INK, CREAM),
        padding="0.5rem 0.75rem",
        font_family=DISPLAY,
        font_size="0.72rem",
        letter_spacing="0.12em",
        text_transform="uppercase",
        border_radius="0",
    )


def _place(place) -> rx.Component:
    return rx.box(
        rx.box(
            rx.el.h2(
                place.name,
                font_family=DISPLAY,
                font_weight="560",
                font_size=["1.7rem", "2rem"],
                letter_spacing="-0.03em",
                line_height="1",
            ),
            rx.el.p(
                place.latitude,
                font_family=DISPLAY,
                font_size="0.78rem",
                letter_spacing="0.08em",
                color=SAFFRON,
            ),
            display="flex",
            justify_content="space-between",
            align_items="baseline",
            gap="1rem",
        ),
        rx.el.p(
            place.country,
            "  ·  ",
            place.continent,
            "  ·  ",
            place.season,
            margin_top="0.45rem",
            color=CREAM_SOFT,
            font_size="0.98rem",
        ),
        rx.el.p(
            place.summary,
            margin_top="0.75rem",
            font_size="1.08rem",
            line_height="1.5",
            max_width="42rem",
        ),
        rx.el.p(
            place.note,
            margin_top="0.55rem",
            font_style="italic",
            color=CREAM_SOFT,
            max_width="40rem",
        ),
        rx.cond(
            place.dispatch_slug != "",
            rx.link(
                "Read the dispatch",
                href="/dispatches/" + place.dispatch_slug,
                underline="none",
                text_decoration="none",
                display="inline-block",
                margin_top="0.8rem",
                font_family=DISPLAY,
                font_size="0.74rem",
                letter_spacing="0.14em",
                text_transform="uppercase",
                color=SAFFRON,
                _hover={"color": CREAM},
            ),
            rx.box(),
        ),
        padding_top="1.15rem",
        padding_bottom="1.15rem",
        border_top=f"1px solid {LINE}",
    )


@rx.page(
    route="/atlas",
    title="Atlas — The Copper Latitude",
    description="Places Inez Marlow keeps returning to, filtered by continent.",
    image=FAVICON,
    on_load=NavState.close_menu,
)
def atlas() -> rx.Component:
    """Filterable destination index."""
    return page_shell(
        panel(
            kicker("The atlas"),
            rx.el.h1(
                "Places, not pins",
                font_family=DISPLAY,
                font_weight="560",
                font_size=["3rem", "4.2rem", "5rem"],
                letter_spacing="-0.035em",
                line_height="0.9",
            ),
            rx.el.p(
                "Fifteen cities and stretches of road she has slept in, or means to. Choose a continent. The list is the whole of her geography for this issue, which is another way of saying it is unfinished.",
                margin_top="1rem",
                max_width="40rem",
                font_size="1.15rem",
                line_height="1.5",
                color=CREAM_SOFT,
            ),
            rx.box(
                *[_chip(name) for name in CONTINENTS],
                display="flex",
                flex_wrap="wrap",
                gap="0.5rem",
                margin_top="1.25rem",
            ),
            rx.el.p(
                AtlasState.count_label,
                margin_top="0.9rem",
                font_family=DISPLAY,
                font_size="0.95rem",
                color=SAFFRON,
            ),
            soft=True,
        ),
        panel(
            rx.foreach(AtlasState.places, _place),
        ),
    )
