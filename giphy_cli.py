import os
import click
import requests

BASE_URL = "https://api.giphy.com/v1/gifs"

@click.group()
def gif():
    print("Welcome to the Giphy CLI!")

@gif.command()
@click.option("--api-key", envvar="GIPHY_API_KEY", required=True, help="Giphy API key")
@click.option('--limit', default=10, help='Number of trending gifs to fetch.')
def trending(api_key, limit):
    print("Trending subcommand called!")
    
    # Construct the API URL for trending GIFs
    url = f"{BASE_URL}/trending?api_key={api_key}&limit={limit}"

    try:
        print("Making a request to the Giphy API...")
        
        # Make a GET request to the Giphy API
        response = requests.get(url)

        print(f"Response status code: {response.status_code}")
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Print the retrieved data
            print("Retrieved data:")
            for gif in data["data"]:
                print(f"GIF ID: {gif['id']}")
                print(f"GIF URL: {gif['url']}")
                print(f"GIF Title: {gif['title']}")
                print("---")
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

@gif.command()
@click.option("--api-key", envvar="GIPHY_API_KEY", required=True, help="Giphy API key")
@click.option('--query', required=True, help='Search query.')
@click.option('--limit', default=10, help='Number of search results to fetch.')
def search(api_key, query, limit):
    print("Search subcommand called!")
    
    # Construct the API URL for search
    url = f"{BASE_URL}/search?api_key={api_key}&q={query}&limit={limit}"

    try:
        print("Making a request to the Giphy API...")
        
        # Make a GET request to the Giphy API
        response = requests.get(url)

        print(f"Response status code: {response.status_code}")
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Print the retrieved data
            print("Retrieved data:")
            for gif in data["data"]:
                print(f"GIF ID: {gif['id']}")
                print(f"GIF URL: {gif['url']}")
                print(f"GIF Title: {gif['title']}")
                print("---")
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    gif()
