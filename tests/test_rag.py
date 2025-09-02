from app.rag_node import rag_answer

def test_rag_empty():
    result = rag_answer("Nonexistent query")
    assert "No relevant information" in result
