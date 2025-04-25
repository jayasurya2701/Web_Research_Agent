from bs4 import BeautifulSoup
import requests

def extract_relevant_content(url, max_paragraphs=10):
    """Extracts the most relevant text from a URL."""
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()

        soup = BeautifulSoup(res.content, "html.parser")
        article = soup.find('article') or soup.find('div', {'class': 'content'}) or soup.find('main')
        paragraphs = article.find_all('p') if article else soup.find_all('p')
        
        text = " ".join(p.get_text() for p in paragraphs[:max_paragraphs])
        return text.strip()
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"
