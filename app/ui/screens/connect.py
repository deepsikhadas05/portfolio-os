from textual import events
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import ListView, ListItem, Static
from app.ui.screens.base import BaseScreen
import webbrowser



class SocialLinkItem(ListItem):
    can_focus = True

    def __init__(self, icon: str, label: str, url: str):
        super().__init__()
        self.add_class("social-link-item")
        self.icon = icon
        self.label = label
        self.url = url

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Static(self.icon, classes="social-icon"),
            Static(self.label, classes="social-label"),
            classes="social-link",
        )

    def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
            webbrowser.open(self.url)
            event.stop()


class ConnectScreen(BaseScreen):

    PAGE_TITLE = "Let's Connect"

    BINDINGS = [
        ("enter", "open_link", "Open"),
        ("escape", "app.pop_screen", "Back"),
    ]

    LINKS = [
        ("💼", "LinkedIn", "https://www.linkedin.com/in/deepsikha-das-347976253/"),
        ("💻", "GitHub", "https://github.com/deepsikhadas05"),
        ("✉", "Email", "mailto:deepsikha1104@gmail.com"),
    ]

    def compose_body(self) -> ComposeResult:
        items = [
            SocialLinkItem(icon, label, url)
            for icon, label, url in self.LINKS
        ]
        yield ListView(*items, id="connect-list")

    def on_mount(self):
        self.query_one(ListView).focus()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        item = event.item

        if isinstance(item, SocialLinkItem):
            webbrowser.open(item.url)