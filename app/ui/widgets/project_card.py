from textual.containers import Vertical
from textual.widgets import Static
import webbrowser
from textual import events


class ProjectCard(Static):

    can_focus = True

    def __init__(
        self,
        title: str,
        subtitle: str,
        description: str,
        tech: str,
        github: str,
    ):
        super().__init__()

        self.github = github

        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.tech = tech

    def compose(self):

        yield Static(
            f"[bold #F472B6]✦ {self.title}[/]\n[#B9B2C9]{self.subtitle}[/]",
            classes="project-title",
        )

        yield Static(
            self.description,
            classes="project-description",
        )

        yield Static(
            f"[#3f75da]{self.tech}[/]",
            classes="project-tech",
        )

        yield Static(
            "[bold #C084FC]↗ Open Repository[/]",
            classes="project-link",
        )
    
    def on_key(self, event: events.Key):

        if event.key == "enter":
            webbrowser.open(self.github)
    
    
    