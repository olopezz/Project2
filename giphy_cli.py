# Class handles user input
from giphy_api import GiphyAPI

class GiphyCLI:
    def __init__(self, api_key):
        self.giphy_api = GiphyAPI(api_key)

    def trending(self, count=5, markdown=False, lucky=False):
        data = self.giphy_api.trending()
        
        if lucky:
            gif = data["data"][0]
            self.print_gif(gif, markdown, lucky)
        else:
            gifs = data["data"][:count]
            self.print_gifs(gifs, markdown)

    def search(self, query, count=5, markdown=False, lucky=False):
        data = self.giphy_api.search(query)
        
        if lucky:
            gif = data["data"][0]
            self.print_gif(gif, markdown, lucky)
        else:
            gifs = data["data"][:count]
            self.print_gifs(gifs, markdown)

    def print_gifs(self, gifs, markdown):
        for i, gif in enumerate(gifs, start=1):
            if markdown:
                print(f"{i}) ![{gif['title']}]({gif['images']['original']['url']})")
            else:
                print(f"{i}) {gif['title']} ({gif['url']})")

    def print_gif(self, gif, markdown, lucky):
        if markdown:
            print(f"![{gif['title']}]({gif['images']['original']['url']})")
        else:
            if lucky:
                print(f"{gif['title']} ({gif['url']})")
            else:
                print(f"1) {gif['title']} ({gif['url']})")
