#!/usr/bin/python3
""" Pints the top 10 hot posts of a subreddit"""

import requests


def top_ten(subreddit):
    """Prints the top 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    param = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=param,
                            allow_redirects=False).json

    if response.status_code == 404:
        print("None")
        return 0
    for post in response.get("data").get("children"):
        print(post.get("data").get("title"))
