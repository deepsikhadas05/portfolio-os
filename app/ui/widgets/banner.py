from pathlib import Path

from textual.app import ComposeResult
from textual.widgets import Static


class BannerWidget(Static):

    def compose(self) -> ComposeResult:

        banner = (
            Path(__file__)
            .parents[2]
            / "assets"
            / "banners"
            / "speed.txt"
        ).read_text(encoding="utf-8")

        yield Static(
            banner,
            id="speed-banner",
        )