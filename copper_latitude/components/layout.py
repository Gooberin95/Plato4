"""Page chrome. The painting is applied once, on the root box."""

import reflex as rx

from copper_latitude.data import Post
from copper_latitude.state import NavState
from copper_latitude.theme import (
    BODY,
    CREAM,
    CREAM_FAINT,
    CREAM_SOFT,
    DISPLAY,
    ISSUE,
    ISSUE_NAME,
    LINE,
    NAV_LINKS,
    NAVY,
    PANEL,
    PANEL_SOFT,
    SAFFRON,
    SEASON,
    SITE,
)

_SIDEBAR_WIDTH = "272px"


def kicker(text) -> rx.Component:
    """Small copper label above a headline."""
    return rx.el.p(
        text,
        font_family=DISPLAY,
        font_size="0.74rem",
        letter_spacing="0.16em",
        text_transform="uppercase",
        color=SAFFRON,
        margin_bottom="0.7rem",
    )


def meta_line(date, place, read_time) -> rx.Component:
    """Date, place, and reading time on one line."""
    return rx.el.p(
        date,
        "  ·  ",
        place,
        "  ·  ",
        read_time,
        font_family=DISPLAY,
        font_size="0.92rem",
        letter_spacing="0.02em",
        color=CREAM_SOFT,
        margin_top="0.85rem",
    )


def rule() -> rx.Component:
    """A hairline the color of the issue."""
    return rx.box(
        width="100%",
        height="1px",
        background_color="rgba(242, 193, 78, 0.45)",
        margin_top="1.25rem",
        margin_bottom="1.25rem",
    )


def panel(*children, soft: bool = False, **props) -> rx.Component:
    """A translucent sheet so the painting stays visible and the type stays readable."""
    return rx.box(
        *children,
        background_color=PANEL_SOFT if soft else PANEL,
        backdrop_filter="blur(16px)",
        border=f"1px solid {LINE}",
        padding=["1.25rem", "1.45rem", "1.8rem", "2.15rem"],
        **props,
    )


def _nav_link(label: str, href: str, section: str, large: bool) -> rx.Component:
    active = NavState.section == section
    return rx.link(
        rx.box(
            rx.box(
                width="0.42rem",
                height="0.42rem",
                flex_shrink="0",
                transform="rotate(45deg)",
                background_color=rx.cond(active, SAFFRON, "transparent"),
                border=rx.cond(
                    active,
                    f"1px solid {SAFFRON}",
                    "1px solid rgba(246, 241, 231, 0.4)",
                ),
            ),
            rx.el.span(label),
            display="flex",
            align_items="center",
            gap="0.75rem",
        ),
        href=href,
        underline="none",
        text_decoration="none",
        display="block",
        width="100%",
        color=rx.cond(active, SAFFRON, CREAM),
        font_family=DISPLAY,
        font_size="1.85rem" if large else "1.08rem",
        font_style="italic" if large else "normal",
        font_weight="500",
        padding_top="0.42rem",
        padding_bottom="0.42rem",
        _hover={"color": SAFFRON, "text_decoration": "none"},
        on_click=NavState.close_menu,
    )


def _wordmark(compact: bool = False) -> rx.Component:
    return rx.link(
        rx.el.span(
            "The Copper",
            display="block",
            font_family=DISPLAY,
            font_weight="600",
            font_size="1.15rem" if compact else "1.55rem",
            letter_spacing="-0.03em",
            line_height="0.95",
            color=CREAM,
        ),
        rx.el.span(
            "Latitude",
            display="block",
            font_family=DISPLAY,
            font_style="italic",
            font_weight="500",
            font_size="1.15rem" if compact else "1.55rem",
            letter_spacing="-0.03em",
            line_height="0.95",
            color=SAFFRON,
        ),
        href="/",
        underline="none",
        text_decoration="none",
        _hover={"text_decoration": "none"},
        on_click=NavState.close_menu,
    )


