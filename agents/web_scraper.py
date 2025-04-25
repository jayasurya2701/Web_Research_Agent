import requests
from bs4 import BeautifulSoup

def extract_content(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.content, "html.parser")
        paragraphs = soup.find_all('p')
        text = " ".join(p.get_text() for p in paragraphs[:10])  
        return text.strip()
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"
