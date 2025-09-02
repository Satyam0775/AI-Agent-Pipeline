import os
from dotenv import load_dotenv
from langsmith import Client
from app.pipeline import build_pipeline

# Load environment variables
load_dotenv(dotenv_path=".env", override=True)

# Setup LangSmith client
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
client = Client(api_key=LANGSMITH_API_KEY) if LANGSMITH_API_KEY else None

# Build LangGraph pipeline
pipeline = build_pipeline()

def run_pipeline(query: str) -> str:
    """Run LangGraph pipeline and log result to LangSmith."""
    state = {"query": query, "result": ""}
    result = pipeline.invoke(state)

    final_answer = result["result"]

    # ✅ Log to LangSmith if client exists
    if client:
        client.create_run(
            project_name="AI_Agent_Assignment",
            name="pipeline_run",          # required
            run_type="chain",             # required
            inputs={"query": query},
            outputs={"result": final_answer},
        )
        print("✅ LangSmith log sent!")
    else:
        print("⚠️ LangSmith logging skipped (no client).")

    return final_answer
