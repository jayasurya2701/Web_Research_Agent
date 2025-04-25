import os
import requests
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def summarize_content_groq(text, query):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": f"Summarize this content in response to the query: '{query}'\n\n{text}"}
        ],
        "model": "meta-llama/llama-4-scout-17b-16e-instruct"
    }
    res = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)
    if res.status_code == 200:
        return res.json()["choices"][0]["message"]["content"]
    return "Summary unavailable due to API error."
