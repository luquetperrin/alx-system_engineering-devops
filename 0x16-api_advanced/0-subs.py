#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    usr = {"User-Agent": "custom-user-agent"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=usr, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except (KeyError, TypeError, ValueError):
        return 0
