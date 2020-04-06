import json
import requests
from urllib.parse import urljoin


class ResponseStatusException(Exception):
    pass


class Client:

    def __init__(self, user, password):
        self.base_url = 'https://target.my.com'
        self.session = requests.Session()
        self.user = user
        self.password = password
        self.csrf_token = None

    def _request(self, method, location, headers=None, data=None):
        url = urljoin(self.base_url, location)
        response = self.session.request(method, url, headers=headers,
                                        data=data)
        return response

    def get_token(self):
        location = 'csrf/'
        headers = self._request('GET', location).headers
        self.csrf_token = headers['Set-Cookie'].split(';')[0].split('=')[-1]

    def login(self):
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'login': self.user,
            'password': self.password,
            'continue': 'https://account.my.com/login_continue/?continue=https%3A%2F%2Faccount.my.com',
            'failure': 'https://account.my.com/login/?continue=https%3A%2F%2Faccount.my.com',
        }
        response = self._request('POST', location, headers=headers,
                                 data=data).url
        self.get_token()
        return self.csrf_token
