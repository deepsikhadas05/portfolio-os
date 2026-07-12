from textual.app import ComposeResult
from textual.widgets import Static
from app.ui.screens.base import BaseScreen


class DeepDevScreen(BaseScreen):

    PAGE_TITLE = "Talk With My AI Twin"

    BINDINGS = [
        ("escape", "app.pop_screen", "Back")
    ]

    def compose_body(self) -> ComposeResult:
        yield Static(
            """
DEEP DEV

Coming Soon...
""",
            id="screen-title",
        )