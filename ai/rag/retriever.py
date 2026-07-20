from ai.rag.vectorstore import vectorstore

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
    },
)


def retrieve(query: str):
    return retriever.invoke(query)