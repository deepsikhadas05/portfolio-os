from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage

from rag.retriever import get_retriever
from agent.graph import graph

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.retriever = get_retriever()
    yield

app = FastAPI(title="DeepDev API", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    thread_id: str
    question: str

@app.on_event("startup")
async def startup_event():
    app.state.retriever = get_retriever()

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