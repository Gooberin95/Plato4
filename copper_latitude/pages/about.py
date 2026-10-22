"""Who Inez Marlow is, and how the journal is made."""

import reflex as rx

from copper_latitude.components.layout import kicker, page_shell, panel, rule
from copper_latitude.data import METHOD, TIMELINE
from copper_latitude.state import NavState
from copper_latitude.theme import CREAM, CREAM_SOFT, DISPLAY, FAVICON, SAFFRON


def _year(entry: tuple[str, str, str]) -> rx.Component:
    year, place, text = entry
    return rx.box(
        rx.el.p(
            year,
            font_family=DISPLAY,
            font_style="italic",
            font_size="1.35rem",
            color=SAFFRON,
        ),
        rx.el.h2(
            place,
            font_family=DISPLAY,
            font_weight="500",
            font_size="1.45rem",
            letter_spacing="-0.03em",
            margin_top="0.15rem",
        ),
        rx.el.p(
            text,
            margin_top="0.4rem",
            color=CREAM_SOFT,
            line_height="1.5",
            max_width="40rem",
        ),
        padding_top="0.95rem",
        padding_bottom="0.95rem",
        border_top="1px solid rgba(246, 241, 231, 0.16)",
    )


def _rule_row(item: tuple[str, str]) -> rx.Component:
    title, text = item
    return rx.box(
        rx.el.h2(
            title,
            font_family=DISPLAY,
            font_weight="500",
            font_size="1.35rem",
            letter_spacing="-0.02em",
        ),
        rx.el.p(
            text,
            margin_top="0.35rem",
            color=CREAM_SOFT,
            line_height="1.5",
            max_width="40rem",
        ),
        margin_bottom="1rem",
    )


@rx.page(
    route="/about",
    title="Colophon — The Copper Latitude",
    description="About Inez Marlow, the fictional traveler behind The Copper Latitude.",
    image=FAVICON,
    on_load=NavState.close_menu,
)
def about() -> rx.Component:
    """The colophon and the traveler's method."""
    return page_shell(
        panel(
            kicker("Colophon"),
            rx.el.h1(
                "Inez Marlow",
                font_family=DISPLAY,
                font_weight="500",
                font_size=["3rem", "4.4rem", "5.4rem"],
                letter_spacing="-0.035em",
                line_height="0.9",
            ),
            rx.el.p(
                "Born in Setúbal, nominally housed in a rented room in Lisbon’s Alfama, and gone for most of the year. She used to edit railway timetables. She left in 2019, after a strike season convinced her that the interesting part of transport was the waiting.",
                margin_top="1.1rem",
                max_width="40rem",
                font_size="1.2rem",
                line_height="1.55",
            ),
            rx.el.p(
                "The Copper Latitude is her field journal: long dispatches, an atlas of places she keeps meaning to return to, and the short list of things that earn a place in the bag. She writes longhand the same day and types later, usually in a station café that would prefer she buy a second coffee.",
                margin_top="0.85rem",
                max_width="40rem",
                font_size="1.12rem",
                line_height="1.55",
                color=CREAM_SOFT,
            ),
            soft=True,
        ),
        panel(
            kicker("Method"),
            rx.el.h2(
                "How she travels",
                font_family=DISPLAY,
                font_weight="500",
                font_size=["2rem", "2.5rem"],
                letter_spacing="-0.03em",
                margin_bottom="1rem",
            ),
            *[_rule_row(item) for item in METHOD],
        ),
        panel(
            kicker("A route so far"),
            rx.el.h2(
                "The short chronology",
                font_family=DISPLAY,
                font_weight="500",
                font_size=["2rem", "2.5rem"],
                letter_spacing="-0.03em",
                margin_bottom="0.4rem",
            ),
            *[_year(entry) for entry in TIMELINE],
        ),
        panel(
            kicker("The name"),
            rx.el.h2(
                "Why copper, why latitude",
                font_family=DISPLAY,
                font_weight="500",
                font_size=["2rem", "2.5rem"],
                letter_spacing="-0.03em",
            ),
            rx.el.p(
                "The week she resigned, the roofs in Alfama held the evening the way a copper pan holds heat. She wrote the latitude of the room in the margin, a habit from the timetable desk, and the two words stayed together. Every dispatch still ends with the latitude of the bed, even when she does not publish the number.",
                margin_top="0.85rem",
                max_width="40rem",
                font_size="1.12rem",
                line_height="1.55",
                color=CREAM,
            ),
            rule(),
            rx.el.p(
                "Inez Marlow is fictional. The cities are real. The journeys, the dentist on the sleeper, the lime seller, and the station cook are invented. The journal is a magazine, not a booking engine.",
                max_width="40rem",
                font_size="1.05rem",
                line_height="1.5",
                color=CREAM_SOFT,
            ),
            rx.el.p(
                "Set in Fraunces and Newsreader. Issue 07 is titled Between Stations.",
                margin_top="0.7rem",
                font_family=DISPLAY,
                font_size="0.95rem",
                color=SAFFRON,
            ),
        ),
    )
