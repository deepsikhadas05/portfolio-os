from textual.widgets import Static


class DeepFooter(Static):
    def __init__(self):
        super().__init__(
            "[← →] to navigate   [enter] to open   [esc] to go back   [R] resume   [Q] quit",
            id="deep-footer",
            markup=False,
        )