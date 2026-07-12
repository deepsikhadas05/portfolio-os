from textual.app import ComposeResult
from textual.widgets import Static
from dataclasses import dataclass

@dataclass(slots=True)
class MenuItem:
    title: str
    screen: str
    
class Navigation(Static):
    """Horizontal navigation widget."""

    def __init__(self):
        super().__init__()
        self.items = [
            MenuItem("projects", "projects"),
            MenuItem("experience", "experience"),
            MenuItem("deepDev", "deepdev"),
            MenuItem("connect", "connect"),
        ]
        self.selected = 0
        self.animation_frame = 2
        self.animation_running = False

    def compose(self) -> ComposeResult:
        yield Static(self.render_menu(), id="navigation")

    def render_menu(self) -> str:
        menu = []

        stars = ["☆", "★", "☆"]

        for index, item in enumerate(self.items):

            title = item.title
            
            if index == self.selected:

                star = stars[self.animation_frame]

                menu.append(
                    f"[bold cyan]{star} {title.upper()}[/bold cyan]"
                )

            else:

                menu.append(
                    f"[grey50]☆ {title}[/grey50]"
                )

        return "     ".join(menu)
    
    def on_mount(self) -> None:
        self.set_interval(0.6, self.animate_selection)
    
    def animate_selection(self) -> None:

        if self.animation_running:
            return

        self.animation_running = True
        self.animation_frame = 0
        self.refresh_menu()

        self.set_timer(0.18, self.animation_step_one)

    def animation_step_one(self) -> None:

        self.animation_frame = 1
        self.refresh_menu()

        self.set_timer(0.18, self.animation_step_two)
    
    def animation_step_two(self) -> None:

        self.animation_frame = 2
        self.refresh_menu()

        self.set_timer(0.18, self.animation_step_three)

    def animation_step_three(self) -> None:

        self.animation_frame = 1
        self.refresh_menu()

        self.animation_running = False

    def refresh_menu(self) -> None:
        self.query_one("#navigation", Static).update(self.render_menu())

    def move_left(self) -> None:

        if self.selected > 0:
            self.selected -= 1
            self.animate_selection()

    def move_right(self) -> None:

        if self.selected < len(self.items) - 1:
            self.selected += 1
            self.animate_selection()
        

    @property
    def current(self) -> MenuItem:
        return self.items[self.selected]