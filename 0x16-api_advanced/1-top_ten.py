#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for post in posts[:10]:
                print(post.get('data', {}).get('title', ""))

            if len(posts) == 0:
                print("None")
        except ValueError:
            print("None")
    else:
        print("None")
