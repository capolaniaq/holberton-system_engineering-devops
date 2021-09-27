#!/usr/bin/python3
"""Script that return of the number of suscriptors in
subreddit with reppli api"""
import requests


def number_of_subscribers(subreddit):
    """Function that return how many suscriptors ahve in a subredit"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.get(url, headers=headers)

    data_value = res.json()['data']
    for key, value in data_value.items():
        if key == "subscribers":
            return value
    return 0
