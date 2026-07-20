from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Static, Input, Markdown
from app.api.deepdev_client import DeepDevClient
from app.ui.screens.base import BaseScreen
from textual.widgets import Input

class DeepDevScreen(BaseScreen):

    PAGE_TITLE = "Talk With My AI Twin"
    def __init__(self):
        super().__init__()
        self.client = DeepDevClient()

    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
    ]
    
    async def on_input_submitted(self, event: Input.Submitted) -> None:
        question = event.value.strip()

        if not question:
            return

        result = self.client.ask(question)

        history = self.query_one("#chat-history", VerticalScroll)

        await history.mount(
            Static(f"> [bold pink]You:[/] {question}\n")
        )

        await history.mount(
            Static("✦ [bold purple]DeepDev:[/]\n")
        )

        answer = result["answer"]

        markdown = Markdown("")
        await history.mount(markdown)

        for i in range(len(answer)):
            markdown.update(answer[: i + 1])

        event.input.value = ""

        history.scroll_end(animate=False)
    def compose_body(self) -> ComposeResult:

        with VerticalScroll(id="chat-history"):

            yield Static(
                "[b]DeepDev[/b]\n\n"
                "Hello! I'm DeepDev.\n"
                "Ask me anything about Deepsikha's experience, skills, projects or career.",
                id="welcome-message",
            )

        yield Input(
            placeholder="Ask DeepDev anything...",
            id="chat-input",
        )