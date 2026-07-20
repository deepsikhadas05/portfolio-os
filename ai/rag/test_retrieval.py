from ai.rag.retriever import retrieve

query = input("Question: ")

docs = retrieve(query)

print(f"\nRetrieved {len(docs)} documents:\n")

for i, doc in enumerate(docs, start=1):
    print("=" * 80)
    print(f"Document {i}")
    print("-" * 80)

    print("Metadata:")
    print(doc.metadata)

    print("\nContent:")
    print(doc.page_content[:500])
    print()