# main click program to use GiphyCLI
import os
import click
from giphy_cli import GiphyCLI

@click.group()
def gif():
    pass

@gif.command()
@click.option("--api-key", envvar="GIPHY_API_KEY", required=True, help="Giphy API key")
@click.option("--count", type=int, default=5, help="Number of GIFs to display")
@click.option("--markdown", is_flag=True, help="Print GIFs in Markdown format")
@click.option("--lucky", is_flag=True, help="Return only the first GIF")
def trending(api_key, count, markdown, lucky):
    giphy_cli = GiphyCLI(api_key)
    giphy_cli.trending(count, markdown, lucky)

@gif.command()
@click.option("--api-key", envvar="GIPHY_API_KEY", required=True, help="Giphy API key")
@click.argument('query', nargs=-1, required=True)
@click.option("--count", type=int, default=5, help="Number of GIFs to display")
@click.option("--markdown", is_flag=True, help="Print GIFs in Markdown format")
@click.option("--lucky", is_flag=True, help="Return only the first GIF")
def search(api_key, query, count, markdown, lucky):
    giphy_cli = GiphyCLI(api_key)
    search_query = ' '.join(query)
    giphy_cli.search(search_query, count, markdown, lucky)

if __name__ == "__main__":
    gif()
