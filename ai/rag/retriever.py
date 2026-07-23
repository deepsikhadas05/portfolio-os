from rag.vectorstore import get_vectorstore


def get_retriever():
    vectorstore = get_vectorstore()
    return vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
        },
    )


def retrieve(query: str):
    retriever = get_retriever()
    return retriever.invoke(query)