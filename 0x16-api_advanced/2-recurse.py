#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list
of titles of all hot articles for a given subreddit."""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit.
    If no results are found, returns None."""
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            hot_list.extend([post.get('data', {}).get('title', "") for post in posts])
            
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list if hot_list else None
        else:
            return None
    except requests.RequestException:
        return None
