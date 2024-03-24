# Class handles Giphy backend API
import requests

class GiphyAPI:
    BASE_URL = "https://api.giphy.com/v1/gifs"

    def __init__(self, api_key):
        self.api_key = api_key

    def trending(self):
        url = f"{self.BASE_URL}/trending?api_key={self.api_key}"
        response = requests.get(url)
        return response.json()

    def search(self, query):
        url = f"{self.BASE_URL}/search?api_key={self.api_key}&q={query}"
        response = requests.get(url)
        return response.json()
