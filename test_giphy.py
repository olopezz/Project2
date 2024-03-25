# test_giphy.py
import os
import unittest
from unittest.mock import patch
from io import StringIO
from giphy_cli import GiphyCLI

class TestGiphyCLI(unittest.TestCase):
    def setUp(self):
        self.api_key = os.environ.get("GIPHY_API_KEY")
        if not self.api_key:
            raise ValueError("GIPHY_API_KEY environment variable is not set.")
        self.giphy_cli = GiphyCLI(self.api_key)

    # Small Tests (without calling the Giphy API)
    @patch("giphy_api.GiphyAPI.trending")
    def test_trending_small(self, mock_trending):
        # Mock the response from the GiphyAPI trending method
        mock_response = {
            "data": [
                {"id": "1", "title": "GIF 1", "url": "https://giphy.com/gif1"},
                {"id": "2", "title": "GIF 2", "url": "https://giphy.com/gif2"},
            ]
        }
        mock_trending.return_value = mock_response

        # Call the trending method and get the output
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.giphy_cli.trending(count=2)
            output = fake_out.getvalue().strip()

        # Expected output
        expected_output = "1) GIF 1 (https://giphy.com/gif1)\n2) GIF 2 (https://giphy.com/gif2)"
        self.assertEqual(output, expected_output)

    @patch("giphy_api.GiphyAPI.search")
    def test_search_small(self, mock_search):
        # Mock the response from the GiphyAPI search method
        mock_response = {
            "data": [
                {"id": "1", "title": "GIF 1", "url": "https://giphy.com/gif1"},
                {"id": "2", "title": "GIF 2", "url": "https://giphy.com/gif2"},
            ]
        }
        mock_search.return_value = mock_response

        # Call the search method and get the output
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.giphy_cli.search(query="hello", count=2)
            output = fake_out.getvalue().strip()

        # Expected output
        expected_output = "1) GIF 1 (https://giphy.com/gif1)\n2) GIF 2 (https://giphy.com/gif2)"
        self.assertEqual(output, expected_output)

    # Medium Tests (calling the Giphy API)
    def test_trending_medium(self):
        # Call the trending method and get the output
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.giphy_cli.trending(count=2)
            output = fake_out.getvalue().strip()

        # Cofirm that the output contains the required format
        self.assertRegex(output, r"1\) .+ \(https://.+\)\n2\) .+ \(https://.+\)")

    def test_search_medium(self):
        # Call the search method and get the output
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.giphy_cli.search(query="hello", count=2)
            output = fake_out.getvalue().strip()

        # Confirm that the output contains the required format
        self.assertRegex(output, r"1\) .+ \(https://.+\)\n2\) .+ \(https://.+\)")

if __name__ == "__main__":
    unittest.main()
