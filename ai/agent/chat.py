from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
)

from prompts.system import SYSTEM_PROMPT
from rag.context import build_context


def build_chat_messages(question: str):

    retrieval = build_context(question)

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=question),
        HumanMessage(
            content=f"""
Context:

{retrieval["context"]}
"""
        ),
    ]

    return messages, retrieval["sources"]