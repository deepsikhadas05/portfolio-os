from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Static

from app.ui.screens.base import BaseScreen


class ExperienceScreen(BaseScreen):

    PAGE_TITLE = "Experience"

    def compose_body(self) -> ComposeResult:

        with VerticalScroll():

            yield Static(
                """
[bold #3f75da]🚢 A.P Moller Maersk[/]

[#B9B2C9]Intern - Infrastructure Engineer[/]
[#A78BFA]Jul 2025 – Jul 2026[/]

[#6EE7B7]│[/]
[#6EE7B7]├─[/] Automated deployment of cybersecurity agents across
    9,000+ systems in air-gapped maritime environments.

[#6EE7B7]├─[/] Built an offline WSUS patch deployment framework
    using PowerShell, WSUS and Ansible.

[#6EE7B7]├─[/] Provisioned Cyber Security Gateway virtual
    machines across 300+ vessel infrastructures.

[#6EE7B7]├─[/] Developed a Streamlit dashboard for monitoring
    patch deployment status.

[#6EE7B7]├─[/] Supported infrastructure operations through
    ServiceNow incident and change management.

[#6EE7B7]└─[/] Diagnosed Windows, networking and application
    issues across enterprise maritime environments.
""",
                classes="experience-card",
            )