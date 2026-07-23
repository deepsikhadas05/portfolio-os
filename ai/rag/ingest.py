from datetime import date, datetime
from pathlib import Path

import frontmatter
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.vectorstore import get_vectorstore

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def _sanitize_metadata(value):
    """Convert metadata values into Chroma-compatible primitives."""
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {k: _sanitize_metadata(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize_metadata(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def load_markdown_documents() -> list[Document]:
    """Load every markdown file inside ai/data."""

    documents = []

    for file in DATA_DIR.rglob("*.md"):
        post = frontmatter.load(file)

        metadata = {
            key: _sanitize_metadata(value)
            for key, value in post.metadata.items()
        }

        metadata["source"] = str(file.relative_to(DATA_DIR))

        documents.append(
            Document(
                page_content=post.content,
                metadata=metadata,
            )
        )

    return documents

def ingest():
    documents = load_markdown_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(documents)

    get_vectorstore().add_documents(chunks)

    print(f"Loaded {len(documents)} markdown files.")

    print(f"Created {len(chunks)} chunks.")

if __name__ == "__main__":
    ingest()