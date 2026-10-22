"""Issue opener: masthead, featured dispatch, and the rest of the contents."""

import reflex as rx

from copper_latitude.components.layout import kicker, page_shell, panel, story_card
from copper_latitude.data import PLACES, POSTS
from copper_latitude.state import NavState
from copper_latitude.theme import (
    CREAM,
    CREAM_SOFT,
    DISPLAY,
    FAVICON,
    ISSUE,
    ISSUE_NAME,
    SAFFRON,
    SEASON,
)

FEATURED = POSTS[0]
ALSO = POSTS[1:4]
REST = POSTS[4:]
TEASER_PLACES = (PLACES[0], PLACES[3], PLACES[6])


def _masthead() -> rx.Component:
    return panel(
        rx.box(
            rx.el.p(
                f"Issue {ISSUE}",
                font_family=DISPLAY,
                font_size="0.74rem",
                letter_spacing="0.18em",
                text_transform="uppercase",
                color=SAFFRON,
            ),
            rx.el.p(
                f"{ISSUE_NAME}  ·  {SEASON}",
                font_family=DISPLAY,
                font_size="0.74rem",
                letter_spacing="0.18em",
                text_transform="uppercase",
                color=CREAM_SOFT,
            ),
            display="flex",
            flex_wrap="wrap",
            justify_content="space-between",
            gap="0.6rem",
        ),
        rx.box(
            rx.el.span(
                ISSUE,
                position="absolute",
                right="0",
                top="-0.4rem",
                font_family=DISPLAY,
                font_style="italic",
                font_weight="500",
                font_size=["5.5rem", "8rem", "9.5rem"],
                line_height="0.8",
                color="rgba(242, 193, 78, 0.18)",
                pointer_events="none",
                user_select="none",
                display=["none", "block", "block"],
            ),
            rx.el.h1(
                "The Copper",
                rx.el.span(
                    " Latitude",
                    display="block",
                    font_style="italic",
                    color=SAFFRON,
                ),
                font_family=DISPLAY,
                font_weight="560",
                font_size=["3.5rem", "5rem", "6.3rem", "7rem"],
                line_height="0.88",
                letter_spacing="-0.035em",
                color=CREAM,
                max_width="11ch",
                position="relative",
                margin_top="1.1rem",
            ),
            position="relative",
            overflow="hidden",
        ),
        rx.el.p(
            "Dispatches from trains, ferries, and kitchens that belong to someone else. Inez Marlow files them the day they happen, before memory has a chance to tidy the room.",
            font_size=["1.15rem", "1.28rem"],
            line_height="1.5",
            max_width="38rem",
            margin_top="1.25rem",
            color=CREAM,
        ),
        rx.el.p(
            "This issue is about the hours between arrival and the first cup of something hot.",
            font_size="1.08rem",
            font_style="italic",
            color=CREAM_SOFT,
            margin_top="0.75rem",
            max_width="36rem",
        ),
        soft=True,
    )


def _also_card(post) -> rx.Component:
    return rx.box(
        story_card(post),
        padding_top="0.35rem",
        border_top="1px solid rgba(246, 241, 231, 0.14)",
    )


def index() -> rx.Component:
    """The journal's front page."""
    return page_shell(
        _masthead(),
        panel(
            kicker("The lead dispatch"),
            story_card(FEATURED, featured=True),
        ),
        panel(
            kicker("Also in this issue"),
            rx.box(
                *[_also_card(post) for post in ALSO],
                display="grid",
                grid_template_columns=["1fr", "1fr", "1fr 1fr", "1fr 1fr 1fr"],
                gap="1.25rem",
                margin_top="0.4rem",
            ),
        ),
        panel(
            kicker("Further back in the book"),
            *[
                rx.box(
                    story_card(post),
                    padding_top="0.85rem",
                    border_top="1px solid rgba(246, 241, 231, 0.14)",
                    margin_top="0.85rem",
                )
                for post in REST
            ],
            rx.link(
                "The full dispatch book",
                href="/dispatches",
                underline="none",
                text_decoration="none",
                display="inline-block",
                margin_top="1.2rem",
                font_family=DISPLAY,
                font_size="0.78rem",
                letter_spacing="0.14em",
                text_transform="uppercase",
                color=SAFFRON,
                _hover={"color": CREAM},
            ),
        ),
        rx.box(
            panel(
                kicker("Atlas"),
                rx.el.h2(
                    "Places she keeps going back to",
                    font_family=DISPLAY,
                    font_weight="560",
                    font_size=["1.7rem", "2rem"],
                    letter_spacing="-0.03em",
                    line_height="1.05",
                ),
                *[
                    rx.el.p(
                        rx.el.span(place.name, color=CREAM),
                        f"  ·  {place.country}",
                        margin_top="0.7rem",
                        color=CREAM_SOFT,
                    )
                    for place in TEASER_PLACES
                ],
                rx.link(
                    "Filter the atlas",
                    href="/atlas",
                    underline="none",
                    color=SAFFRON,
                    text_decoration="none",
                    display="inline-block",
                    margin_top="1rem",
                    font_family=DISPLAY,
                    font_size="0.78rem",
                    letter_spacing="0.14em",
                    text_transform="uppercase",
                    _hover={"color": CREAM},
                ),
            ),
            panel(
                kicker("Field kit"),
                rx.el.h2(
                    "What actually goes in the bag",
                    font_family=DISPLAY,
                    font_weight="560",
                    font_size=["1.7rem", "2rem"],
                    letter_spacing="-0.03em",
                    line_height="1.05",
                ),
                rx.el.p(
                    "Eighteen things, counted by hand. Tick the ones you would carry. The list lives in this browser session and nowhere else.",
                    margin_top="0.75rem",
                    color=CREAM_SOFT,
                    line_height="1.45",
                ),
                rx.link(
                    "Open the kit",
                    href="/kit",
                    underline="none",
                    color=SAFFRON,
                    text_decoration="none",
                    display="inline-block",
                    margin_top="1rem",
                    font_family=DISPLAY,
                    font_size="0.78rem",
                    letter_spacing="0.14em",
                    text_transform="uppercase",
                    _hover={"color": CREAM},
                ),
            ),
            display="grid",
            grid_template_columns=["1fr", "1fr", "1fr 1fr"],
            gap="1.35rem",
        ),
    )


@rx.page(
    route="/",
    title="The Copper Latitude — Field journal of Inez Marlow",
    description="Issue 07 of The Copper Latitude, the fictional field journal of traveler Inez Marlow.",
    image=FAVICON,
    on_load=NavState.close_menu,
)
def home() -> rx.Component:
    """Front page of the issue."""
    return index()
