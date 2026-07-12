from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import RichLog


class BootScreen(Screen):
    """DeepShell boot screen."""

    BOOT_LINES = [
        "",
        "[bold cyan]DeepShell OS v0.1[/bold cyan]",
        "",
        "Initializing secure session...\n",
        "[green]✓[/green] Loading Profile",
        "[green]✓[/green] Loading AI Assistant",
        "[green]✓[/green] Loading Knowledge Base",
        "[bold green]✓ System Ready[/bold green]",
        "",
        "[cyan]Launching DeepShell...[/cyan]",
    ]

    def compose(self) -> ComposeResult:
        yield RichLog(
            id="boot-log",
            highlight=False,
            markup=True,
            wrap=False,
        )

    def on_mount(self) -> None:
        self.index = 0
        self.boot_log = self.query_one(RichLog)

        # Write one line every 250 ms
        self.boot_timer = self.set_interval(0.25, self.boot_step)

    def boot_step(self) -> None:
        if self.index < len(self.BOOT_LINES):
            self.boot_log.write(self.BOOT_LINES[self.index])
            self.index += 1
        else:
            self.boot_timer.stop()
            self.app.push_screen("home")