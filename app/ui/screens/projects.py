from textual.app import ComposeResult
from textual.widgets import Static
from app.ui.screens.base import BaseScreen



class ProjectsScreen(BaseScreen):

    PAGE_TITLE = "Featured Projects"
    BINDINGS = [
        ("escape", "app.pop_screen", "Back")
    ]

    def compose_body(self) -> ComposeResult:
        yield Static(
            """
            PROJECTS

            Coming Soon...
            """,
            id="screen-title",
        )