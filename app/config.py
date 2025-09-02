import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(dotenv_path=".env", override=True)

# --- API Keys ---
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# --- LangSmith ---
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT", "AI_Agent_Assignment")
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING", "true")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT", "https://api.smith.langchain.com")

# --- Models ---
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "google/flan-t5-base"

# --- Qdrant settings ---
QDRANT_URL = "http://localhost:6333"
QDRANT_COLLECTION = "pdf_docs"
