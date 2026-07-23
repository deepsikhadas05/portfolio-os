
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

from ai.agent.state import AgentState
from ai.prompts.system import SYSTEM_PROMPT
from ai.agent.llm import llm
from ai.rag.context import build_context


def validate_question(state: AgentState):

    question = state["messages"][-1].content.strip()

    if not question:
        raise ValueError("Question cannot be empty.")

    return {
        "messages": [
            HumanMessage(content=question)
        ]
    }

# def build_prompt(state: AgentState):

#    return {

#          "system_prompt": SYSTEM_PROMPT

#    }



def generate_answer(state: AgentState):

    question = state["messages"][-1].content

    retrieval = build_context(question)

    response = llm.invoke(
        [
            SystemMessage(content=SYSTEM_PROMPT),
            *state["messages"],
            HumanMessage(
                content=f"""
Context:

{retrieval["context"]}
"""
            ),
        ]
    )

    return {
        "messages": [
            AIMessage(content=response.content)
        ],
        "metadata": {
            "sources": retrieval["sources"]
        }
    }