from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from agent.state import AgentState
from agent.nodes import (
    validate_question,
    generate_answer,
)

builder = StateGraph(AgentState)

builder.add_node("validate", validate_question)
builder.add_node("answer", generate_answer)

builder.add_edge(START, "validate")
builder.add_edge("validate", "answer")

memory = MemorySaver()
graph = builder.compile(
    checkpointer=memory
)