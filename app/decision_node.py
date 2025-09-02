from app.weather_node import fetch_weather
from app.rag_node import rag_answer

def decide_and_execute(query: str) -> str:
    """Decide if query is about weather or PDF RAG."""
    keywords = ["weather", "temperature", "forecast", "climate"]
    if any(word in query.lower() for word in keywords):
        return fetch_weather(query)   # query is passed directly now
    else:
        return rag_answer(query)