def _sidebar() -> rx.Component:
    return rx.el.nav(
        _wordmark(),
        rx.el.p(
            f"Field journal of Inez Marlow",
            color=CREAM_SOFT,
            font_size="0.98rem",
            margin_top="0.85rem",
            line_height="1.35",
        ),
        rx.el.p(
            f"Vol. {ISSUE} · {ISSUE_NAME}",
            color=CREAM_FAINT,
            font_family=DISPLAY,
            font_size="0.72rem",
            letter_spacing="0.14em",
            text_transform="uppercase",
            margin_top="0.45rem",
        ),
        rx.box(
            height="1px",
            background_color=LINE,
            margin_top="1.2rem",
            margin_bottom="0.7rem",
        ),
        *[_nav_link(label, href, section, large=False) for label, href, section in NAV_LINKS],
        rx.box(flex_grow="1"),
        rx.box(
            height="1px",
            background_color=LINE,
            margin_top="1.2rem",
            margin_bottom="0.9rem",
        ),
        rx.el.p(
            "Now writing from",
            font_family=DISPLAY,
            font_size="0.68rem",
            letter_spacing="0.16em",
            text_transform="uppercase",
            color=SAFFRON,
        ),
        rx.el.p(
            "Lisbon, between trains",
            margin_top="0.3rem",
            color=CREAM,
            font_size="1rem",
        ),
        rx.el.p(
            SEASON,
            margin_top="0.2rem",
            color=CREAM_FAINT,
            font_size="0.92rem",
        ),
        display=["none", "none", "none", "flex"],
        flex_direction="column",
        position="fixed",
        top="0",
        left="0",
        width=_SIDEBAR_WIDTH,
        height="100vh",
        overflow_y="auto",
        z_index="30",
        padding="1.55rem 1.3rem 1.3rem",
        background_color="rgba(8, 6, 12, 0.72)",
        backdrop_filter="blur(18px)",
        border_right=f"1px solid {LINE}",
        aria_label="Sections",
    )


def _menu_button() -> rx.Component:
    return rx.el.button(
        rx.cond(
            NavState.menu_open,
            rx.el.span(
                "Close",
                font_family=DISPLAY,
                font_size="0.78rem",
                letter_spacing="0.16em",
                text_transform="uppercase",
            ),
            rx.box(
                rx.box(width="1.35rem", height="1px", background_color=CREAM),
                rx.box(
                    width="0.95rem",
                    height="1px",
                    background_color=SAFFRON,
                    margin_left="auto",
                ),
                rx.box(width="1.35rem", height="1px", background_color=CREAM),
                display="flex",
                flex_direction="column",
                gap="5px",
                width="1.35rem",
            ),
        ),
        type="button",
        on_click=NavState.toggle_menu,
        aria_label="Open or close the menu",
        cursor="pointer",
        border="none",
        background_color="transparent",
        color=CREAM,
        padding="0.35rem",
    )


def _mobile_header() -> rx.Component:
    return rx.box(
        _wordmark(compact=True),
        _menu_button(),
        display=["flex", "flex", "flex", "none"],
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="40",
        align_items="center",
        justify_content="space-between",
        padding="0.75rem 1rem",
        background_color="rgba(8, 6, 12, 0.8)",
        backdrop_filter="blur(16px)",
        border_bottom=f"1px solid {LINE}",
    )


def _mobile_menu() -> rx.Component:
    return rx.cond(
        NavState.menu_open,
        rx.box(
            rx.box(
                _wordmark(compact=True),
                _menu_button(),
                display="flex",
                align_items="center",
                justify_content="space-between",
                margin_bottom="1.5rem",
            ),
            rx.el.p(
                f"Issue {ISSUE} · {ISSUE_NAME}",
                font_family=DISPLAY,
                font_size="0.72rem",
                letter_spacing="0.16em",
                text_transform="uppercase",
                color=SAFFRON,
                margin_bottom="0.8rem",
            ),
            *[
                _nav_link(label, href, section, large=True)
                for label, href, section in NAV_LINKS
            ],
            position="fixed",
            top="0",
            right="0",
            bottom="0",
            left="0",
            z_index="50",
            overflow_y="auto",
            padding="0.85rem 1.15rem 2rem",
            background_color="rgba(8, 6, 12, 0.9)",
            backdrop_filter="blur(18px)",
        ),
    )


