import requests, re
from app.config import OPENWEATHERMAP_API_KEY

def extract_city(query: str) -> str:
    """
    Extract the city name from a query string.
    Example:
    "What's the weather in Patna?" -> "Patna"
    "Weather forecast in Delhi, IN" -> "Delhi IN"
    """
    # Find 'in <city>' in the query
    match = re.search(r"\bin\s+([A-Za-z\s,]+)", query, re.IGNORECASE)
    if match:
        city = match.group(1).strip()
    else:
        # fallback: assume last word is the city
        city = query.split()[-1]

    # Clean punctuation like '?' or ','
    city = re.sub(r"[^\w\s]", "", city)
    return city.title()


def fetch_weather(query: str) -> str:
    """Fetch weather data from OpenWeatherMap API using extracted city name."""
    if not OPENWEATHERMAP_API_KEY:
        return "❌ Error: Missing OpenWeather API key."

    # ✅ Always extract city
    city = extract_city(query)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        try:
            error_msg = response.json().get("message", "Unknown error")
        except Exception:
            error_msg = response.text
        return f"❌ Error fetching weather for '{city}': {error_msg}"

    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    country = data['sys'].get('country', '')

    return f"🌦️ The current temperature in {city}, {country} is {temp}°C with {desc}."
