"""A packing list the visitor can tick off."""

import reflex as rx

from copper_latitude.components.layout import kicker, page_shell, panel
from copper_latitude.data import KIT_TOTAL
from copper_latitude.state import KitState, NavState
from copper_latitude.theme import (
    CREAM,
    CREAM_SOFT,
    DISPLAY,
    FAVICON,
    INK,
    LEAF,
    LINE,
    SAFFRON,
)


def _action(label: str, handler) -> rx.Component:
    return rx.el.button(
        label,
        type="button",
        on_click=handler,
        cursor="pointer",
        border=f"1px solid {LINE}",
        background_color="transparent",
        color=CREAM,
        padding="0.55rem 0.75rem",
        font_family=DISPLAY,
        font_size="0.72rem",
        letter_spacing="0.12em",
        text_transform="uppercase",
        _hover={"border_color": SAFFRON, "color": SAFFRON},
    )


def _row(row) -> rx.Component:
    return rx.box(
        rx.cond(
            row.show_category,
            rx.el.h2(
                row.category,
                font_family=DISPLAY,
                font_weight="500",
                font_size="1.55rem",
                letter_spacing="-0.03em",
                margin_top="0.6rem",
                margin_bottom="0.2rem",
            ),
            rx.box(),
        ),
        rx.el.button(
            rx.box(
                rx.cond(
                    row.checked,
                    rx.el.span(
                        "✓",
                        color=INK,
                        font_size="0.85rem",
                        line_height="1",
                    ),
                    rx.el.span(""),
                ),
                width="1.35rem",
                height="1.35rem",
                display="flex",
                align_items="center",
                justify_content="center",
                flex_shrink="0",
                margin_top="0.15rem",
                border=rx.cond(
                    row.checked,
                    f"1px solid {SAFFRON}",
                    "1px solid rgba(246, 241, 231, 0.45)",
                ),
                background_color=rx.cond(row.checked, SAFFRON, "transparent"),
            ),
            rx.box(
                rx.el.span(
                    row.label,
                    display="block",
                    font_size="1.12rem",
                    color=CREAM,
                    text_decoration=rx.cond(row.checked, "line-through", "none"),
                    text_align="left",
                ),
                rx.el.span(
                    row.note,
                    display="block",
                    margin_top="0.2rem",
                    color=CREAM_SOFT,
                    font_size="0.98rem",
                    font_style="italic",
                    text_align="left",
                ),
                text_align="left",
            ),
            type="button",
            on_click=KitState.toggle(row.id),
            display="flex",
            width="100%",
            gap="0.9rem",
            align_items="flex-start",
            cursor="pointer",
            background_color="transparent",
            border="none",
            border_bottom=f"1px solid {LINE}",
            padding_top="0.85rem",
            padding_bottom="0.85rem",
            padding_left="0",
            padding_right="0",
            color=CREAM,
            font_family=DISPLAY,
        ),
    )


@rx.page(
    route="/kit",
    title="Field kit — The Copper Latitude",
    description="Tick off the packing list Inez Marlow actually carries.",
    image=FAVICON,
    on_load=NavState.close_menu,
)
def kit() -> rx.Component:
    """Interactive packing checklist."""
    return page_shell(
        panel(
            kicker("The bag"),
            rx.el.h1(
                "Field kit",
                font_family=DISPLAY,
                font_weight="560",
                font_size=["3rem", "4.2rem", "5rem"],
                letter_spacing="-0.035em",
                line_height="0.9",
            ),
            rx.el.p(
                "Tick what you would actually carry. Nothing is stored on a server. The ticks live in this browser session, and they leave when you do.",
                margin_top="1rem",
                max_width="40rem",
                font_size="1.15rem",
                line_height="1.5",
                color=CREAM_SOFT,
            ),
            rx.el.p(
                KitState.packed_label,
                margin_top="1.1rem",
                font_family=DISPLAY,
                font_size="1.2rem",
                color=SAFFRON,
            ),
            rx.box(
                rx.box(
                    width=KitState.progress_width,
                    height="100%",
                    background_color=LEAF,
                ),
                width="100%",
                height="4px",
                margin_top="0.55rem",
                background_color="rgba(246, 241, 231, 0.16)",
            ),
            rx.box(
                _action("Pack the whole list", KitState.pack_all),
                _action("Empty the bag", KitState.empty_bag),
                display="flex",
                flex_wrap="wrap",
                gap="0.55rem",
                margin_top="1rem",
            ),
            rx.cond(
                KitState.packed_count == KIT_TOTAL,
                rx.el.p(
                    "The bag is closed. You can still change your mind.",
                    margin_top="0.9rem",
                    font_style="italic",
                    color=CREAM_SOFT,
                ),
                rx.box(),
            ),
            soft=True,
        ),
        panel(
            rx.foreach(KitState.rows, _row),
        ),
    )
