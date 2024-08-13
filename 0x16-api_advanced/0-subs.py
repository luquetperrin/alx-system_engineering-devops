#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit. Returns 0 for invalid subreddits."""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        except ValueError:
            return 0
    else:
        return 0
