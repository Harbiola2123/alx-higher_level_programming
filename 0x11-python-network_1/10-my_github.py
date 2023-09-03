"""Sends a search request for a given string to the Star Wars API.

Usage: ./9-starwars.py <search string>
  - The search request is sent to the Star Wars API search people endpoint.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    results = requests.get(url.json())

    user_name = "Harbiola2123"
    password = "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"

    
