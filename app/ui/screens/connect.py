from textual.app import ComposeResult
from textual.widgets import Static
from app.ui.screens.base import BaseScreen


class ConnectScreen(BaseScreen):

    PAGE_TITLE = "Let's Connect"


    BINDINGS = [
        ("escape", "app.pop_screen", "Back")    
    ]
    def compose_body(self) -> ComposeResult:
        yield Static(
            """
CONNECT

Coming Soon...
""",
            id="screen-title",
        )