def footer() -> rx.Component:
    """Issue line, set after the last panel so the painting shows above it."""
    return rx.box(
        rx.el.p(
            f"{SITE}  ·  Issue {ISSUE}, {ISSUE_NAME}",
            font_family=DISPLAY,
            font_size="0.95rem",
            color=CREAM,
        ),
        rx.el.p(
            "Set in Fraunces and Newsreader. Inez Marlow is fictional.",
            margin_top="0.35rem",
            color=CREAM_SOFT,
            font_size="0.95rem",
        ),
        padding_top="0.2rem",
        padding_bottom="0.4rem",
    )


def story_card(post: Post, featured: bool = False) -> rx.Component:
    """A contents-page entry that links to its own dispatch."""
    return rx.link(
        rx.box(
            rx.box(
                rx.el.span(
                    post.number,
                    font_family=DISPLAY,
                    font_style="italic",
                    font_size="1.8rem" if featured else "1.35rem",
                    color=SAFFRON,
                    line_height="1",
                ),
                kicker(post.kicker),
                display="flex",
                align_items="baseline",
                gap="0.8rem",
            ),
            rx.el.h2(
                post.title,
                font_family=DISPLAY,
                font_weight="560",
                font_size=["1.85rem", "2.15rem", "2.7rem"] if featured else ["1.45rem", "1.6rem"],
                letter_spacing="-0.03em",
                line_height="1.02",
                color="inherit",
                margin_top="0.35rem",
            ),
            rx.el.p(
                post.dek,
                color=CREAM_SOFT,
                font_size="1.12rem" if featured else "1.02rem",
                line_height="1.45",
                margin_top="0.75rem",
                max_width="40rem",
            ),
            meta_line(post.date, post.place, post.read_time),
            rx.el.p(
                "Read the dispatch",
                margin_top="1rem",
                font_family=DISPLAY,
                font_size="0.78rem",
                letter_spacing="0.14em",
                text_transform="uppercase",
                color=SAFFRON,
            ),
            padding=["0.2rem", "0.35rem"],
        ),
        href=post.href,
        underline="none",
        text_decoration="none",
        display="block",
        color=CREAM,
        _hover={"color": SAFFRON, "text_decoration": "none"},
    )


def page_shell(*children) -> rx.Component:
    """Root frame shared by every page.

    The painting is the background of this single box, not of each section.
    Sections sit on translucent panels so the canvas shows through as you scroll,
    and background_attachment stays fixed to the viewport.
    """
    return rx.box(
        rx.el.a("Skip to content", href="#content", class_name="skip-link"),
        _sidebar(),
        _mobile_header(),
        _mobile_menu(),
        rx.box(
            rx.box(
                rx.el.main(
                    *children,
                    id="content",
                    display="flex",
                    flex_direction="column",
                    gap="1.35rem",
                ),
                footer(),
                display="flex",
                flex_direction="column",
                gap="1.35rem",
                width="100%",
                max_width="1120px",
                margin_x="auto",
                padding_x=["1rem", "1.2rem", "1.55rem", "2.15rem"],
                padding_top=["1.05rem", "1.2rem", "1.45rem", "1.8rem"],
                padding_bottom="2.4rem",
            ),
            margin_left=["0", "0", "0", _SIDEBAR_WIDTH],
            padding_top=["4.35rem", "4.35rem", "4.35rem", "0"],
            min_height="100vh",
        ),
        id="page-root",
        background_image="url('/background.jpg')",
        background_size="cover",
        background_position="center",
        background_attachment="fixed",
        background_repeat="no-repeat",
        background_color=NAVY,
        color=CREAM,
        font_family=BODY,
        min_height="100vh",
        width="100%",
    )
