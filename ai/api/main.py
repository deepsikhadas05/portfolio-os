from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from ai.agent.graph import graph

app = FastAPI(title="DeepDev API")


class ChatRequest(BaseModel):
    thread_id: str
    question: str


@app.get("/")
def health():
    return {"status": "DeepDev Online"}


@app.post("/ask")
def ask(request: ChatRequest):

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=request.question)
            ]
        },
        config={
            "configurable": {
                "thread_id": request.thread_id
            }
        }
    )

    return {
        "answer": result["messages"][-1].content,
        "sources": result["metadata"]["sources"],
    }