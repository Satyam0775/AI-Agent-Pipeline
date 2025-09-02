from typing_extensions import TypedDict
from langgraph.graph import StateGraph, END
from app.weather_node import fetch_weather
from app.rag_node import rag_answer
from app.llm_node import refine_answer

# Graph state definition
class AgentState(TypedDict):
    query: str
    result: str

# Weather node
def weather_node(state: AgentState) -> AgentState:
    city = state["query"].split()[-1]
    state["result"] = fetch_weather(city)
    return state

# PDF node
def rag_node(state: AgentState) -> AgentState:
    state["result"] = rag_answer(state["query"])
    return state

# Decision node
def decision_node(state: AgentState) -> str:
    keywords = ["weather", "temperature", "forecast", "climate"]
    if any(word in state["query"].lower() for word in keywords):
        return "weather"
    return "rag"

# LLM node
def llm_node(state: AgentState) -> AgentState:
    state["result"] = refine_answer(f"Summarize this: {state['result']}")
    return state

# Build pipeline
def build_pipeline():
    workflow = StateGraph(AgentState)

    workflow.add_node("weather", weather_node)
    workflow.add_node("rag", rag_node)
    workflow.add_node("llm", llm_node)

    workflow.set_entry_point("llm")

    workflow.add_conditional_edges(
        "llm",
        decision_node,
        {"weather": "weather", "rag": "rag"},
    )

    workflow.add_edge("weather", END)
    workflow.add_edge("rag", END)

    return workflow.compile()
