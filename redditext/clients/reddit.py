from logging import Logger
import random
import requests

from redditext.defs import HEADER


class Reddit:

    def __init__(self, subs: list, logger: Logger):
        self.__logger = logger
        self.__subs = subs

    def __url(self, sub, cat='hot', window=None):
        if cat is 'top':
            t = f'?t={window}'
        else:
            t = ''

        return f'https://www.reddit.com/r/{sub}/{cat}.json{t}'

    # TODO: better name, guy
    def get_sub_front_page(self, sub, cat='hot', window=None):
        url = self.__url(sub=sub, cat=cat, window=window)

        self.__logger.info(f'Fetching {url}...')
        response = requests.get(url, headers=HEADER)

        return response.json()

    def __choose_sub(self):
        i = random.randint(0, len(self.__subs) - 1)
        return self.__subs[i]

    def get_post(self, sub=None, cat='hot', window=None):
        if sub is None:
            sub = self.__choose_sub()

        s = self.get_sub_front_page(sub, cat, window)

        if 'data' not in s:
            return self.get_post(sub, cat, window)

        if 'children' not in s['data']:
            return self.get_post(sub, cat, window)

        cs = s['data']['children']
        i2 = random.randint(0, len(cs) - 1)

        return {
            'sub': sub,
            'title': cs[i2]['data']['title'],
            'permalink': cs[i2]['data']['permalink'],
            'url': cs[i2]['data']['url']
        }

