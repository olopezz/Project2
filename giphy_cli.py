import click
import requests

API_KEY = "tFRkU1RvdbGFdp76FKKBuHvMRPpCrmM7"  # Use your API key
BASE_URL = "https://api.giphy.com/v1/gifs/trending"

@click.command()
@click.option('--limit', default=10, help='Number of trending gifs to fetch.')
def main(limit):
    # Construct the API URL with the API key and limit
    url = f"{BASE_URL}?api_key={API_KEY}&limit={limit}"

    try:
        # Make a GET request to the Giphy API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            print(data)
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

