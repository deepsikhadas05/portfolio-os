from textual.screen import Screen
from textual.containers import Horizontal
from textual.widgets import Header, Footer
from textual.app import ComposeResult

from app.ui.widgets.profile_panel import ProfilePanel
from app.ui.widgets.info_panel import InfoPanel
from app.ui.widgets.deep_header import DeepHeader
from app.ui.widgets.deep_footer import DeepFooter
from app.ui.widgets.starfield import StarField
class HomeScreen(Screen):

    def compose(self) -> ComposeResult:

        yield DeepHeader()

        with Horizontal(id="body"):
            yield StarField()
            yield ProfilePanel(id="left-panel")

            yield InfoPanel(id="right-panel")

        yield DeepFooter()