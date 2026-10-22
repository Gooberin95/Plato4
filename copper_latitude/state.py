"""Visitor state: navigation, the atlas filter, and the field kit."""

from dataclasses import dataclass

import reflex as rx

from copper_latitude.data import (
    CONTINENTS,
    KIT_ITEMS,
    KIT_TOTAL,
    MISSING,
    PLACES,
    POSTS,
    POSTS_BY_SLUG,
    Place,
    Post,
)


class NavState(rx.State):
    """Sidebar on wide screens, a menu overlay on small ones."""

    menu_open: bool = False

    @rx.var
    def path(self) -> str:
        """Browser path with the trailing slash removed."""
        raw = self.router.url.path or "/"
        if len(raw) > 1 and raw.endswith("/"):
            raw = raw[:-1]
        return raw or "/"

    @rx.var
    def section(self) -> str:
        """Which nav item should read as the current page."""
        path = self.path
        if path.startswith("/dispatches"):
            return "dispatches"
        if path.startswith("/atlas"):
            return "atlas"
        if path.startswith("/kit"):
            return "kit"
        if path.startswith("/about"):
            return "about"
        return "journal"

    def toggle_menu(self):
        """Open or close the small-screen menu."""
        self.menu_open = not self.menu_open

    def close_menu(self):
        """Shut the menu after a choice, and on each page load."""
        self.menu_open = False


class AtlasState(rx.State):
    """Filter the atlas by continent."""

    continent: str = "All"

    def choose(self, name: str):
        """Show one continent, or the whole atlas."""
        if name in CONTINENTS:
            self.continent = name

    @rx.var
    def places(self) -> list[Place]:
        """Places in the chosen continent."""
        chosen = self.continent
        if chosen == "All":
            return list(PLACES)
        return [place for place in PLACES if place.continent == chosen]

    @rx.var
    def count_label(self) -> str:
        """A short count for the filter row."""
        count = len(self.places)
        noun = "place" if count == 1 else "places"
        where = "the atlas" if self.continent == "All" else self.continent
        return f"{count} {noun} · {where}"


@dataclass(frozen=True)
class KitRow:
    """One line of the checklist, ready for the page."""

    id: str
    category: str
    label: str
    note: str
    checked: bool
    show_category: bool


class KitState(rx.State):
    """A packing list the visitor can tick for this browser session."""

    packed: list[str] = []

    def toggle(self, item_id: str):
        """Tick or untick one item."""
        if item_id in self.packed:
            self.packed = [packed_id for packed_id in self.packed if packed_id != item_id]
        else:
            self.packed = [*self.packed, item_id]

    def pack_all(self):
        """Mark the whole list."""
        self.packed = [item.id for item in KIT_ITEMS]

    def empty_bag(self):
        """Clear every tick."""
        self.packed = []

    @rx.var
    def packed_count(self) -> int:
        """How many items are ticked."""
        return len(self.packed)

    @rx.var
    def packed_label(self) -> str:
        """Progress as a sentence."""
        count = len(self.packed)
        return f"{count} of {KIT_TOTAL} packed"

    @rx.var
    def progress_width(self) -> str:
        """Width of the saffron progress bar."""
        if KIT_TOTAL == 0:
            return "0%"
        percent = round(100 * len(self.packed) / KIT_TOTAL)
        return f"{percent}%"

    @rx.var
    def rows(self) -> list[KitRow]:
        """Checklist rows, with a category flag on the first of each group."""
        packed = set(self.packed)
        rows: list[KitRow] = []
        last_category = ""
        for item in KIT_ITEMS:
            rows.append(
                KitRow(
                    id=item.id,
                    category=item.category,
                    label=item.label,
                    note=item.note,
                    checked=item.id in packed,
                    show_category=item.category != last_category,
                )
            )
            last_category = item.category
        return rows


class DispatchState(rx.State):
    """The dispatch matching the URL slug."""

    @rx.var
    def current(self) -> Post:
        """The open dispatch, or a blank record when the slug is unknown."""
        path = self.router.url.path or "/"
        parts = [part for part in path.split("/") if part]
        slug = parts[1] if len(parts) >= 2 and parts[0] == "dispatches" else ""
        return POSTS_BY_SLUG.get(slug, MISSING)

    @rx.var
    def found(self) -> bool:
        """Whether the slug matches a filed dispatch."""
        return self.current.slug != ""

    @rx.var
    def page_title(self) -> str:
        """Browser title for the open dispatch."""
        if self.current.slug == "":
            return "Missing dispatch — The Copper Latitude"
        return f"{self.current.title} — The Copper Latitude"

    @rx.var
    def page_description(self) -> str:
        """Browser description for the open dispatch."""
        if self.current.slug == "":
            return "No dispatch in The Copper Latitude matches this page."
        return self.current.dek

    @rx.var
    def next_dispatch(self) -> Post:
        """The following piece in the issue, wrapping at the end."""
        slug = self.current.slug
        for index, post in enumerate(POSTS):
            if post.slug == slug:
                return POSTS[(index + 1) % len(POSTS)]
        return POSTS[0]

    @rx.var
    def related(self) -> list[Post]:
        """Two other dispatches, preferring the same continent."""
        current = self.current
        if current.slug == "":
            return []
        same = [
            post
            for post in POSTS
            if post.continent == current.continent and post.slug != current.slug
        ]
        others = [
            post
            for post in POSTS
            if post.continent != current.continent and post.slug != current.slug
        ]
        return [*same, *others][:2]
