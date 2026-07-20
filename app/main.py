from textual.app import App
from app.ui.screens.boot import BootScreen
from app.ui.screens.home import HomeScreen
from app.ui.widgets.navigation import Navigation
from app.ui.screens.projects import ProjectsScreen
from app.ui.screens.experience import ExperienceScreen
from app.ui.screens.connect import ConnectScreen
from app.ui.screens.deepDev import DeepDevScreen
import webbrowser

class DeepShell(App):
    """DeepShell"""

    TITLE = "DeepShell"

    CSS_PATH = [
    "ui/styles/colors.tcss",
    "ui/styles/layout.tcss",
    "ui/styles/widgets.tcss",
    ]

    BINDINGS = [
        ("left", "nav_left", ""),
        ("right", "nav_right", ""),
        ("enter", "nav_select", ""),
        ("q", "quit", "Quit"),
        ("r", "resume", "Resume"),
    ]

    def on_mount(self):

        self.install_screen(HomeScreen(), "home")
        self.install_screen(BootScreen(), "boot")
        self.install_screen(ProjectsScreen(), "projects")
        self.install_screen(ExperienceScreen(), "experience")
        self.install_screen(ConnectScreen(), "connect")
        self.install_screen(DeepDevScreen(), "deepdev")

        self.push_screen("boot")
    
    def action_nav_left(self) -> None:
        self.screen.query_one(Navigation).move_left()


    def action_nav_right(self) -> None:
        self.screen.query_one(Navigation).move_right()


    def action_nav_select(self) -> None:
        nav = self.screen.query_one(Navigation)
        self.push_screen(nav.current.screen)
        print(f"Opening {nav.current}")
    
    def action_resume(self):
        webbrowser.open(
            "https://raw.githubusercontent.com/deepsikhadas05/portfolio-os/app/assets/resume_deepsikha_AI.pdf"
        )

if __name__ == "__main__":
    DeepShell().run()
