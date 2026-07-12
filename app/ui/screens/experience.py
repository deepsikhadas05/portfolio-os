from textual.app import ComposeResult
from textual.widgets import Static
from app.ui.screens.base import BaseScreen

class ExperienceScreen(BaseScreen):
    PAGE_TITLE = "Professional Journey"
    BINDINGS = [
        ("escape", "app.pop_screen", "Back")
    ]

    def compose_body(self) -> ComposeResult:
        yield Static(
            """
EXPERIENCE

Coming Soon...
""",
            id="screen-title",
        )