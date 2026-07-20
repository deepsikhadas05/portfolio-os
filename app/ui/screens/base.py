from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen

from app.ui.widgets.deep_header import DeepHeader
from app.ui.widgets.deep_footer import DeepFooter
from app.ui.widgets.starfield import StarField


class BaseScreen(Screen):

    BINDINGS = [
        ("escape", "back", "Back"),
    ]

    PAGE_TITLE = "[#FAFAFA]Available for Work[/#FAFAFA]"
    def compose(self) -> ComposeResult:
        yield StarField()
        yield DeepHeader(self.PAGE_TITLE)
        with Container(id="page-body"):
            yield from self.compose_body()
        yield DeepFooter()

    def compose_body(self) -> ComposeResult:
        """Override in child screens."""
        yield

    def action_back(self) -> None:
        self.app.pop_screen()