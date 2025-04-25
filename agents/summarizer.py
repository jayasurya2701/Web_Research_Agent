import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def summarize_content_groq(text, query):
    """Summarize content based on the query using Groq API."""
    if not text or "Error fetching" in text:
        return "Sorry, there was an issue retrieving relevant content. Please try another source or query."

    # Adjust the prompt to be more specific
    prompt = f"""
    You are a news summarizer. Given the content below, summarize the article in a way that answers the user's query:

    Query: {query}
    Content: {text}

    Please summarize in a concise manner while staying on topic.
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": prompt}
        ],
        "model": "meta-llama/llama-4-maverick-17b-128e-instruct"
    }

    res = requests.post("https://api.groq.com/openai/v1/chat/completions", json=data, headers=headers)

    if res.status_code == 200:
        return res.json()["choices"][0]["message"]["content"]
    
    return "Summary unavailable due to API error."
