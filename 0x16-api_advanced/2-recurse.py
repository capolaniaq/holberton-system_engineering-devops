#!/usr/bin/python3
"""hot articles"""

from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """Recursive function that return the list with the host_list"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit, after)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        data = res.json().get('data')
        children = data.get('children')
        [hot_list.append(x.get('data').get('title')) for x in children]
        after = data.get('after')
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    except:
        return None
