from random import choice, randrange

from textual.events import Resize
from textual.widgets import Static

STAR_CHARS = ["✦", "✧", "⋆", "·", "."]

class StarField(Static):

    def __init__(self):
        super().__init__("")

    def on_mount(self) -> None:
        self.set_timer(0.1, self.refresh_stars)
        self.set_interval(0.6, self.refresh_stars)

    def on_resize(self, event: Resize) -> None:
        self.refresh_stars()

    def refresh_stars(self) -> None:
        width = self.size.width
        height = self.size.height
        if width <= 0 or height <= 0:
            return

        total_cells = width * height
        star_count = max(80, int(total_cells * 0.035))
        positions = set()

        while len(positions) < star_count:
            positions.add((randrange(height), randrange(width)))

        rows = [[" "] * width for _ in range(height)]
        for y, x in positions:
            rows[y][x] = choice(STAR_CHARS)

        self.update("\n".join("".join(row) for row in rows))