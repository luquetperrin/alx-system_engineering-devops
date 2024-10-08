#!/usr/bin/python3
"""Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            
            if not posts:
                print("None")
                return
            
            for post in posts[:10]:
                print(post.get('data', {}).get('title', ""))
        else:
            print("None")
    except requests.RequestException:
        print("None")
