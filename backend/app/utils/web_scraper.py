import requests
from bs4 import BeautifulSoup

def fetch_page(url, headers=None):
    """Fetches a web page by URL."""
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html):
    """Parses HTML content using BeautifulSoup."""
    return BeautifulSoup(html, 'html.parser')

def extract_data(soup, selector):
    """Extracts data from the parsed HTML based on a CSS selector."""
    return soup.select(selector)
