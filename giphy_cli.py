# Class will handle user input
from giphy_api import GiphyAPI

class GiphyCLI:
    def __init__(self, api_key):
        self.giphy_api = GiphyAPI(api_key)

    def trending(self, limit=10, offset=0, rating='g'):
        data = self.giphy_api.trending(limit, offset, rating)
        self.print_gifs(data)

    def search(self, query, limit=10, offset=0, rating='g', lang='en'):
        data = self.giphy_api.search(query, limit, offset, rating, lang)
        self.print_gifs(data)

    def print_gifs(self, data):
        for gif in data["data"]:
            print(f"GIF ID: {gif['id']}")
            print(f"GIF URL: {gif['url']}")
            print(f"GIF Title: {gif['title']}")
            print("---")
