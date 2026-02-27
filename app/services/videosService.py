import requests
from flask import current_app

def get_crypto_videos(max_results=4):
    return search_videos("cryptocurrency news", max_results)


def search_videos(query, max_results=6):
    try:
        api_key = current_app.config["YOUTUBE_API_KEY"]

        url = "https://www.googleapis.com/youtube/v3/search"

        params = {
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "key": api_key
        }

        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()

        return response.json().get("items", [])

    except Exception:
        return []