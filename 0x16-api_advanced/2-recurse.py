#!/usr/bin/python3
"""hot articles"""

from requests import get


def recurse(subreddit, hot_list=[], last=0):
    """Recursive function that return the list with the host_list"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        hot_list = []
        for post in res.json()['data']['children']:
            hot_list.append(post['data']['title'])
        if last == 0:
            recurse(subreddit, hot_list, 1)
        return hot_list
    except:
        return None
