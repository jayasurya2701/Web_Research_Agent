import os
import requests
from dotenv import load_dotenv
load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")


def search_web(keywords, num_results=5):
    query = "+".join(keywords)
    url = f"https://serpapi.com/search.json?q={query}&api_key={SERPAPI_KEY}&num={num_results}"
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        data = response.json()
        for result in data.get("organic_results", [])[:num_results]:
            results.append({
                "title": result.get("title"),
                "link": result.get("link"),
                "snippet": result.get("snippet")
            })
    return results