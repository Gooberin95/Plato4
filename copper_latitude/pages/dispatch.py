"""A single dispatch, addressed by its slug."""

import reflex as rx

from copper_latitude.components.layout import kicker, meta_line, page_shell, panel, rule
from copper_latitude.state import DispatchState, NavState
from copper_latitude.theme import (
    CREAM,
    CREAM_SOFT,
    DISPLAY,
    FAVICON,
    SAFFRON,
)


def _paragraph(text) -> rx.Component:
    return rx.el.p(
        text,
        font_size="1.18rem",
        line_height="1.7",
        max_width="40rem",
        margin_bottom="1.1rem",
        color=CREAM,
    )


def _related(post) -> rx.Component:
    return rx.link(
        rx.box(
            rx.el.p(
                post.kicker,
                font_family=DISPLAY,
                font_size="0.7rem",
                letter_spacing="0.14em",
                text_transform="uppercase",
                color=SAFFRON,
            ),
            rx.el.h3(
                post.title,
                font_family=DISPLAY,
                font_weight="560",
                font_size="1.35rem",
                letter_spacing="-0.03em",
                line_height="1.1",
                margin_top="0.4rem",
                color="inherit",
            ),
            rx.el.p(
                post.place,
                margin_top="0.45rem",
                color=CREAM_SOFT,
                font_size="0.98rem",
            ),
        ),
        href=post.href,
        underline="none",
        text_decoration="none",
        display="block",
        color=CREAM,
        padding_top="0.35rem",
        _hover={"color": SAFFRON, "text_decoration": "none"},
    )


def _article() -> rx.Component:
    post = DispatchState.current
    nxt = DispatchState.next_dispatch
    return rx.box(
        panel(
            kicker(post.kicker),
            rx.el.h1(
                post.title,
                font_family=DISPLAY,
                font_weight="560",
                font_size=["2.4rem", "3.2rem", "4.3rem"],
                letter_spacing="-0.035em",
                line_height="0.96",
                max_width="16ch",
            ),
            rx.el.p(
                post.dek,
                margin_top="1rem",
                max_width="38rem",
                font_size=["1.15rem", "1.28rem"],
                line_height="1.45",
                font_style="italic",
                color=CREAM_SOFT,
            ),
            meta_line(post.date, post.place, post.read_time),
            rule(),
            rx.box(
                rx.el.span(
                    post.lead_initial,
                    float="left",
                    font_family=DISPLAY,
                    font_weight="600",
                    font_size="4.4rem",
                    line_height="0.78",
                    padding_right="0.45rem",
                    color=SAFFRON,
                ),
                rx.el.p(
                    post.lead_rest,
                    margin="0",
                ),
                max_width="40rem",
                font_size="1.32rem",
                line_height="1.55",
                font_style="italic",
                color=CREAM,
            ),
            rx.el.blockquote(
                post.pull,
                margin_top="1.4rem",
                margin_bottom="1.4rem",
                max_width="34rem",
                font_family=DISPLAY,
                font_style="italic",
                font_weight="500",
                font_size=["1.45rem", "1.7rem"],
                line_height="1.25",
                letter_spacing="-0.02em",
                color=SAFFRON,
                border_left=f"2px solid {SAFFRON}",
                padding_left="1rem",
            ),
            rx.foreach(post.body, _paragraph),
            soft=True,
        ),
        panel(
            kicker("Continue"),
            rx.link(
                rx.el.span(nxt.kicker, display="block", color=SAFFRON, font_family=DISPLAY, font_size="0.72rem", letter_spacing="0.14em", text_transform="uppercase"),
                rx.el.span(
                    nxt.title,
                    display="block",
                    margin_top="0.45rem",
                    font_family=DISPLAY,
                    font_size=["1.6rem", "2rem"],
                    letter_spacing="-0.03em",
                    line_height="1.05",
                    color="inherit",
                ),
                href=nxt.href,
                underline="none",
                text_decoration="none",
                color=CREAM,
                _hover={"color": SAFFRON, "text_decoration": "none"},
            ),
        ),
        panel(
            kicker("Also filed"),
            rx.box(
                rx.foreach(DispatchState.related, _related),
                display="grid",
                grid_template_columns=["1fr", "1fr", "1fr 1fr"],
                gap="1rem",
            ),
            rx.link(
                "Back to the dispatch book",
                href="/dispatches",
                underline="none",
                text_decoration="none",
                display="inline-block",
                margin_top="1.1rem",
                font_family=DISPLAY,
                font_size="0.78rem",
                letter_spacing="0.14em",
                text_transform="uppercase",
                color=SAFFRON,
                _hover={"color": CREAM},
            ),
        ),
        display="flex",
        flex_direction="column",
        gap="1.35rem",
    )


def _missing() -> rx.Component:
    return panel(
        kicker("Unfiled"),
        rx.el.h1(
            "This dispatch was never filed",
            font_family=DISPLAY,
            font_weight="560",
            font_size=["2.3rem", "3.2rem"],
            letter_spacing="-0.03em",
            line_height="0.98",
        ),
        rx.el.p(
            "Nothing in the book matches this page. The notebook has limits, even when the URL does not.",
            margin_top="1rem",
            max_width="36rem",
            font_size="1.15rem",
            line_height="1.5",
            color=CREAM_SOFT,
        ),
        rx.link(
            "Return to the dispatches",
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
    )


@rx.page(
    route="/dispatches/[slug]",
    title=DispatchState.page_title,
    description=DispatchState.page_description,
    image=FAVICON,
    on_load=NavState.close_menu,
)
def dispatch_page() -> rx.Component:
    """One dispatch, or a note that the slug was never filed."""
    return page_shell(
        rx.cond(DispatchState.found, _article(), _missing()),
    )
