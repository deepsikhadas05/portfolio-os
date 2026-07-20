from ai.rag.retriever import retrieve


def build_context(question: str) -> dict:
    """
    Retrieve relevant documents and return both the context
    string and the list of unique source documents.
    """

    docs = retrieve(question)

    sections = []
    sources = []
    seen_sources = set()

    for doc in docs:
        title = doc.metadata.get("title", "Untitled")
        doc_type = doc.metadata.get("type", "unknown")
        source = doc.metadata.get("source", "unknown")

        sections.append(
            f"""
### {title}

Type: {doc_type}
Source: {source}

{doc.page_content}
"""
        )

        if source not in seen_sources:
            sources.append(
                {
                    "title": title,
                    "source": source,
                    "type": doc_type,
                }
            )

            seen_sources.add(source)
                

    return {
        "context": "\n\n".join(sections),
        "sources": sources,
    }