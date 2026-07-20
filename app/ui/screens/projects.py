from textual.app import ComposeResult
from textual.containers import VerticalScroll
import webbrowser
from app.ui.screens.base import BaseScreen
from app.ui.widgets.project_card import ProjectCard


class ProjectsScreen(BaseScreen):

    PAGE_TITLE = "Featured Projects"

    BINDINGS = [
        ("up", "focus_previous", "Up"),
        ("down", "focus_next", "Down"),
        ("enter", "open_project", "Open"),
        ("escape", "app.pop_screen", "Back"),
    ]

    def compose_body(self) -> ComposeResult:

        with VerticalScroll():

            yield ProjectCard(
                title="DeepShell",
                subtitle="AI Terminal Portfolio",
                description=(
                    "AI-powered terminal portfolio featuring DeepDev, FastAPI, "
                    "LangGraph orchestration, ChromaDB-powered RAG and Groq LLM."
                ),
                tech="Python • Textual • FastAPI • LangGraph • ChromaDB • Groq",
                github="https://github.com/deepsikhadas05/portfolio-os",
            )

            yield ProjectCard(
                title="Brain Tumor Segmentation",
                subtitle="Brain Tumor Segmentation using Attention U-Net",
                description=(
                    "MRI brain tumor segmentation using an "
                    "Attention U-Net architecture for accurate "
                    "medical image analysis."
                ),
                tech="Python • PyTorch • Attention U-Net • Medical Imaging",
                github="https://github.com/deepsikhadas05/MRI-Brain-Tumor-Detection-Segmentation-using-Attention-U-Net",
            )

            yield ProjectCard(
                title="🎵 Story Mood Playlist",
                subtitle="Mood-Based Spotify Playlist Generator",
                description=(
                    "Chrome extension that analyzes the emotional tone of web pages "
                    "and recommends Spotify playlists to match the reader's mood. "
                    "Features AI-powered mood detection, Spotify integration, "
                    "genre/language filters, and secure PKCE authentication."
                ),
                tech="Python • Chrome Extension • Spotify API • AI",
                github="https://github.com/deepsikhadas05/STORY-MOOD-PLAYLIST",
            )

    
    def on_mount(self):
        self.set_timer(
            0.05,
            lambda: self.query(ProjectCard).first().focus()
        )


    def action_focus_next(self):
        cards = list(self.query(ProjectCard))
        if not cards:
            return

        current = self.app.focused
        if current not in cards:
            cards[0].focus()
            return

        index = cards.index(current)
        next_index = (index + 1) % len(cards)
        cards[next_index].focus()
        cards[next_index].scroll_visible(duration=0.15)

    def action_focus_previous(self):
        cards = list(self.query(ProjectCard))
        if not cards:
            return

        current = self.app.focused
        if current not in cards:
            cards[0].focus()
            return

        index = cards.index(current)
        prev_index = (index - 1) % len(cards)
        cards[prev_index].focus()
        cards[prev_index].scroll_visible(duration=0.15)
    
    def action_open_project(self):
        focused = self.app.focused

        if isinstance(focused, ProjectCard):
            webbrowser.open(focused.github)