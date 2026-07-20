from typing import TypedDict, NotRequired
from langgraph.graph import MessagesState

class AgentState(MessagesState):
    context: NotRequired[str]
    metadata: NotRequired[dict]