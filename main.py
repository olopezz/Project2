# main click program to use GiphyCLI
import os
import click
from giphy_cli import GiphyCLI

@click.group()
def gif():
    pass

@gif.command()
@click.option("--api-key", envvar="GIPHY_API_KEY", required=True, help="Giphy API key")
@click.option('--limit', default=10, show_default=True, help='Number of trending GIFs to fetch')
@click.option('--offset', default=0, show_default=True, help='Offset for pagination')
@click.option('--rating', type=click.Choice(['g', 'pg', 'pg-13', 'r'], case_sensitive=False), default='g', show_default=True, help='Maximum rating of GIFs')
def trending(api_key, limit, offset, rating):
    giphy_cli = GiphyCLI(api_key)
    giphy_cli.trending(limit, offset, rating)

@gif.command()
@click.option("--api-key", envvar="GIPHY_API_KEY", required=True, help="Giphy API key")
@click.argument('query', nargs=-1, required=True)
@click.option('--limit', default=10, show_default=True, help='Number of search results to fetch')
@click.option('--offset', default=0, show_default=True, help='Offset for pagination')
@click.option('--rating', type=click.Choice(['g', 'pg', 'pg-13', 'r'], case_sensitive=False), default='g', show_default=True, help='Maximum rating of GIFs')
@click.option('--lang', default='en', show_default=True, help='Specify language using a 2-letter ISO 639-1 language code')
def search(api_key, query, limit, offset, rating, lang):
    giphy_cli = GiphyCLI(api_key)
    search_query = ' '.join(query)
    giphy_cli.search(search_query, limit, offset, rating, lang)

if __name__ == "__main__":
    gif()
