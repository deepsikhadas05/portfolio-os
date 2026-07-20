from textual.containers import Vertical
from textual.widgets import Static
from textual.app import ComposeResult
from app.ui.widgets.navigation import Navigation
from app.ui.widgets.banner import BannerWidget

from app.ui.widgets.starfield import StarField

class InfoPanel(Vertical):

    def compose(self) -> ComposeResult:
        yield StarField()
        yield BannerWidget()
        yield Static("> whoami", classes="panel-title")

        yield Static(
            """
Hi, I'm Deepsikha.

I build AI systems,
Infrastructure Automation,
and Agentic Applications.

Currently exploring
the depths of Agentic AI and LLMs.

Want to know more about me ? Use my digital twin DeepDev to chat ↓
            """,
            classes="panel-content",
        )

        yield Navigation()