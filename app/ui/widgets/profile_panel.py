from textual.containers import Vertical
from textual.widgets import Static
from textual.app import ComposeResult
from app.ui.widgets.profile import ProfileWidget

class ProfilePanel(Vertical):

    def compose(self) -> ComposeResult:
        yield ProfileWidget()
        yield Static(
    """
Building intelligent systems.
""",
id="profile-info")