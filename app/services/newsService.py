import requests
from flask import current_app

def get_crypto_news():
    try:
        api_key = current_app.config["NEWS_API_KEY"]

        url = "https://newsapi.org/v2/everything"

        params = {
            "q": "cryptocurrency",
            "apiKey": api_key,
            "language": "es",
            "pageSize": 5,
            "sortBy": "publishedAt"
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        return response.json().get("articles", [])

    except Exception:
        return []