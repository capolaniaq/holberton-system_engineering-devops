#!/usr/bin/python3
"""Script that return of the number of suscriptors in
subreddit with reppli api"""
from requests import get


def number_of_subscribers(subreddit):
    """Function that return how many suscriptors ahve in a subredit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0

    data_value = res.json()['data']
    if data_value["subscribers"]:
        suscribers = data_value["subscribers"]
        return suscribers
    return 0
