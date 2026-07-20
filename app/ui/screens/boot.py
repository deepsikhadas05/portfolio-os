from rich.align import Align
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import RichLog
from textual.containers import Center


class BootScreen(Screen):
    """DeepShell boot screen."""

    BOOT_LINES = [
        "",
        "[bold #F472B6]DeepShell OS v1.0[/bold #F472B6]",
        "",
        "[#B9B2C9]Initializing secure session...[/#B9B2C9]",
        "",
        "[#6EE7B7]✓[/#6EE7B7] [#F8F7FC]Loading Profile[/#F8F7FC]",
        "[#6EE7B7]✓[/#6EE7B7] [#F8F7FC]Loading AI Assistant[/#F8F7FC]",
        "[#6EE7B7]✓[/#6EE7B7] [#F8F7FC]Loading Knowledge Base[/#F8F7FC]",
        "",
        "[bold #C084FC]✦ DeepDev Online[/bold #C084FC]",
        "[bold #6EE7B7]✓ System Ready[/bold #6EE7B7]",
        "",
        "[bold #F472B6]Launching DeepShell...[/bold #F472B6]",
    ]

    def compose(self) -> ComposeResult:
        with Center():
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
            self.boot_log.write(
                Align.center(self.BOOT_LINES[self.index])
            )
            self.index += 1
        else:
            self.boot_timer.stop()
            self.app.push_screen("home")