
from ai.agent.state import AgentState
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)


from ai.prompts.system import SYSTEM_PROMPT
from ai.agent.llm import llm
from ai.rag.context import build_context
from ai.agent.chat import build_chat_messages

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

    messages, sources = build_chat_messages(question)

    response = llm.invoke(messages)

    return {
        "messages": [
            AIMessage(content=response.content)
        ],
        "metadata": {
            "sources": sources
        }
    }