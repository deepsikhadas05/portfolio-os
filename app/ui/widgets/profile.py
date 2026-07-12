from pathlib import Path

from textual.app import ComposeResult
from textual.widgets import Static


class ProfileWidget(Static):

    def compose(self) -> ComposeResult:

        portrait_path = (
            Path(__file__)
            .parents[2]
            / "assets"
            / "portrait.txt"
        )

        portrait = portrait_path.read_text(
            encoding="utf-8"
        )

        yield Static(
            portrait,
            id="portrait",
        )