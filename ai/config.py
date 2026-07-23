from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
JINA_API_KEY = os.getenv("JINA_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found.")

if not JINA_API_KEY:
    raise ValueError("JINA_API_KEY not found.")