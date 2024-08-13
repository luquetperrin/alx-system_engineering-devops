#!/usr/bin/python3
"""Recursive function that queries the Reddit API, counts occurrences of keywords
in hot article titles, and prints the sorted results."""

import requests
import re

def count_words(subreddit, word_list, word_count=None, after=None):
    """Returns a sorted count of given keywords (case-insensitive) in hot articles' titles."""
    
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}
    
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            after = data.get('after')

            if not posts:
                print_sorted_counts(word_count)
                return

            for post in posts:
                title = post.get('data', {}).get('title', "").lower()
                for word in word_count:
                    word_count[word] += len(re.findall(r'\b{}\b'.format(re.escape(word)), title))

            if after:
                return count_words(subreddit, word_list, word_count, after)
            else:
                print_sorted_counts(word_count)
        else:
            return
    except requests.RequestException:
        return

def print_sorted_counts(word_count):
    """Prints the keyword counts sorted by frequency and alphabetically."""
    
    sorted_counts = sorted(
        ((word, count) for word, count in word_count.items() if count > 0),
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_counts:
        print(f"{word}: {count}")
