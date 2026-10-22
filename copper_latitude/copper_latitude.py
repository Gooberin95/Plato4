"""The Copper Latitude, a field journal."""

import reflex as rx

from copper_latitude.pages import (  # noqa: F401
    about,
    atlas,
    dispatch,
    dispatches,
    home,
    kit,
    not_found,
)
from copper_latitude.theme import FONT_STYLESHEET

app = rx.App(
    stylesheets=[FONT_STYLESHEET, "/styles.css"],
    html_lang="en",
)
