from app.llm_node import refine_answer

def test_llm_response(monkeypatch):
    monkeypatch.setattr("app.llm_node.generator", lambda prompt, max_length, do_sample: [{"generated_text": "Clean Answer"}])
    result = refine_answer("Raw text")
    assert result == "Clean Answer"
