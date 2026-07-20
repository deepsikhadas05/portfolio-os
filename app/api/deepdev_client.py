import uuid
import requests


class DeepDevClient:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"
        self.thread_id = str(uuid.uuid4())

    def ask(self, question: str):
        response = requests.post(
            f"{self.base_url}/ask",
            json={
                "thread_id": self.thread_id,
                "question": question,
            },
        )

        response.raise_for_status()
        return response.json()