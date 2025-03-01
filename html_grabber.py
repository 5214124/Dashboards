from bs4 import BeautifulSoup
from typing import Optional
import requests

class Video():
    def __init__(self, url: str):
        self.url = url

    def get_html(self) -> Optional[BeautifulSoup]:
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {self.url}: {e}")
            return None
    