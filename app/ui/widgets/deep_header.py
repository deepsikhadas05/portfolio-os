from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static


class DeepHeader(Horizontal):

    def __init__(self, status: str = "Available for Work"):
        super().__init__()
        self.status = status

    def compose(self) -> ComposeResult:
        yield Static("⬢ DeepShell", id="header-logo")
        yield Static(self.status, id="header-status")
        yield Static("ONLINE", id="header-online")