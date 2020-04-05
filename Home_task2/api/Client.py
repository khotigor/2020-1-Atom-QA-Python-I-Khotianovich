import json
import requests
from urllib.parse import urljoin


class ResponseStatusException(Exception):
    pass


class Client:

    def __init__(self):
        self.base_url = 'https://target.my.com'

    def _request(self, method, location, headers=None, params=None):

        url = urljoin(self.base_url, location)

        response = requests.request(method, url, headers=headers, params=params)

        # if response.status_code != status_code:
        #     raise ResponseStatusException(
        #         'Got {code} for url {url}'.format(code=response.status_code,
        #                                           url=url))
        return response

    def get_token(self):
        location = 'csrf/'
        result = self._request('GET', location).headers
        print(result)

    def login(self):
        pass
