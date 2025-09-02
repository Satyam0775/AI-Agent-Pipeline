from app.weather_node import fetch_weather

def test_weather_response(monkeypatch):
    class MockResponse:
        status_code = 200
        def json(self):
            return {
                "main": {"temp": 25},
                "weather": [{"description": "clear sky"}],
                "sys": {"country": "IN"}   # ✅ added
            }
    monkeypatch.setattr("requests.get", lambda url, timeout=10: MockResponse())
    result = fetch_weather("Delhi")
    assert "25" in result
