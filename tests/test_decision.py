from app.decision_node import decide_and_execute

def test_decision_weather(monkeypatch):
    monkeypatch.setattr("app.weather_node.fetch_weather", lambda city: "Sunny 30°C")
    result = decide_and_execute("What's the weather in Delhi?")
    # Accept both real or mocked response
    assert "Sunny" in result or "temperature" in result
