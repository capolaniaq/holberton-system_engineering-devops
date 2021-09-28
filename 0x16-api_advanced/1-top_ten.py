#!/usr/bin/python3
"""top ten hot posts"""

from requests import get


def top_ten(subreddit):
    """Function that pint the top 10 hot post in a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        print(None)
        return 0

    js = res.json()
    try:
        data = js.get("data")
        children = data.get("children")
        for child in children[:10]:
            post = child.get("data")
            print(post.get("title"))
    except:
        print(None)
