#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0."""
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0
