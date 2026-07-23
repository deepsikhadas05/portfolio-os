from pathlib import Path
import requests

from langchain_core.embeddings import Embeddings
from langchain_chroma import Chroma

from config import JINA_API_KEY


BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "db"


class JinaEmbeddings(Embeddings):
    def __init__(self):
        self.url = "https://api.jina.ai/v1/embeddings"
        self.headers = {
            "Authorization": f"Bearer {JINA_API_KEY}",
            "Content-Type": "application/json",
        }

    def _embed(self, texts, task):
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "model": "jina-embeddings-v3",
                "input": texts,
                "task": task,
                "normalized": True,
            },
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()["data"]

        return [item["embedding"] for item in data]

    def embed_documents(self, texts):
        return self._embed(texts, "retrieval.passage")

    def embed_query(self, text):
        return self._embed([text], "retrieval.query")[0]


_vectorstore = None


def get_vectorstore():
    global _vectorstore

    if _vectorstore is None:
        embeddings = JinaEmbeddings()

        _vectorstore = Chroma(
            persist_directory=str(DB_DIR),
            embedding_function=embeddings,
        )

    return _vectorstore