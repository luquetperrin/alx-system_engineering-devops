#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None."""
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            for post in posts[:10]:
                print(post.get('data', {}).get('title', ""))
                
            if not posts:
                print("None")
        else:
            print("None")
    except Exception:
        print("None")
