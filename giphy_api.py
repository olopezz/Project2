# Class will handle Giphy backend API
import requests

class GiphyAPI:
    BASE_URL = "https://api.giphy.com/v1/gifs"

    def __init__(self, api_key):
        self.api_key = api_key

    def trending(self, limit=10, offset=0, rating='g'):
        url = f"{self.BASE_URL}/trending?api_key={self.api_key}&limit={limit}&offset={offset}&rating={rating}"
        response = requests.get(url)
        return response.json()

    def search(self, query, limit=10, offset=0, rating='g', lang='en'):
        url = f"{self.BASE_URL}/search?api_key={self.api_key}&q={query}&limit={limit}&offset={offset}&rating={rating}&lang={lang}"
        response = requests.get(url)
        return response.json()
